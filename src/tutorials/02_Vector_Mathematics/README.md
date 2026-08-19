# Chapter 2: Vector Mathematics

In the physical world, a "Vector" represents two things: a direction and a magnitude (how hard or fast it is moving in that direction). In the digital world, we represent vectors as 1D arrays of numbers, usually mapped to coordinates like `[X, Y, Z]`.

If an autonomous search drone is hovering at a specific GPS location, and a sudden gust of wind pushes it, how does the onboard computer calculate its new location? 

It uses **Vector Addition**.

---

## The Speed of Vector Math

If you want to combine two datasets in standard Python, you have to write a loop to add the first numbers together, then the second numbers, then the third. 

In NumPy, you simply use the `+` symbol between two arrays. 

NumPy aligns the arrays and instantly adds the corresponding numbers together at the exact same time. This parallel processing is what allows real-time flight controllers to calculate thousands of physics adjustments per second without freezing.

### Lesson 02.1: Vector Addition and Spatial Math
In this lesson, we will simulate a drone's movement in 3D space `[X, Y, Z]`.
*   **Vector 1** will be the drone's starting coordinates.
*   **Vector 2** will be the movement vector (the direction and distance it travels).
*   By adding them together instantly, we output the drone's exact new location.

### Your Mission
Open `02.1_vector_addition.py` and run it. Notice how clean the syntax is when you allow the hardware to handle the mathematics.

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

