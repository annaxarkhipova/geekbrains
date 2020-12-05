# 8. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
# https://drive.google.com/file/d/15FPVBNFRXg_L7e0yv5YixfWFyEiCyPCQ/view?usp=sharing


def program(a):
    if a > 0:
        if a == 1:
            return 1
        count = a - 1
        if a % 2 == 0:
            return program(count) - (1 / 2 ** count)
        return program(count) + (1 / 2 ** count)
    return f"{a} меньше 0"


n = int(input(" число "))
print(program(n))

