import numpy as np
import matplotlib.pyplot as plt
import scipy
from scipy.stats import norm
from fitting_functions import *

data=np.loadtxt('project2_python.csv',delimiter=';',dtype=str)
x = data[1:, 0].astype(np.float32)
y=data[1:,1].astype(np.float32)
params, params_cov = scipy.optimize.curve_fit(linear, x, y)
slope = params[0]
intercept = params[1]

##EXERCISE 1
y_units='mm'
x_units='g'
print_equation(slope,intercept,y_units,x_units)# the equation is y=-0.0524mm/g x +62 mm

##EXERCISE 2
fig = plt.figure()
plt.scatter(x, y, label='LineFit')
plt.plot(x, linear(x, slope, intercept),label='Linear Fit') #change this label if you have a non-linear fit
plt.legend(loc='best')
plt.xlabel("time (s)") #change the units as appropriate
plt.ylabel("distance in x direction (meters)")  #change the units as appropriate
plt.show()


