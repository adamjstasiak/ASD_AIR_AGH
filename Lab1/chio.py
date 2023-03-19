

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

    def chio(self, const=1):
        det_matrix = Matrix(deepcopy(self.matrix))
        rows, cols = det_matrix.size()
        if rows != cols or rows < 1:
            raise ValueError(f"Wrong size of matrix")
        if rows == 1:
            return det_matrix
        if rows == 2 and rows == cols:
            result = (det_matrix[0][0]*det_matrix[1][1] -
                      det_matrix[0][1] * det_matrix[1][0])*const
            return result
        if rows > 2 and rows == cols:
            if det_matrix[0][0] == 0:
                holder_1 = Matrix((1, cols), 0)
                for i in range(rows):
                    holder_1[0][i] = det_matrix[0][i]
                for i in range(cols):
                    if det_matrix[i][0] != 0:
                        k = i
                        const = const * - 1
                        for j in range(rows):
                            det_matrix[0][j] = det_matrix[k][j]
                            det_matrix[k][j] = holder_1[0][j]
                        break
            result = Matrix((rows-1, cols-1), 0)
            const *= 1/((det_matrix[0][0])**(rows-2))
            for i in range(rows):
                for j in range(cols):
                    result[i-1][j-1] = det_matrix[0][0] * det_matrix[i][j] - \
                        det_matrix[0][j] * det_matrix[i][0]
            return result.chio(const)


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
    matrix = [

        [5, 1, 1, 2, 3],

        [4, 2, 1, 7, 3],

        [2, 1, 2, 4, 7],

        [9, 1, 0, 7, 0],

        [1, 4, 7, 2, 2]

    ]

    matrix_1 = [
        [0, 1, 1, 2, 3],
        [4, 2, 1, 7, 3],
        [2, 1, 2, 4, 7],
        [9, 1, 0, 7, 0],
        [1, 4, 7, 2, 2]
    ]
    mat = Matrix(matrix)
    mat_1 = Matrix(matrix_1)
    print("pierwsza macierz")
    print(mat)
    print("druga macierz")
    print(mat_1)
    print("wyznacznik nr 1")
    print(mat.chio())
    print("wyznacznik nr 2")
    print(mat_1.chio())


if __name__ == "__main__":
    main()
