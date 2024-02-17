import csv
import re
from decorators_task_2 import logger


path = 'write_final_contacts.log'


def read_contacts() -> list:
    """Функция чтения файла и записи csv в list"""
    with open("phonebook_raw.csv", encoding="utf-8") as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)
    return contacts_list


def format_names(contacts_list: list) -> list:
    """Функция для приведения ФИО в нужный формат"""

    contacts_list_new = []

    for contact in contacts_list:
        name_temp, info_temp = contact[:3], contact[3:]
        name_temp = ' '.join(name_temp)
        contact_new = name_temp.split(' ')
        for index, name_part in enumerate(contact_new):
            """Цикл нужен чтобы удалить пустую строку посередине
               (кейс с Лукиной Ольгой, иначе при формировании списка
               contact_new[:3])теряется ее отчество)"""
            if name_part == '':
                del contact_new[index]
        contacts_list_new.append(contact_new[:3] + info_temp)
    return contacts_list_new


def format_phones(contacts_list: list) -> list:
    """Функция приведения телефонов в нужный формат"""
    pattern = r"(\+7|8)\s*\(*(\d{3})\)?\s?-?(\d{3})\-?(\d{2})-?(\d{2})\s?\(?(доб.)?\s?(\d*)\)?"
    sub_pattern = r"+7(\2)\3-\4-\5 \6\7"

    for i in range(1, len(contacts_list)):
        text = contacts_list[i][5]
        contacts_list[i][5] = re.sub(pattern, sub_pattern, text)

    return contacts_list


def join_dublicates(contacts_list: list) -> list:
    """Функция для объединения информации по дублирующим записям"""

    contact_dict = {}

    for contact in contacts_list:
        key = contact[0], contact[1]
        data = {
            "surname": contact[2],
            "organization": contact[3],
            "position": contact[4],
            "phone": contact[5],
            "email": contact[6],
            }
        if contact_dict.get(key):
            dict_temp = contact_dict.get(key)[0]
            for item_1, item_2 in dict_temp.items():
                if item_2 != '':
                    data[item_1] = item_2
            contact_dict[key] = [data]
        else:
            contact_dict[key] = [data]

    contacts_list_final = []

    for key, data in contact_dict.items():
        contacts_list_final.append(list(key) + list(data[0].values()))

    return contacts_list_final


@logger(path)
def write_contacts(contacts_list_final: list):
    """Функция для записи файла в csv формате"""
    with open("phonebook.csv", "w", encoding="utf-8") as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(contacts_list_final)


if __name__ == "__main__":
    contacts_list = read_contacts()
    contacts_list_new = format_names(contacts_list)
    contacts_list_new = format_phones(contacts_list_new)
    contacts_list_final = join_dublicates(contacts_list_new)
    contact_list_final_csv = write_contacts(contacts_list_final)
