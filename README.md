### Project-Red_Cat

# Assignment

Create a program that will take as input the 2D coordinates of points A, B, C, and X. The coordinates should be read from a file. The program should:
1. check if these three points can be vertices of a rectangle (square). If they cannot, the program must stop working in a controlled manner and inform the user of the error,
2. check if point X is inside the rectangle (square) ABC and inform the user of the result,
3. calculate the diagonal of the shape.

# Addition

• depending on the points A, B, and C, the program needs to recognize what type of rectangle it is (rectangle or cuboid) and dynamically determine which classes or functions will be called for execution

• expand the program to support the input of points A, B, C, D, and X, each with three dimensions. Let the program check if points A, B, C, and D can be vertices of a cuboid. Let it check if point X is inside the cuboid ABCD. Let it calculate the spatial diagonal.

• make the program work with an arbitrary number of dimensions from the previous task

# Input and Output Examples

Input:
0, 0
5, 0
0, 5
2, 2
Output:
True

Input:
0, 0, 0
5, 0, 0
0, 3, 0
0, 0, 1
1, 1, 2
Output:
False
 
