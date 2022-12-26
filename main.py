import csv
import re


def get_right_format_data(contacts_list):
    updated_data = []
    for person in contacts_list[1:]:
        full_name = ' '.join(person[0:3])
        phone = person[-2]
        phone_num = r"(\+7|8)?\s*\(?(\d{3})\)?[-\s]*(\d{3})[-\s]*(\d{2})[-\s]*(\d{2})(\s*[\(\д\о\б\.]*\s*)((\d{4})\)?)?"
        if len(phone.split('доб')) == 2:
            correct_phone_format = r"+7(\2)\3-\4-\5 доб.\8"
        else:
            correct_phone_format = r"+7(\2)\3-\4-\5"
        new_format_phone = re.sub(phone_num, correct_phone_format, phone)
        person_with_correct_data = [full_name.split(' ')[0], full_name.split(' ')[
            1], full_name.split(' ')[2], person[3], person[4], new_format_phone, person[6]]
        updated_data.append(person_with_correct_data)
    persons = []
    others_parameters = []
    for item in updated_data:
        last_name_with_name = ' '.join(item[0:2])
        new_format = [last_name_with_name, item[2],
                      item[3], item[4], item[5], item[6]]
        persons.append(last_name_with_name)
        others_parameters.append(new_format)
    final_list = []
    for i in set(persons):
        lastname = set()
        firstname = set()
        surname = set()
        organization = set()
        position = set()
        phone = set()
        email = set()
        fin = []
        for j in others_parameters:
            if i == j[0]:
                lastname.add(i.split(' ')[0])
                firstname.add(i.split(' ')[1])
                surname.add(j[1])
                organization.add(j[2])
                position.add(j[3])
                phone.add(j[4])
                email.add(j[5])

        fin.extend(list(lastname))
        fin.extend(list(firstname))
        fin.extend(list(surname))
        fin.extend(list(organization))
        fin.extend(list(position))
        fin.extend(list(phone))
        fin.extend(list(email))
        final_list.append(fin)
    return(final_list)


if __name__ == '__main__':
    with open("phonebook_raw.csv", encoding='utf-8') as f:
        rows = csv.reader(f, delimiter=",")
        contacts_list = list(rows)

    final_list = get_right_format_data(contacts_list)

    with open("phonebook.csv", "w", newline='', encoding='utf-8') as f:
        datawriter = csv.writer(f, delimiter=',')
        datawriter.writerows(final_list)
