# 3. По введенным пользователем координатам двух точек вывести уравнение прямой вида y = kx + b,
# проходящей через эти точки.
# https://drive.google.com/file/d/1ydDhgRFY0F_4WXiqLSupQQdnR_XbU7Fo/view?usp=sharing

print("Введи координаты двух точек")
x1 = int(input("Первая точка: x = "))
y1 = int(input("y ="))
x2 = int(input("Вторая точка: x = "))
y2 = int(input("y = "))
k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print(f"Уравнение прямой y = {k}x + {b}")
