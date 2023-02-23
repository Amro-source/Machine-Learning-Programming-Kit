import numpy as np

from matplotlib.pyplot import *

x = np.array([1, 2, 3, 4, 5])

y = np.array([2, 3, 4, 4, 5])

n = np.max(x.shape)

X = np.vstack([np.ones(n), x]).T


a = np.linalg.lstsq(X, y)[0]

print(a)