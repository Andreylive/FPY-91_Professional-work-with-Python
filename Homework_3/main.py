
import requests
import fake_headers
from bs4 import BeautifulSoup
import json


def gen_headers():
    headers_gen = fake_headers.Headers(os="win", browser="chrome")
    return headers_gen.generate()


url = 'https://spb.hh.ru/search/vacancy?text=python&area=1&area=2'

main_response = requests.get(url, headers=gen_headers())
main_html_data = main_response.text
main_soup = BeautifulSoup(main_html_data, "lxml")

vacancies = main_soup.find_all("div", class_="vacancy-serp-item__layout")

parsed_data = []

for vacancy in vacancies:
    company = vacancy.find(
           "a", {"data-qa": "vacancy-serp__vacancy-employer"}
    ).text
    full_adress = vacancy.find(
           "div", {"data-qa": "vacancy-serp__vacancy-address"}
    ).text
    city = full_adress.split(",")[0]
    link = vacancy.find("a", class_="bloko-link")["href"]
    salary_teg = vacancy.find(
            "span", {"data-qa": "vacancy-serp__vacancy-compensation"})
    salary = salary_teg.text if salary_teg else "Не указана"

    full_vacancy_text = requests.get(link, headers=gen_headers())
    full_vacancy_html_data = full_vacancy_text.text
    full_vacancy_soup = BeautifulSoup(full_vacancy_html_data, "lxml")
    full_vacancy_tag = full_vacancy_soup.find(
            "div", {"data-qa": "vacancy-description"})
    full_vacancy_text = full_vacancy_tag.text.strip()

    if "Django" in full_vacancy_text or "Flask" in full_vacancy_text:
        parsed_data.append(
            {
                "Company": company,
                "City": city,
                "Salary": salary,
                "link": link
            }
        )

with open("vacancies.json", "w", encoding="utf-8") as f:
    json.dump(parsed_data, f, ensure_ascii=False, indent=4)
