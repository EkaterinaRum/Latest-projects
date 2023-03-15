import pandas as pd
import math

df = pd.DataFrame(pd.read_excel("C:/Users/Database"))

# deleting useless columns
df = df.drop(['Modified on', 'Reserved', 'Offlimit'], axis=1)

# deleting all rows without phone numbers
df.dropna(axis=0, subset=["Primary phone"], inplace=True)

# delete duplicated rows
df = df.drop_duplicates()

# уберу все символы и пробелы в номерах
df['Primary phone'] = df['Primary phone'].str.replace('\W', '', regex=True)
df

# deleting all rows without phone numbers
df.dropna(axis=0, subset=["Primary phone"], inplace=True)
df

df[['Primary phone']].count(axis=1)
df['Primary phone'].isnull().sum()

# Ладно, сначала просто создам колонку справа и назову ее. Ну и переименую колонки удобно, а то че.
df['Comments'] = ''
df.rename(columns = {'Full name':'Name', 'Job title':'Position', 'Compan':'Company', 'Primary phone':'Phone', 'Primary Email':'Email'}, inplace = True)
df

# Дальше я хочу еще раз проверить все номера и вывести на экран те строки, где есть не только цифры, но и буквы (узнала, что
# они есть, когда хотела перевести из srt в int и получила ошибку)
test = df[df['Phone'].apply(lambda x: not x.isnumeric())]
test
# Результат говорит о том, что в 2785 строках с номерами есть буквы!
# Значит, следующим шагом я хочу создать колонку справа и перенести туда эти буквы от номеров.

# Создаю колонку справа (от самой правой) и переношу буквы из колонки с телефонами в эту колонку. Назову её "comments".
# Дальше \D - обозначение всех символов, которые не цифры
# Отделить от столбца все что не цифры
df['Primary phone'] = df['Primary phone'].str.replace('\W', '', regex=True)

# добавляю буквы из Phone в Comments на тестовом датасете
def find_letters(text):
    res = ''
    for c in text:
        if not c.isnumeric():
            res = text[text.find(c):]
            break
    return res

test['Comments'] = test['Phone'].apply(lambda x: ''.join(find_letters(x)))    # - все верно, добавляет нужное в Comments
test

# удаляю буквы и то, что после них, из Phone
def digits_to_remain_in_phone(text):
    res = ''
    for c in text:
        if c.isnumeric():
            res += c
        elif c.isnumeric == False:
            break
    return res

test['Phone'] = test['Phone'].apply(lambda x: ''.join(digits_to_remain_in_phone(x)))
test

# теперь добавляю буквы из Phone в Comments на основном датасете
def find_letters(text):
    res = ''
    for c in text:
        if not c.isnumeric():
            res = text[text.find(c):]
            break
    return res

df['Comments'] = df['Phone'].apply(lambda x: ''.join(find_letters(x)))    # - все верно, добавляет нужное в Comments
df

# удаляю буквы и то, что после них, из Phone
def digits_to_remain_in_phone(text):
    res = ''
    for c in text:
        if c.isnumeric():
            res += c
        elif c.isnumeric == False:
            break
    return res

df.Phone = df['Phone'].apply(lambda x: ''.join(digits_to_remain_in_phone(x)))
df

# проверка, все ли получилось на основном датасете
test = df[df['Phone'].apply(lambda x: not x.isnumeric())]
test

df.to_csv(r"C:/Users/Database2.csv")
