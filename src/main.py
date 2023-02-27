from calculation import *
from visualization import *
import time

if __name__ == "__main__":
    mainLagi = True
    while(mainLagi == True):
        print("\033[1;31m" + "==================================================================================================" + "\033[0m")
        print("\033[1;32m" + "                                  CLOSEST PAIR PROBLEM SOLVER           " + "\033[0m")
        print("\033[1;36m" + "                                  by : M. Rifqi F. / 13521166              " + "\033[0m")
        print("\033[1;31m" + "==================================================================================================" + "\033[0m")

        print("\033[1;33m")
        count = int(input(">> Masukkan jumlah tuple: "))
        dimension = int(input(">> Masukkan dimensi vektor: "))
        print("\033[0m")

        print("\033[1;34m")
        minVal = int(input(">> Masukkan nilai minimum: "))
        maxVal = int(input(">> Masukkan nilai maksimum: "))
        print("\033[0m")

        while(minVal >= maxVal):
            print("\033[1;31m" + "Nilai minimum harus lebih kecil dari nilai maksimum!" + "\033[0m")
            print("\033[1;34m")
            minVal = int(input(">> Masukkan nilai minimum: "))
            maxVal = int(input(">> Masukkan nilai maksimum: "))
            print("\033[0m")

        vectorList = inputRandom(count, dimension, minVal, maxVal)
        # print a message to inform the user that the generated vectors have been saved to "input.txt"
        print("\033[1;36m" + "Point-point hasil input random telah disimpan dalam file input.txt pada folder input" + "\033[0m")
        print("\033[1;31m" + "==================================================================================================" + "\033[0m")
        
        # DIVIDE AND CONQUER
        # catat waktu awal
        start_time = time.time()
        d, res1, res2 = closestPairDNC(vectorList, count)
        # catat waktu selesai
        end_time = time.time()
        # hitung selisih waktu
        total_time = end_time - start_time
        print("\033[1;32m")
        print(f"Jarak terdekat Divide and Conquer\t\t: {d:.2f}")
        print(f"Pasangan titik terdekat Divide and Conquer\t: {res1}, {res2}")
        print("Waktu yang diperlukan Divide and Conquer\t:", total_time, "detik")
        print("\033[0m")

        print("\033[1;31m" + "==================================================================================================" + "\033[0m")
        # BRUTE FORCE
        # catat waktu awal
        start_time = time.time()
        best_dist, res1, res2 = closestPairBruteForce(vectorList)
        # catat waktu selesai
        end_time = time.time()
        # hitung selisih waktu
        total_time = end_time - start_time
        print("\033[1;35m")
        print(f"Jarak terdekat Brute Force\t\t\t: {best_dist:.2f}")
        print(f"Pasangan titik terdekat Brute Force\t\t: {res1, res2}")
        print("Waktu yang diperlukan Brute Force\t\t:", total_time, "detik")
        print("\033[0m")

        print("\033[1;31m" + "==================================================================================================" + "\033[0m")
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
        print("\033[1;34m")
        main = input(">> Apakah Anda ingin main lagi? (y/n): ")
        print("\033[0m")
        while(main != "y" and main != "n"):
            print("\033[1;31m" + "Input tidak valid!" + "\033[0m")
            print("\033[1;34m")
            main = input(">> Apakah Anda ingin mulai lagi? (y/n): ")
            print("\033[0m")
        if(main == "n"):
            mainLagi = False
    print("\033[1;31m" + "==================================================================================================" + "\033[0m")
    print("\033[1;31m" + "                                        Thank You :)" + "\033[0m")
    print("\033[1;31m" + "==================================================================================================" + "\033[0m")