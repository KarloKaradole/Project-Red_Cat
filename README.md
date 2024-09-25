# Project Red Cat

## Overview
This project involves creating a program that processes 2D and 3D coordinates to check for geometric properties like whether given points form a rectangle or cuboid, and whether another point lies inside these shapes. The program is designed to handle both basic 2D scenarios and expanded 3D space, as well as being flexible to work with arbitrary dimensions.

---

## Assignment

### 2D Task (Simple):

1. **Input**: The program takes as input the 2D coordinates of points A, B, C, and X from a file.
2. **Rectangle Check**: 
   - Verify if points A, B, and C can form the vertices of a rectangle (or square).
   - If they cannot, the program will stop and inform the user of the error in a controlled manner.
3. **Point Location**: 
   - Check if point X lies inside the rectangle (or square) ABC and inform the user of the result.
4. **Diagonal Calculation**: 
   - Calculate and display the diagonal length of the rectangle (or square).

### Additional Requirements:
- **Rectangle Type Recognition**: Based on the points A, B, and C, the program must dynamically recognize whether the shape is a rectangle or square. Depending on the type, the program will dynamically determine which classes or functions to call for execution.
  
---

### 3D Task (Advanced):

1. **Description**:
   - Extend the program to take as input points A, B, C, D, and X in three dimensions.
   - Check if points A, B, C, and D can form the vertices of a cuboid.
   - Check if point X is inside the cuboid ABCD and calculate the spatial diagonal of the cuboid.

---

## Input and Output Examples

### Example 1 (2D):
- **Input**:  

A: 0, 0;
B: 5, 0;
C: 0, 5;
X: 2, 2

- **Output**:  

True

### Example 2 (3D):
- **Input**:  

A: 0, 0, 0;
B: 5, 0, 0;
C: 0, 3, 0;
D: 0, 0, 1;
X: 1, 1, 2


- **Output**:  

False


---

## Key Features
- **Dynamic Shape Recognition**: The program can recognize and differentiate between a rectangle, square, or cuboid based on the input points.
- **Point-in-Shape Detection**: Efficient algorithms are used to check if point X lies inside the specified shape (rectangle, cuboid, or higher-dimensional shapes).
- **Scalable Design**: The program is flexible and scalable to handle an arbitrary number of dimensions beyond the standard 2D and 3D scenarios.

---

## Key Skills Demonstrated:
- **Python 3.x**: Algorithm design, custom functions.
- **Advanced mathematics**: Use of the advanced mathematical thinking and modeling.
- **Problem-solving**: Breaking down complex problems into clear, efficient solutions.

---

## How to Use
1. Prepare a file with the coordinates of points A, B, C (and optionally D) and X.
2. Run the program, which will:
 - Read the coordinates from the file.
 - Perform the necessary checks and calculations.
 - Output whether the points form a valid shape and whether point X lies inside.

---

Thank you for visiting this repository. Feedback and suggestions are welcome!
 
