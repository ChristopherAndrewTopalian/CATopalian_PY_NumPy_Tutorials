# boolean_masking.py

import numpy as np

def main():
    print("1. 1D Boolean Masking (Thermal Anomaly Detection)")
    # A drone scans a line of ocean water. Most temps are freezing (around 32F).
    # A human body will register much higher (around 98F).
    ocean_scan = np.array([32, 33, 31, 98, 32, 97, 34])
    print("Raw Ocean Scan   :", ocean_scan)

    # Step A: Create the "Mask" (Ask the true/false question)
    # This instantly creates an array of True/False values
    is_survivor = ocean_scan > 90
    print("Logical Mask     :", is_survivor)

    # Step B: Apply the Mask
    # NumPy physically extracts only the data points where the mask is True
    survivors_found = ocean_scan[is_survivor]
    print("Anomalies Found  :", survivors_found)

    print("\n------------------------------------------------\n")

    print("2. 2D Boolean Replacement (Signal Cleanup)")
    # Imagine a 3x3 grid of sonar data. 
    # Any negative number is static/noise that we need to zero out.
    sonar_data = np.array([
        [ 15, -5,  22],
        [-10,  8,  14],
        [ 30, 25, -2]
    ])
    print("Raw Sonar Data:\n", sonar_data)

    # Instantly replace all negative numbers with 0 without a single loop!
    # "If sonar_data is less than 0, set it to 0"
    sonar_data[sonar_data < 0] = 0
    
    print("\nCleaned Sonar Data:\n", sonar_data)

if __name__ == '__main__':
    main()

####

'''
1. 1D Boolean Masking (Thermal Anomaly Detection)
Raw Ocean Scan   : [32 33 31 98 32 97 34]
Logical Mask     : [False False False  True False  True False]
Anomalies Found  : [98 97]

------------------------------------------------

2. 2D Boolean Replacement (Signal Cleanup)
Raw Sonar Data:
 [[ 15  -5  22]
 [-10   8  14]
 [ 30  25  -2]]

Cleaned Sonar Data:
 [[15  0 22]
 [ 0  8 14]
 [30 25  0]]
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

