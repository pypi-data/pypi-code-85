#!/usr/bin/env python
import os
import re
import argparse
import shutil
import numpy as np
import xml.etree.ElementTree as ET
import miind.directories3 as directories
from collections import Counter
import miind.reporting as reporting
import miind.connections as connections

# These algorithms can feature in a MeshAlgorithmGroup simulation, and no others
MESH_ALGORITHM_GROUP_LIST = ['GridAlgorithmGroup', 'MeshAlgorithmGroup', 'DelayAlgorithm', 'RateFunctor' ]

def parse_rate_functors(algorithms):
     s=''
     for algorithm in algorithms:
          if algorithm.attrib['type'] == 'RateFunctor':
             expression = algorithm.find('expression')
             name=re.sub(r'\s+', '_', algorithm.attrib['name']) # a user may use white space, we need to replace it
             s += 'MPILib::Rate ' + name + '( MPILib::Time t ){\n'
             s += '\treturn ' + expression.text + ';\n'
             s += '}\n\n'
     return s


def generate_variable_declarations(variables):
     s = ''
     for variable in variables:
          s += 'const float ' + variable.attrib['Name'] + ' = ' + variable.text + ';\n'
     s += '\n'
     return s


def generate_preamble(fn, variables, nodes, algorithms, connections, parameters, cuda):
    '''Generates the function declarations, required for RateFunctors etc in the C++ file. fn is the file name where the C++
    is to be written. variable, nodes and algorithms are XML elements.'''

    # the rate functor functions need to be declared before the main program
    function_declarations = parse_rate_functors(algorithms)
    variable_declarations = generate_variable_declarations(variables)
    time_step = parameters.find('t_step').text

    if cuda == True:
         template_argument = 'fptype'
    else:
         template_argument = 'MPILib::Rate'

    with open(fn,'w') as f:
        f.write('//Machine-generated by miind.py. Edit at your own risk.\n\n')
        f.write('#include <boost/timer/timer.hpp>\n')
        f.write('#include <GeomLib.hpp>\n')
        f.write('#include <TwoDLib.hpp>\n')
        if cuda == True: f.write('#include <CudaTwoDLib.hpp>\n')
        f.write('#include <MPILib/include/RateAlgorithmCode.hpp>\n')
        f.write('#include <MPILib/include/SimulationRunParameter.hpp>\n')
        f.write('#include <MPILib/include/DelayAlgorithmCode.hpp>\n')
        f.write('#include <MPILib/include/RateFunctorCode.hpp>\n\n')
        f.write('#include <MiindLib/VectorizedNetwork.hpp>\n\n')
        if cuda == True: f.write('typedef CudaTwoDLib::fptype fptype;\n')
        f.write('\n')
        f.write(variable_declarations)
        f.write('\n')
        f.write(function_declarations)
        f.write('\n')
        f.write('\nint main(int argc, char *argv[]){\n')
        f.write('\n')
        f.write('#ifdef ENABLE_MPI\n')
        f.write('\t// initialise the mpi environment this cannot be forwarded to a class\n')
        f.write('\tboost::mpi::environment env(argc, argv);\n')
        f.write('#endif\n\n')
        f.write('\tMiindLib::VectorizedNetwork network('+ time_step +');\n')
        f.write('\tpugi::xml_document doc;\n')
        f.write('\n')

def generate_closing(fn,parameters):
    end_time = parameters.find('t_end').text
    time_step = parameters.find('t_step').text

    steps = ''
    master_steps = parameters.findall('master_steps')
    if(len(master_steps) > 0):
        steps = master_steps[0].text

    '''Generates the closing statements in the C++ file.'''
    with open(fn,'a') as f:
        f.write('\tnetwork.setDisplayNodes(display_nodes);\n')
        f.write('\tnetwork.setRateNodes(rate_nodes, rate_node_intervals);\n')
        f.write('\tnetwork.setDensityNodes(density_nodes,density_node_start_times,density_node_end_times,density_node_intervals);\n')
        f.write('\n')
        f.write('\tnetwork.initOde2DSystem('+ steps +');\n')
        f.write('\n')
        f.write('\tnetwork.mainLoop(0.0, '+ end_time + ','+ time_step + ', true);\n')
        f.write('\n')
        f.write('\treturn 0;\n')
        f.write('}\n')

