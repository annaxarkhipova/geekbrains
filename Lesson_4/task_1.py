# Проанализировать скорость и сложность одного любого алгоритма из разработанных в рамках домашнего задания
# первых трех уроков.
# Примечание. Идеальным решением будет:
# ● выбрать хорошую задачу, которую имеет смысл оценивать,
# ● написать 3 варианта кода (один у вас уже есть),
# ● проанализировать 3 варианта и выбрать оптимальный,
# ● результаты анализа вставить в виде комментариев в файл с кодом (не забудьте указать,
#   для каких N вы проводили замеры),
# ● написать общий вывод: какой из трёх вариантов лучше и почему.

import timeit
import cProfile
from Lesson_2.task_4 import program

# var 1 (imported)
print(timeit.timeit("program(900)", number=100, globals=globals()))  # 0.20329175
print(cProfile.run("program(900)"))
#     900/1    0.002    0.000    0.002    0.002 task_4.py:6(program)


# var 2
def program2(a):
    while a >= 0:
        if a == 1:
            return 1
        if a % 2 == 0:
            count = a - 1
            res = count - (1 / 2 ** count)
            return res
        else:
            count = a - 1
            res = count + (1 / 2 ** count)
            return res
    return


print(timeit.timeit("program2(900)", number=100, globals=globals()))  # 0.0002934929999999919
print(cProfile.run("program(900)"))
#         900/1    0.003    0.000    0.003    0.003 task_4.py:6(program)


# var 3
def program3(a):
    for i in range(a + 1):
        if i == 1:
            return i
        return i - (1/2 ** i) if a % 2 == 0 else i + (1 / 2 ** i)
    return


print(timeit.timeit("program3(900)", number=100, globals=globals()))  # 0.0002278190000000041
print(cProfile.run("program(900)"))
#        903 function calls (4 primitive calls) in 0.005 seconds
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.005    0.005 <string>:1(<module>)
#  900/1    0.005    0.000    0.005    0.005 task_4.py:6(program)
#      1    0.000    0.000    0.005    0.005 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


