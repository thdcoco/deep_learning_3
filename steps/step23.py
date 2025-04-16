import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))  # 부모 디렉터리 추가


import numpy as np
from dezero.core_simple import *
setup_variable()
x = Variable(np.array(1.0))
y = (x + 3) ** 2
y.backward()

print(y)
print(x.grad)