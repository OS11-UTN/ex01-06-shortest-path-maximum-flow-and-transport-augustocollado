import numpy as np
from scipy.optimize import linprog
from basic_utils import nn2na
import math

# parameters

NN = np.array([
    [0, 1, 1, 0, 0, 0],
    [0, 0, 0, 1, 0, 1],
    [0, 0, 0, 0, 1, 0],
    [0, 0, 0, 0, 0, 1],
    [0, 0, 0, 0, 0, 1],
    [1, 0, 0, 0, 0, 0],
])

# order of the arcs should be the same as nn2na returns
arcs = np.array( ['S2', 'S3', '24', '2T', '35', '4T', '5T', 'TS'] )
Capacity = np.array( [7, 1, 2, 3, 2, 1, 2, math.inf] ) 
Cost = np.array( [0, 0, 0, 0, 0, 0, 0, -1] ) 

B = [0, 0, 0, 0, 0, 0]

# solution

Aeq = nn2na(NN)

Beq = np.array(B)

bounds = tuple( [ (0, Capacity[i]) for i in range (0, Aeq.shape[1]) ] )

result = linprog(Cost, A_eq = Aeq, b_eq = Beq, bounds=bounds, method='simplex' )

indexes = np.where(np.array(result.x) > 0.9)

print('Max flox/Min Cut: %s' % (result.fun * -1))

for i in indexes:
    print('%s: %s' % (arcs[i], result.x[i]))


