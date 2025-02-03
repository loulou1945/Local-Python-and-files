import random


def words_file():
    points = 0
    words = open('words.txt')
    for word in words:
        word_new = ''.join(random.sample(list(word[:-1]), len(list(word[:-1]))))
        print(f'Угадайте слово: {word_new}')
        answer = input()
        if answer == word[:-1]:
            print('Верно! Вы получаете 10 очков')
            points += 10
        else:
            print(f'Неверно! Правильный ответ - {word[:-1]}')
    words.close()
    return points


def history_file():
    history = open('history.txt', 'a+')
    history.write(f'{name} ')
    history.write(f'{points}\n')
    history.close()


def history_record():
    record = 0
    history = open('history.txt')
    for line in history:
        info = line.split(' ')
        if int(info[1]) > record:
            record = int(info[1])
    return record


def history_counts():
    count = 0
    history = open('history.txt')
    for line in history:
        count += 1
    return count


print('Введите имя')
name = input()
points = words_file()
history_file()
record = history_record()
count_games = history_counts()
print(f'Всего игр сыграно: {count_games}')
print(f'Максимальный рекорд: {record}')
