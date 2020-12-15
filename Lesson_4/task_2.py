# Написать два алгоритма нахождения i-го по счёту простого числа.
# Функция нахождения простого числа должна принимать на вход натуральное и возвращать
# соответствующее простое число. Проанализировать скорость и сложность алгоритмов.
# Первый — с помощью алгоритма «Решето Эратосфена».
# Второй — без использования «Решета Эратосфена».


# Первый — с помощью алгоритма «Решето Эратосфена».
def sieve(n):
    size = 100
    a = [0] * size
    for i in range(size):
        a[i] = i

    # вторым элементом является единица, которую не считают простым числом
    # забиваем ее нулем.
    a[1] = 0

    m = 2  # замена на 0 начинается с 3-го элемента (первые два уже нули)
    while m < size:  # перебор всех элементов до заданного числа
        if a[m] != 0:  # если он не равен нулю, то
            j = m * 2  # увеличить в два раза (текущий элемент - простое число)
            while j < size:
                a[j] = 0  # заменить на 0
                j = j + m  # перейти в позицию на m больше
        m += 1

    # вывод простых чисел на экран (может быть реализован как угодно)
    b = []
    for i in a:
        if a[i] != 0:
            b.append(a[i])

    del a
    return b[n-1]


print(sieve(1))

# Второй — без использования «Решета Эратосфена».


def prime(z):
    for s in range(2, z):
        if z % s == 0:
            return False
    return True


def find_prime_index(v):
    primes = []
    for r in range(2, 100):
        if prime(r) is True:
            primes.append(r)

    return primes[v-1]


print(find_prime_index(1))




