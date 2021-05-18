import base64
import json
import os
import random
import shutil
import string

from pybuilder.core import Logger, Project, depends, after
from pybuilder.core import task
from pybuilder.pluginhelper.external_command import ExternalCommandBuilder
from pybuilder.reactor import Reactor

DOCKER_IMAGE_TEMPLATE = string.Template("""
FROM ${build_image}
MAINTAINER ${maintainer_name}
COPY ${dist_file} .
RUN ${prepare_env_cmd}
RUN ${package_cmd}
""")


@task(description="Package artifact into a docker container with the tag "
                  "${docker_package_build_img}:${docker_package_build_version} (defaults to ${project.name} and ${project.version}).  "
                  "This task expects a docker file to be located in 'src/main/docker' (override with property"
                  " 'docker_package_dir').  The docker file will be built then a new container will be created"
                  " from the image with the distribution package of the python project installed into the system"
                  "python.")
@depends("publish")
def docker_package(project: Project, logger: Logger, reactor: Reactor):
    do_docker_package(project, logger, reactor)


@after("publish")
def do_docker_package(project, logger, reactor):
    project.set_property_if_unset("docker_package_build_dir", "src/main/docker")
    project.set_property_if_unset("docker_package_build_img", project.name)
    project.set_property_if_unset("docker_package_build_version", project.version)
    dist_dir = prepare_dist_directory(project)
    reactor.pybuilder_venv.verify_can_execute(["docker", "--version"], prerequisite="docker", caller="docker_package")
    # is true if user set verbose in build.py or from command line
    verbose = project.get_property("verbose")
    project.set_property_if_unset("docker_package_verbose_output", verbose)
    temp_build_img = 'pyb-temp-{}:{}'.format(project.name, project.version)
    build_img = get_build_img(project)
    logger.info("Executing primary stage docker build for image - {}.".format(build_img))
    # docker build --build-arg buildVersion=${BUILD_NUMBER} -t ${BUILD_IMG} src/
    exec_command(executable="docker",
                 args=[
                     'build',
                     '--build-arg',
                     f"buildVersion={project.get_property('docker_package_build_version')}",
                     "-t",
                     f"{temp_build_img}",
                     f"{project.get_property('docker_package_build_dir')}"
                 ],
                 output_file_name='docker_package_build', project=project, logger=logger, reactor=reactor,
                 exeception_message="Error building primary stage docker image")
    write_docker_build_file(project=project, build_image=temp_build_img, dist_dir=dist_dir)
    copy_dist_file(project=project, dist_dir=dist_dir)
    logger.info("Executing secondary stage docker build for image - {}.".format(build_img))
    exec_command(executable="docker",
                 args=[
                     'build',
                     "-t",
                     f"{build_img}",
                     f"{dist_dir}"
                 ],
                 output_file_name='docker_package_img', project=project, logger=logger, reactor=reactor,
                 exeception_message="Error building primary stage docker image")
    logger.info("Finished build docker image - {} - with dist file - {}".format(build_img, dist_dir))


def get_build_img(project):
    return project.get_property('docker_package_build_img', '{}:{}'.format(project.name, project.version))


@task(description="Publish artifact into a docker registry. "
                  "${docker_push_registry} - the registry to push the image to "
                  "                       (If you provide an AWS ECR registry the aws cli will be used to authenticate.)"
                  "${docker_push_tag_as_latest} - tag the image as LATEST before push (default TRUE)"
                  "${ensure_ecr_registry_created} - create the ECR registry if it doesn't exist (default TRUE)")
@depends("docker_package")
def docker_push(project, logger, reactor: Reactor):
    do_docker_push(project, logger, reactor)

# aws ecr get-authorization-token --output text --query 'authorizationData[].authorizationToken' | base64 -D | cut -d: -f2
# docker login -u AWS -p <my_decoded_password> -e <any_email_address> <aws_account_id>.dkr.ecr.us-west-2.amazonaws.com
def _ecr_login(project, registry, logger, reactor):
    res = exec_command('aws', [
        'ecr', 'get-authorization-token', '--output', 'text', '--query',
        'authorizationData[].authorizationToken'
    ], 'docker_ecr_get_token', project, logger=logger, reactor=reactor, exeception_message="Error getting token")
    pass_token = base64.b64decode(res.report_lines[0])
    split = str(pass_token).split(':')
    exec_command('docker', ['login', '-u', f"{split[0]}", "-p", f"{split[1]}", f"{registry}"],
                 "docker_ect_docker_login", project, logger=logger, reactor=reactor,
                 exeception_message="Error authenticating")


def _prep_ecr(project, fq_artifact, registry, logger, reactor):
    _ecr_login(project, registry, logger, reactor)
    create_ecr_registry = project.get_property("ensure_ecr_registry_created", True)
    if create_ecr_registry:
        _create_ecr_registry(fq_artifact, project, logger, reactor)


def _create_ecr_registry(fq_artifact, project, logger, reactor):
    res = exec_command('aws', ['ecr', 'describe-repositories', '--repository-names', f"{fq_artifact}"],
                       'docker_ecr_registry_discover', project, logger=logger, reactor=reactor, exeception_message=None)
    # if it is not found then create
    if res.exit_code > 0:
        exec_command('aws', ["ecr", "create-repository", "--repository-name", f"{fq_artifact}"],
                     'docker_ecr_registry_create', project, logger=logger, reactor=reactor,
                     exeception_message="Unable to create ecr registry")


