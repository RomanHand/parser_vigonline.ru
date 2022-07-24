import csv
import requests
from bs4 import BeautifulSoup
import re


def parscrad(items):
    # штука что бы умные сайты не забанили
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    req = requests.get(items, headers=headers)
    src = req.text
    # качаем и работаем с сайтом
    with open("index.html", "w", encoding='utf8') as file:
        file.write(src)

    with open("index.html", encoding='utf8') as file:
        src = file.read()
    # переменная soup = весь сайт
    soup = BeautifulSoup(src, "lxml")

    # В переменную ищем необходимые классы
    sobitie1 = soup.find_all(itemprop="brand")  # Бренд
    sobitie2 = soup.find_all(class_="img-responsive")  # Картинка
    sobitie3 = soup.find_all(class_="inbreadcrumb")  # Имя
    sobitie4 = soup.find_all(class_="pr_weight")  # вес
    sobitie5 = soup.find_all(class_="breadcrumb")  # раздел
    sobitie6 = soup.find_all(class_="tab-pane active")  # Описание

    if len(sobitie1) > 0:
        branditem = str(sobitie1[0].text)
        # print(branditem)
    else:
        branditem = "none"

    picitembl = str(sobitie2[1])
    picitem = re.findall(r'https://vigonline.ru/\S+/\S+/\S+/\S+.', picitembl, flags=0)
    picitem = str(picitem)
    picitem = picitem[2:-4]
    # print(picitem)

    if len(sobitie3) > 0:
        nameitem = str(sobitie3[0].text)
        # print(nameitem)
    else:
        nameitem = "none"

    if len(sobitie4) > 0:
        weightitem = str(sobitie4[0].text)
        # print(weightitem)
    else:
        weightitem = "none"

    roaditem = sobitie5[0].text
    roaditem = str(roaditem)
    roaditem = roaditem.replace(nameitem, " ")
    roaditem = roaditem.replace('...', "")
    roaditem = roaditem.strip()
    roaditem = roaditem.replace('Главная', "")

    textitem = sobitie6[0].text

    # Выводим инфу
    print(nameitem, weightitem, picitem, branditem, roaditem, textitem)

    return nameitem, weightitem, picitem, branditem, roaditem, textitem


#items = "https://vigonline.ru/rk-marine-2303"
#parscrad(items)
