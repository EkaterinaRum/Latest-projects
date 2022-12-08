import random

count = 1
again = 'да'

# загадываю рандомное число из введенного диапазона
def num(a, b):
    return random.randint(int(a), int(b))

# проверяю, что это вообще число и в загаданном диапазоне
def is_valid(n):
    if n.isdigit() and int(a) <= int(n) <= int(b):
        return True
    else:
        return False

def core():
    count = 1
    while again == 'да':
        num = input()
        if is_valid(num) == False:
            print(
                f'А может быть все-таки введешь целое число от {a} до {b}?')
        elif is_valid(num):
            num = int(num)
            if num < num1:
                print('Твое число меньше загаданного, попробуйте еще разок')
                count += 1
            elif num > num1:
                print('Твое число больше загаданного, попробуйте еще разок')
                count += 1
            elif num == num1:
                print(f'Угадано с {count} попытки, ура!')
                print()
                break

print('Добро пожаловать в числовую угадайку!')

while again == 'да':
    print('Давай выберем диапазон, в котором я загадаю число. Введи любое целое число')
    a = input()
    print('Теперь введи второе число. Оно должно быть больше первого')
    b = input()
    num1 = num(a, b)
    print(
        f'Теперь угадывай, какое число я загадал! Введи число от {a} до {b} включительно')
    core()
    print("Хочешь сыграть еще раз? Напиши 'да' или 'нет'")
    again = input()
    while again != 'да' and again != 'нет':
        print('да или нет?')
        again = input()
    if again == 'нет':
        print('Спасибо, что играли в числовую угадайку. Еще увидимся...')
