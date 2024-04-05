"""
Упражнение 125. Тасуем колоду карт.
Начните с написания функции createDeck. В ней должны использоваться циклы для создания полной колоды карт путем
сохранения в список двухсимвольных аббревиатур всех 52 карт. Именно этот список и будет возвращаемым из данной функции
значением. На вход функция createDeck принимать параметры не будет.
Напишите вторую функцию с именем shuffle, которая будет случайным образом перетасовывать карты в списке.
Одна из техник тасования колоды заключается в проходе по элементам и перестановке их с любым другим случайным элементом
в этом списке. Вы должны создать свой собственный цикл для тасования карт в колоде,
а не пользоваться стандартной функцией shuffle языка Python.
Используйте обе созданные функции в основной программе, в которой должна отображаться колода карт до и после тасования.
Убедитесь, что основная программа выполняется только в случае, если файл не импортирован в качестве модуля.
"""
from random import randrange

# Колода карт
def createDeck():
    deck = []
    nominal = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
    suits = ['s', 'h', 'd', 'c']
    for suit in suits:
        for nom in nominal:
            deck.append(nom + suit)
    return deck

# Тасовка карт
def shuffle(deck):
    for i in range(len(deck)):
        x = randrange(0, len(deck))
        deck[i], deck[x] = deck[x], deck[i]

def display():
    cards = createDeck()
    print("Исходная колода карт: ", cards)
    print()
    shuffle(cards)
    print('Перетасованная колода карт', cards)

if __name__ == '__main__':
    display()