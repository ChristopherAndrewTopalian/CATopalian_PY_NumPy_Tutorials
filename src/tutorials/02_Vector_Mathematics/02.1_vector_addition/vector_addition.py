# vector_addition.py

import numpy as np

def main():
    print("1. Basic Vector Addition (Combining Sensors)")
    # Imagine these are readings from two different sensor arrays
    sensor_a = np.array([10, 20, 30])
    sensor_b = np.array([1, 2, 3])
    
    # NumPy instantly adds index 0 to index 0, index 1 to index 1, etc.
    combined_sensors = sensor_a + sensor_b
    print("Sensor A:      ", sensor_a)
    print("Sensor B:      ", sensor_b)
    print("Combined total:", combined_sensors)

    print("\n------------------------------------------------\n")

    print("2. Spatial Math (Drone Trajectory in 3D Space)")
    # [X, Y, Z] coordinates
    # X = East/West | Y = North/South | Z = Altitude
    
    current_location = np.array([100, 50, 400])
    print("Starting Location [X, Y, Z]:", current_location)
    
    # The drone moves 50 units East, 0 units North, and drops 20 units in Altitude
    movement_vector = np.array([50, 0, -20])
    print("Movement Vector            :", movement_vector)
    
    # Calculate the exact new location in one seamless operation
    new_location = current_location + movement_vector
    print("New Exact Location         :", new_location)

if __name__ == '__main__':
    main()

####

'''
1. Basic Vector Addition (Combining Sensors)
Sensor A:       [10 20 30]
Sensor B:       [ 1  2  3]
Combined total: [11 22 33]

------------------------------------------------

2. Spatial Math (Drone Trajectory in 3D Space)
Starting Location [X, Y, Z]: [100  50 400]
Movement Vector            : [ 50   0 -20]
New Exact Location         : [150  50 380]
'''

####

# Dedicated to God the Father
# All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026
# https://github.com/ChristopherAndrewTopalian
# https://github.com/ChristopherTopalian
# https://sites.google.com/view/CollegeOfScripting

