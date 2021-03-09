### Question 7 ###

# needed for floor()
import math
# needed for prod()
import numpy as np

# 7.1) b)
# given matrix dimensions and coordinates, convert to index
def coord_to_ind(L1, L2, x1, x2):
    I = x1 + (L1*x2)
    return I

# read/initialise the input and format the output
in_coord_7_1 = open('./input_coordinates_7_1.txt', 'r')
out_index_7_1 = open('./output_index_7_1.txt', 'w')
next(in_coord_7_1)
out_index_7_1.write('index\n')
for c in in_coord_7_1:
    x1 = int(c.split('\t')[0])
    x2 = int(c.split('\t')[1])
    # check that coordinates are within the matrix
    if x1 > 50 or x2 > 57:
        out_index_7_1.write('Coordinates are out of the bounds of this matrix\n')
    else:
        out_index_7_1.write(str(coord_to_ind(50, 57, x1, x2)) + '\n')
out_index_7_1.close()

# given matrix dimensions and index, convert to coordinates
def ind_to_coord(L1, L2, I):
    x1 = I % L1
    x2 = math.floor(I/L1)
    return (x1,x2)

# read/initialise the input and format the output
in_index_7_1 = open('./input_index_7_1.txt', 'r')
out_coord_7_1 = open('./output_coordinates_7_1.txt', 'w')
next(in_index_7_1)
out_coord_7_1.write('x1\tx2\n')
for i in in_index_7_1:
    I = int(i)
    # check that index lies within the matrix
    if I > (50*57-1):
        out_coord_7_1.write('Index is out of the bounds of this matrix\n')
    else:
        c = ind_to_coord(50, 57, I)
        out_coord_7_1.write(str(c[0]) + '\t')
        out_coord_7_1.write(str(c[1]) + '\n')
out_coord_7_1.close()

# 7.2) b)
# given matrix dimensions and coordinates, convert to index
def coord_to_ind_6(L, x):
    I = x[0]
    for i in range(1, len(x)):
        mul = 1
        for j in range(i):
            mul *= L[j]
        I += mul * x[i]
    return I

# read/initialise the input and format the output
grid = [4, 8, 5, 9, 6, 7]
in_coord_7_2 = open('./input_coordinates_7_2.txt', 'r')
out_index_7_2 = open('./output_index_7_2.txt', 'w')
next(in_coord_7_2)
out_index_7_2.write('index\n')
for c in in_coord_7_2:
    x = c.rstrip().split('\t')
    x = list(map(int, x))
    diff = [grid - x for (grid, x) in zip(grid, x)]
    # check that coordinates are within the matrix
    if all(d >= 0 for d in diff):
        out_index_7_2.write(str(coord_to_ind_6(grid, x)) + '\n')
    else:
        out_index_7_2.write('Coordinates are out of the bounds of this matrix\n')
out_index_7_2.close()

# given matrix dimensions and index, convert to coordinates
def ind_to_coord_6(L, I):
    x = [0] * 6
    for i in range(len(x)):
        div = 1
        for j in range(i):
            div *= L[j]
        mod = div * L[i]
        x[i] = math.floor((I % mod)/div)
    return x

# read/initialise the input and format the output
in_index_7_2 = open('./input_index_7_2.txt', 'r')
out_coord_7_2 = open('./output_coordinates_7_2.txt', 'w')
next(in_index_7_2)
out_coord_7_2.write('x1\tx2\tx3\tx4\tx5\tx6\n')
for i in in_index_7_2:
    I = int(i)
    c = ind_to_coord_6(grid, I)
    # check that index lies within the matrix
    if I > (np.prod(grid)-1):
        out_coord_7_2.write('Index is out of the bounds of this matrix\n')
    else:
        for j in range(5):
            out_coord_7_2.write(str(c[j]) + '\t')
        out_coord_7_2.write(str(c[5]) + '\n')
out_coord_7_2.close()