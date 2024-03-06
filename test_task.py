import requests
import re
from typing import Iterable


class Organization:
    def __init__(self, name: str, url: str, contact_pages: Iterable):
        self.name = name
        self.url = url
        self.contact_pages = contact_pages

    def __str__(self):
        return self.name


class PhoneFinder:
    def __init__(self):
        self.phone_regex = re.compile(
            r"""(?:\+7|8)\s?[-(]?\s?9\d{2}\s?[-)]?\s?\d{3}[-]?\s?\d{2}[-]?\s?\d{2}|(?:\+7|8)\s?[-(]?\s?49\d{1}\s?[-)]?\s?\d{3}[-]?\s?\d{2}[-]?\s?\d{2}|(?:\+7|8)\s?[-(]?\s?800\s?[-)]?\s?\d{3}[-]?\s?\d{2}[-]?\s?\d{2}|(?:\+7|8)\s?[-(]?\s?9\d{2}\s?[-)]?\s?\d{7}
        """,
            re.VERBOSE,
        )

    def find_phone_numbers(self, organization):
        phone_numbers = set()
        for contact_page in organization.contact_pages:
            try:
                response = requests.get(organization.url + contact_page)
                html_content = response.text
                numbers_on_page = self.phone_regex.findall(html_content)
                for number in numbers_on_page:
                    phone_numbers.add("".join(number))
            except Exception as e:
                print(f"Ошибка при обработке {organization.name}: {e}")
        return phone_numbers

    def format_phone_number(self, phone_number):
        # Убираем лишние символы из номера и приводим его к единому формату
        formatted_number = re.sub(r"\D", "", phone_number)
        return formatted_number


if __name__ == "__main__":
    organizations = [
        Organization("Hands", "https://hands.ru", ["/company/about"]),
        Organization("Repetitors", "https://repetitors.info", ["/contacts"]),
    ]

    phone_finder = PhoneFinder()

    for org in organizations:
        found_numbers = phone_finder.find_phone_numbers(org)
        print(f"Найденные номера телефонов для {org}:")
        for number in found_numbers:
            formatted_number = phone_finder.format_phone_number(number)
            print(formatted_number)
