# Отсортируйте по возрастанию методом слияния одномерный вещественный массив,
# заданный случайными числами на промежутке [0; 50). Выведите на экран исходный и отсортированный массивы.

from random import randrange

SIZE = 10
a = [float(randrange(0, 50)) for _ in range(SIZE)]


def sorting_array(array, left, right):
    if left == right:
        return
    mid = (left + right) // 2
    sorting_array(a, left, mid)
    sorting_array(a, mid + 1, right)

    i, j = left, mid + 1
    buffer = array.copy()
    for step in range(0, right - left + 1):
        if j > right or i <= mid and a[i] < a[j]:
            buffer[step] = a[i]
            i += 1
        else:
            buffer[step] = a[j]
            j += 1
    for step in range(0, right - left + 1):
        array[left + step] = buffer[step]
    return buffer


print(a)
print(sorting_array(a, 0, len(a) - 1))
