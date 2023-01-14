import csv
import re


def word_processing(string):
    refactored_string = re.compile(r'<[^>]+>').sub('', string)
    refactored_string = refactored_string.replace(" ", " ").replace(" ", " ").replace("  ", " ").replace(
        "  ", " ").strip()
    return refactored_string


def print_most_popular_skills():
    for year in sorted_skills.keys():
        top_n = {}
        skills_count = len(sorted_skills[year])
        skills = []
        table_html = '<table><tbody><tr><td>Навык</td><td>Количество упоминаний</td></tr>'
        for i in sorted_dict_skills[year].keys():
            skills.append(i)
        for i in range(min(skills_count, 10)):
            skill = skills[i]
            times = sorted_dict_skills[year][skill]
            top_n[f'{skill}'] = times
            table_html += f'<tr><td>{skill}</td><td>{times}</td></tr>'
        if top_n:
            generate_img(top_n, year)
            print(year)
            print(table_html+'</tbody></table>')
            print()



def sort_dict_skills():
    for year in dictionary.keys():
        sorted_dict_skills[year] = {}
        sorted_skills = sorted(dictionary[year], key=dictionary[year].get, reverse=True)
        for i in sorted_skills:
            sorted_dict_skills[year][i] = dictionary[year][i]
    return sorted_dict_skills


def csv_reader_second(file_name):
    with open(file_name, encoding="utf-8-sig") as File:
        reader = csv.reader(File)
        first_element = True
        for rows in reader:
            year = rows[6][:4]
            if first_element:
                first_element = False
                continue
            else:
                if year not in dictionary.keys():
                    dictionary[year] = {}
                profession_splited = rows[0].lower().split()
                flag = True
                for chunk in profession_splited:
                    if chunk in ['analytic', 'аналитик', 'analyst', 'аналітик']:
                        flag = False
                        break
                if flag:
                    continue
                for skill in word_processing(rows[1]).split("\n"):
                    if skill == "":
                        continue
                    if skill not in list(dictionary[year].keys()):
                        dictionary[year][skill] = 1
                    else:
                        dictionary[year][skill] += 1


def get_skills(amount):
    if amount % 100 != 11 and amount % 10 == 1:
        return "скилла"
    return "скиллов"



def generate_img(dic, year):
    import matplotlib.pyplot as plt
    y1 = list(dic.values())
    x1 = list(dic.keys())
    f = plt.figure()
    f.set_size_inches(10, 5)
    plt.barh(x1, y1, color='gray')
    plt.plot()
    plt.xlabel("кол-во вакансий")
    plt.title(f"Топ навыков для профессии аналитик за {year} год")
    plt.tight_layout()
    plt.savefig(f'graph{year}.png')


dictionary = {}
file_name = "vacancies_with_skills.csv"
dict_skills = {}
sorted_dict_skills = {}
csv_reader_second(file_name)
sorted_skills = sort_dict_skills()

print_most_popular_skills()