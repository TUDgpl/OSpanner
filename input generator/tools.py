import numpy as np
from enum import Enum
# generate random integer

# uniform model
# generate one integr in the closed interval [low, high]
def uniform_integer(low, high):
    return np.random.random_integers(low, high) 


def str_gen(list_str):
    name = ""
    for e in list_str:
        name += str( e )
        name += "_"
    name += "0"
    return name

class Model( Enum ):
    UNIFORM = 1
