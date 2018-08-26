from scipy.optimize import minimize
import numpy as np
import random

def Rosenbrock(x):
    """
    :param x: an array of starting point
    :return: the value of the calculated Rrosenbrock function
    """
    return 100*(x[1]-x[0]**2)**2+(1-x[0])**2+100*(x[2]-x[1]**2)**2+(1-x[1])**2

def gradient(x):
    return np.array([400*x[0]**3-400*x[1]*x[0]-2+2*x[0],
                     400*x[1]**3-400*x[2]*x[1]-200*x[0]**2-2+202*x[1],
                     200*x[2]-200*x[1]**2])

if __name__ == "__main__":

    n = 20
    res = np.zeros(n)
    for i in range(n):
        x_init = np.random.uniform(-999,999,3)
        res[i] = minimize(Rosenbrock, x_init, method="BFGS", jac = gradient).fun
    print("the minimum function value is :"+ str(min(res)))
    print(min(res))

