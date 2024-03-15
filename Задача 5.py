import csv

with open("vacancy.csv", "r", encoding="utf-8") as file:
    reader = list(csv.reader(file, delimiter=";"))
    d = {}  # Словарь, в котором ключ - компания, а значение - кортеж (профессия, макс. зарплата)
    for i in reader[1:]:
        # Salary;Work_Type;Company_Size;Role;Company
        if d.get(i[4]) is None:  # Если человека с такой компании не было
            d[i[4]] = [(i[3], i[0], i[1],)]  # Заносим его профессию, зарплату, тип
        else:
            d[i[4]].append((i[3], i[0], i[1],))  # Дополняем его профессию, зарплату, тип


print(max(d, key=lambda x: len(d[x])))  # Выводим компанию с самым большим количеством вакансий в словаре,
# по ключу длины списка вакансий
