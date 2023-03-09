from random import shuffle

# Функция зашифрования шифром простой замены
def easy_replacement(text, key, lang='ru'):
    alph = {}
    if lang == 'ru':
        for i in range(1072, 1104):
            alph[chr(i)] = i - 1072
    elif lang == 'en':
        for i in range(97, 123):
            alph[chr(i)] = i - 97
    shifr_text = []
    # Приведения текста к одному виду и зашифрование
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i] == 'ё':
                text[i] = 'е'

            elif text[i] == 'Ё':
                text[i] = 'Е'
            if text[i].upper() == text[i]:

                shifr_text.append(key[alph[text[i].lower()]].upper())
            else:
                shifr_text.append(key[alph[text[i]]])
        else:
            shifr_text.append(text[i])
    # Запись шифртекста в файл
    with open('output.txt', encoding='UTF-8', mode='w') as out:
        for i in shifr_text:
            out.write(i)
    return ''.join(shifr_text)

# Функция расшифрования шифра простой замены
def deshifr_easy_replacement(shift_text, key, lang='ru'):
    alph = []
    if lang == 'ru':
        alph = [chr(i) for i in range(1072, 1104)]


    elif lang == 'en':
        alph = [chr(i) for i in range(97, 123)]
    dict_key = {}
    # Создание словаря для расшифрования
    for i in range(len(key)):
        dict_key[key[i]] = i
    text = []
    # Расшифрование
    for i in range(len(shift_text)):
        if shift_text[i].isalpha():
            if shift_text[i].upper() == shift_text[i]:
                text.append(alph[dict_key[shift_text[i].lower()]].upper())
            else:
                text.append(alph[dict_key[shift_text[i]]])
        else:
            text.append(shift_text[i])
    return ''.join(text)


# считывание текста из input.txt
inp = ''
with open('input.txt', encoding='UTF-8') as f:
    for i in f:
        inp += i
inp = list(inp)
# print(inp)

# генерация случайного ключа
# ru_key = [chr(i) for i in range(1072, 1104)]
# shuffle(ru_key)
# print(''.join(ru_key))
#
# en_key = [chr(i) for i in range(97, 123)]
# shuffle(en_key)
# print(''.join(en_key))

shifred = easy_replacement(inp, 'uncrsiyhojpmdexgwqkztabvfl', lang='en')
print(shifred)
print('---------------------------------------------------------------------------------------------------------------')
print(deshifr_easy_replacement(shifred, 'uncrsiyhojpmdexgwqkztabvfl', lang='en'))

# # print('uncrsiyhojpmdexgwqkztabvfl')