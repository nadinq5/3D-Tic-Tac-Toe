from MATRIX import Matrix
class Cube:

    def __init__(self, matrix1, matrix2, matrix3):
        self.T = matrix1
        self.M = matrix2
        self.B = matrix3

    def __str__(self):
        print(self.T)
        print(self.M)
        print(self.B)
        return ""

def main():

    matrix1 = Matrix()
    matrix2 = Matrix()
    matrix3 = Matrix()
    cube = Cube(matrix1, matrix2, matrix3)
    print(cube.M)

if __name__ == '__main__':
    main()