import numpy as np
import math
from scipy.stats import chi2_contingency

d = np.array([[91,68], [35,56]])
OR=(d[0][0]*d[1][1])/(d[0][1]*d[1][0])
print('OR=',OR)
x=math.log(OR)
e=1.96*(1/d[0][0]+1/d[0][1]+1/d[1][0]+1/d[1][1])**0.5
L=math.exp(x-e)
R=math.exp(x+e)
print('L=',L)
print('R=',R)
print('p=',chi2_contingency(d)[1])
