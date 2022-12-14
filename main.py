import csv
import random
from russian_names import RussianNames

status_list = ["студент", "магистрант"]
group_list = ["ГРб-19-1", "СМ-17-1", "РРб-20-1", "ЛМБм-20-1", "КНб-19-1", "ФКб-20-1", "ДСб-20-1", "СУЗ-20-1", "ЭСТб-18-2", "ХТТбп-18-1", "ПОм-21-1", "РМ-20-1"]
inst_list = ['ИИТиАД', 'ИЭ', 'ИАМиТ', 'ИАСиД', 'ИВТ', 'ИН', 'ИЭУП']

def generate_person(napr):
    if(napr == "НИД"):
        with open(f"{napr}.csv", mode="w", encoding='cp1251') as w_file:
            file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
            file_writer.writerow(["Ф.И.О.", "Состояние", "Группа", "Факультет", "Направление Рейтинга", "ID записи", "Балл достижений", "Уровень достижений (НИД)"])
            i = 0
            while i < 50:
                r = random.randint(1, 6)
                file_writer.writerow([f"{RussianNames().get_person()}", f"{random.choice(status_list)}", f"{random.choice(group_list)}", f"{random.choice(inst_list)}", f"{napr}", f"{random.randint(10000, 99999)}", f"{random.randint(30, 150)}", f"{random.randint(1, 3)}"])
                i += 1
    else:
        with open(f"{napr}.csv", mode="w", encoding='cp1251') as w_file:
            file_writer = csv.writer(w_file, delimiter=";", lineterminator="\r")
            file_writer.writerow(["Ф.И.О.", "Состояние", "Группа", "Факультет", "Направление Рейтинга", "ID записи", "Балл достижений", "Уровень достижений (НИД)"])
            i = 0
            while i < 50:
                r = random.randint(1, 6)
                file_writer.writerow([f"{RussianNames().get_person()}", f"{random.choice(status_list)}", f"{random.choice(group_list)}", f"{random.choice(inst_list)}", f"{napr}", f"{random.randint(10000, 99999)}", f"{random.randint(30, 150)}"])
                i += 1

def main():
    print("УД")
    generate_person("УД")
    print("СД")
    generate_person("СД")
    print("НИД")
    generate_person("НИД")
    print("КТД")
    generate_person("КТД")
    print("ОД")
    generate_person("ОД")

if __name__ == '__main__':
    main()