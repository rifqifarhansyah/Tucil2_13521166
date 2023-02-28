# Tugas Kecil 2 Strategi Algoritma 2022/2023
<h2 align="center">
  🧩 Closest Pair Problem Solution 🧩<br/>
</h2>
<hr>

## Table of Contents
1. [General Info](#general-information)
2. [Creator Info](#creator-information)
3. [Features](#features)
4. [Technologies Used](#technologies-used)
5. [Setup](#setup)
6. [Usage](#usage)
7. [Screenshots](#screenshots)
7. [Structure](#structure)
8. [Project Status](#project-status)
9. [Room for Improvement](#room-for-improvement)
10. [Acknowledgements](#acknowledgements)
11. [Contact](#contact)

<a name="general-information"></a>

## General Information
A simple program to solve the closest pair problem. The program will take a number of tuples, dimension, and set of points (randomize by system) as input and will output the closest pair of points. Program will also output the number of euclidean distance steps calculation, distance between the points, and execution time of each algorithm. This project is based on the Divide and Conquer Algorithm (Brute Force Algorithm is just for reference) and write in python programming language (Command Line Interface).

<a name="creator-information"></a>

## Creator Information

| Nama                        | NIM      | E-Mail                      |
| --------------------------- | -------- | --------------------------- |
| Mohammad Rifqi Farhansyah   | 13521166 | 13521166@std.stei.itb.ac.id |

<a name="features"></a>

## Features
- Output `the closest pair` of the points
- Output the `number` of euclidean distance steps calculation
- Show the `execution time`
- Many `input item` (tuple, dimension, and range of the points)
- `Colorful output` (classificate by the bracket type)
- Save the output to a `txt` file

<a name="technologies-used"></a>

## Technologies Used
- python 3.9
- pip 22.3.1
- matplotlib 3.5.0

> Note: The version of the libraries above is the version that we used in this project. You can use the latest version of the libraries.

<a name="setup"></a>

## Setup
1. Download python 3.9 from [here](https://www.python.org/downloads/).
2. Download pip 22.3.1 from [here](https://pypi.org/project/pip/).
3. Download matplotlib 3.5.0 from [here](https://pypi.org/project/matplotlib/).
4. Install the libraries above.
5. Clone this repository to your local directory by using this command:
```bash
git clone https://github.com/rifqifarhansyah/Tucil2_13521166.git
```
6. Change your directory to the directory of this project.
7. Go to the `src` directory.
8. Run the `main.py` file by using this command:
```bash
python main.py
```
9. Enjoy the program!

<a name="usage"></a>

## Usage
1. Input the number of tuples (number of points that you want to test). The number must greater than 1.
2. Input the dimension of the points (the dimension must greater than 0).
3. Input the range of the points (minimum and maximum value of the points).
4. System will generate the points randomly.
5. This program will write the set of points that have been generated randomly by system (placed in `src/input/input.txt`).
6. The program will show the closest pair of the points, number of euclidean distance steps calculation, and execution time of each algorithm.
7. You can see the visualization of the points by choose `y` in the `Apakah Anda ingin menampilkan grafik? (y/n)` question.
8. The output file will automatically saved in `src/output/output.txt`.

<a name="screenshots"></a>

## Screenshots
<p>
  <img src="/image/SS1.png/">
  <p>Figure 1. Main Menu</p>
  <nl>
  <img src="/image/SS2.png/">
  <p>Figure 2. The Closest Pair Solution (BF and DnC)</p>
  <nl>
  <img src="/image/SS3.png/">
  <p>Figure 3. Example of the points visualization (in 3D)</p>
  <nl>
  <img src="/image/SS4.png/">
  <p>Figure 4. Input txt file</p>
  <nl>
  <img src="/image/SS5.png/">
  <p>Figure 5. Output txt file</p>
  <nl>
</p>

<a name="structure"></a>

## Structure
```bash
│   README.md
│
├───doc
│       Tucil2_K2_13521166_MohammadRifqiFarhansyah.pdf
│
├───image
│       1000(2).png
│       1000(3).png
│       128(2).png
│       128(3).png
│       16(2).png
│       16(3).png
│       64(2).png
│       64(3).png
│       SS1.png
│       SS2.png
│       SS3.png
│       SS4.png
│       SS5.png
│
└───src
    │   calculation.py
    │   main.py
    │   visualization.py
    │
    ├───input
    │       input.txt
    │
    ├───output
    │       output.txt
    │
    └───__pycache__
            calculation.cpython-39.pyc
            visualization.cpython-39.pyc
```

<a name="project-status">

## Project Status
Project is: _complete_

<a name="room-for-improvement">

## Room for Improvement
Room for Improvement:
- Optimalization of the Closest Pair Problem Algorithm code
- Adding more features
- Create the better UI for this project

<a name="acknowledgements">

## Acknowledgements
- Thanks To Allah SWT
- This project was inspired by [Closest-Pair-Problem](
https://informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2010-2011/Makalah2010/MakalahStima2010-055.pdfhttps:/informatika.stei.itb.ac.id/~rinaldi.munir/Stmik/2010-2011/Makalah2010/MakalahStima2010-055.pdf)

<a name="contact"></a>

## Contact
<h4 align="center">
  Contact Me : mrifki193@gmail.com<br/>
  2023
</h4>
<hr>
