import numpy as np
from scipy.optimize import linprog
from basic_utils import nn2na
import math

# parameters

NN = np.array([
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
])

# order of the arcs should be the same as nn2na returns
arcs = np.array( ['1A', '1B', '2A', '2B', '3A', '3B'] )
Cost = np.array( [10, 20, 10, 10, 10, 30] ) 

B = [10, 20, 15, -25, -20]

# solution

Aeq = nn2na(NN)

Beq = np.array(B)

bounds = tuple( [ (0, math.inf) for i in range (0, Aeq.shape[1]) ] )

result = linprog(Cost, A_eq = Aeq, b_eq = Beq, bounds=bounds, method='simplex' )

indexes = np.where(np.array(result.x) > 0.9)

print('Min Cost: %s' % (result.fun))

for i in indexes:
    print('%s: %s' % (arcs[i], result.x[i]))


