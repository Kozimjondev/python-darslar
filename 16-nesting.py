
# car0 = {
#         'model':'lacetti',
#         'rang':'oq',
#         'yil':2018,
#         'narh':13000,
#         'km':50000,
#         'korobka':'avtomat'
#         }

# car1 = {
#         'model':'nexia 3',
#         'rang':'qora',
#         'yil':2015,
#         'narh':9000,
#         'km':89000,
#         'korobka':'mexanika'
#         }

# car2 = {
#         'model':'gentra',
#         'rang':'qizil',
#         'yil':2019,
#         'narh':15000,
#         'km':20000,
#         'korobka':'mexanika'
#         }

# # car=car2
# # print(f"{car['model'].title()}, "
# # f"{car['rang']} rang, "
# # f"{car['yil']}, {car['narh']}$")

# cars=[car0, car1, car2]
# # for car in cars:
# #     print(f"{car['model'].title()}, "
# #     f"{car['rang']} rang, "
# #     f"{car['yil']}-yil, {car['narh']}$")

# # print(cars)
# # print(f"{cars[2]['rang'].title()} "
# #       f"{cars[2]['model']}")

# malibus=[]
# for n in range(10):
#     new_car={
#         'model': 'lacetti',
#         'rang' : 'none',
#         'yil': 2022,
#         'narh': 'none',
#         'km': 0,
#         'korobka': 'avto'
#         }
#     malibus.append(new_car)

# for malibu in malibus[:3]:
#     malibu['rang']='qizil'

# # for malibu in malibus:
# #     print(malibu)

# for malibu in malibus[3:6]:
#     malibu['rang']='qora'

# for malibu in malibus[6:11]:
#     malibu['rang']='ko\'k'
#     malibu['korobka']='mexanika'

# for malibu in malibus:
#     if malibu['korobka']=='avto':
#         malibu['narh']=40000
#     else:
#         malibu['narh']=30000
        
# for malibu in malibus:
#      print(malibu)

# print(f"{cars[0]['rang'].title()} {cars[0]['model']}")

# LUG'AT ICHIDA RO'YHAT
dasturchilar={
    'ali': ['python', 'c++'],
    'vali': ['html', 'css', 'js'],
    'hasan': ['php', 'sql'],
    'husan': ['python', 'php'],
    'maryam': ['c++', 'c#']
}

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(til.upper())

for ism, tillar in dasturchilar.items():
    print(f"\n{ism.title()} quyidagi dasturlash tillarini biladi:")
    for til in tillar:
        print(f"{til.upper()}" , end=" ")

hamkasblar={
    'ali': {
        'familiya': 'aliyev',
        'tyil': 2000,
        "malumot": 'oliy',
        'tillar': ['python', 'c++']
    },
    'vali': {
        'familiya': 'valiyev',
        'tyil': 1999,
        "malumot": 'maxsus',
        'tillar': ['js', 'html', 'css']
    },
    'hasan': {
        'familiya': 'Husanov',
        'tyil': 1997,
        "malumot": "o'rta-maxsus",
        'tillar': ['php', 'laravel']
    }
}

for key, info in hamkasblar.items():
    print(f"\n{key.title()} {info['familiya'].title()}",
    f"{info['tyil']}-yilda tug'ilgan.",
    f"Ma'lumoti: {info['malumot']}. \n"
    "Quyidagi dasturlash tillarini biladi:")
    for til in info['tillar']:
        print(f"{til.upper()}", end=" ")