def process_tree(root):

    variables=root.findall(".//Variable")
    nodes=root.findall('.//Node')
    algorithms=root.findall('.//Algorithm')
    connections=root.findall('.//Connection')
    parameters=root.findall('.//SimulationRunParameter')
    io=root.findall('.//SimulationIO')
    return variables, nodes, algorithms, connections, parameters[0], io

def parse(fn):
    '''Takes a filename. Puts the file with filename fn through the XML parser. Returns nothing.'''
    try:
        tree = ET.parse(fn)
        root = tree.getroot()
        return root
    except FileNotFoundError:
        print('No file ' + fn)


def generate_model_files(fn, nodes,algorithms):
     with open(fn,'a') as f:
         node_id = 0
         for node in nodes:
              algorithm = None
              algname = node.attrib['algorithm']
              for alg in algorithms:
                   if alg.attrib['name'] == algname: # here we assume the name is unique
                        algorithm = alg

              if not algorithm:
                  raise Exception('No algorithm named \'' + algname + '\' for node \'' + node.attrib['name'] + '\'')

              if algorithm.attrib['type'] == 'MeshAlgorithmGroup':
                  ref = 0.0
                  if 'tau_refractive' in algorithm.attrib.keys():
                       ref = algorithm.attrib['tau_refractive']

                  f.write('\tpugi::xml_parse_result result' + str(node_id) + ' = doc.load_file(\"' + algorithm.attrib['modelfile'] +'\");\n')
                  f.write('\tpugi::xml_node  root' + str(node_id) + ' = doc.first_child();\n\n')
                  f.write('\tTwoDLib::Mesh mesh' + str(node_id) +' = TwoDLib::RetrieveMeshFromXML(root' + str(node_id) + ');\n')
                  f.write('\tstd::vector<TwoDLib::Redistribution> vec_rev' + str(node_id) + ' = TwoDLib::RetrieveMappingFromXML("Reversal",root' + str(node_id) + ');\n')
                  f.write('\tstd::vector<TwoDLib::Redistribution> vec_res' + str(node_id) + ' = TwoDLib::RetrieveMappingFromXML("Reset",root' + str(node_id) + ');\n\n')
                  f.write('\tnetwork.addMeshNode(mesh'+ str(node_id) +', vec_rev'+ str(node_id) +', vec_res'+ str(node_id) +', ' + str(ref) + ');\n')
                  f.write('\n')

                  node_id = node_id + 1

              elif algorithm.attrib['type'] == 'GridAlgorithmGroup':
                  ref = 0.0
                  if 'tau_refractive' in algorithm.attrib.keys():
                     ref = algorithm.attrib['tau_refractive']

                  f.write('\tpugi::xml_parse_result result' + str(node_id) + ' = doc.load_file(\"' + algorithm.attrib['modelfile'] +'\");\n')
                  f.write('\tpugi::xml_node  root' + str(node_id) + ' = doc.first_child();\n\n')
                  f.write('\tTwoDLib::Mesh mesh' + str(node_id) +' = TwoDLib::RetrieveMeshFromXML(root' + str(node_id) + ');\n')
                  f.write('\tstd::vector<TwoDLib::Redistribution> vec_rev' + str(node_id) + ' = TwoDLib::RetrieveMappingFromXML("Reversal",root' + str(node_id) + ');\n')
                  f.write('\tstd::vector<TwoDLib::Redistribution> vec_res' + str(node_id) + ' = TwoDLib::RetrieveMappingFromXML("Reset",root' + str(node_id) + ');\n\n')
                  f.write('\tTwoDLib::TransitionMatrix transform' + str(node_id) + '(\"' + algorithm.attrib['transformfile'] + '\");\n')
                  f.write('\tnetwork.addGridNode(mesh'+ str(node_id) +', transform'+ str(node_id) +', ' + str(algorithm.attrib['start_v']) + ', ' + str(algorithm.attrib['start_w']) +', vec_rev'+ str(node_id) +', vec_res'+ str(node_id) +', '+ ref +');\n')
                  f.write('\n')

                  node_id = node_id + 1
              elif algorithm.attrib['type'] == 'RateFunctor':
                  rn = algorithm.attrib['name']
                  f.write('\tnetwork.addRateNode(' + rn + ');\n')
                  node_id = node_id + 1

