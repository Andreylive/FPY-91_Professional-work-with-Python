from pprint import pprint
import csv
import re

with open("phonebook_raw.csv", encoding="utf-8") as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)

# 1. Correct name data in dataset
contacts_list_new = []

for contact in contacts_list:
    info_temp = contact[3:]
    name_temp = ' '.join(contact[:3])
    contact_new = name_temp.split(' ')[0:3]
    contact_new = contact_new + info_temp
    contacts_list_new.append(contact_new)

for contact in contacts_list_new:
    print(contact)

# Correct phone data in dataset
pattern = r"(\+7|8)\s*\(*(\d{3})\)?\s?-?(\d{3})\-?(\d{2})-?(\d{2})\s?\(?(доб.)?\s?(\d*)\)?"
sub_pattern = r"+7(\2)\3-\4-\5 \6\7"

for i in range(1, len(contacts_list_new)):
    text = contacts_list_new[i][5]
    contacts_list_new[i][5] = re.sub(pattern, sub_pattern, text)
 
for contact in contacts_list_new:
    print(contact)


