# Упражнение № 66
# *Задача изменена под потребности СНГ, нынешнего времени
# Напишите программу, запрашивающую у пользователя цены в рублях, пока не будет введена пустая строка.
# На первой строке выведите сумму всех введенных пользователем сумм, а на второй
# – сумму, которую покупатель должен заплатить наличными.



price = input('Введите цены продуктов. Для выхода оставьте запрос пустым: ')
result = 0.0
while price != '':
    result += float(price)
    price = input('Введите цены продуктов. Для выхода оставьте запрос пустым: ')

print('Сумма ваших покупок: %.2f' % result)
print('Вы должны заплатить %d (Руб)' % round(result))