import random
from typing import Callable

from faker import Faker
import json

from conf import MODEL

fake_ru = Faker('ru_RU')


def pk() -> Callable[[], int]:
    """
    счётчик, который увеличивается на единицу при генерации нового объекта


    """
    pk1 = 0

    def pk_() -> int:
        nonlocal pk1
        pk1 += 1
        return pk1

    return pk_


def title() -> str:
    """
    Содержит в себе название книги

    """
    fil = open("books.txt", 'r', encoding='utf-8')
    titl = fil.read().splitlines()
    titl_ = random.choice(titl)
    return titl_


def year() -> int:
    """
    год натуральное число и генерируется случайным образом
    """
    year_ = random.randint(1900, 2022)
    return year_


def pages() -> int:
    """
    страницы является натуральным числом и генерируется случайным образом
    :return:
    """
    pag = random.randint(100, 500)
    return pag


def isbn13():
    """
    международный стандартный книжный номер, генерируется случайным образом
    """
    isb = fake_ru.isbn13()
    return isb


def rating() -> float:
    """
    число с плавающей запятой в диапазоне от 0 до 5 генерируется случайным образом
    """
    rat = random.uniform(0, 5)
    return round(rat, 2)


def price() -> float:
    """
    число с плавающей запятой, генерируется случайным образом
    """
    pri = random.uniform(100, 5000)
    return round(pri, 2)


def author() -> tuple:
    """
    список авторов содержит от 1 до 3 авторо, имя и фамилия автора выбираются случайным образом
    """
    author_1 = fake_ru.name()
    author_2 = fake_ru.name(), fake_ru.name()
    author_3 = fake_ru.name(), fake_ru.name(), fake_ru.name()
    num = random.randint(1, 3)
    if num == 3:
        return author_3
    elif num == 2:
        return author_2
    else:
        return author_1


def main():
    """
    функцию-генератор, которая возвращает словари
    """
    dict_ = {}
    pk1_ = pk()
    for i in range(1, 101):
        dict_[i] = {"model": MODEL, "pk": pk1_(),
                    "fields": {"title": title(), "year": year(),
                               "pages": pages(), "isbn13": isbn13(),
                               "rating": rating(), "price": price(),
                               "author": [author()]}}
        with open("DS.txt", 'w', encoding='utf-8') as f:
            json.dump(dict_, f, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()