from calculation import closestPairDNC, closestPairBruteForce, inputRandom
from visualization import *
import time
import os


if __name__ == "__main__":
    PATH = os.path.dirname(os.path.realpath(__file__))
    mainLagi = True
    while(mainLagi == True):
        print("\033[1;31m" + "==================================================================================================" + "\033[0m")
        print("\033[1;35m" + "              .d88b 8    .d88b. .d88b. 8888 .d88b. 88888    888b.    db    888 888b. ")
        print("              8P    8    8P  Y8 YPwww. 8www YPwww.   8      8  .8   dPYb    8  8  .8 ")
        print("              8b    8    8b  d8     d8 8        d8   8      8wwP'  dPwwYb   8  8wwK' ")
        print("              `Y88P 8888 `Y88P' `Y88P' 8888 `Y88P'   8      8     dP    Yb 888 8  Yb " + "\033[0m")
        print("\033[1;32m" + "              P    R    O    B    L    E    M             S    O    L    V    E    R               " + "\033[0m")
        print("\033[1;36m" + "                                  by : M. Rifqi F. / 13521166              " + "\033[0m")
        print("\033[1;31m" + "==================================================================================================" + "\033[0m")

        print("\033[1;33m")
        count = int(input(">> Masukkan jumlah tuple: "))
        dimension = int(input(">> Masukkan dimensi vektor: "))
        print("\033[0m")

        while(count < 2 or dimension < 0):
            print("\033[1;31m" + "Jumlah tuple dan dimensi vektor tidak valid!" + "\033[0m")
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
        # waktu awal 
        start_time = time.time()
        # perhitungan jarak terdekat
        counterDivideAndConquer = [0]
        d, res1, res2 = closestPairDNC(vectorList, count, counterDivideAndConquer)
        # waktu selesai
        end_time = time.time()
        # selisih waktu
        total_time = end_time - start_time
        print("\033[1;32m")
        print("                                        Divide and Conquer")
        print(f"Jarak terdekat\t\t: {d:.2f}")
        print(f"Pasangan titik terdekat\t: {res1}, {res2}")
        print(f"Jumlah operasi\t\t: {counterDivideAndConquer[0]}")
        print("Waktu yang diperlukan\t:", total_time, "detik")
        print("\033[0m")

        print("\033[1;31m" + "==================================================================================================" + "\033[0m")
        # BRUTE FORCE
        # waktu awal
        start_time = time.time()
        # perhitungan jarak terdekat
        counterBruteForce = int((len(vectorList)-1) * len(vectorList) / 2)
        best_dist, res3, res4 = closestPairBruteForce(vectorList)
        # waktu selesai
        end_time = time.time()
        # selisih waktu
        time_total = end_time - start_time
        print("\033[1;35m")
        print("                                             Brute Force ")
        print(f"Jarak terdekat\t\t: {best_dist:.2f}")
        print(f"Pasangan titik terdekat\t: {res3, res4}")
        print(f"Jumlah operasi\t\t: {counterBruteForce}")
        print("Waktu yang diperlukan\t:", time_total, "detik")
        print("\033[0m")

        # membuka file teks baru untuk menulis
        with open(f"{PATH}/output/output.txt", "w") as f:
            # menuliskan hasil keluaran ke dalam file
            f.write(f"==================================================================================================\n")
            f.write(f"Jumlah tuple\t\t\t: {count}\n")
            f.write(f"Dimensi vektor\t\t\t: {dimension}\n")
            f.write(f"Nilai minimum\t\t\t: {minVal}\n")
            f.write(f"Nilai maksimum\t\t\t: {maxVal}\n")
            f.write(f"==================================================================================================\n")
            f.write(f"                                        Divide and Conquer\n")
            f.write(f"Jarak terdekat\t\t\t: {d:.2f}\n")
            f.write(f"Pasangan titik terdekat\t: {res1}, {res2}\n")
            f.write(f"Jumlah operasi\t\t\t: {counterDivideAndConquer[0]}\n")
            f.write(f"Waktu yang diperlukan\t: {total_time} detik\n")
            f.write(f"==================================================================================================\n")
            f.write(f"                                            Brute Force \n")
            f.write(f"Jarak terdekat\t\t\t: {best_dist:.2f}\n")
            f.write(f"Pasangan titik terdekat\t: {res3, res4}\n")
            f.write(f"Jumlah operasi\t\t\t: {counterBruteForce}\n")
            f.write(f"Waktu yang diperlukan\t: {time_total} detik\n")
            f.write(f"==================================================================================================\n")

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
    print("\033[1;32m" + "                                        Thank You :)" + "\033[0m")
    print("\033[1;31m" + "==================================================================================================" + "\033[0m")