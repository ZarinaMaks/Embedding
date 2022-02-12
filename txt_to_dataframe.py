import csv
import pandas as pd

# Выделим для начала csv страницу с показателями
# Тип автомобиля, Марка автомобиля, Модель автомобиля, Цвет, Описание,
# Пробег, Год, Рубли, С салона, Колличество дверей, Количество владельцев

if __name__ == "__main__":
    with open('autoru_parsing_result1.txt', 'r') as file:
        lines = file.readlines()

    signs = {'Тип автомобиля', 'Марка автомобиля', 'Модель автомобиля', 'Цвет', 'Пробег',
             'Год', 'Рубли', 'С салона', 'Колличество дверей', 'Количество владельцев'}

    prefix = '//avatars.'  # to remove unnececcasy images for now
    newlines = [x for x in lines if not x.startswith(prefix)]

    separator = '=================================================================================================================================\n'
    index = 0
    labels = [[]]
    for line in newlines:
        if line:
            first_word = line.split(':')[0]
            if first_word in signs:
                second_word = line.split(': ')[1].replace("\n", "")
                labels[index].append((first_word, second_word))
            if line == separator:
                index += 1
                labels.append([])
    labels.pop()

    data = pd.DataFrame(columns=signs)

    for label in labels:
        labeldict = {}
        for i in range(len(label)):
            labeldict[label[i][0]] = label[i][1]
        data = data.append(labeldict, ignore_index=True)