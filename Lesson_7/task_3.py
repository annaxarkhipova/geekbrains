# Массив размером 2m + 1, где m — натуральное число, заполнен случайным образом.
# Найдите в массиве медиану. Медианой называется элемент ряда, делящий его на две равные части:
# в одной находятся элементы, которые не меньше медианы, в другой — не больше медианы.
# Примечание: задачу можно решить без сортировки исходного массива.
# Но если это слишком сложно, используйте метод сортировки, который не рассматривался на уроках
# (сортировка слиянием также недопустима).

from random import randrange

m = int(input("Число "))
SIZE = 2 * m + 1
array = [int(randrange(0, 50)) for _ in range(SIZE)]
print(array)

if SIZE % 2 != 0:
    med = array[round(SIZE % 2)]
    print(med)
