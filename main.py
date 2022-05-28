import random

from faker import Faker
import json

from conf import MODEL

def pk(x):
    x += 1
    yield x

def title():
    fil = open("books.txt", 'r', encoding='utf-8')
    titl = fil.readlines()
    titl_ = random.choice(titl)
    return titl_



def year():
    year_ = random.randint(1900,2022)
    return year_

def pages():
    pag = random.randint(0,500)
    return pag

def isbn13():
    isd = fake_ru.isbn13()
    return isd

def rating():
    rat = random.uniform(0,5)
    return rat

def price():
    pri = random.uniform(100,20000)
    return pri

def author():
    author_ = fake_ru.name()
    return author_




if __name__ == "__main__":
    dict_ = {}
    for i in range(1, 250):
        # name = fake_ru.name()
        # tn = fake_ru.phone_number()
        # j = fake_ru.job()
        # ad = fake_ru.address()
        #dict_[i] = {name: [ad, j, tn]}
        dict_[] = {f"model":}
        with open("DS.txt", 'w', encoding='utf-8') as f:
            json.dump(dict_, f, indent=4, ensure_ascii=False)