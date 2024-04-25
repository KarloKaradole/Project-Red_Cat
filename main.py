import os
from services.CheckShapes import CheckShape
from services.CheckSolids import CheckSolid 


def read_coordinates(filename):
        with open(filename, 'r') as file:
            lines = file.readlines()
        coordinates = [tuple(map(float, line.strip().split())) for line in lines]
        
        if coordinates:
            dimensions = len(coordinates[0])
        else:
            dimensions = 0
        
        return coordinates, dimensions
                        
if __name__ == "__main__":
    os.system("cls")
    
    filename = input("Enter the filename containing the coordinates: ")
    coordinates, dimensions = read_coordinates(filename)
    
    if dimensions == 3:
        CheckSolid.main_3d(coordinates)
    elif dimensions == 2:
        CheckShape.main_2d(coordinates)
    else:
        print("Unsupported dimensionality or empty file.")
    
