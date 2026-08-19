# Lesson 03.1: Boolean Masking and Instant Filtering

If you have an array of 10,000 temperature readings and you want to find the ones that are dangerously high, standard programming requires you to examine each one individually. 

In digital physics, we don't look for the data. We force the data to reveal itself.

---

## The Concept: The Logical Mask

**Boolean Masking** happens in two steps:
1. **The Question:** You ask the entire array a mathematical question (e.g., `array > 90`). 
2. **The Mask:** NumPy instantly returns a new array of the exact same shape, filled entirely with `True` or `False`. This is the "Mask."
3. **The Extraction:** When you apply that Mask back onto the original array, NumPy acts like a physical sieve, letting the `True` data pass through while blocking the `False` data.

---

## Real-World Applications

### 1. Target Detection (Extraction)
Imagine a rescue drone flying over the ocean at night. The water temperature is a steady 32 degrees. The drone's thermal array scans a line of water: `[32, 33, 31, 98, 32]`.
*   We apply the mask: `ocean_scan > 90`.
*   NumPy instantly returns: `[False, False, False, True, False]`.
*   When we apply this mask to the data, the freezing water vanishes, leaving only the `[98]` degree anomaly. The drone has found the survivor.

### 2. Signal Cleanup (Replacement)
Sensors are not perfect. A sonar ping might return a negative number due to hardware static. If we try to run math on a negative distance, the drone's navigation will crash.
*   Instead of writing a loop to check every number, NumPy allows us to assign a value to a condition.
*   By writing `sonar_data[sonar_data < 0] = 0`, the hardware instantly locates every negative number in the entire grid and rewrites it to `0`. The noise is silenced in a fraction of a millisecond.

---

### Your Mission
Open the `03.1_boolean_masking.py` script. 

Watch how we use logic operators (`>` and `<`) to bend the dataset to our will. Notice how the code reads almost exactly like a plain English sentence: *"Ocean scan, where ocean scan is greater than 90."*

---

// Dedicated to God the Father  
// All Rights Reserved Christopher Andrew Topalian Copyright 2000-2026  
// https://github.com/ChristopherAndrewTopalian  
// https://github.com/ChristopherTopalian  
// https://sites.google.com/view/CollegeOfScripting

