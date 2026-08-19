# scalars_vectors_matrices.py

import numpy as np

def main():
    print("0D: The Scalar")
    # A single number
    scalar = np.array(5)
    print("Scalar:\n", scalar)

    print("\n1D: The Vector")
    # A single row of data
    vector = np.array([10, 20, 30])
    print("Vector:\n", vector)

    print("\n2D: The Matrix")
    # A grid of data (lists inside a list)
    matrix = np.array([
        [1, 2, 3],
        [4, 5, 6]
    ])
    print("Matrix:\n", matrix)

    print("\nVectorization (The Magic)")
    # Multiply every number in the grid by 10 instantly
    multiplied = matrix * 10
    print("Multiplied by 10:\n", multiplied)

if __name__ == '__main__':
    main()

####

'''
0D: The Scalar
Scalar:
 5

1D: The Vector
Vector:
 [10 20 30]

2D: The Matrix
Matrix:
 [[1 2 3]
 [4 5 6]]

Vectorization (The Magic)
Multiplied by 10:
 [[10 20 30]
 [40 50 60]]
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

