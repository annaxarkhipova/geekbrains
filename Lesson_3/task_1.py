# 1. В диапазоне натуральных чисел от 2 до 99 определить,
# сколько из них кратны каждому из чисел в диапазоне от 2 до 9.

MIN_ITEM = 2
MAX_ITEM = 9
multiples = dict()

for p in range(MIN_ITEM, MAX_ITEM + 1):
    multiples[p] = [n for n in range(2, 99 + 1) if n % p == 0]
for key, val in multiples.items():
    print(f"{key}", ", ".join(str(v) for v in val), sep=" -> ")


