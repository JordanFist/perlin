from numpy import *
from perlin import *



def getTopLeftCorner(coords, size, zoom):
    """
    Get the top left corner with the coord of the midd square and the size of the screen
    """
    
    subMatrixWidth = size[0] // zoom
    subMatrixHeight = size[1] // zoom


    return coords[0] - subMatrixWidth // 2, coords[1] - subMatrixHeight // 2
    

def getSubMatrix(matrix, coords, size, zoom):
    """
    map : The top matrice which the one we will create the sub matrix \n
    topLeftCorner : tuple of x and y of the sub matrice\n
    size : the n + to add to got the bottomRightCorner of sub matrix
    """
    
    x, y = getTopLeftCorner(coords, size, zoom)
    print(x,y)

    subMatrixWidth = size[0] // zoom
    subMatrixHeight = size[1] // zoom

    return matrix[x:x + subMatrixWidth, y:y + subMatrixWidth ]


"""
matrix = zeros((100,100))

nbr = 0
for i in range(100):
    for j in range(100):
        nbr += 1
        matrix[i][j] = nbr
print(matrix)

print(getSubMatrix(matrix, (50, 50), (500, 500), 16))
"""