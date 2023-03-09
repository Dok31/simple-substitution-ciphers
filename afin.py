LANG = 'en'

if LANG == 'en':
    M = 26
    base_alph = [chr(i) for i in range(97, 123)]
elif LANG == 'ru':
    M = 32
    base_alph = [chr(i) for i in range(1072, 1104)]


def mult_inversion(a):
    global M
    for i in range(M):
        if (a * i) % M == 1:
            return i

    print(a, 'не подходит в качестве ключа')


def afin(text, key):
    global base_alph, M
    a, b = key
    shifr_text = []
    for i in range(len(text)):
        if text[i].isalpha():
            if text[i].lower() == 'ё':
                shifr_text.append(base_alph[(base_alph.index('е') * a + b) % M])
            else:
                shifr_text.append(base_alph[(base_alph.index(text[i].lower()) * a + b) % M])
        else:
            shifr_text.append(text[i])
    with open('output.txt', encoding='UTF-8', mode='w') as out:
        for i in shifr_text:
            out.write(i)
    return ''.join(shifr_text)


def deshifr_afin(shifr_text, key):
    global base_alph, M
    a, b = key
    k1 = mult_inversion(a)
    text = []
    for i in range(len(shifr_text)):
        if shifr_text[i].isalpha():
            text.append(base_alph[((base_alph.index(shifr_text[i]) - b) * k1) % M])
        else:
            text.append(shifr_text[i])

    return ''.join(text)

# считывание текста из input.txt
inp = ''
with open('input.txt', encoding='UTF-8') as f:
    for i in f:
        inp += i
print(inp)



shifred = afin(inp, (3, 8))
print(shifred)
print('---------------------------------------------')
text = deshifr_afin(shifred, (3, 8))
print(text)
