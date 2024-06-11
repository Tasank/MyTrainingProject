"""
Упражнение 139. Азбука Морзе.
Азбука Морзе зашифровывает буквы и цифры при помощи точек и тире. В данном упражнении вам необходимо написать программу,
в которой соответствие символов из азбуки Морзе будет храниться в виде словаря. В табл. 6.3 приведена та часть азбуки,
которая вам понадобится при решении этого задания.
В основной программе вам необходимо запросить у пользователя строку. После этого программа должна преобразовать его в
соответствующую последовательность точек и тире, вставляя пробелы между отдельными символами. Символы,
не представленные в таблице, можно игнорировать. Например, сообщение Hello, World! может быть представлено
следующей последовательностью: .... . .–.. .–.. ––– .–– ––– .–. .–.. –..
"""

MORSE_DICT = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.',
    'G': '--.', 'H': '....', 'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..',
    'M': '--', 'N': '-.', 'O': '---', 'P': '.--.', 'Q': '--.-', 'R': '.-.',
    'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
    'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---',
    '3': '...--', '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.'
}

def upgrade(text):
    total = []
    for char in text.upper():
        if char in MORSE_DICT:
            total.append(MORSE_DICT[char])
    return ''.join(total)

def main():
    text = input('Введите строку: ')
    print(upgrade(text))
main()