from random import *

answers = [
    'Бесспорно', 'Предрешено', 'Никаких сомнений', 'Определённо да', 'Можешь быть уверен в этом',
    'Мне кажется - да', 'Вероятнее всего', 'Хорошие перспективы', 'Знаки говорят - да', 'Да',
    'Пока неясно, попробуй снова', 'Спроси позже', 'Лучше не рассказывать', 'Сейчас нельзя предсказать', 'Сконцентрируйся и спроси опять',
    'Даже не думай', 'Мой ответ - нет', 'По моим данным - нет', 'Перспективы не очень хорошие', 'Весьма сомнительно'
    ]

print('Привет Мир, я магический шар, и я знаю ответ на любой твой вопрос.')
print('Как тебя зовут?')
print('Привет,', input() + '!')

def prediction():
    print('Задавай вопрос!')
    question = input()
    print(choice(answers))
    print()
    print('Хочешь ещё спросить что-нибудь? (Да/Нет)')
    return input()

answer = prediction()

while answer == 'Да':
    answer = prediction()

print('Возвращайся если возникнут вопросы!')