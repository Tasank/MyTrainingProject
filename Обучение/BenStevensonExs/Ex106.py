"""
Упражнение 106. Дни в месяце.
Напишите функцию для определения количества дней в конкретном месяце. Ваша функция должна принимать два параметра:
номер месяца в виде целого числа в диапазоне от 1 до 12 и год, состоящий из четырех цифр. Убедитесь,
что функция корректно обрабатывает февраль високосного года. В основной программе запросите у пользователя номер месяца
и год и отобразите на экране количество дней в указанном месяце. При решении этой задачи вам может
пригодиться написанная вами функция из упражнения 58.
"""
def check_day(month, year):
    leap_year = False
    # Проверка на високосный год
    if year % 4 == 0 or year % 400 == 0 and year % 100 != 0:
        leap_year = True

    day_31 = [1, 3, 5, 7, 8, 10, 12]
    day_30 = [4, 6, 9, 11]

    if month in day_31:
        return 31
    elif month in day_30:
        return 30

    elif month == 2:
        if leap_year:
            return 29
        else:
            return 28
    if month > 12 or month < 1:
        return 'Неверные значения!'

def main():
    month = int(input('Введите номер месяца: '))
    year = int(input('Введите год: '))
    print('Дней в этом месяце = ', check_day(month, year))

main()