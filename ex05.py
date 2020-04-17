import numpy as np
from scipy.optimize import linprog
from basic_utils import nn2na
import math

def dfs(NN, initialNode, goalNode, path = np.array(0)):

    if initialNode == goalNode:
        return True, path

    goalReachers = NN[:,goalNode]
    reachersIndexes = np.argwhere(goalReachers)
    for newGoal in reachersIndexes:
        result, newPath = dfs(NN, initialNode, newGoal.item(0), np.append(path, newGoal) )
        if result:
            return True, newPath
        
    return False, None

def minimumArcValue(arcs, Capacity, path):
    minimum = math.inf
    toNode = path.item(0)
    for fromNode in path[1:]:
        index = getArcIndex(arcs, fromNode, toNode)
        if minimum > Capacity[index]:
            minimum = Capacity[index]
        toNode = fromNode
    return minimum

def changeResiduals(residuals, arcs, path, value, NN):
    toNode = path.item(0)
    for fromNode in path[1:]:
        index = getArcIndex(arcs, fromNode, toNode)
        residuals[0][index] = residuals[0][index] - value
        residuals[1][index] = residuals[1][index] + value
        if residuals[0][index] == 0:
            NN[fromNode][toNode] = 0

        toNode = fromNode
    return

def getArcIndex(arcs, fromNode, toNode):
    for index, arc in enumerate(arcs):
        if arc[0] == fromNode and arc[1] == toNode:
            return index
    return None

def FordFulkerson():

    # Node-node graph representation
    NN = np.array([
            [0, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, 0, 1],
            [0, 0, 0, 0, 1, 0],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 1],
            [0, 0, 0, 0, 0, 0],
    ])

    arcs = np.argwhere(NN)
    residuals = np.array( [[7, 1, 2, 3, 2, 1, 2], [0, 0, 0, 0, 0, 0, 0]] ) 

    existsPath, path = dfs(NN, 0, 5, np.array(5))
    while existsPath:
        value = minimumArcValue(arcs, residuals[0], path)
        changeResiduals(residuals, arcs, path, value, NN)
        existsPath, path = dfs(NN, 0, 5, np.array(5))

    print(residuals[0])
    print(residuals[1])
    return