
# talaba_0={
#     'ism': 'alijon',
#     'familiya': 'shamsiyev',
#     'yosh': 22,
#     'fakultet': 'matematika',
#     'kurs': 4
# }
# print(talaba_0.items())

# for key,value in talaba_0.items():
#     print(f"Kalit: {key}")
#     print(f"Qiymat: {value}\n")

# telefonlar={
#     'ali': 'iphone 13',
#     'vali': 'galaxy s9',
#     'ikrom': 'redmi ',
#     'temur': 'nokia 1202'
# }
# for k,q in telefonlar.items():
#     print(f"{k.title()}ning telefoni {q}.")

# mahsulotlar={
#     'olma': 10000,
#     'anjir': 15000,
#     'uzum': 9000,
#     'nok': 20000,
#     'anor': 24000
# }
# print(mahsulotlar.keys())

# print("Do'kondagi mahsulotlar:")
# for mahsulot in mahsulotlar.keys():
#     print(mahsulot.title())

# print("Do'kondagi mahsulotlar:")
# for mahsulot in mahsulotlar:
#     print(mahsulot.title())

mahsulotlar={
    'olma': 10000,
    'anjir': 15000,
    'uzum': 9000,
    'nok': 20000,
    'anor': 24000
}
# bozorlik=['anor', 'olma', 'non', 'baliq']
# for mahsulot in mahsulotlar:
#     if mahsulot in bozorlik:
#         print(f"{mahsulot.title()} {mahsulotlar[mahsulot]} so'm")

# for buyum in bozorlik:
#     if buyum not in mahsulotlar:
#         print(f"Iltimos do'koningizga {buyum} ham olib keling")

# print("Do'konimizdagi mahsulotlar:")
# for mahsulot in sorted(mahsulotlar):
#     print(mahsulot.title())

# telefonlar={
#     'ali': 'iphone 13',
#     'vali': 'galaxy s9',
#     'ikrom': 'redmi ',
#     'temur': 'nokia 1202'
# }
# print(telefonlar.values())
# print("Foydalanuvchilar quyidagi telefonlar ishlatadi:")
# for tel in telefonlar.values():
#     print(tel)

telefonlar = {
    'ali':'iphone x',
    'vali':'galaxy s9',
    'olim':'mi 10 pro',
    'orif':'nokia 3310',
    'hamida':'galaxy s9',
    'maryam':'huawei p30',
    'tohir':'iphone x',
    'umar':'iphone x'    
    }
print("Foydalanuvchilari quyidagi telefonlar ishlatadi:")
for tel in set(telefonlar.values()):
    print(tel)
