def extract_efficacy(fn):
     '''Extract efficacy from a matrix file. Takes a filename, returns efficacy as a single float. In the
     file efficacies are represented by two numbers. We will assume for now that one of them in zero. We will
     return the non-zero number as efficacy.'''

     with open(fn) as f:
          line=f.readline()
          nrs = [ float(x) for x in line.split()]
          if nrs[0] == 0.:
               return nrs[1]
          else:
               if nrs[1] != 0:
                    raise ValueError('Expected at least one non-zero value')
               return nrs[0]

def construct_CSR_map(nodes,algorithms,connections, connection_type):
     '''Creates a list that corresponds one-to-one with the connection structure. Returns a tuple: [0] node name of receiving node,[1] matrix file name for this connection  '''
     csrlist=[]
     combi = []
     for connection in connections:
          for node in nodes:
               if connection.attrib['Out'] == node.attrib['name']:
                    # we have the right node, now see if it's a MeshAlgorithmGroup
                    nodealgorithm=node.attrib['algorithm']
                    for algorithm in algorithms:
                         if nodealgorithm == algorithm.attrib['name']:
                              if algorithm.attrib['type'] == 'MeshAlgorithmGroup':

                                   mfs=algorithm.findall('MatrixFile')
                                   mfn= [ mf.text for mf in mfs]
                                   efficacy = None
                                   if connection_type == "DelayedConnection":
                                       efficacy=connection.text.split()[1]
                                   elif connection_type == "CustomConnectionParameters":
                                       efficacy=connection.attrib['efficacy']
                                   effs= [extract_efficacy(fn) for fn in mfn]

                                   count = Counter(combi)
                                   combi.append((connection.attrib['Out'],connection.attrib['In']))
                                   nr_connection = count[(connection.attrib['Out'],connection.attrib['In'])]

                                   if efficacy.isnumeric():
                                       efficacy = float(efficacy)
                                       candidates=[]
                                       for i, eff in enumerate(effs):
                                           if np.isclose(eff,efficacy):
                                               candidates.append(i)
                                       if len(candidates) == 0: raise ValueError('No efficacy found that corresponds to the connection efficacy ' + str(efficacy))
                                       if len(candidates) > 1: raise ValueError('Same efficacy found twice')

                                       csrlist.append([node.attrib['name'],mfn[candidates[0]], effs[candidates[0]],connection.attrib['In'],nr_connection,connection])
                                   else:
                                        csrlist.append([node.attrib['name'],None, efficacy, connection.attrib['In'],nr_connection,connection])

     return csrlist

def GenerateAllMatrixFiles(nodes,algorithms,connections, connection_type):
    csrlist=[]
    combi = []
    for connection in connections:
          for node in nodes:
               if connection.attrib['Out'] == node.attrib['name']:
                    # we have the right node, now see if it's a MeshAlgorithmGroup
                    nodealgorithm=node.attrib['algorithm']
                    for algorithm in algorithms:
                         if nodealgorithm == algorithm.attrib['name']:
                              if algorithm.attrib['type'] == 'MeshAlgorithmGroup':

                                   mfs=algorithm.findall('MatrixFile')
                                   mfn= [ mf.text for mf in mfs]
                                   effs= [extract_efficacy(fn) for fn in mfn]
                                   count = Counter(combi)
                                   combi.append((connection.attrib['Out'],connection.attrib['In']))
                                   nr_connection = count[(connection.attrib['Out'],connection.attrib['In'])]
                                   csrlist.append([node.attrib['name'],mfn, effs,connection.attrib['In'],nr_connection,connection])
    return csrlist

