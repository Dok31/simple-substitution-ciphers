LANG = 'en'

if LANG == 'en':
    base_alph = [chr(i) for i in range(97, 123)]
    M = 26
elif LANG == 'ru':
    M = 32
    base_alph = [chr(i) for i in range(1072, 1104)]


def mult_inversion(a):
    global M
    for i in range(M):
        if (a * i) % M == 1:
            return i

    print(a, 'не подходит в качестве ключа')


def recur_afin(text, key):
    global base_alph, M
    a1, b1, a2, b2 = key

    shifr_text = []
    for i in range(len(text)):
        a, b = a1, b1
        if text[i].isalpha():
            if text[i] == 'ё':
                text[i] = 'е'
            elif text[i] == 'Ё':
                text[i] = 'Е'
            shifr_text.append(base_alph[(base_alph.index(text[i].lower()) * a + b) % M])
        else:
            shifr_text.append(text[i])
        a1, b1 = a2, b2
        a2, b2 = a * a1 % M, (b + b1) % M
    with open('output.txt', encoding='UTF-8', mode='w') as out:
        for i in shifr_text:
            out.write(i)
    return ''.join(shifr_text)


def deshifr_recur_afin(shifr_text, key):
    global base_alph, M
    a1, b1, a2, b2 = key

    text = []
    for i in range(len(shifr_text)):
        a, b = a1, b1
        k1 = mult_inversion(a)
        if shifr_text[i].isalpha():
            text.append(base_alph[(base_alph.index(shifr_text[i]) - b) * k1 % M])
        else:
            text.append(shifr_text[i])
        a1, b1 = a2, b2
        a2, b2 = a * a1 % M, (b + b1) % M
    return ''.join(text)


# считывание текста из input.txt
inp = ''
with open('input.txt', encoding='UTF-8') as f:
    for i in f:
        inp += i
print(inp)

# a1,b2, a2,b2
shifred = recur_afin(inp, (5, 2, 7, 4))
print(shifred)
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
print('--------------------------------------------')
text = deshifr_recur_afin(shifred, (5, 2, 7, 4))
print(text)
