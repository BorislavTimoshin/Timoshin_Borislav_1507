import csv

with open("vacancy.csv", "r", encoding="utf-8") as file:
    reader = list(csv.reader(file, delimiter=";"))[1:]


def middle_salary(work_type):
    summa = 0
    lenght = 0
    for j in reader:
        if j[1] == work_type:
            summa += int(j[0])
            lenght += 1
    return summa / lenght


with open("vacancy_procent.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file, delimiter=";")
    writer.writerow("Salary;Work_Type;Company_Size;Role;Company;percent".split(";"))  # Вписываем столбцы
    for i in reader:
        salary = int(i[0])
        writer.writerow(i + [f"{salary / (middle_salary(i[1]) * 100)}%"])  # Вписываем строки


