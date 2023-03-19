# skończone

from copy import deepcopy


class Matrix:
    def __init__(self, matrix, parametr=0):
        if isinstance(matrix, tuple):
            rows = matrix[0]
            cols = matrix[1]
            self.matrix = [[parametr] * cols for _ in range(rows)]
        elif all(isinstance(el, list) for el in matrix):
            self.matrix = matrix

    def __getitem__(self, item):
        return self.matrix[item]

    def __add__(self, matrix_add):
        if isinstance(matrix_add, Matrix):
            base_matrix = Matrix(deepcopy(self.matrix))
            rows, cols = self.size()
            matrix_add_rows, matrix_add_cols = matrix_add.size()
            if rows == matrix_add_rows and cols == matrix_add_cols:
                for i in range(rows):
                    for j in range(cols):
                        base_matrix[i][j] += matrix_add[i][j]
                return base_matrix
            else:
                raise ValueError(f"Wrong size of matrix")
        else:
            raise ValueError(f"Wrong type of matrix")

    def __mul__(self, matrix_mul):
        if isinstance(matrix_mul, Matrix):
            base_matrix = Matrix(deepcopy(self.matrix))
            rows, cols = base_matrix.size()
            matrix_mul_rows, matrix_mul_cols = matrix_mul.size()
            if cols == matrix_mul_rows:
                result_size = rows, matrix_mul_cols
                result = Matrix(result_size, 0)
                for i in range(rows):
                    for j in range(matrix_mul_cols):
                        for k in range(cols):
                            result[i][j] += base_matrix[i][k] * \
                                matrix_mul[k][j]
                return result
            else:
                raise ValueError(f"Wrong size of matrix")
        else:
            raise ValueError(f"Wrong type of Matrix")

    def __str__(self):
        description = ''
        for row in self.matrix[:-1]:
            description += str(row)
            description += '\n'
        description += str(self.matrix[-1])
        return description

    def size(self):
        rows = len(self.matrix)
        cols = 0
        if rows > 0:
            cols = len(self.matrix[0])
        return rows, cols


def transpose(mat):
    if all(isinstance(el, list) for el in mat) or isinstance(mat, Matrix):
        matrix_T = deepcopy(mat)
        rows, cols = matrix_T.size()
        matrix_T_size = cols, rows
        transpose_mat = Matrix(matrix_T_size, 0)
        for i in range(cols):
            for j in range(rows):
                transpose_mat[i][j] = matrix_T[j][i]
        return transpose_mat
    else:
        raise ValueError(f"Wrong type of matrix")


def main():
    matrix_1 = [[1, 0, 2], [-1, 3, 1]]
    mat_1 = Matrix(matrix_1)
    matrix_2 = (2, 3)
    mat_2 = Matrix(matrix_2, 1)
    matrix_3 = [[3, 1], [2, 1], [1, 0]]
    mat_3 = Matrix(matrix_3)
    print("Macierz nr 1")
    print(mat_1)
    print("macierz nr 2")
    print(mat_2)
    add_mat = mat_1 + mat_2
    print("Macierz nr 3")
    print(mat_3)
    print("Dodawanie macierzy")
    print(add_mat)
    mul_mat = mat_1*mat_3
    print("Mnozenie macierzy")
    print(mul_mat)
    print("Transpozycja macierzy")
    mat_1_t = transpose(mat_1)
    print(mat_1_t)


if __name__ == "__main__":
    main()
