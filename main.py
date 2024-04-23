import math
import os

def read_coordinates(filename):
    """Read coordinates from a file and return them as a list of tuples."""
    with open(filename, 'r') as file:
        lines = file.readlines()
    coordinates = [tuple(map(float, line.strip().split())) for line in lines]
    return coordinates

def are_perpendicular(p1, p2, p3):
    """Check if the line segments between p1-p2 and p2-p3 are perpendicular."""
    vec_p1p2 = (p2[0] - p1[0], p2[1] - p1[1])
    vec_p2p3 = (p3[0] - p2[0], p3[1] - p2[1])
    dot_product = vec_p1p2[0] * vec_p2p3[0] + vec_p1p2[1] * vec_p2p3[1]
    return math.isclose(dot_product, 0, abs_tol=1e-9)

def check_rectangle_formation(A, B, C):
    """Check if three points can form a rectangle, and return the diagonal points if true."""
    
    """dAB = math.dist(A, B)
    dBC = math.dist(B, C)
    dCA = math.dist(C, A)"""
    if are_perpendicular(A, B, C) and """dAB == dBC""":
        return (A, C)
    elif are_perpendicular(B, C, A) and """dBC == dCA""":
        return (B, A)
    elif are_perpendicular(C, A, B) and """dCA == dAB""":
        return (B, C)
    return None

def calculate_diagonal(opposite_point1, opposite_point2):
    """Calculate the diagonal of the rectangle from two opposite points."""
    return math.dist(opposite_point1, opposite_point2)

def point_inside_rectangle(A, B, C, X):
    """Check if point X is inside the triangle ABC, used to approximate rectangle inclusion."""
    def sign(p1, p2, p3):
        return (p1[0] - p3[0]) * (p2[1] - p3[1]) - (p2[0] - p3[0]) * (p1[1] - p3[1])
    d1 = sign(X, A, B)
    d2 = sign(X, B, C)
    d3 = sign(X, C, A)
    has_neg = (d1 < 0) or (d2 < 0) or (d3 < 0)
    has_pos = (d1 > 0) or (d2 > 0) or (d3 > 0)
    return not (has_neg and has_pos)

def calculate_point_d(A, B, C, right_angle_point):
    """Calculate the fourth point D in a rectangle, given points A, B, and C,
       and the point label ('A', 'B', or 'C') that has the right angle."""

    # Determine vectors based on the right angle location
    if right_angle_point == 'A':
        # Vectors BA and CA
        vec1 = (A[0] - B[0], A[1] - B[1])  # Vector from B to A
        vec2 = (A[0] - C[0], A[1] - C[1])  # Vector from C to A
        origin = A
        other1 = B
        other2 = C
    elif right_angle_point == 'B':
        # Vectors AB and CB
        vec1 = (B[0] - A[0], B[1] - A[1])  # Vector from A to B
        vec2 = (B[0] - C[0], B[1] - C[1])  # Vector from C to B
        origin = B
        other1 = A
        other2 = C
    elif right_angle_point == 'C':
        # Vectors AC and BC
        vec1 = (C[0] - A[0], C[1] - A[1])  # Vector from A to C
        vec2 = (C[0] - B[0], C[1] - B[1])  # Vector from B to C
        origin = C
        other1 = A
        other2 = B

    # Calculate perpendicular vectors
    perp1 = (-vec1[1], vec1[0])  # Perpendicular to vec1
    perp2 = (-vec2[1], vec2[0])  # Perpendicular to vec2

    a, b, c, d = perp1[0], -perp2[0], perp1[1], -perp2[1]
    e, f = other2[0] - other1[0], other2[1] - other1[1]
    det = a * d - b * c
    if det == 0:
        raise ValueError("Lines do not intersect, cannot form a rectangle")

    # Cramer's rule
    t = (e * d - b * f) / det

    # Calculate D using parameter t in one of the line equations
    D_x = other1[0] + t * perp1[0]
    D_y = other1[1] + t * perp1[1]

    return (D_x, D_y)

def main():
    filename = input("Enter the filename containing the coordinates: ")
    try:
        coordinates = read_coordinates(filename)
        if len(coordinates) < 4:
            print("Not enough points provided.")
            return

        A, B, C, X = coordinates[:4]
        diagonal_points = check_rectangle_formation(A, B, C)
        if diagonal_points:
            print("Given points can be part of the rectangle.")
            #point_d = calculate_point_d(A, B, C, right_angle_point)
            diagonal_length = calculate_diagonal(*diagonal_points)
            inside = point_inside_rectangle(A, B, C, X)
            print(f"The diagonal of the rectangle is: {diagonal_length}")
            print(f"Point X inside the triangle approximation of rectangle: {inside}")
        else:
            print("Given points cannot be part of the rectangle.")
    except FileNotFoundError:
        print("File not found. Please ensure the filename is correct and the file exists in the specified path.")
    except Exception as e:
        print(f"An error occurred: {e}")

if __name__ == "__main__":
    os.system("cls")
    main()
