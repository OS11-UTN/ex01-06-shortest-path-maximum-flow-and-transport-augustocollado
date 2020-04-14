import numpy as np
import math

# My very first implementation of Dijkstra's algorithm

def dijkstra(NN):

    nodeCount = NN.shape[0]
    distances = np.array([math.inf] * nodeCount)
    distances.itemset(0, 0)
    precedents = np.zeros(NN[0].shape, dtype=int)
    
    currentNode = 0

    while currentNode < nodeCount:

        neighbors = np.argwhere(NN[currentNode])
        for neighbor in neighbors:

            if distances[neighbor] > distances[currentNode] + NN[currentNode][neighbor]:
                distances[neighbor] = distances[currentNode] + NN[currentNode][neighbor]
                precedents[neighbor] = currentNode
            
        currentNode = currentNode + 1

    return distances, precedents

