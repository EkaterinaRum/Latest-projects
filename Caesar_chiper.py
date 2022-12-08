lowercase_letters_eng = list('abcdefghijklmnopqrstuvwxyz')
uppercase_letters_eng = list('ABCDEFGHIJKLMNOPQRSTUVWXYZ')
lowercase_letters_rus = list('абвгдежзийклмнопрстуфхцчшщъыьэюя')
uppercase_letters_rus = list('АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ')
punctuation = list('!#$%&*+-=?@^_0123456789')

print('Работаю с зашифровкой и дешифровкой текста по шифру Цезаря')
print('Тебе нужно зашифровать или дешифровать текст? Введи 0, если зашифровать, и 1, если дешифровать')
a = int(input())

print('Текст на русском или английском? Введи 0, если на русском, и 1, если на английском')
lang = int(input())

print('Какой шаг сдвига вправо? Введи одну цифру')
k = int(input())

print('А теперь введи сам текст')
text = list(input())

def Caesar_cipher(a, lang, k, text):
    chars = ''
    if lang == 0:
        n = 32
    elif lang == 1:
        n = 26

    for i in range(len(text)):
        if a == 0 and lang == 0:
            if text[i].islower():
                text[i] = lowercase_letters_rus[(lowercase_letters_rus.index(text[i]) + k) % n]
            elif text[i].isupper():
                text[i] = uppercase_letters_rus[(uppercase_letters_rus.index(text[i]) + k) % n]
            chars += text[i]
        elif a == 0 and lang == 1:
            if text[i].islower():
                text[i] = lowercase_letters_eng[(
                    lowercase_letters_eng.index(text[i]) + k) % n]
            elif text[i].isupper():
                text[i] = uppercase_letters_eng[(
                    uppercase_letters_eng.index(text[i]) + k) % n]
            chars += text[i]
        elif a == 1 and lang == 0:
            if text[i].islower():
                text[i] = lowercase_letters_rus[(
                    lowercase_letters_rus.index(text[i]) - k) % n]
            elif text[i].isupper():
                text[i] = uppercase_letters_rus[(
                    uppercase_letters_rus.index(text[i]) - k) % n]
            chars += text[i]
        elif a == 1 and lang == 1:
            if text[i].islower():
                text[i] = lowercase_letters_eng[(
                    lowercase_letters_eng.index(text[i]) - k) % n]
            elif text[i].isupper():
                text[i] = uppercase_letters_eng[(
                    uppercase_letters_eng.index(text[i]) - k) % n]
            chars += text[i]
    return chars


cipher = Caesar_cipher(a, lang, k, text)
print(cipher)