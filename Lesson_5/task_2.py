# Написать программу сложения и умножения двух шестнадцатеричных чисел.
# При этом каждое число представляется как коллекция, элементы которой — цифры числа.
# Например, пользователь ввёл A2 и C4F. Нужно сохранить их как [‘A’, ‘2’] и [‘C’, ‘4’, ‘F’] соответственно.
# Сумма чисел из примера: [‘C’, ‘F’, ‘1’], произведение - [‘7’, ‘C’, ‘9’, ‘F’, ‘E’].

from collections import deque, Counter


# Десятичные	    0	1	2	3	4	5	6	7	8	9	10	11	12	13	14	15	16  17
# Шестнадцатеричные	0	1	2	3	4	5	6	7	8	9	a	b	c	d	e	f   10  11
count = Counter(A=10, B=11, C=12, D=13, E=14, F=15)
first_digit = deque(input("Введи первое число "))   #      [‘A’, ‘2’]
second_digit = deque(input("Введи второе число "))  # [‘C’, ‘4’, ‘F’]


symbols_to_sum = deque([])
if len(first_digit) != len(second_digit):
    diff = len(first_digit) - len(second_digit)
    if diff < 0:
        symbols_to_sum.extendleft(second_digit[0])


for t in range(len(first_digit)-1, 0, -1):
    for e in range(len(second_digit) - 1, 0, -1):
        if first_digit[t] in count:
            symbols_to_sum.extend([first_digit[t], second_digit[e]])

        if second_digit[e] in count:
            symbols_to_sum.extend([second_digit[e], first_digit[t]])
        t -= 1
print(symbols_to_sum)





#########################################
# def func(expr):
#     result = 0
#     for ind, _ in enumerate(expr):
#         k = len(expr) - ind - 1
#         r = count.get(expr[k]) if expr[k] in count else int(expr[k])
#         f = r * 16 ** ind
#         result += f
#

# common = first_digit + second_digit
# summa_first = 0
# for ind, _ in enumerate(first_digit):
#     k = len(first_digit) - ind - 1
#     r = count.get(first_digit[k]) if first_digit[k] in count else int(first_digit[k])
#     f = r * 16 ** ind
#     summa_first+=f
#
# summa_sec = 0
# for ind, _ in enumerate(second_digit):
#     k = len(second_digit) - ind - 1
#     r = count.get(second_digit[k]) if second_digit[k] in count else int(second_digit[k])
#     f = r * 16 ** ind
#     summa_sec+=f
# print(summa_first + summa_sec)
