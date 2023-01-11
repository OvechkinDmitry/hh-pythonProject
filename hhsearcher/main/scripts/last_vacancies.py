import numpy as np
import pandas as pd
import requests
import json

pd.set_option("display.max_columns", None)

valutes = {
        "AZN": "манат.",
        "BYR": "бел. руб.",
        "EUR": "евро",
        "GEL": "груз. лари",
        "KGS": "кирг. сом",
        "KZT": "тнг.",
        "RUR": "руб.",
        "UAH": "гривн.",
        "USD": "долл.",
        "UZS": "узб. сум",
    }

class hh_parser:
    """Класс для парсинга вакансий с hh
    Attributes:
        info (dict): словарь для формирования csv-файла с названием профессии, зарплатой, местностью и датой публикации
    """
    def __init__(self, day):
        """Инициализирует класс hh_parser"""
        day = int(day)
        self.day = str(day) if len(str(day)) == 2 else "0" + str(day)
        self.next_day = str(day + 1) if len(str(day + 1)) == 2 else "0" + str(day + 1)
        self.needed_vacancies = ['analytic', 'аналитик', 'analyst', 'аналітик']
        self.info = {'name': [], "salary": [],
                     'area_name': [], 'published_at': [], "employer_name": [],
                     "snippet_requirement": [], "snippet_responsibility": [], }

    def fetch_data(self):
        """Запрашивает данные с сайта hh.ru и записывает их в словарь"""
        for date_from in [f'2022-12-{self.day}T00:00:00',f'2022-12-{self.day}T06:00:00',
                          f'2022-12-{self.day}T12:00:00',f'2022-12-{self.day}T18:00:00',
                          f'2022-12-{self.next_day}T00:00:00']:
            date_to = f'2022-12-{self.next_day}T00:00:00'
            for page in range(1, 20):
                if len(self.info["name"]) > 10:
                    break
                request = requests.get(f'https://api.hh.ru/vacancies?date_from={date_from}&date_to={date_to}&specialization=1&per_page=100&page={page}')
                if "items" not in json.loads(request.text).keys():
                    continue
                for item in json.loads(request.text)['items']:
                    condition_array = np.in1d(item['name'].split(), self.needed_vacancies)
                    if True not in condition_array:
                        continue
                    self.info['name'].append(item['name'])
                    salary = item['salary']
                    salary_from, salary_to, salary_currency = None, None, None
                    if salary is not None:
                        salary_from = salary['from']
                        salary_to = salary['to']
                        salary_currency = valutes[f'{salary["currency"]}']
                        salary_currency = "" if salary_currency is None else " "+salary_currency
                        if salary_from is None:
                            self.info["salary"].append(str(salary_to) + salary_currency)
                        elif salary_to is None:
                            self.info["salary"].append(str(salary_from) + salary_currency)
                        else:
                            self.info["salary"].append(str(((salary_from + salary_to) / 2)) + salary_currency)
                    else:
                        self.info["salary"].append("Не указана")
                    snippet = item['snippet']
                    employer = item['employer']
                    self.info["snippet_requirement"].append(snippet['requirement'])
                    self.info["snippet_responsibility"].append(snippet['responsibility'])
                    self.info["employer_name"].append(employer["name"])
                    area = item['area']
                    area_name = None
                    if area is not None:
                        area_name = area['name']
                    self.info['area_name'].append(area_name)
                    self.info['published_at'].append(item['published_at'].split("T")[0])
        df = pd.DataFrame(self.info)
        df = df.drop_duplicates()
        df = df.sort_values(by=["published_at"]).head(10)
        records = df.to_dict('records')
        return records