def construct_grid_connection_map(nodes,algorithms,connections):
     '''Creates a list that corresponds one-to-one with the connection structure. Returns a tuple: [0] node name of receiving node,[1] matrix file name for this connection  '''
     gridlist=[]
     for connection in connections:
          for node in nodes:
               if connection.attrib['Out'] == node.attrib['name']:
                    # we have the right node, now see if it's a MeshAlgorithmGroup
                    nodealgorithm=node.attrib['algorithm']
                    for algorithm in algorithms:
                         if nodealgorithm == algorithm.attrib['name']:
                              if algorithm.attrib['type'] == 'GridAlgorithmGroup':
                                   gridlist.append([node.attrib['name'],connection])

     return gridlist

def node_name_to_node_id(nodes):
     '''Create a map from name to NodeId from node elements. Return this map.'''
     d ={}
     for i,node in enumerate(nodes):
          d[node.attrib['name']] = i
     return d

def generate_connections(fn,conns, nodes, algorithms, weighttype):
    grid_cons = construct_grid_connection_map(nodes, algorithms, conns)
    mesh_cons = construct_CSR_map(nodes, algorithms, conns, weighttype.text)
    nodemap = node_name_to_node_id(nodes)

    all_mats = GenerateAllMatrixFiles(nodes, algorithms, conns, weighttype.text)

    with open(fn,'a') as f:
        for cn in all_mats:
            cpp_name = 'mat_' + str(nodemap[cn[0]]) + '_' + str(nodemap[cn[3]]) + '_' + str(cn[4])
            f.write('\tstd::map<float,TwoDLib::TransitionMatrix> '+ cpp_name + ';\n')
            for mfn in range(len(cn[1])):
                f.write('\t' + cpp_name + '[' + str(cn[2][mfn]) + '] = TwoDLib::TransitionMatrix(\"' + cn[1][mfn] + '\");\n')
        if weighttype.text ==  "DelayedConnection":
            for cn in mesh_cons:
                cpp_name = 'mat_' + str(nodemap[cn[0]]) + '_' + str(nodemap[cn[3]]) + '_' + str(cn[4])
                mat_name = cpp_name + '.at(' + str(cn[2]) + ')'
                f.write(connections.parse_mesh_connection(cn[5], nodemap, mat_name))

        if weighttype.text == "CustomConnectionParameters":
            for cn in mesh_cons:
                cpp_name = 'mat_' + str(nodemap[cn[0]]) + '_' + str(nodemap[cn[3]]) + '_' + str(cn[4])
                mat_name = cpp_name + '.at(' + str(cn[2]) + ')'
                f.write(connections.parse_mesh_vectorized_connection(cn[5],nodemap,mat_name))

        for cn in grid_cons:
            f.write(connections.parse_grid_vectorized_connection(cn[1],nodemap))

        f.write('\n')


def create_cpp_file(xmlfile, dirpath, progname, modname, cuda):
    '''Write the C++ file specified by xmlfile into dirpath as progname.'''
    root=parse(xmlfile)
    variables, nodes, algorithms, connections, parameter, io=process_tree(root)
    if sanity_check(algorithms) == False: raise NameError('An algorithm incompatible with MeshAlgorithmGroup was used')
    if cuda == True:
         fn=os.path.join(dirpath, progname)+'.cu'
    else:
         fn=os.path.join(dirpath, progname)+'.cpp'

    generate_preamble(fn, variables, nodes, algorithms,connections,parameter, cuda)

    generate_model_files(fn,nodes,algorithms)
    weighttype = root.find('WeightType')
    generate_connections(fn,connections,nodes,algorithms,weighttype)
    nodemap = node_name_to_node_id(nodes)
    with open(fn,'a') as f:
        f.write(reporting.define_display_nodes(root,nodemap))
        f.write(reporting.define_rate_nodes(root,nodemap))
        f.write(reporting.define_density_nodes(root,nodemap))
    generate_closing(fn,parameter)

def sanity_check(algorithms):
    '''Check if only the allowd algorithms feature in this simulation. Returns True if so, False otherwise.'''

    for algorithm in algorithms:
        if algorithm.attrib['type'] not in MESH_ALGORITHM_GROUP_LIST:
            return False
        else:
            return True

