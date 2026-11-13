import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *

data=np.loadtxt('project2_python.csv',delimiter=';',dtype=str)
x = data[1:, 0].astype(np.float32)
y=data[1:,1].astype(np.float32)
print('x=',x)
print('y=',y)
