# 1. Найти сумму и произведение цифр трехзначного числа, которое вводит пользователь.
# https://drive.google.com/file/d/1ydDhgRFY0F_4WXiqLSupQQdnR_XbU7Fo/view?usp=sharing

print("Введи трехзначное число")  # целые числа
a = int(input("Первая цифра - "))
b = int(input("Вторая цифра - "))
c = int(input("Третья цифра - "))
if a < 0 or b < 0 or c < 0:
    print("Решений нет")
else:
    d = a + b + c
    f = a * b * c
    print(f"Сумма цифр {d=}, произведение - {f=}")
