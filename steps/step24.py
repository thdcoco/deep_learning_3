if '__file__' in globals():
    import os, sys
    sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import numpy as np
from dezero.core_simple import *


def beale(x, y):
    term1 = (1.5 - x + x * y)
    term2 = (2.25 - x + x * (pow(y,2)))
    term3 = (2.625 - x + x * (pow(y,3)))
    return pow(term1,2) + pow(term2,2) + pow(term3,2)

x = Variable(np.array(1.0))
y = Variable(np.array(0.0))
z = beale(x, y)
z.backward()
print(x.grad, y.grad)