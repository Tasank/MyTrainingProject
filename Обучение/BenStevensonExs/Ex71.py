# Упражнение 71. Приблизительное число π
# Напишите программу, выводящую на экран 15 приближений числа π.
# В первом приближении должно быть использовано только первое слагаемое приведенного бесконечного ряда.
# Каждое очередное приближение должно учитывать следующее слагаемое, тем самым увеличивая точность расчета.
a = 2
b = 3
c = 4

pi = 3 + (4 / (a * b * c))
print('Приближённое число π', pi)

for i in range(7):
    a += 1
    b += 1
    c += 1
    pi = pi - (4 / (a * b * c))
    print('Приближённое число π', pi)
    a += 1
    b += 1
    c += 1
    pi = pi + (4 / (a * b * c))
    print('Приближённое число π', pi)