import os
import sys
import subprocess
from aheadworks_bitbucket_manager.api.bitbucket_api_manager import BitbucketApiManager
from aheadworks_bitbucket_manager.api.dockerhub_api_manager import DockerhubApiManager
from aheadworks_bitbucket_manager.api.version_control_manager import VersionControlManager
from aheadworks_bitbucket_manager.api.file_manager import FileManager
from aheadworks_bitbucket_manager.api.db_manager import DbManager
from aheadworks_bitbucket_manager.model.parser.php import Php as PhpParser
from aheadworks_bitbucket_manager.model.data.dockerhub import DockerHubConfig
from aheadworks_bitbucket_manager.model.data.bitbucket import BitbucketConfig
from aheadworks_bitbucket_manager.model.ssh_manager import SshManager


class Console:
    """
    this application needed next env variables
    BITBUCKET_KEY
    BITBUCKET_SECRET
    BITBUCKET_REPO_SLUG
    BITBUCKET_WORKSPACE
    DOCKERHUB_LOGIN
    DOCKERHUB_PASSWORD
    DOCKERHUB_REPO
    """

    def __init__(self):
        self.available_pipe_name = [
            'build',
            'release/*',
            'build-and-deploy-to-staging-sandbox',
            'build-and-deploy-to-staging-box'
        ]
        docker_hub_config = DockerHubConfig(
            dockerhub_user=os.getenv('DOCKERHUB_LOGIN'),
            dockerhub_password=os.getenv('DOCKERHUB_PASSWORD')
        )
        bitbucket_config = BitbucketConfig(
            bitbucket_key=os.getenv('BITBUCKET_KEY'),
            bitbucket_secret=os.getenv('BITBUCKET_SECRET'),
            bitbucket_workspace=os.getenv('BITBUCKET_WORKSPACE'),
            bitbucket_repo_slug=os.getenv('BITBUCKET_REPO_SLUG')
        )
        self.bitbucket_api_manager = BitbucketApiManager(bitbucket_config)
        self.docker_hub_api_manager = DockerhubApiManager(docker_hub_config, bitbucket_config)
        self.file_manager = FileManager()
        self.version_control_manager = VersionControlManager()
        self.db_manager = DbManager()
        self.php_parser = PhpParser()
        self.ssh_manager = SshManager()

    # Docker Hub
    def remove_deprecated_versions_images(self, repo=None):
        """
        :param repo:
        :return:
        """

        repo = repo or os.getenv('DOCKERHUB_REPO')
        self.docker_hub_api_manager.remove_deprecated_versions_images(repo)

    def renew_images_by_tag(self, commit_hash, repo=None, pipe_name=None):
        """
        :param commit_hash:
        :param repo:
        :param pipe_name:
        :return:
        """
        try:
            if pipe_name is None:
                pipe_name = self.available_pipe_name

            exit_code = 0
            repo = repo or os.getenv('DOCKERHUB_REPO')
            self.docker_hub_api_manager.renew_images_by_tag(commit_hash, repo, pipe_name)
        except Exception as error:
            print('Error: ' + repr(error))
            exit_code = 1

        exit(exit_code)

    def push_images(self, images):
        print(self.docker_hub_api_manager.push_images(images))

    # Version Control
    def run_common_app(self, check_containers, up_cmd, host=None, user=None):
        try:
            host, user = self._get_default_ssh_cred(host, user)
            print(self.version_control_manager.run_common_app(check_containers, up_cmd, host, user))
            exit_code = 0
        except subprocess.CalledProcessError as error:
            print('Error: ' + error.output)
            exit_code = 1
        except Exception as error:
            print('Error: ' + repr(error))
            exit_code = 1

        exit(exit_code)

    def run_app(
            self,
            path_to_versions,
            path_to_project,
            up_cmd,
            down_exclude_current,
            down_cmd,
            host=None,
            user=None
    ):
        try:
            host, user = self._get_default_ssh_cred(host, user)
            print(self.version_control_manager.run_app(
                path_to_versions,
                path_to_project,
                up_cmd,
                down_exclude_current,
                down_cmd,
                host,
                user
            ))
            exit_code = 0
        except subprocess.CalledProcessError as error:
            print('Error: ' + error.output)
            exit_code = 1
        except Exception as error:
            print('Error: ' + repr(error))
            exit_code = 1

        exit(exit_code)

    def modify_env(self, path, template):
        self.version_control_manager.modify_env(path, template)

    def get_version_uid(self, version):
        print(self.version_control_manager.get_version_uid(version))

    def get_traefik_version_query(self, path_to_versions):
        print(self.version_control_manager.get_traefik_version_query(path_to_versions))

    # --priority_type low or --priority_type height
    def get_free_priority(self, label_name, priority_type, host=None, user=None):
        host, user = self._get_default_ssh_cred(host, user)
        try:
            print(self.version_control_manager.get_free_priority(label_name, priority_type, host, user))
        except Exception:
            exit(1)

    def get_free_port(self, host=None, user=None):
        host, user = self._get_default_ssh_cred(host, user)
        try:
            print(self.version_control_manager.get_free_port(host, user))
        except Exception:
            exit(1)

    def get_variable_from_php_file(self, var_name, file):
        print(self.php_parser.get_variable_from_file(var_name, file))

    # Db manager
    def create_dump(self, path_to_sh, host=None, user=None):
        host, user = self._get_default_ssh_cred(host, user)
        print(self.db_manager.create_dump(path_to_sh, host, user))

    # File Manager
    def add_info_to_file_header(self, directories: list, file_extensions: list, info_string: str):
        for _ in self.file_manager.add_info_to_file_header(directories, file_extensions, info_string):
            print(_)

    # Bitbucket Api
    def get_build_by_commit(self, commit_hash: str, pipe_name=None):
        try:
            if pipe_name is None:
                pipe_name = self.available_pipe_name

            print(self.bitbucket_api_manager.get_build_by_commit(commit_hash, pipe_name))
        except Exception as error:
            print('Error: ' + repr(error), file=sys.stderr)
            exit(1)

    # Ssh manager
    def run_ssh_command(self, cmd, host=None, user=None):
        host, user = self._get_default_ssh_cred(host, user)
        run_result = self.ssh_manager.run_ssh_command(cmd, host, user)
        run_result = type(run_result) == list and '\n'.join(run_result)

        print('run_result:\n' + run_result)

    def _get_default_ssh_cred(self, host, user):
        user = user or os.getenv('HOST_USER') or 'root'
        host = host or os.getenv('HOST')

        return [host, user]
