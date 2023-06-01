# Task_1
text = input('Введіть текст для перевірки на паліндром: ')
text_2 = text[::-1]

if text.lower() == text_2.lower():
    print('Рядок є паліндромом')
else:
    print('Рядок не є паліндромом')

# Task_2
text = input('Введіть текст: ')
res_words = input('Введіть зарезервовані слова через кому: ').split(',')

for word in res_words:
    text = text.replace(word, word.upper())

print('Змінений текст:', text)

# Task_3
text = input('Введіть текст в якому потрібно підрахувати кількість пропозицій: ')

sentences = text.split('. ') + text.split('? ') + text.split('! ')
num_sentences = len(sentences)

print("Кількість пропозицій у тексті: ", num_sentences)
