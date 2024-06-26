import math

class CheckSolid:
    def orthogonality_3D(A, B, C, D):
        """Check for vector perpendicularity.
        Return: Boolean and Integer"""

        vectors = {
            "vec_AB" : (B[0] - A[0], B[1] - A[1], B[2] - A[2]),
            "vec_AC" : (C[0] - A[0], C[1] - A[1], C[2] - A[2]),
            "vec_AD" : (D[0] - A[0], D[1] - A[1], D[2] - A[2]),
            "vec_BA" : (A[0] - B[0], A[1] - B[1], A[2] - B[2]),
            "vec_BC" : (C[0] - B[0], C[1] - B[1], C[2] - B[2]),
            "vec_BD" : (D[0] - B[0], D[1] - B[1], D[2] - B[2]),
            "vec_CA" : (A[0] - C[0], A[1] - C[1], A[2] - C[2]),
            "vec_CB" : (B[0] - C[0], B[1] - C[1], B[2] - C[2]),
            "vec_CD" : (D[0] - C[0], D[1] - C[1], D[2] - C[2]),
            "vec_DA" : (A[0] - D[0], A[1] - D[1], A[2] - D[2]),
            "vec_DB" : (B[0] - D[0], B[1] - D[1], B[2] - D[2]),
            "vec_DC" : (C[0] - D[0], C[1] - D[1], C[2] - D[2])
        }
        
        dot_products = {
        "dot_AB_AC" : ("vec_AB", "vec_AC"),
        "dot_AB_AD" : ("vec_AB", "vec_AD"),
        "dot_AC_AD" : ("vec_AC", "vec_AD"),
        "dot_BA_BC" : ("vec_BA", "vec_BC"),
        "dot_BA_BD" : ("vec_BA", "vec_BD"),
        "dot_BC_BD" : ("vec_BC", "vec_BD"),
        "dot_CA_CB" : ("vec_CA", "vec_CB"),
        "dot_CA_CD" : ("vec_CA", "vec_CD"),
        "dot_CB_CD" : ("vec_CB", "vec_CD"),
        "dot_DA_DB" : ("vec_DA", "vec_DB"),
        "dot_DA_DC" : ("vec_DA", "vec_DC"),
        "dot_DB_DC" : ("vec_DB", "vec_DC")
    }
        
        orthogonal_vec = []
            
        for _, (vec1, vec2) in dot_products.items():
            vector1 = vectors[vec1]
            vector2 = vectors[vec2]
            dot_product = vector1[0] * vector2[0] + vector1[1] * vector2[1] + vector1[2] * vector2[2]

            if math.isclose(dot_product, 0, abs_tol=1e-9):
                orthogonal_vec.append((vector1, vector2))
            
        if len(orthogonal_vec) == 3 or len(orthogonal_vec) == 4:
            return True, len(orthogonal_vec)
            
        elif len(orthogonal_vec) == 0:
            dAB = math.dist(A, B)
            dAC = math.dist(A, C)
            dAD = math.dist(A, D)
            dBC = math.dist(B, C)
            dBD = math.dist(B, D)
            dCD = math.dist(C, D)
            
            if dAB == dCD and dAC == dBD and dAD != dBC:
                return False
            elif dAB == dCD and dAD == dBC and dAC != dBD:
                return False
            
            if dAC == dBD and dAB == dCD and dAD != dBC:
                return False
            elif dAC == dBD and dAD == dBC and dAB != dCD:
                return False
            
            if dAD == dBC and dAC == dBD and dAB != dCD:
                return False
            elif dAD == dBC and dAB == dCD and dAC != dBD:
                return False
            
            if dAB != dAC or dAB != dAD or dAC != dAD:
                if dAB == dCD or dAC == dBD or dAD == dBC:
                    return True, len(orthogonal_vec) 
                return False
            
            return True, len(orthogonal_vec)
    
    def calculate_diagonal_3d(A, B, C, D, num):
        """Calculate the diagonal of the cuboid using number of dot products being equal zero,
        to determine the possible positioning of the input points.
        Return: Float"""
        if num == 3:
            distances = {
                "dAB" : math.dist(A, B),
                "dAC" : math.dist(A, C),
                "dAD" : math.dist(A, D),
                "dBD" : math.dist(B, D),
                "dBC" : math.dist(B, C),
                "dCD" : math.dist(C, D)
            }
            max_distance_value = distances[max(distances, key=distances.get)]
            return max_distance_value
    
        elif num == 4:
            distances = {
                "dAB" : math.dist(A, B),
                "dAC" : math.dist(A, C),
                "dAD" : math.dist(A, D),
            }
            max_distance_value = distances[max(distances, key=distances.get)]
            return max_distance_value
        
        else:
            diagonal_1 = math.dist(A, B) ** 2
            diagonal_2 = math.dist(A, C) ** 2
            diagonal_3 = math.dist(A, D) ** 2
            
            a_squared = (diagonal_2 + diagonal_1 - diagonal_3) / 2
            b_squared = (diagonal_1 + diagonal_3 - diagonal_2) / 2
            c_squared = (diagonal_2 + diagonal_3 - diagonal_1) / 2

            space_diagonal = math.sqrt(a_squared + b_squared + c_squared)
            
            return space_diagonal
        
    def point_X_inside_hexahedron(A, B, C, D, X):
        """Determines if the point X is inside cuboid or cube.
        Condition: Cuboid or cube has three edges on axis.
        Status: Unfinished.
        Return: Boolean."""
        
        min_x = min(A[0], B[0], C[0], D[0])
        max_x = max(A[0], B[0], C[0], D[0])
        min_y = min(A[1], B[1], C[1], D[1])
        max_y = max(A[1], B[1], C[1], D[1])
        min_z = min(A[2], B[2], C[2], D[2])
        max_z = max(A[2], B[2], C[2], D[2])
        return min_x <= X[0] <= max_x and min_y <= X[1] <= max_y and min_z <= X[2] <= max_z

    def main_3d(points):
        try:
            if len(points) < 4:
                print("Not enough points provided.")
                return

            A, B, C, D = points[:4]
            X = points[4]
            perpendicular = CheckSolid.orthogonality_3D(A, B, C, D)
            if perpendicular:
                print("Given points CAN be part of the cuboid.")
                inside = CheckSolid.point_X_inside_hexahedron(A, B, C, D, X)
                print(f"Point X inside the cuboid: {inside}")
                diagonal_length3D = CheckSolid.calculate_diagonal_3d(A, B, C, D, num = perpendicular[1])
                print(f"The space diagonal of the cuboid has length: {diagonal_length3D}")
            else:
                print("Given points CANNOT be part of the cuboid.")
        except FileNotFoundError:
            print("File not found. Please ensure the filename is correct and the file exists in the specified path.")
        except Exception as e:
            print(f"An error occurred: {e}")