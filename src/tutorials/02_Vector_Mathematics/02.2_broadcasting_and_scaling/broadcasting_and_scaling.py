# broadcasting_and_scaling.py

import numpy as np

def main():
    print("1. Scaling a 1D Vector (Audio Amplification)")
    # Imagine this is a tiny snippet of a digital audio wave
    audio_wave = np.array([20, 40, 15, -10, 5])
    print("Original Audio Wave :", audio_wave)
    
    # To double the volume, we multiply the entire array by a Scalar (2).
    # NumPy 'broadcasts' the 2 to every single element instantly.
    amplified_wave = audio_wave * 2
    print("Amplified Audio Wave:", amplified_wave)

    print("\n------------------------------------------------\n")

    print("2. Broadcasting across a 2D Matrix (Sensor Calibration)")
    # Imagine a 3x3 grid of thermal sensors on a rescue drone.
    # The factory calibration is off by exactly 5 degrees.
    sensor_grid = np.array([
        [70, 72, 71],
        [68, 69, 70],
        [73, 74, 75]
    ])
    print("Original Sensor Grid:\n", sensor_grid)

    # Add 5 to every sensor simultaneously without writing a loop
    calibrated_grid = sensor_grid + 5
    print("\nCalibrated Sensor Grid (+5):\n", calibrated_grid)

if __name__ == '__main__':
    main()

####

'''
1. Scaling a 1D Vector (Audio Amplification)
Original Audio Wave : [ 20  40  15 -10   5]
Amplified Audio Wave: [ 40  80  30 -20  10]

------------------------------------------------

2. Broadcasting across a 2D Matrix (Sensor Calibration)
Original Sensor Grid:
 [[70 72 71]
 [68 69 70]
 [73 74 75]]

Calibrated Sensor Grid (+5):
 [[75 77 76]
 [73 74 75]
 [78 79 80]]
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

