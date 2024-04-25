import math, os

class vector_2d:
    def read_coordinates(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        coordinates = [tuple(map(float, line.strip().split())) for line in lines]
        return coordinates

    def orthogonality2D(A, B, C):
        """Check for vector perpendicularity.
        Return: tuple containing two points."""
        vec_AB = (B[0] - A[0], B[1] - A[1])
        vec_AC = (C[0] - A[0], C[1] - A[1])
        
        vec_BA = (A[0] - B[0], A[1] - B[1])
        vec_BC = (C[0] - B[0], C[1] - B[1])
        
        vec_CA = (A[0] - C[0], A[1] - C[1])
        vec_CB = (B[0] - C[0], B[1] - C[1])
        
        dot_product_ABAC = vec_AB[0] * vec_AC[0] + vec_AB[1] * vec_AC[1]
        dot_product_BABC = vec_BA[0] * vec_BC[0] + vec_BA[1] * vec_BC[1]
        dot_product_CACB = vec_CA[0] * vec_CB[0] + vec_CA[1] * vec_CB[1]
        
        if math.isclose(dot_product_ABAC, 0, abs_tol=1e-9):
            return (B, C)
        if math.isclose(dot_product_BABC, 0, abs_tol=1e-9):
            return (A, C)
        if math.isclose(dot_product_CACB, 0, abs_tol=1e-9):
            return (A, B)
        
        return False

    def calculate_diagonal(diagonal_point1, diagonal_point2):
        """Calculate the diagonal of the rectangle using two opposite points in initial triangle.
        Return: distance between two diagonal points as float number."""
        return math.dist(diagonal_point1, diagonal_point2)

    def position_of_fourth_point(A, B, C):
        """Finding the fourth point of a rectangle given three points A, B, and C. 
        Calculate coordinates using vector addition.
        Return: Fourth point D as tuple."""
        
        opposite_points = vector_2d.orthogonality2D(A, B, C)
        
        if opposite_points == (B, C):
            D = (B[0] + C[0] - A[0], B[1] + C[1] - A[1])
        elif opposite_points == (A, C):
            D = (A[0] + C[0] - B[0], A[1] + C[1] - B[1])
        elif opposite_points == (A, B):
            D = (A[0] + B[0] - C[0], A[1] + B[1] - C[1])
    
        return D

    def point_X_inside_quadrilateral(A, B, C, X, D):
        """Determines if the point X is inside rectangle or square.
        Condition: Rectangle or square has two sides on axis.
        Return: Boolean."""
        min_x = min(A[0], B[0], C[0], D[0])
        max_x = max(A[0], B[0], C[0], D[0])
        min_y = min(A[1], B[1], C[1], D[1])
        max_y = max(A[1], B[1], C[1], D[1])
        return min_x <= X[0] <= max_x and min_y <= X[1] <= max_y
    
    def type_of_rectangle(A, B, C):
        """Using simple calculation with distances to identify type of quadriliteral.
        Return: String - Rectangle or Square."""
        
        opposite_points = vector_2d.orthogonality2D(A,B,C)
        
        if opposite_points == (B, C):
            dAB = math.dist(A, B)
            dAC = math.dist(A, C)
            if dAB == dAC:
                return "Square"
            else:
                return "Rectangle"
        elif opposite_points == (A, C):
            dBA = math.dist(B, A)
            dBC = math.dist(B, C)
            if dBA == dBC:
                return "Square"
            else:
                return "Rectangle"
        elif opposite_points == (A, B):
            dCA = math.dist(C, A)
            dCB = math.dist(C, B)
            if dCA == dCB:
                return "Square"
            else:
                return "Rectangle"
    
    def main():
        filename = input("Enter the filename containing the points: ")
        try:
            points = vector_2d.read_coordinates(filename)
            if len(points) < 4:
                print("Not enough points provided.")
                return

            A, B, C, X = points[:4]
            perpendicular = vector_2d.orthogonality2D(A, B, C)
            if perpendicular:
                print("Given points CAN be part of the rectangle.")
                fourth_point = vector_2d.position_of_fourth_point(A, B, C)
                print(f"Position of fourth point is: {fourth_point}")
                rectangle_type = vector_2d.type_of_rectangle(A, B, C)
                print(f"Type of quadrilateral: {rectangle_type}")
                inside = vector_2d.point_X_inside_quadrilateral(A, B, C, X, fourth_point)
                print(f"Point X inside the {rectangle_type.lower()}: {inside}")
                diagonal_length = vector_2d.calculate_diagonal(*perpendicular)
                print(f"The diagonal of the rectangle has length: {diagonal_length}")
            else:
                print("Given points CANNOT be part of the rectangle.")
        except FileNotFoundError:
            print("File not found. Please ensure the filename is correct and the file exists in the specified path.")
        except Exception as e:
            print(f"An error occurred: {e}")
                
if __name__ == "__main__":
    os.system("cls")
    vector_2d.main()