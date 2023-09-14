# generate point set instances for the Ospanner project
# DIMACS-style format 
# c command line, human-readable information, generation configuration
# p problem line, specifying the type and the size   
# Description lines <x> <y> <w> 
import pathlib
import tools
import os
import numpy as np
import branch_gen

nt_data_path = 'D:/GIT/OSpanner/instances'
instance_sizes = [2,4,8,16]
#instance_sizes = [2]
W = 1000
H = 1000
instance_number = 2
# main function






if __name__ == "__main__":    
    if os.name == 'nt':
        data_path = pathlib.Path( nt_data_path )
        uniform_1d_folder = data_path/'1D'/'Uniform'
        unit_1d_folder = data_path/'1D'/'Unit'
    for instance_size in instance_sizes:
            branch_gen.generate_branch( tools.Model.UNIFORM, 1,  uniform_1d_folder, instance_size, instance_number, W, H)
            branch_gen.generate_branch( tools.Model.UNIT,1, unit_1d_folder, instance_size, instance_number, W, H)
