import numpy as np
from scipy.optimize import linprog
from basic_utils import nn2na
import math

def dfs(NN, initialNode, goalNode, path):

    if initialNode == goalNode:
        return True, path

    goalReachers = NN[:,goalNode]
    reachersIndexes = np.argwhere(goalReachers)
    for newGoal in reachersIndexes:
        result, newPath = dfs(NN, initialNode, newGoal.item(0), np.append(path, newGoal) )
        if result:
            return True, newPath
        
    return False, None



    
    
    if initialNode in reachersIndexes:
        return initialNode
    else:
        print('no')
