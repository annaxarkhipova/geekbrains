# 8. Матрица 5x4 заполняется вводом с клавиатуры,
# кроме последних элементов строк. Программа должна вычислять сумму введенных элементов каждой строки и записывать ее
# в последнюю ячейку строки.
# В конце следует вывести полученную матрицу.


SIZE_line = 5
SIZE_elem = 4


def foo():
    s = 0
    matrix_output = []

    for i in range(SIZE_line):
        matrix_input = list(input(f"введи 3 цифры для  матрицы, 4ый элемент - сумма введенных тобой чисел: "))
        if len(matrix_input) != SIZE_elem - 1:
            print("Введи 3 цифры")
            break
        for a in matrix_input:
            s += int(a)
        matrix_output.insert(i, [int(f) for f in matrix_input] + [s])
        s = 0
    return matrix_output


print(*foo(), sep="\n")
