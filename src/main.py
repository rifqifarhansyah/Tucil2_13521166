from calculation import *
from visualization import *
import time

if __name__ == "__main__":
    print("\033[1;31m" + "=================================================" + "\033[0m")
    print("\033[1;32m" + "          CLOSEST PAIR PROBLEM SOLVER           " + "\033[0m")
    print("\033[1;31m" + "             M. Rifqi F / 13521166              " + "\033[0m")
    print("\033[1;31m" + "=================================================" + "\033[0m")

    print("\033[1;33m")
    count = int(input(">> Masukkan jumlah tuple: "))
    dimension = int(input(">> Masukkan dimensi vektor: "))
    print("\033[0m")

    print("\033[1;34m")
    minVal = int(input(">> Masukkan nilai minimum: "))
    maxVal = int(input(">> Masukkan nilai maksimum: "))
    print("\033[0m")

    while(minVal >= maxVal):
        print("Nilai minimum harus lebih kecil dari nilai maksimum!")
        print("\033[1;34m")
        minVal = int(input(">> Masukkan nilai minimum: "))
        maxVal = int(input(">> Masukkan nilai maksimum: "))
        print("\033[0m")

    vectorList = inputRandom(count, dimension, minVal, maxVal)
    
    # DIVIDE AND CONQUER
    # catat waktu awal
    start_time = time.time()
    d, res1, res2 = closestPairDNC(vectorList, count)
    # catat waktu selesai
    end_time = time.time()
    # hitung selisih waktu
    total_time = end_time - start_time
    print("\033[1;32m")
    print(f"Jarak terdekat Divide and Conquer: {d:.2f}")
    print(f"Pasangan titik terdekat Divide and Conquer: {res1}, {res2}")
    print("Waktu yang diperlukan Divide and Conquer:", total_time, "detik")
    print("\033[0m")

    print("\033[1;31m" + "=================================================" + "\033[0m")
    # BRUTO FORCE
    # catat waktu awal
    start_time = time.time()
    best_dist, res1, res2 = closestPairBruteForce(vectorList)
    # catat waktu selesai
    end_time = time.time()
    # hitung selisih waktu
    total_time = end_time - start_time
    print("\033[1;31m")
    print(f"Jarak terdekat Brute Force: {best_dist:.2f}")
    print(f"Pasangan titik terdekat Brute Force: {res1, res2}")
    print("Waktu yang diperlukan Brute Force:", total_time, "detik")
    print("\033[0m")
    print("\033[1;31m" + "=================================================" + "\033[0m")
    if(dimension == 3 or dimension == 2):
        print("\033[1;33m")
        show = input(">> Apakah Anda ingin menampilkan grafik? (y/n): ")
        print("\033[0m")
        while(show != "y" and show != "n"):
            print("Input tidak valid!")
            print("\033[1;33m")
            show = input(">> Apakah Anda ingin menampilkan grafik? (y/n): ")
            print("\033[0m")
        if(show == "y"):
            if (dimension == 3):
                show3d(vectorList, res1, res2)
            if (dimension == 2):
                show2d(vectorList, res1, res2)
        else:
            print("Grafik tidak ditampilkan.")
    print("\033[1;31m" + "Thank You" + "\033[0m")