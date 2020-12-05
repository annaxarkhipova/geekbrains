# 7. Напишите программу, доказывающую или проверяющую,
# что для множества натуральных чисел выполняется равенство:
# 1+2+...+n = n(n+1)/2, где n — любое натуральное число.
# https://drive.google.com/file/d/15FPVBNFRXg_L7e0yv5YixfWFyEiCyPCQ/view?usp=sharing


def check(n):
    if n <= 0:
        return "введено не нат число"

    r1 = func(n)
    r2 = n*(n+1)/2
    if r1 == r2:
        return f"равенство 1+2+...+n = n(n+1)/2 верно - {r1} == {r2}"
    return


def func(m):
    if m == 1:
        return 1
    return func(m-1) + m


print(check(3))
