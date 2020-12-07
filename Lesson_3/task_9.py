# 9. Найти максимальный элемент среди минимальных элементов столбцов матрицы.
import random

SIZE_M = 4
SIZE_N = 6
MIN_ITEM = 0
MAX_ITEM = 100
matrix = [[random.randint(MIN_ITEM, MAX_ITEM) for _ in range(SIZE_N)] for _ in range(SIZE_M)]
print(*matrix, sep="\n")

minimal_digits = []
for i in range(SIZE_N):
    matrix_columns = [line[i] for line in matrix]
    minimum = matrix_columns[0]
    for symbol in matrix_columns:
        if symbol < minimum:
            minimum = symbol
    minimal_digits.append(minimum)

maximum = minimal_digits[0]
for symbol in minimal_digits:
    if symbol > maximum:
        maximum = symbol
print(maximum)

