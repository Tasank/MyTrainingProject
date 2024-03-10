"""
 Упражнение 72. Игра Fizz-Buzz.
 Разработайте программу, реализующую алгоритм игры Fizz-Buzz применительно к первым 100 числам.
 Каждый следующий ответ должен отображаться на новой строке.
 Первый игрок говорит «Один» и передает ход тому, кто слева.
 Каждый следующий игрок должен мысленно прибавить к предыдущему числу единицу и произнести либо его,
 либо одно из ключевых слов: Fizz, если число без остатка делится на три, или Buzz, если на пять.
 Если соблюдаются оба этих условия, он произносит Fizz-Buzz
"""

# Алгоритм действия игры

print('Первый способ решения, без участия игроков')
for i in range(1, 100):
    if i % 3 == 0 and i % 5 == 0:
        print('Fizz-Buzz, число ->', i)
    elif i % 3 == 0:
        print('Fizz, число ->', i)
    elif i % 5 == 0:
        print('Buzz, число ->', i)

# Игра с участием пользователя ввода -> вывода, находится в файле Fizz-Buzz_Game





