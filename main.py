from pprint import pprint
import csv
import re
# читаем адресную книгу в формате CSV в список contacts_list
with open("phonebook_raw.csv", encoding='utf-8') as f:
    rows = csv.reader(f, delimiter=",")
    contacts_list = list(rows)
pprint(contacts_list)
updated_data = []
for person in contacts_list[1:]:
    full_name = ' '.join(person[0:3])
    # print(full_name)
    phone = person[-2]
    phone_num = r"(\+7|8)?\s*\(?(\d{3})\)?[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})(\s*[\(\д\о\б\.]*\s*)((\d{4})\)?)?"
    if len(phone.split('доб')) == 2:
        correct_phone_format = r"+7(\2)\3-\4-\5 доб.\8"
    else:
        correct_phone_format = r"+7(\2)\3-\4-\5"
    new_format_phone = re.sub(phone_num, correct_phone_format, phone)
    # print(new_format_phone)
    person_with_correct_data = [full_name.split(' ')[0], full_name.split(' ')[
        1], full_name.split(' ')[2], person[3], person[4], new_format_phone, person[6]]
    # print(person_with_correct_data)
    updated_data.append(person_with_correct_data)
# print(updated_data[0])
# final = updated_data[0]
# for item in updated_data[1:]:
#     if item[0] ==  and item[1]
# persons = []
# persons_with_last_name_and_name = []
# for person in updated_data:
#     last_name_with_name = ' '.join(person[0:2])
#     persons.append(last_name_with_name)
# # есть список уникальных фИ
# lastname = []
# firstname = []
# surname = []
# for uniq_name in set(persons):
#     # print(uniq_name)
#     for item in updated_data:
#         fi = (' ').join(item[0:2])
#         if uniq_name == fi:
#             x = {
#                 f'{uniq_name}': {
#                     'lastname': item[0],
#                     'firstname': item[1],
#                     'surname': item[2],
#                 }
#             }
#             # print(x)
#             # lastname.append(item[0])
#             # firstname.append(item[1])
#             # surname.append(item[2])
#             # x = {'lastname': item[0],
#             #      'firstname': item[1],
#             #      'surname': item[2],
#             #      'organization': item[3],
#             #      'position': item[4],
#             #      'phone': item[5],
#             #      'email': item[6],
#             #      }
#             # print(x)
# # print(lastname)

with open("phonebook.csv", "w", encoding='utf-8') as f:
    datawriter = csv.writer(f, delimiter=',')
    # Вместо contacts_list подставьте свой список
    datawriter.writerows(updated_data)
