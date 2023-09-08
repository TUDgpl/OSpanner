# generate point set instances for the Ospanner project
# DIMACS-style format 
# c command line, human-readable information, generation configuration
# p problem line, specifying the type and the size   
# Description lines <x> <y> <w> 
import pathlib
import tools
import os
import numpy as np
# main function
nt_data_path = 'D:/GIT/C++/geowordle_core_cmake/data'



def make_instances_set(folder_name, instance_sizes):
    if os.name == 'nt':
        data_path = pathlib.Path( nt_data_path )
        uniform_1d_folder = data_path /folder_name/'1D'/'Uniform'
    for instance_size in instance_sizes:
        for c in color_numbers:
            generate_uniform_branch( uniform_folder, instance_size, c, 1000, 1000, instance_number, 4)
            generate_gaussian_branch( gaussian_folder, instance_size, c, 1000, 1000, instance_number, 4)


if __name__ == "__main__":
    np.random.seed(2)
    print(tools.uniform_integer(1,4))