import functools


def det_3x3(matrix):
    size_1 = len(matrix)

    main_diag = functools.reduce(lambda x, y: x * y, [matrix[0][0], matrix[1][1], matrix[2][2]])
    second_diag = functools.reduce(lambda x, y: x * y, [matrix[0][1], matrix[1][2], matrix[2][0]])
    third_diag = functools.reduce(lambda x, y: x * y, [matrix[0][2], matrix[1][0], matrix[2][1]])

    anti_diag = functools.reduce(lambda x, y: x * y, [matrix[0][2], matrix[1][1], matrix[2][0]])
    second_anti_diag = functools.reduce(lambda x, y: x * y, [matrix[0][0], matrix[1][2], matrix[2][1]])
    third_anti_diag = functools.reduce(lambda x, y: x * y, [matrix[0][1], matrix[1][0], matrix[2][2]])

    det = (main_diag + second_diag + third_diag) - (anti_diag + second_anti_diag + third_anti_diag)
    return det


while True:
    size = input("Выберите размерность матрицы: 2, 3, 4: ")
    while size not in ['2', '3', '4']:
        print("Проверьте корректность ввода")
        size = input("Выберите размерность матрицы: 2, 3, 4: ")
    size = int(size)
    list_of_elements = (input("Введите матрицу через пробел: ")).split()
    check = [i.isdigit() for i in list_of_elements]
    while sum(check) != size ** 2:
        print(
            "Все элементы матрицы должны быть числом, а также количество элементов должно быть размерности матрицы в квадрате")
        list_of_elements = (input("Введите матрицу через пробел: ")).split()
        check = [i.isdigit() for i in list_of_elements]
    list_of_elements = [int(i) for i in list_of_elements]
    matrix = [list_of_elements[i * size: (i + 1) * size] for i in range(size)]
    if size == 2:
        print(functools.reduce(lambda x, y: x * y, [matrix[i][i] for i in range(size)]) - functools.reduce(
            lambda x, y: x * y, [matrix[i][size - i - 1] for i in range(size)]))

    elif size == 3:
        print(det_3x3(matrix))
    elif size == 4:
        minor = []
        temp_matrix = []
        k, result = 0, []
        for d in range(size):
            for i in range(size):
                for j in range(size):
                        if j != k and i != 0:
                            minor.append(matrix[i][j])

            k+=1
            for l in range(3):
                temp_matrix.append(minor[l * 3:(l+1)*3])

            minor = []

        for i in range(4):
            temp_matrix_2 = temp_matrix[i * 3:(i+1)*3]
            result.append((-1)**i*(det_3x3(temp_matrix_2))*matrix[0][i])
        print(sum(result))

    break
#1 3 2 4 5 4 6 7 1 1 2 3 4 5 4 3