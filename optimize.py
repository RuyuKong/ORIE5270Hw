from scipy.optimize import minimize
import numpy as np

def Rosenbrock(x):
    """
    :param x: an array of starting point
    :return: the value of the calculated Rrosenbrock function
    """
    return 100 * (x[1] - x[0] ** 2) ** 2 + (1 - x[0]) ** 2 + 100 * (x[2] - x[1]) ** 2 + (1 - x[1]) ** 2

def gradient(x):
    rad = np.array([-400 * x[0] * x[1] + 400 * x[0] ** 3 - 2 * (1 - x[0]),
                    -400 * x[1] * x[2] + 400 * x[1] ** 3 - 2 * (1 - x[1]) + 200 * (x[1] - x[0] ** 2),
                    200 * (x[2] - x[1] ** 2)])
    return grad



if __name__ =="__main__":
    x1 = np.array([5, 10, 15])
    x2 = np.array([1, 20, -10])
    x3 = np.array([-5, 20, 30])
    x4 = np.array([21, 100, 200])
    x5 = np.array([-100, 500, 9999])
    x =[x1,x2,x3,x4,x5]
    res = []
    for x0 in x:
        res.append(optimize.minimize(Rosenbrock, x0, method='BFGS', jac=gradient).fun)
    print(min(res))
