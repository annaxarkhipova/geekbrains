# 2. Посчитать четные и нечетные цифры введенного натурального числа.
# Например, если введено число 34560, в нем 3 четные цифры (4, 6 и 0) и 2 нечетные (3 и 5).
# https://drive.google.com/file/d/15FPVBNFRXg_L7e0yv5YixfWFyEiCyPCQ/view?usp=sharing


def program():
    print("Введи число")
    number = input(" ")
    odds = 0
    even = 0
    for digit in number:
        if int(digit) % 2 == 0:
            even += 1
        else:
            odds += 1
    return f"{odds=}, {even=}"


print(program())
