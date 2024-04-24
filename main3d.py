import math
import os
from collections import Counter

def read_coordinates(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
    coordinates = [tuple(map(float, line.strip().split())) for line in lines]
    return coordinates

def orthogonality3D(A, B, C, D):
    """Check for vector perpendicularity."""
    vectors = {
        'vec_AB': (B[0] - A[0], B[1] - A[1], B[2] - A[2]),
        'vec_AC': (C[0] - A[0], C[1] - A[1], C[2] - A[2]),
        'vec_AD': (D[0] - A[0], D[1] - A[1], D[2] - A[2]),
        'vec_BA': (A[0] - B[0], A[1] - B[1], A[2] - B[2]),
        'vec_BC': (C[0] - B[0], C[1] - B[1], C[2] - B[2]),
        'vec_BD': (D[0] - B[0], D[1] - B[1], D[2] - B[2]),
        'vec_CA': (A[0] - C[0], A[1] - C[1], A[2] - C[2]),
        'vec_CB': (B[0] - C[0], B[1] - C[1], B[2] - C[2]),
        'vec_CD': (D[0] - C[0], D[1] - C[1], D[2] - C[2]),
        'vec_DA': (A[0] - D[0], A[1] - D[1], A[2] - D[2]),
        'vec_DB': (B[0] - D[0], B[1] - D[1], B[2] - D[2]),
        'vec_DC': (C[0] - D[0], C[1] - D[1], C[2] - D[2])
    }
    
    dot_products = {
        'dot_AB_AC': vectors['vec_AB'][0] * vectors['vec_AC'][0] + vectors['vec_AB'][1] * vectors['vec_AC'][1] + vectors['vec_AB'][2] * vectors['vec_AC'][2],
        'dot_AB_AD': vectors['vec_AB'][0] * vectors['vec_AD'][0] + vectors['vec_AB'][1] * vectors['vec_AD'][1] + vectors['vec_AB'][2] * vectors['vec_AD'][2],
        'dot_AC_AD': vectors['vec_AC'][0] * vectors['vec_AD'][0] + vectors['vec_AC'][1] * vectors['vec_AD'][1] + vectors['vec_AC'][2] * vectors['vec_AD'][2],
    
        'dot_BA_BC': vectors['vec_BA'][0] * vectors['vec_BC'][0] + vectors['vec_BA'][1] * vectors['vec_BC'][1] + vectors['vec_BA'][2] * vectors['vec_BC'][2],
        'dot_BA_BD': vectors['vec_BA'][0] * vectors['vec_BD'][0] + vectors['vec_BA'][1] * vectors['vec_BD'][1] + vectors['vec_BA'][2] * vectors['vec_BD'][2],
        'dot_BC_BD': vectors['vec_BC'][0] * vectors['vec_BD'][0] + vectors['vec_BC'][1] * vectors['vec_BD'][1] + vectors['vec_BC'][2] * vectors['vec_BD'][2],
    
        'dot_CA_CB': vectors['vec_CA'][0] * vectors['vec_CB'][0] + vectors['vec_CA'][1] * vectors['vec_CB'][1] + vectors['vec_CA'][2] * vectors['vec_CB'][2],
        'dot_CA_CD': vectors['vec_CA'][0] * vectors['vec_CD'][0] + vectors['vec_CA'][1] * vectors['vec_CD'][1] + vectors['vec_CA'][2] * vectors['vec_CD'][2],
        'dot_CB_CD': vectors['vec_CB'][0] * vectors['vec_CD'][0] + vectors['vec_CB'][1] * vectors['vec_CD'][1] + vectors['vec_CB'][2] * vectors['vec_CD'][2],
   
        'dot_DA_DB': vectors['vec_DA'][0] * vectors['vec_DB'][0] + vectors['vec_DA'][1] * vectors['vec_DB'][1] + vectors['vec_DA'][2] * vectors['vec_DB'][2],
        'dot_DA_DC': vectors['vec_DA'][0] * vectors['vec_DC'][0] + vectors['vec_DA'][1] * vectors['vec_DC'][1] + vectors['vec_DA'][2] * vectors['vec_DC'][2],
        'dot_DB_DC': vectors['vec_DB'][0] * vectors['vec_DC'][0] + vectors['vec_DB'][1] * vectors['vec_DC'][1] + vectors['vec_DB'][2] * vectors['vec_DC'][2]
    }
    
    orthogonal_vec = []
    
    for key, value in dot_products.items():
        if math.isclose(value, 0, abs_tol=1e-3):
            orthogonal_vec.append(key)
        
    if len(orthogonal_vec) > 0:
        return True
        
    elif len(orthogonal_vec) == 0:
        dBC = math.dist(B, C)
        dAD = math.dist(A, D)
        
        if dBC == dAD:
            return True
        else:
            return False
    
def calculate_diagonal_3d(diagonal_point1, diagonal_point2, diagonal_point3):
    """Calculate the diagonal of the rectangle using two opposite points in initial triangle."""
    return math.dist(diagonal_point1, diagonal_point2)

def position_of_points(A, B, C, D):
    """Finding the fourth point of a rectangle given four points A, B, C and D. 
    Calculate coordinates using vector addition."""
    
    opposite_points = orthogonality3D(A, B, C, D)
    
    if opposite_points == (B, C):
        D = (B[0] + C[0] - A[0], B[1] + C[1] - A[1])
    elif opposite_points == (A, C):
        D = (A[0] + C[0] - B[0], A[1] + C[1] - B[1])
    elif opposite_points == (A, B):
        D = (A[0] + B[0] - C[0], A[1] + B[1] - C[1])
  
    return D

def point_X_inside_cuboid(A, B, C, X, D):
    """Determines if the point X is inside cuboid."""
    min_x = min(A[0], B[0], C[0], D[0])
    max_x = max(A[0], B[0], C[0], D[0])
    min_y = min(A[1], B[1], C[1], D[1])
    max_y = max(A[1], B[1], C[1], D[1])
    return min_x <= X[0] <= max_x and min_y <= X[1] <= max_y

def main():
    filename = input("Enter the filename containing the points: ")
    try:
        points = read_coordinates(filename)
        if len(points) < 4:
            print("Not enough points provided.")
            return

        A, B, C, D = points[:4]
        X = points[4]
        perpendicular = orthogonality3D(A, B, C, D)
        if perpendicular:
            #diagonal_length = calculate_diagonal_3d(*perpendicular)
            #inside = point_X_inside_rectangle(A, B, C, X, fourth_point)
            print("Given points CAN be part of the cuboid.")
            #print(f"Type of rectangle: {rectangle_type}")
            #print(f"The diagonal of the rectangle has length: {diagonal_length}")
            #print(f"Position of fourth point is: {fourth_point}")
            #print(f"Point X inside the rectangle: {inside}")
        else:
            print("Given points CANNOT be part of the cuboid.")
    except FileNotFoundError:
        print("File not found. Please ensure the filename is correct and the file exists in the specified path.")
    except Exception as e:
        print(f"An error occurred: {e}")
              
if __name__ == "__main__":
    os.system("cls")
    main()