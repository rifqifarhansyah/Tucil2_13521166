from typing import List
import math
import random
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
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
            
def findClosestPair(P: List, n: int):
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
    d1, p1, p2 = findClosestPair(S1, mid+(n%2))
    d2, q1, q2 = findClosestPair(S2, n-(mid+(n%2)))
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
    # print a message to inform the user that the generated vectors have been saved to "input.txt"
    print("Titik-titik hasil input acak telah disimpan dalam file input.txt.")
    return vectorList

def findClosestPairES(P):
    n = len(P)
    best_dist = float('inf')
    best_pair = None
    for i in range(n):
        for j in range(i+1, n):
            dist = euclideanDistance(P[i], P[j])
            if dist < best_dist:
                best_dist = dist
                best_pair = (P[i], P[j])
                
    print(f"Jarak terdekat Brute Force: {best_dist:.2f}")
    print(f"Pasangan titik terdekat Brute Force: {best_pair}")
    # return best_pair, best_dist

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

if __name__ == "__main__":
    count = int(input("Masukkan jumlah tuple: "))
    dimension = int(input("Masukkan dimensi vektor: "))
    minVal = int(input("Masukkan nilai minimum: "))
    maxVal = int(input("Masukkan nilai maksimum: "))
    while(minVal >= maxVal):
        print("Nilai minimum harus lebih kecil dari nilai maksimum!")
        minVal = int(input("Masukkan nilai minimum: "))
        maxVal = int(input("Masukkan nilai maksimum: "))
    vectorList = inputRandom(count, dimension, minVal, maxVal)
    
    # catat waktu awal
    start_time = time.time()
    
    d, res1, res2 = findClosestPair(vectorList, count)
    
    # catat waktu selesai
    end_time = time.time()

    # hitung selisih waktu
    total_time = end_time - start_time

    print(f"Jarak terdekat Divide and Conquer: {d:.2f}")
    print(f"Pasangan titik terdekat Divide and Conquer: {res1}, {res2}\n")
    print("Waktu yang diperlukan Divide and Conquer:", total_time, "detik")

    # d = cari_distance_terdekat(vectorList)
    # print(d)

    # catat waktu awal
    start_time = time.time()

    findClosestPairES(vectorList)

    # catat waktu selesai
    end_time = time.time()

    # hitung selisih waktu
    total_time = end_time - start_time

    print("Waktu yang diperlukan Brute Force:", total_time, "detik")

    if (dimension == 3):
        show3d(vectorList, res1, res2)
    
    if (dimension == 2):
        show2d(vectorList, res1, res2)