def exec_command(executable, args, output_file_name, project, logger, reactor, exeception_message=None):
    command = ExternalCommandBuilder(executable, project, reactor)
    for arg in args:
        command.use_argument(arg)
    res = command.run("{}/{}".format(prepare_reports_directory(project), output_file_name))
    if res.exit_code != 0 and exeception_message:
        logger.error(res.error_report_lines)
        raise Exception(exeception_message)
    return res


def do_docker_push(project: Project, logger: Logger, reactor: Reactor):
    verbose = project.get_property("verbose")
    project.set_property_if_unset("docker_push_verbose_output", verbose)
    tag_as_latest = project.get_property("docker_push_tag_as_latest", True)
    registry = project.get_mandatory_property("docker_push_registry")
    local_img = get_build_img(project)
    fq_artifact = project.get_property("docker_push_img", get_build_img(project))
    if "ecr" in registry:
        _prep_ecr(project=project, fq_artifact=fq_artifact, registry=registry, logger=logger, reactor=reactor)
    registry_path = f"{registry}/{fq_artifact}"
    tags = [project.version]
    if tag_as_latest:
        tags.append('latest')
    for tag in tags:
        remote_img = f"{registry_path}:{tag}"
        _run_tag_cmd(project, local_img, remote_img, logger, reactor)
        _run_push_cmd(project=project, remote_img=remote_img, logger=logger, reactor=reactor)
    generate_artifact_manifest(project, registry_path)


def generate_artifact_manifest(project, registry_path):
    artifact_manifest = {'artifact-type': 'container', 'artifact-path': registry_path,
                         'artifact-identifier': project.version}
    with open(project.expand_path('$dir_target', 'artifact.json'), 'w') as target:
        json.dump(artifact_manifest, target)


def _run_tag_cmd(project, local_img, remote_img, logger, reactor):
    logger.info("Tagging local docker image {} - {}".format(local_img, remote_img))
    exec_command('docker', ['tag', f"{local_img}", f"{remote_img}"], 'docker_tag', project,
                 logger=logger,
                 reactor=reactor,
                 exeception_message="Failed to tag image")


def _run_push_cmd(project, remote_img, logger, reactor):
    logger.info("Pushing remote docker image - {}".format(remote_img))
    exec_command('docker', ['push', f"{remote_img}"], 'docker_push', project,
                 logger=logger,
                 reactor=reactor,
                 exeception_message=f"Error pushing image to remote registry - {remote_img}")


#
# docker tag ${APPLICATION}/${ROLE} ${DOCKER_REGISTRY}/${APPLICATION}/${ROLE}:${BUILD_NUMBER}
# docker tag ${DOCKER_REGISTRY}/${APPLICATION}/${ROLE}:${BUILD_NUMBER} ${DOCKER_REGISTRY}/${APPLICATION}/${ROLE}:latest
# docker push ${DOCKER_REGISTRY}/${APPLICATION}/${ROLE}:latest
# docker push ${DOCKER_REGISTRY}/${APPLICATION}/${ROLE}:${BUILD_NUMBER}

def copy_dist_file(project, dist_dir):
    dist_file = get_dist_file(project=project)
    dist_file_path = project.expand_path("$dir_dist", 'dist', dist_file)
    shutil.copy2(dist_file_path, dist_dir)


def write_docker_build_file(project, build_image, dist_dir):
    setup_script = os.path.join(dist_dir, "Dockerfile")
    with open(setup_script, "w") as setup_file:
        setup_file.write(render_docker_buildfile(project, build_image))
    os.chmod(setup_script, 0o755)


def render_docker_buildfile(project, build_image):
    # type: (Project, str) -> str

    dist_file = get_dist_file(project)
    default_package_cmd = "pip install {}".format(dist_file)
    template_values = {
        "build_image": build_image,
        "dist_file": dist_file,
        "maintainer_name": project.get_property("docker_package_image_maintainer",
                                                "anonymous"),
        "prepare_env_cmd": project.get_property("docker_package_prepare_env_cmd",
                                                "echo 'empty prepare_env_cmd installing into python'"),
        "package_cmd": project.get_property("docker_package_package_cmd", default_package_cmd)
    }

    return DOCKER_IMAGE_TEMPLATE.substitute(template_values)


def get_dist_file(project):
    default_dist_file = "{name}-{version}.tar.gz".format(name=project.name, version=project.version)
    return project.get_property("docker_package_dist_file", default_dist_file)


def randomWord(param):
    return ''.join(random.choice(string.ascii_lowercase) for i in range(param))


def prepare_reports_directory(project):
    return prepare_directory("$dir_reports", project)


def prepare_dist_directory(project):
    return prepare_directory("$dir_dist", project)


def prepare_directory(dir_variable, project):
    package__format = f"{dir_variable}/docker"
    reports_dir = project.expand_path(package__format)
    if not os.path.exists(reports_dir):
        os.mkdir(reports_dir)
    return reports_dir
