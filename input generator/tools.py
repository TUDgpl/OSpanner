import numpy as np
from enum import Enum
import numpy.random as random
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import os

# uniform model
# generate list of uniform random numbers of [low, high-1]
def uniform_list(low, high, instance_size):
    points_x = set()
    while len( points_x ) < instance_size:
        x_rand = random.randint( low, high)
        points_x.add(x_rand)
    list_x = list( points_x )
    random.shuffle( list_x )
    return list_x 
# generate list  [low, +1...., high-1]
def unit_list(low, high, instance_size):
    return list(range(low,high,1))

class Model( Enum ):
    UNIFORM = "uniform"
    UNIT = "unit"

def str_gen(list_str):
    name = ""
    for e in list_str:
        name += str( e )
        name += "_"
    name += "0"
    return name


# draw the instance point set
def draw_points(X, Y, width,height, file_name):
    if os.name == 'nt':
        df = pd.DataFrame(dict(x=X, y=Y))
        print(df.head())
        lm =sns.scatterplot(data=df, x="x", y="y")
        lm.set(xlim=(0, width))
        lm.set(ylim=(0, height))
        #plt.show()
        plt.savefig(file_name)     
        """
if __name__ == "__main__":
    tips = sns.load_dataset("tips")
    lm =sns.scatterplot(data=tips, x="total_bill", y="tip")
    plt.show()
    """


