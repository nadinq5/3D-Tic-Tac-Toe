class Matrix:

    def __init__(self):
        self.matrix = [[0 for i in range(3)] for j in range(3)]

    def __str__(self):
       print(f'\\{self.matrix[0][0]}\\{self.matrix[0][1]}\\{self.matrix[0][2]}\\')
       print(f'\\{self.matrix[1][0]}\\{self.matrix[1][1]}\\{self.matrix[1][2]}\\')
       print(f'\\{self.matrix[2][0]}\\{self.matrix[2][1]}\\{self.matrix[2][2]}\\')
       return ""

    # def __str__(self):
    #     print(f'\\ \\ \\ \\')
    #     print(f'\\ \\ \\ \\')
    #     print(f'\\ \\ \\ \\')
    #     return ""


# def main():
#     matrix = Matrix()
#     print(matrix)
#
# if __name__ == '__main__':
#     main()
