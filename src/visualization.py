from typing import List
import math
import random
import matplotlib.pyplot as plt
import time

def show3d(vectorList, res1, res2):
    # create 3D object axes
    fig = plt.figure()
    ax = fig.add_subplot(111, projection='3d')
    # Adding points to the plot
    for point in vectorList:
        if point == res1 or point == res2:
            ax.scatter(point[0], point[1], point[2], c = "green") # green marker used for closest points
        else:
            ax.scatter(point[0], point[1], point[2], c = "red") # red marker used for other points
    # Adding line to the plot
    xs = [res1[0], res2[0]]
    ys = [res1[1], res2[1]]
    zs = [res1[2], res2[2]]
    ax.plot(xs, ys, zs, c="green") # green line to connect closest points
    
    plt.show()

def show2d(vectorList, res1, res2):
    # create 2D object axes
    fig = plt.figure()
    ax = fig.add_subplot(111)
    # Adding points to the plot
    for point in vectorList:
        if point == res1 or point == res2:
            ax.scatter(point[0], point[1], c = "green") # green marker used for closest points
        else:
            ax.scatter(point[0], point[1], c = "red") # red marker used for other points
    # Adding line to the plot
    ax.plot([res1[0], res2[0]], [res1[1], res2[1]], c="green") # green line to connect closest points
    plt.show()