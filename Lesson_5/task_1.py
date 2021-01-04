# Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартал (т.е. 4 числа)
# для каждого предприятия.
# Программа должна определить среднюю прибыль (за год для всех предприятий)
# и отдельно вывести наименования предприятий, чья прибыль выше среднего и ниже среднего.

from collections import Counter, deque


amount = int(input(f"Введи количество предприятий: "))
avrg = 0
company_income = Counter()
for i in range(1, amount+1):
    name = input(f"Введи название компании: ")
    income = [int(input(f"Введи прибыль за {a} квартал: ")) for a in range(1, 4 + 1)]
    for t in income:
        avrg += t
        company_income[name] += t

avrg = avrg / len(company_income)
print(f"{avrg=}")
for v, b in company_income.items():
    if b > avrg:
        print(f"Наиболее прибыльные - {v}")
    else:
        print(f"Наименее прибыльные - {v}")
