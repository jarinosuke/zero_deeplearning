import numpy as np
import sys, os
sys.path.append(os.pardir)
from common.util import im2col

x1 = np.random.rand(1, 3, 7, 7)
print(x1)
col1 = im2col(x1, 5, 5, stride=1, pad=0)
print(col1)
print(col1.shape)
