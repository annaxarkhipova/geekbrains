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
# print(timeit.timeit("program(900)", number=100, globals=globals()))
# print(cProfile.run("program(900)"))
# 0.25896524
#          903 function calls (4 primitive calls) in 0.003 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#     900/1    0.002    0.000    0.002    0.002 task_4.py:6(program)
#         1    0.000    0.000    0.003    0.003 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# var 2
def program2(a):
    res = 1
    for b in range(1, a):
            res += (1 / 2 ** b) if b % 2 == 0 else -(1 / 2 ** b)
    return res


print(timeit.timeit("program2(900)", number=100, globals=globals()))
print(cProfile.run("program2(900)"))
# 0.17264186799999998
#          4 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 task_1.py:31(program2)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

