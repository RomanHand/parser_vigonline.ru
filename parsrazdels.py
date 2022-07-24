import csv
import requests
from bs4 import BeautifulSoup
import re




def parsrazdels(url):
    # юрла нашего сайта
    url = "https://vigonline.ru/"
    # штука что бы умные сайты не забанили
    headers = {
        "Accept": "*/*",
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/102.0.0.0 Safari/537.36"
    }
    req = requests.get(url, headers=headers)
    src = req.text
    # качаем и работаем с сайтом
    with open("index.html", "w", encoding='utf8') as file:
        file.write(src)

    with open("index.html", encoding='utf8') as file:
        src = file.read()
    # переменная soup = весь сайт
    soup = BeautifulSoup(src, "lxml")
    # В переменную ищем необходимые классы
    sobitie = soup.find_all(class_='home_catwalls_podcat')
    # print(sobitie)

    i = 0
    a = len(sobitie)
    resoult = []

    while i < a:
        sobitie[i] = str(sobitie[i])
        urls = re.findall(r'https://vigonline.ru/\S+/\S+', sobitie[i], flags=0)
        urls = str(urls)
        urls = urls[2:-5]
        urls = urls.replace('&amp;', '&')
        resoult.append(urls)
        i = i + 1
        #print(urls)
    return resoult

#url = "https://vigonline.ru/"
#parsrazdels(url)
