from sys import stdin
import csv

with open("vacancy.csv", "r", encoding="utf-8") as file:
    reader = list(csv.reader(file, delimiter=";"))[1:]  # Список списков, в котором хранится
    # информация и всех профессиях всех компаний

for company in stdin:
    if company.strip() == "None":  # Если введенная компания равна None, то завершаем проргамму
        break
    finded = False  # Флаг, означающий, что хотя бы одну вакансию вывели или нет
    for i in reader:  # Проход по всем профессиям за O(n)
        if i[4] == company.strip():  # Если компаиня совпала, то выводим ответ
            print(f"В {company.strip()} найдена вакансия: {i[3]}. З/п составит: {i[0]}")
            finded = True
    if not finded:  # Есил ни одной вакансии не вывели, то выводи сообщеине
        print("К сожалению, ничего не удалось найти")
