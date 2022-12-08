import random

digits = '23456789'
lowercase_letters = 'abcdefghjkmnpqrstuvwxyz'
uppercase_letters = 'ABCDEFGHIJKMNPQRSTUVWXYZ'
punctuation = '!#$%&*+-=?@^_'
symbols = 'il1Lo0O'

chars = ''

def generate_password(lenth, chars):
    password = random.sample(chars, lenth)
    return password

print('Привет. Давай создадим для тебя безопасный пароль')
print('Введи, сколько тебе нужно паролей')
count = int(input())
print('Дальше для всех паролей давай настроим одинаковые критерии:')
print('Введи длину пароля')
lenth = int(input())
print('Дальше отвечай только "1" = да или "0" = нет')
print('Включать ли цифры 0123456789?')
num = input()
if num.lower() == '1':
    chars += digits
print('Включать ли прописные буквы?')
upp = input()
if upp.lower() == '1':
    chars += uppercase_letters
print('Включать ли строчные буквы?')
low = input()
if low.lower() == '1':
    chars += lowercase_letters
print('Включать ли символы !#$%&*+-=?@^_ ?')
sumb = input()
if sumb.lower() == '1':
    chars += punctuation
print('Включать ли неоднозначные символы il1Lo0O ?')
sumb1 = input()
if sumb1.lower() == '1':
    chars += symbols
chars = chars * 1000000

co = 1

for i in range(count):
    password = generate_password(lenth, chars)
    print(f'Вот твой {co} пароль:', ' ', *password, sep='')
    co += 1
