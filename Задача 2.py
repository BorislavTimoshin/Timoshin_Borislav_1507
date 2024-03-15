import csv

with open("vacancy.csv", "r", encoding="utf-8") as file:
    reader = list(csv.reader(file, delimiter=";"))[1:]  # Список списков, в котором хранится
    # информация и всех профессиях всех компаний


def quick_sort(people):
    """Описание функции quick_sort - быстрая сортировка O(nlogn)

    Описание аргументов: people - информация о профессиях людей в компании

    """
    if len(people) <= 2:  # Если людей не больше 2, возвращаем их
        return people
    first_people = people[0]  # Берем первого человека
    amount_of_people_company_first_people = int(first_people[2])  # Количество людей в компании первого человека
    left = []  # Люди, у которых количество людей в компании, в
    # которой они работают меньше amount_of_people_company_first_people
    right = []  # Наоборот left
    for i in people[1:]:
        # Если количество людей в компании, в которой работает человек меньше amount_of_people_company_first_people
        if int(i[2]) <= amount_of_people_company_first_people:  # Добавляем такого человека
            left.append(i)
        else:
            right.append(i)
    return quick_sort(left) + [first_people] + quick_sort(right)


new_reader = quick_sort(reader)  # Новый список списков работников, отсортированный по кол-ву работников в компании
for j in new_reader:
    if j[3] == "классный руководитель":  # Если профессия равна классный руководитель
        print(f"В компании {j[4]} есть заданная профессия: {j[3]}, з/п в такой компании составит: {j[0]}")
        break  # Заканчиваем работу проргаммы
