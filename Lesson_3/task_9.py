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
    minimum = [matrix_columns[0]]
    for symbol in matrix_columns:
        if symbol < minimum[-1]:
            minimum = [symbol]
    minimal_digits.extend(minimum)

maximum = [minimal_digits[0]]
for symbol in minimal_digits:
    if symbol > minimal_digits[-1]:
        maximum = [symbol]
print(*maximum)
