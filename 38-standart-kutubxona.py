# import datetime as dt
# now=dt.datetime.now()
# print(now)
# print(type(now))

# bugun=dt.date.today()
# print(f"Bugungi sana: {bugun}")
# ertaga=dt.date(2022, 9, 7)
# print(f"Ertangi sana: {ertaga}")

# time()
# hozir=dt.datetime.now()
# vaqthozir=hozir.time()
# print(f"Hozir soat: {vaqthozir}")
# vaqtkeyin=dt.time(23, 45, 58)
# print(f"Ertangi vaqt: {vaqtkeyin}")


# Sanalar orasidagi farq
# bugun=dt.date.today()
# ramazon=dt.date(2023, 3, 22)
# farq=ramazon-bugun
# # print(farq)
# print(f"Ramazonga {farq.days} kun qoldi.")


# Soatlar orasidagi farq
# hozir=dt.datetime.now()
# futbol=dt.datetime(2022, 9, 7, 0, 0, 0)
# farq=futbol-hozir
# # print(futbol)
# # print(farq)
# sekundlar=farq.seconds
# # print(sekundlar)
# minutlar=int(sekundlar/60)
# soatlar=int(minutlar/60)
# # print(soatlar)
# print(f"Futbol boshlanishiga {farq.days} kunu {soatlar} qoldi.")


# import math
# PI=math.pi
# print(f"PI ning qiymati: {PI}")
# E=math.e
# print(f"E ning qiymati: {E}")

# trigonometriya
# print(math.sin(PI/2))
# print(math.cos(0))
# print(math.tan(PI))


# radianlar va burchaklar o`rtasida konvertatsya
# print(math.degrees(math.pi/2))
# print(math.radians(90))


# logarifmlar
# natural logarifm
# print(math.log(math.e))
# 10 asosli logarifm
# print(math.log10(1000))


# Sonlarni yaxlitlash
x=4.6
# print(math.ceil(x))
# print(math.floor(x))


# Kvadrat ildiz
x=81
# print(math.sqrt(x))


# Darajaga oshirish
# print(math.pow(x,3))
# print(math.pow(x,0.5))
# print(math.pow(x,1/4))


# from pprint import pprint
# import json

# filename='bemor.json'
# with open(filename) as f:
#     bemor=json.load(f)

# pprint(bemor)



import re

word1='tulpor'
word2='temir'
word3='tomir'

# andoza='^t...r$'

# print(re.match(andoza, word1))
# print(re.match(andoza, word2))
# print(re.match(andoza, word3))

matn = """Maqolalar  2020-yilning 20-martiga qadar rtmkonferensiya2021@mail.ru elektron pochtasida qabul qilinadi.
Quyidagi yo'nalishdagi maqolalar qabul qilinadi:
👉 Aniq va tabiiy fanlarni zamonaviy pedagogik texnologiyalar asosida o‘qitish  metodikasi.
👉 Umumta’lim  fanlarini o‘qitishda  kozimjon@gmail.com STEAM yondashuvning o’rni va ahamiyati. """

andoza = '[^@ \t\r\n]+@[^@ \t\r\n]+\.[^@ \t\r\n]+'
email = re.findall(andoza,matn)
print(email)

# andoza='^(?=.*?[A-Z])(?=.*?[a-z])(?=.*?[0-9])(?=.*?[#?!@$ %^&*-]).{8,}$'

# msg="Yangi parol kiriting(kamida 8 ta belgidan iborat, kamida 1 ta lotin bosh harf, 1 ta kichik harf, 1 ta son va 1 ta maxsus belgi bo'lishi kerak):\n "

# while True:
#     password=input(msg)
#     if re.match(andoza, password):
#         print("Maxfiy so'z qabul qilindi.")
#         break
#     else:
#         print("Maxfiy so'z qabul qilinmadi.")




