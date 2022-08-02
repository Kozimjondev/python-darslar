# Python izohli lug'atini yarating va lug'atga kamida 10 ta so'z qo'shing. Lug'atdagi har bir kalit va qiymatni for tsikli yordamida, alifbo ketma-ketligida chiroyli qilib konsolga chiqaring. 
# dictionary={
#     'string': 'Matn kiritiladi',
#     'integer': 'Butun son',
#     'float': "O'nli son",
#     'if': 'Shartlarni tekshirish operatori',
#     'for': 'Biror amalni qayta bajarish operatori',
#     'list': 'Ro\'yhat',
#     'tuple': "O'zgarmas ro'yhat",
#     'boolean': "Manriqiy qiymat"
# }
# for k,q in sorted(dictionary.items()):
#     print(f"{k.title()}-{q}")

# Davlatlar va ularning poytaxtlari lug'atini tuzing. Avval lug'atdagi davlatlarni, keyin poytaxtlarni alohida-alohida, alifbo ketma-ketligida konsolga chiqaring. 
countries={
    'usa': 'Washington',
    'uzbekistan': 'tashkent',
    'canada': 'ottawa',
    'australia': 'canberra',
    'russia': 'moscow',
    'spain': 'madrid',
    'france': 'paris',
    'germany': 'berlin'
}
# print("Dunyo davlatlari: ")
# for k in sorted(countries.keys()):
#     print(k.upper())

# print("Davlatlarning poytaxti: ")
# for c in sorted(countries.values()):
#     print(c.title())

# Foydalanuvchidan istalgan davlatni kiritishni so'rang va shu davlatning poytaxtini konsolga chiqaring. Agar foydalanuvchi lug'atda yo'q davlatni kiritsa, "Bizda bunday ma'lumot yo'q" degan xabarni chiqaring.
# country=input("Istalgan davlatni nomini yozing:  ").lower()
# capital=countries.get(country)
# if capital==None:
#     print(f"Bizda bunday ma'lumot yo'q")
# else:
#     print(f"{country.title()}ning poytaxti {capital.title()}.")

# Restoran menusi lug'atini tuzing (kamida 10 ta taom-narh juftligini kiriting). Foydalanuvchidan 3 ta ovqat buyurtma berishni so'rang. Foydalanuvchi kiritgan taomlarni menu bilan solishtiring, agar taom menuda bo'lsa narhini ko'rsating, aks holda "bizda bunday taom yo'q" degan xabarni chiqaring.
taomlar={
    'osh': 20000,
    'manti': 16000,
    'kabob': 12000,
    'somsa': 8000,
    'la\'gmon': 15000,
    'norin': 22000,
    'mastava': 14000,
    'chuchvara': 13000,
    "sho'rva": 17000
}
print("3ta taom buyurtma bering.")
buyurtmalar=[]
for n in range(3):
    buyurtmalar.append(input(f"{n+1}-taom:").lower())
for buyurtma in buyurtmalar:
    if buyurtma in taomlar:
        print(f"{buyurtma.title()} {taomlar[buyurtma]} so'm")
    else:
        print("Bizda bunday taom yo'q")
















