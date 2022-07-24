import csv
from pars1 import pars1
from parsrazdels import parsrazdels
from parscrad import parscrad
url = "https://vigonline.ru/"
# достаем ссылки на разделы
resoult = parsrazdels(url)
print(resoult)

# достаем ссылки на карточки в каждом разделе
i = 0
a = len(resoult)
print(a)
w = 0
items = []
while i < a:
    url = resoult[i]
    itemsraz = pars1(url)
    print(itemsraz)
    a1 = len(pars1(url))
    i1 = 0
    while i1 < a1:
        items.append(itemsraz[i1])
        i1 = i1 + 1
        w = w + 1
        print(w)

    i = i + 1
print(items)
print(len(items))

# достаем инфу из каждой карточки
i = 0
a = len(items)
with open("out.csv", "w", newline="") as f:
    writer = csv.writer(f)
    writer.writerows(
        [["Модель","Вес",  " Ссылка на фото", "Производитель", "Раздел"]]
    )
test= []
while i < a:
    itog = parscrad(items[i])
    i = i +1
    with open("out.csv", "a", newline="") as f:
        writer = csv.writer(f)
        writer.writerows(
            [itog]
        )

print(i)
print("УРА ЭТА ХУЕТА ЗАКОНЧИЛА ДУМАТЬ!!!!")