def mesh_algorithm_group(root):
    '''True if there are MeshAlgorithmGroup algorithms in the XML file, false otherwise.'''
    algorithms=root.findall('.//Algorithm')

    for algorithm in algorithms:
        if algorithm.attrib['type'] in ["MeshAlgorithmGroup","GridAlgorithmGroup"]:
            return True

    return False

def produce_mesh_algorithm_version(dirname, filename, modname, root, enable_mpi, enable_openmp, enable_root, cuda):
    '''Entry point for the vector version of a MIIND C++ file. Filename is file name of the XML file, dirname is the user-specified directory hierarchy
    where the C++ file will be generated and the simulation will be stored. The simulation file will be placed in directory <dirname>/<xml_file_name>.'''

    if not directories.PATH_VARS_DEFINED:
        directories.initialize_global_variables()

    for xmlfile in filename:
        progname = directories.check_and_strip_name(xmlfile)
        dirpath = directories.create_dir(os.path.join(dirname, progname))
        SOURCE_FILE = progname + '.cpp'
        if cuda:
            SOURCE_FILE = progname + '.cu'
        directories.insert_cmake_template(progname,dirpath,enable_mpi, enable_openmp, enable_root,cuda,SOURCE_FILE)
        create_cpp_file(xmlfile, dirpath, progname, modname, cuda)
        directories.move_model_files(xmlfile,dirpath)
        xmlfilename = xmlfile.split(os.path.sep)[-1]
        shutil.copyfile(xmlfile, os.path.join(dirpath,xmlfilename))


def generate_vectorized_network_executable(dirname, filename, modname, enable_mpi, enable_openmp, enable_root, enable_cuda):
    fn = filename[0]
    root=parse(fn)
    if mesh_algorithm_group(root) == True:
        if not enable_cuda:
            raise Exception('Vectorised mode (for MeshAlgorithmGroup/GridAlgorithmGroup) currently not supported without a CUDA enabled MIIND installation. ')
        # Run the MeshAlgorithm version
        produce_mesh_algorithm_version(dirname, filename, modname, root, enable_mpi, enable_openmp, enable_root, enable_cuda)
    else:
        # Simply run the old script
        directories.add_executable(dirname, filename, modname, enable_mpi, enable_openmp, enable_root, False)


if __name__ == "__main__":

    parser = argparse.ArgumentParser(description='Generate C++ from XML descriptions.')
    parser.add_argument('--d', help = 'Provide a packaging directory.',nargs = '?')
    parser.add_argument('-c', '--cuda', action="store_true", dest="cuda", help="if specified, cuda will be generated")
    parser.add_argument('-m','--m', help = 'A list of model and matrix files that will be copied to every executable directory.''', nargs='+')
    parser.add_argument('xml file', metavar='XML File', nargs = '*', help = 'Will create an entry in the build tree for each XML file, provided the XML file is valid.')
    parser.add_argument('--mpi', help = 'Enable MPI.', action='store_true')
    parser.add_argument('--openmp', help = 'Enable OPENMP.', action='store_true')
    parser.add_argument('--no_root', help = 'Disable ROOT.', action='store_true')

    args = parser.parse_args()


    filename = vars(args)['xml file']
    dirname  = vars(args)['d']
    modname  = vars(args)['m']
    enable_mpi = vars(args)['mpi']
    enable_openmp = vars(args)['openmp']
    disable_root = vars(args)['no_root']
    enable_cuda = vars(args)['cuda']

    fn = filename[0]
    root=parse(fn)
    if mesh_algorithm_group(root) == True:
        if not enable_cuda:
            raise Exception('Vectorised mode (for MeshAlgorithmGroup/GridAlgorithmGroup) currently not supported without a CUDA enabled MIIND installation. ')
        # Run the MeshAlgorithm version
        produce_mesh_algorithm_version(dirname, filename, modname, root, vars(args)['cuda'])
    else:
        # Simply run the old script
        if dirname == None:
            raise ValueError("This option is deprecated")
            fn = filename[0]
            directories.add_executable(fn,modname, enable_mpi, enable_openmp, not disable_root)
        else:
            directories.add_executable(dirname, filename, modname, enable_mpi, enable_openmp, not disable_root, enable_cuda)
