"""
Напишите функцию, которая будет принимать в качестве параметров строку s, а также ширину окна в символах – w.
Возвращать функция должна новую строку, в которой в начале добавлено необходимое количество пробелов,
чтобы первоначальная строка оказалась размещена по центру заданного окна.
В вашей основной программе должен осуществляться пример вывода нескольких строк в окнах разной ширины.
"""
#@param s - строка для центрирования
#@param w - ширина окна в символах, в котором будет центрированна строка
def func(s,w):
    if len(s) >= w:
        return s
    total = (w - len(s)) // 2
    result = ' ' * total + s
    return result

def main():
    s = input('Введите строку: ')
    w = int(input('Введите ширину отступа: '))
    print(func(s, w))
main()
