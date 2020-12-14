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

# VAR 1
print(timeit.timeit("program(100)", number=100, globals=globals()))
print(cProfile.run("program(100)"))
# 0.076070337
#          103 function calls (4 primitive calls) in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#     100/1    0.000    0.000    0.000    0.000 task_4.py:6(program)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(timeit.timeit("program(500)", number=100, globals=globals()))
print(cProfile.run("program(500)"))
# 0.08761396399999999
#          503 function calls (4 primitive calls) in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#     500/1    0.001    0.000    0.001    0.001 task_4.py:6(program)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(timeit.timeit("program(900)", number=100, globals=globals()))
print(cProfile.run("program(900)"))
# 0.201378014
#           903 function calls (4 primitive calls) in 0.002 seconds
#
# Ordered by: standard name
#
# ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#      1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#  900/1    0.002    0.000    0.002    0.002 task_1.py:52(program)
#      1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#      1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# #######################################################################################################################
# VAR 2
def program2(a):
    element = 0
    for k in range(1, a - 1):
        for p in range(2, a):
            element = -k / p
        else:
            element += element / p
    return element


print(timeit.timeit("program2(100)", number=100, globals=globals()))
print(cProfile.run("program2(100)"))
# 0.11571743
#          4 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 task_1.py:58(program2)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(timeit.timeit("program2(500)", number=100, globals=globals()))
print(cProfile.run("program2(500)"))
#   3.0030868070000003
#          4 function calls in 0.027 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.027    0.027 <string>:1(<module>)
#         1    0.027    0.027    0.027    0.027 task_1.py:58(program2)
#         1    0.000    0.000    0.027    0.027 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(timeit.timeit("program2(900)", number=100, globals=globals()))
print(cProfile.run("program2(900)"))
# 9.806213238
#          4 function calls in 0.092 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.092    0.092 <string>:1(<module>)
#         1    0.092    0.092    0.092    0.092 task_1.py:58(program2)
#         1    0.000    0.000    0.092    0.092 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

# #######################################################################################################################
# VAR 3
def program3(a):
    res = 1
    for b in range(1, a):
        res += (1 / 2 ** b) if b % 2 == 0 else -(1 / 2 ** b)
    return res


print(timeit.timeit("program3(100)", number=100, globals=globals()))
print(cProfile.run("program3(100)"))
# 0.015613791000000002
#          4 function calls in 0.000 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.000    0.000 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 task_1.py:107(program3)
#         1    0.000    0.000    0.000    0.000 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(timeit.timeit("program3(500)", number=100, globals=globals()))
print(cProfile.run("program3(500)"))
# 0.11930497699999999
#          4 function calls in 0.001 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.001    0.001 <string>:1(<module>)
#         1    0.001    0.001    0.001    0.001 task_1.py:107(program3)
#         1    0.000    0.000    0.001    0.001 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}

print(timeit.timeit("program3(900)", number=100, globals=globals()))
print(cProfile.run("program3(900)"))
# 0.17264186799999998
#          4 function calls in 0.002 seconds
#
#    Ordered by: standard name
#
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    0.000    0.000    0.002    0.002 <string>:1(<module>)
#         1    0.002    0.002    0.002    0.002 task_1.py:31(program3)
#         1    0.000    0.000    0.002    0.002 {built-in method builtins.exec}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}


# Вывод: 1 вариант  - с рекурсией, функция рекурсивно попала на стек 900 раз
#        2 вариант - использовала два вложенных цикла, функция квадратичной сложности
#        3 вариант - в функции генератор выполняет основную задачу, функция линейной сложности

