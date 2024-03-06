# Номера телефонов организаций

Этот репозиторий содержит модуль для поиска и форматирования номеров телефонов организаций на веб-страницах.

## Зачем?

Компания с острова Jost Van Dyke разрабатывает сайт-справочник организаций. Однако, номера телефонов на сайте часто устаревают, что приводит к потере клиентов. Для решения этой проблемы был создан модуль, который находит и форматирует номера телефонов на веб-страницах компаний.

## Результат выполнения программы

```
Найденные номера телефонов для Hands:
74951370720
Найденные номера телефонов для Repetitors:
84955405676
```

## Как использовать?

1. Установите необходимые зависимости, выполнив команду `pip install -r requirements.txt`.
2. Импортируйте классы `Organization` и `PhoneFinder` из модуля `phone_finder.py` в свой код.
3. Создайте объекты класса `Organization`, указав название компании, URL её сайта и список страниц контактов.
4. Создайте объект класса `PhoneFinder`.
5. Используйте метод `find_phone_numbers()` объекта `PhoneFinder`, передавая ему объекты `Organization`, чтобы найти номера телефонов на соответствующих страницах контактов.
6. Отформатируйте найденные номера при необходимости, используя метод `format_phone_number()`.

## Пример использования

```python
from phone_finder import Organization, PhoneFinder

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
```

## Дополнительная информация

- Для запуска скрипта необходимо иметь установленный Python версии 3.x.
- Проект использует библиотеку requests для выполнения HTTP-запросов и регулярные выражения для поиска номеров телефонов на веб-страницах.
