from googletrans import Translator

tarjimon=Translator()

# matn_uz="Python dunyodagi eng mashxur dasturlash tili."

# tarjima=tarjimon.translate(matn_uz)

# Original matn
# print(tarjima.origin)

# Tarjima
# print(tarjima.text)

# Original matn tili
# print(tarjima.src)

# Boshqa tillarga tarjima qilish uchun dest parametridan foydalanamiz.
# tarjima_ru=tarjimon.translate(matn_uz, dest='ru')
# print(tarjima_ru.text)


# Biror matnni ingliz tilidan tarjima qilish.
# matn_en="Tashkent is the capital of Uzbekistan."
# tarjima_uz=tarjimon.translate(matn_en, dest='uz')
# print(tarjima_uz.text)

# msg="Tarjima uchun so'z kiriting (chiqib ketish uchun 'q' deb yozing): "
# while True:
#     text=input(msg)
#     if text=='q':
#         break
#     else:
#         tarjima=tarjimon.translate(text,  dest='en')
#         print(tarjima.text)

# import requests
# from pprint import pprint

# # manzil="https://kun.uz/news/2022/08/31/shht-kollektiv-garbga-qarshi-global-blokka-aylanyaptimi"
# # r=requests.get(manzil)
# # pprint(r.text)

# country='Uzbekistan'
# url = f"https://restcountries.eu/rest/v2/name/{country}"
# r=requests.get(url)
# r_json=r.json()[0]
# print(r_json['capital'])

import requests
from bs4 import BeautifulSoup

sahifa = "https://kun.uz/news/main"
r = requests.get(sahifa)


soup = BeautifulSoup(r.text, 'html.parser')
news = soup.find_all(class_="news-title") # yangiliklarning mavzusini ajratib olamiz
print(news[0].text) # eng birinchi yangilikni konsolga chiqaramiz






