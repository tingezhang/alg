




def GE(matrix, row, col)
    for i in range(0, row -2):
        for j in range(i + 1, row - 1):
            ratio = matrix[j][i] / matrix[i][i]
            for k in range(i, col):
                matrix[j][k] = matrix[j][k] * ( 1 - ratio)


def main():


if '__main__' == __name__:
    main()

