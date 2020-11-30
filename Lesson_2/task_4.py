# 8. Найти сумму n элементов следующего ряда чисел: 1, -0.5, 0.25, -0.125,…
# Количество элементов (n) вводится с клавиатуры.
# https://drive.google.com/file/d/15FPVBNFRXg_L7e0yv5YixfWFyEiCyPCQ/view?usp=sharing


def program(amount):
    res = 1
    for i in range(res, amount + 1):
        res = res / 2
        print(res)
    return


a = int(input(" число "))
print(program(a))

