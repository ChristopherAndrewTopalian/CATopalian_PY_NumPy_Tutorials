# generating_grids_and_zeros.py

import numpy as np

def main():
    print("1. Generating an Empty Search Grid (Zeros)")
    # Creates a 5x5 grid filled with 0s. 
    # dtype=int ensures we get clean whole numbers instead of decimals (0.)
    search_grid = np.zeros((5, 5), dtype=int)
    print("5x5 Grid:\n", search_grid)

    print("\n2. Generating an Active Status Grid (Ones)")
    # Creates a 3x4 grid filled with 1s.
    # Useful for mathematical multipliers or setting all sensors to "Active"
    active_sensors = np.ones((3, 4), dtype=int)
    print("3x4 Grid:\n", active_sensors)

    print("\n3. Generating a Custom Filled Grid")
    # Creates a 4x4 grid filled entirely with the number 7.
    # Imagine 7 represents the ID for "Water" tiles in a game, 
    # or a baseline temperature for a thermal camera.
    water_map = np.full((4, 4), 7)
    print("4x4 Grid filled with 7:\n", water_map)

if __name__ == '__main__':
    main()

####

'''
1. Generating an Empty Search Grid (Zeros)
5x5 Grid:
 [[0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]
 [0 0 0 0 0]]

2. Generating an Active Status Grid (Ones)
3x4 Grid:
 [[1 1 1 1]
 [1 1 1 1]
 [1 1 1 1]]

3. Generating a Custom Filled Grid
4x4 Grid filled with 7:
 [[7 7 7 7]
 [7 7 7 7]
 [7 7 7 7]
 [7 7 7 7]]
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

