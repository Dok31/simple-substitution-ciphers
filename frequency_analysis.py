LANG = 'en'

frequency_of_letters = {}
diction = {}
knowed_frequency = {}
if LANG == 'ru':
    M = 32
    knowed_frequency = {'а': 8.01, 'б': 1.59, 'в': 4.54, 'г': 1.7, 'д': 2.98, 'е': 8.45, 'ж': 0.94, 'з': 1.65,
                        'и': 7.35, 'й': 1.21, 'к': 3.49, 'л': 4.4, 'м': 3.21, 'н': 6.7, 'о': 10.97, 'п': 2.81,
                        'р': 4.73, 'с': 5.47, 'т': 6.26, 'у': 2.62, 'ф': 0.26, 'х': 0.97, 'ц': 0.48, 'ч': 1.44,
                        'ш': 0.73, 'щ': 0.36, 'ъ': 0.04, 'ы': 1.9, 'ь': 1.74, 'э': 0.32, 'ю': 0.64, 'я': 2.01}

    for i in range(1072, 1104):
        frequency_of_letters[chr(i)] = 0
        diction[chr(i)] = ''
elif LANG == 'en':
    M = 26
    knowed_frequency = {'e': 12.7, 't': 9.06, 'a': 8.17, 'o': 7.51, 'i': 6.97, 'n': 6.75, 's': 6.33, 'h': 6.09,
                        'r': 5.99, 'd': 4.25, 'l': 4.03, 'c': 2.78, 'u': 2.76, 'm': 2.41, 'w': 2.36, 'f': 2.23,
                        'g': 2.02, 'y': 1.97, 'p': 1.93, 'b': 1.49, 'v': 0.98, 'k': 0.77, 'x': 0.15, 'j': 0.15,
                        'q': 0.1,  'z': 0.05}
    for i in range(97, 123):
        frequency_of_letters[chr(i)] = 0
        diction[chr(i)] = ''


def analysis(shifr_text):
    letters_cou = 0

    global frequency_of_letters, diction, knowed_frequency
    for i in frequency_of_letters.keys():
        frequency_of_letters[i] = shifr_text.count(i)
        letters_cou += shifr_text.count(i)
    for i in frequency_of_letters.keys():
        frequency_of_letters[i] /= letters_cou
        frequency_of_letters[i] *= 100
        frequency_of_letters[i] = round(frequency_of_letters[i], 2)

    # более быстрый подсчет количества вхождений разных букв
    # for i in range(len(shifr_text)):
    #     if shifr_text[i] in frequency_of_letters.keys():
    #         frequency_of_letters[shifr_text[i]] += 1
    #         letters_cou += 1

    frequency_of_letters = sorted(frequency_of_letters.items(), key=lambda x: x[1], reverse=True)
    knowed_frequency = sorted(knowed_frequency.items(), key=lambda x: x[1], reverse=True)
    for i in range(len(frequency_of_letters)):
        diction[frequency_of_letters[i][0]] = knowed_frequency[i][0]

    print('frequency_of_letters', frequency_of_letters, sep=':')
    print('knowed_frequency', knowed_frequency, sep=':')
    print('diction', diction, sep=':')


    text = []
    for i in range(len(shifr_text)):
        if shifr_text[i].isalpha():
            text.append(diction[shifr_text[i]])
        else:
            text.append(shifr_text[i])

    return ''.join(text)


inp = ''
with open('output.txt', encoding='UTF-8') as f:
    for i in f:
        inp += i.lower()
print(analysis(inp))
