# Bugungi sanadan boshlab 2 hafta farq bilan 10 ta sanani konsolga chiqaring
# import datetime as dt
import re

# bugun=dt.date.today()

# print(bugun)


# Ramazon va qurbon hayitigacha qolgan kunlarni konsolga chiqaring
# bugun1=dt.date.today()
# ramazon=dt.date(2023, 3, 23)
# qurbon_hayit=dt.date(2023, 6, 28)
# farq=ramazon-bugun1
# farq2=qurbon_hayit-bugun1
# print(f"Ramazonga {farq.days} kun qoldi.")
# print(f"Qurbon hayiti kuniga {farq2.days} kun qoldi.")


# Tug'ilgan kuningizdan bugungi sanagacha qancha yil, oy, kun o'tganini qaytaruvchi funksiya yozing.
# bugun=dt.date.today()
# t_kun=dt.date(1999, 8, 29)
# farq=bugun-t_kun
# farq=farq.days
# # print(farq)
# yil=int(farq/365)
# oy=int((farq-yil*365)/30)
# kun=int((farq-yil*365)-oy*30)

# print(f"Tug'ilgan kunimdan shu kungacha {yil} yil, {oy} oy va {kun} kun bo'ldi. ")


# Foydalanuvchidan telefon raqamini kiritishni so'rang. Kiritlgan qiymatni andoza yordamida tekshiring.

# nomer=input("Telefon raqamingizni kiriting: ")

# andoza="^[\+]?[(]?[0-9]{3}[)]?[-\s\.]?[0-9]{3}[-\s\.]?[0-9]{4,6}$"

# print(re.match(andoza, nomer))



# Berilgan matndan veb sahifa manzilini ajratib olyuvchi funksiya yozing. Quyidagi matndan namuna sifatida foydalanishingiz mumkin:

matn="""Assalom alaykum hurmatli do'stlar. Navbatdagi darsimiz YouTubega yuklandi: https://youtu.be/vsxJPRLXpgI
Ushbu darsimizda unittest moduli yordamida klasslarning xususiyatlar va metodlarini tekshiruvchi dastur yozishni o'rganamiz. Bugungi dars manzili: https://python.sariq.dev/testing/37-klass-test"""

andoza="https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{1,256}\.[a-zA-Z0-9()]{1,6}\b([-a-zA-Z0-9()!@:%_\+.~#?&\/\/=]*)"

web_site=re.findall(andoza, matn)
print(web_site)




















