from re import match
import tools
import numpy.random as random
import os

def generate_branch(mod:tools.Model, dim, folder_s, instance_size, instance_num, width, height):
    folder_s.mkdir( parents=True, exist_ok=True )
    for seed in range( 0, instance_num):
        random.seed(seed)
        file_s = "{0}_{1}_{2}_{3}.txt".format(mod,dim, str(instance_size), str(seed))
        generate_instance(mod, dim, folder_s, file_s, instance_size, width, height)


def generate_instance(mod:tools.Model, dim, folder_s, file_s, instance_size, width, height):
    file_path = folder_s / file_s
    with file_path.open("w") as f:
        f.write( "c This is a {0} distributed  {1}-D DIMACS file \n".format(mod.value, str(dim)) )
        f.write( "c width height point_number\n" )
        f.write( f"p {width} {height} {instance_size}\n" )
        match mod: 
            case tools.Model.UNIT:
                points_x = tools. unit_list(1, instance_size+1, instance_size)
            case tools.Model.UNIFORM:
                points_x = tools. uniform_list(1,width , instance_size)
        for i in range( instance_size ):
            f.write( f"{points_x[i]}  0\n" )
    f.close()
    plot_s = folder_s / (file_s+"_plot.png")
    Y = [height/2.0] * instance_size
    tools.draw_points(points_x, Y, width, height, plot_s)