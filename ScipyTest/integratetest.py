# coding=utf-8
# 积分操作

import numpy as np
from scipy.integrate import quad, dblquad

# 一元积分
quadRes = quad(lambda x: 1/x, 1, np.e)
print('quadRes:', quadRes)

# 二元积分
dblQuadRes = dblquad(lambda t, x: np.exp(-x*t)/t**3, 0, np.inf, lambda x:1, lambda x:np.inf)
print('dblquadRes:', dblQuadRes)
