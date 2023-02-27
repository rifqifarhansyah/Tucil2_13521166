from typing import List
import math
import random
import matplotlib.pyplot as plt
import time

def euclideanDistance(p1, p2):
    # Initialize sum to zero
    sum = 0
    # Iterate over each dimension of the points
    for i in range(len(p1)):
        # Calculate the difference between the corresponding coordinates
        diff = p1[i] - p2[i]
        # Square the difference and add it to the sum
        sum += diff ** 2
    # Take the square root of the sum to get the Euclidean distance
    distance = math.sqrt(sum)
    return distance

def distanceOf3(P):
    # Calculate the distances between each pair of points using the Euclidean distance function
    d01 = euclideanDistance(P[0], P[1])
    d02 = euclideanDistance(P[0], P[2])
    d12 = euclideanDistance(P[1], P[2])
    # Compare the distances to find the minimum distance and the corresponding points
    if (d01 < d02):
        if (d01 < d12):
            # Distance between P[0] and P[1] is smallest
            return d01, P[0], P[1]
        else:
            # Distance between P[1] and P[2] is smallest
            return d12, P[1], P[2]
    else:
        if (d02 < d12):
            # Distance between P[0] and P[2] is smallest
            return d02, P[0], P[2]
        else: 
            # Distance between P[1] and P[2] is smallest
            return d12, P[1], P[2]
            
def closestPairDNC(P: List, n: int):
# Base case when there are only two points
    # P = P.sort(key=lambda x: x[0])
    P = sorted(P, key=lambda x: x[0])
    # print(P)
    if n == 2:
        d = euclideanDistance(P[0], P[1])
        return d, P[0], P[1]
    if n == 3:
        return distanceOf3(P)
    # Divide the set into two halves
    mid = n // 2
    S1 = P[:(mid+(n%2))]
    S2 = P[(mid+(n%2)):]
    # Recursive calls to find the closest pair in each half
    d1, p1, p2 = closestPairDNC(S1, mid+(n%2))
    d2, q1, q2 = closestPairDNC(S2, n-(mid+(n%2)))
    d, p1, p2 = (d1, p1, p2) if d1 < d2 else (d2, q1, q2)
    # Find the minimum distance between the two halves
    d = min(d1, d2)
    # Check for closest pair across the two halves
    # result = []
    closest_pair = (d, p1, p2)
    strip = []
    for i in range(n):
        if abs(P[i][0] - P[mid+(n%2)][0]) < d:
            strip.append(P[i])
    strip.sort(key=lambda x: x[1])
    size = len(strip)
    for i in range(size):
        for j in range(i+1, size):
            if strip[j][1] - strip[i][1] >= d:
                continue
            else:
                distance = euclideanDistance(strip[i],strip[j])
                d = min(d, distance)
                if (d == distance):
                    closest_pair = (d,strip[i],strip[j])
    return closest_pair

def closestPairBruteForce(P):
    # Calculate the length of the input list
    n = len(P)
    # Set initial values for the best distance and best pair
    best_dist = float('inf')
    best_pair = None
    # Loop through all pairs of points and calculate their distance
    for i in range(n):
        for j in range(i+1, n):
            dist = euclideanDistance(P[i], P[j])
            # If the distance between the pair of points is less than the best distance,
            # update the best distance and best pair
            if dist < best_dist:
                best_dist = dist
                best_pair = (P[i], P[j])
    # Return the best distance and the two points that form the best pair
    return best_dist, best_pair[0], best_pair[1]

def inputRandom(count, dimension, minVal, maxVal):
    vectorList = []
    # Generate a list of random vectors with the specified number of dimensions
    for i in range(count):
        vector = ()
        for j in range(dimension):
            vector += (random.randint(minVal, maxVal),)
        vectorList.append(vector)
    # Write the list of vectors to a file named "input.txt"
    with open("input.txt", "w") as outFile:
        outFile.write("Tuple\t:\t" + str(count) + "\n" + "Dimensi\t:\t" + str(dimension) + "\n")
        i = 1
        for vector in vectorList:
            outFile.write(str(i) + ".\t")
            for idx, component in enumerate(vector):
                if idx != len(vector) - 1:
                    outFile.write(str(component) + ", ")
                else:
                    outFile.write(str(component))
            outFile.write("\n")
            i += 1
    return vectorList