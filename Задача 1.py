import csv

with open("vacancy.csv", "r", encoding="utf-8") as file:
    reader = list(csv.reader(file, delimiter=";"))
    d = {}  # Словарь, в котором ключ - компания, а значение - кортеж (профессия, макс. зарплата)
    for i in reader[1:]:
        # Salary;Work_Type;Company_Size;Role;Company
        if d.get(i[4]) is None:  # Если человека с такой компании не было
            d[i[4]] = (i[3], i[0],)  # Заносим его профессию и зарплату
        else:
            if i[0] > d[i[4]][1]:  # Если зарплата нового работника больше зарплаты предыдущего работника
                d[i[4]] = (i[3], i[0],)  # Меняем профессию и зарплату

with open("vacancy_new.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow(["company", "role", "Salary"])  # Вписываем столбцы
    for company, (role, salary) in d.items():
        writer.writerow([company.strip(), role, salary])  # Вписываем строки

with open("vacancy_new.csv", "r", encoding="utf-8") as file:
    # Список профессий с максимальными зарплатами каждой компании, сортируем по зарлате в обратном порядке
    reader = sorted(list(csv.reader(file, delimiter=";"))[1:], key=lambda x: int(x[2]), reverse=True)
    top = reader[:3]
    for i in top:
        print(f"{i[0]} - {i[1]} - {i[2]}")

