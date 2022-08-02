# Adabiyot (ilm-fan, san'at, internet) olamidagi 4 ta mashxur shaxlar haqidagi ma'lumotlarni lug'at ko'rinishida saqlang. Lug'atlarni bitta ro'yxatga joylang, va har bir shaxs haqidagi ma'lumotni konsolga chiqaring
buxoriy={
    'ism': 'Abu Abdulloh ibn Ismoil',
    'tyil': 810,
    'vyil': 870,
    'tjoy': 'Buxoro',
    'asarlar': ['Al-jome As-sahih', 'Al-adab al-mufrad', 'At-tarix al-kabir', 'At-tarix as-sag\'ir']
}

temur={
    'ism': 'Amir Temur',
    'tyil': 1336,
    'vyil': 1402,
    'tjoy': 'Samarqand',
    'asarlar': ["Buyuk imoratlar", 'Kundalik', 'Temur tuzuklari', 'Temu saltanati']
}

navoiy={
    'ism': 'Alisher Navoiy',
    'tyil': 1441,
    'vyil': 1501,
    'tjoy': 'Xirot',
    'asarlar': ['Xamsa', 'Lison ut-tayr', 'Mahbub ul-qulub', 'Munojot']
}

vohidov={
    'ism': 'Erkin Vohidov',
    'tyil': 1936,
    'vyil': 2016,
    'tjoy': 'Farg\'ona',
    'asarlar': ['Nido', 'Tong nafasi', 'Bedorlik', 'Iztirob']
}

# shaxslar=[buxoriy, temur, navoiy, vohidov]
# for shaxs in shaxslar:
#     ism=shaxs['ism']
#     tyil=shaxs['tyil']
#     vyil=shaxs['vyil']
#     tjoy=shaxs['tjoy']
#     print(f"{ism.title()} {tyil}-yilda {tjoy}da tug'ilgan.",
#     f"{vyil-tyil} yil umr ko'rgan.")
    
# Yuqoridagi lug'atlarga har bir shaxsning mashxur asarlari ro'yxatini ham qo'shing. For tsikli yordamida muallifning ismi va uning asarlarini konsolga chiqaring.

# for shaxs in shaxslar:
#     ism=shaxs['ism']
#     asarlar=shaxs['asarlar']
#     print(f"\n{ism}ning mashhur asarlari:")
#     for asar in asarlar:
#         print(asar, end=", ")

# Oila a'zolaringiz (do'stlaringiz) dan 3 ta sevimli kino-seriali haqida so'rang. Do'stingiz ismi kalit, uning sevimli kinolarini esa ro'yxat ko'rinishida lug'artga saqlang.  Natijani konsolga chiqaring.
kinolar={
    'diyorbek': ['qasoskorlar', 'hulk', 'Temir odam'],
    'temur': ['warcraft', 'werewolf', 'thor'],
    'nozimjon': ['t-34', 'notanish', 'qaytar dunyo'],
    'shuhratjon': ['the age of adeline', 'green lantern', 'friends']
}
# for ism, skinolar in kinolar.items():
#     print(f"\n{ism.title()}ning sevimli kinolari:")
#     for kino in skinolar:
#         print(kino.title(), end=", ")

# Davlatlar degan lug'at yarating, lug'at ichida bir nechta davlatlar haqida ma'lumotlarni lug'at ko'rinishida saqlang. Har bir davlat haqida ma'lumotni konsolga chiqaring.
davlatlar={
    'uzbekistan':{
        'capital': 'toshkent',
        'language': 'uzbek',
        'regions': 12,
        'people': 35,
        'situated': 'Central asia'
    },
    'usa':{
        'capital': 'washington',
        'language': 'english',
        'regions': 51,
        'people': 500,
        'situated': 'North America'
    },
    'spain':{
        'capital': 'madrid',
        'language': 'spanish',
        'regions': 15,
        'people': 85,
        'situated': 'Europe'
    }
}
# for davlat, info in davlatlar.items():
#     print(f"\n{davlat.title()}ning poytaxti {info['capital'].title()}",
#     f"\nThe national language of {davlat.title()} is {info['language']}",
#     f"\n{info['people']}mln people dwell in {info['regions']} regions",
#     f"\n{davlat.title()} is situated in {info['situated'].title()}")

# Yuqoridagi dasturga o'zgartirish kiriting: konsolga barcha davlatlarni emas, foydalanuvchi so'ragan davlat haqida ma'lumot bering. Agar davlat sizning lug'atingizda mavjud bo'lmasa, "Bizda bu davlat haqida ma'lumot yo'q" degan xabarni chiqaring.
c=input("Davlat nomini kiriting: ").lower()
if c in davlatlar.keys():
        info=davlatlar[c]
        print(f"\n{c.title()}ning poytaxti {info['capital'].title()}",
        f"\nThe national language of {c.title()} is {info['language']}",
        f"\n{info['people']}mln people dwell in {info['regions']} regions",
        f"\n{c.title()} is situated in {info['situated'].title()}")
else:
    print("Bizda bunday davlat yo'q")
    











