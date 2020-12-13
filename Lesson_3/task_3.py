# 2. В массиве случайных целых чисел поменять местами минимальный и максимальный элементы.
import random

SIZE = 5
array = [random.randint(1, 10) for _ in range(SIZE)]
print(f"Получен массив {array}")

maximum = array[0]
minimum = array[0]

for a, b in enumerate(array, 1):
    if b > maximum:
        maximum = b
    elif b < minimum:
        minimum = b

max_pos = array.index(maximum)
min_pos = array.index(minimum)
array[max_pos] = minimum
array[min_pos] = maximum
print(f"{minimum=}, {maximum=} поменялись местами - {array}")
