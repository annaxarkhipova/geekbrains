# Подсчитать, сколько было выделено памяти под переменные в ранее разработанных программах в рамках первых трех уроков.
# Проанализировать результат и определить программы с наиболее эффективным использованием памяти.
# Примечание:
# выбрать хорошую задачу, которую имеет смысл оценивать по памяти;
# написать 3 варианта кода (один у вас уже есть);
# проанализировать 3 варианта и выбрать оптимальный;
# результаты анализа (количество занятой памяти в вашей среде разработки) вставить в виде комментариев в файл с кодом.
# Не забудьте указать версию и разрядность вашей ОС и интерпретатора Python;
# написать общий вывод: какой из трёх вариантов лучше и почему.

# OS & Python 3.8.1 - 64-bit
import sys
from collections import deque, Counter

s = 0


def memory_count(*args):
    global s
    for r in args:
        s += sys.getsizeof(r)
    return s

# 1 var
MIN_ITEM = 2
MAX_ITEM = 9
multiples = dict()  # инициализация словаря c помощью функции
memory_count(multiples, MAX_ITEM, MIN_ITEM)

for p in range(MIN_ITEM, MAX_ITEM + 1):
    multiples[p] = [n for n in range(2, 99 + 1) if n % p == 0]
    memory_count(p)
    memory_count(multiples[p])

for key, val in multiples.items():
    memory_count(print(f"{key}", ", ".join(str(v) for v in val), sep=" -> "))

print(memory_count())  # 2744

# 2 var
MIN_ITEM = 2
MAX_ITEM = 9
multiples = Counter()  # Использование collections.Counter
memory_count(multiples, MAX_ITEM, MIN_ITEM)

for p in range(MIN_ITEM, MAX_ITEM + 1):
    multiples[p] = deque(str(n) for n in range(2, 99 + 1) if n % p == 0)  # использование collections.deque
    memory_count(p)
    memory_count(multiples[p])

for key, val in multiples.items():
    memory_count(key)
    memory_count(val)
    memory_count(print(f"{key}", ", ".join(str(v) for v in val), sep=" -> "))

print(memory_count())  # 5648


# 3 var
MIN_ITEM = 2
MAX_ITEM = 9
multiples = {}  # Инициализация словаря c помощью литерала
memory_count(multiples, MAX_ITEM, MIN_ITEM)

for p in range(MIN_ITEM, MAX_ITEM + 1):
    multiples[p] = [n for n in range(2, 99 + 1) if n % p == 0]
    memory_count(p)
    memory_count(multiples[p])

for key, val in multiples.items():
    memory_count(print(f"{key}", ", ".join(str(v) for v in val), sep=" -> "))

print(memory_count())  # 2576

