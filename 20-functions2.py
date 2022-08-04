
# def toliq_ism_yasa(ism, familiya):
#     """Toliq ism qaytaruvchi funksiya"""
#     toliq_ism=f"{ism} {familiya}"
#     return toliq_ism

# talaba1=toliq_ism_yasa('olim', 'hakimov')
# talaba2=toliq_ism_yasa('hakim', 'olimov')
# print(f"Bugun darsga {talaba1.title()} va {talaba2.title()} kelmadi.")
# print(f"{talaba1.title()} darsga kechikib keldi.")


# def my_function(x):
#   return 5 * x

# print(my_function(3))
# print(my_function(5))
# print(my_function(9))

# IXTIYORIY ARGUMENTLAR
# def toliq_ism_yasa(ism, familiya, otasining_ismi=''):
#     """Toliq ism qaytaruvchi funksiya"""
#     if otasining_ismi:
#         toliq_ism=f"{ism} {otasining_ismi} {familiya}"
#     else:
#         toliq_ism=f"{ism} {familiya}"
#     return toliq_ism.title()

# talaba1=toliq_ism_yasa('olim', 'hakimov')
# talaba2=toliq_ism_yasa('ali', 'alijonov', 'kamolovich')

# print(f"Darsga kelgan talabar {talaba1} va {talaba2}.")

# FUNKSIYADAN LUG'AT QAYTARAMIZ
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto={
#         'company': kompaniya,
#         'model': model,
#         'color': rangi,
#         'type': korobka,
#         'year': yili,
#         'price': narhi
#     }
#     return avto

# avto1=avto_info('GM', 'Malibu', 'qora', 'avtomat', 2018)
# avto2=avto_info('GM', 'Jentra', 'oq', 'mexanika', 2015, 10000)
# avtolar=[avto1, avto2]
# print("Onlayn bozordagi mavjud avtomashinalar")
# for avto in avtolar:
#     if avto['price']:
#         price=avto['price']
#     else:
#         price="Nomalum"
#     print(f"{avto['color'].title()} {avto['model']}. Narhi: {price}.")


# def oraliq(min,max,qadam=2):
#     sonlar=[]
#     while min<max:
#         sonlar.append(min)
#         min+=2
#     return sonlar

# print(oraliq(1,11,2))
# print(oraliq(100,150))


# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto={
#         'company': kompaniya,
#         'model': model,
#         'color': rangi,
#         'type': korobka,
#         'year': yili,
#         'price': narhi
#     }
#     return avto

# print("Saytimizdagi avtolar ro'yhatini shakllantiramiz.")
# avtolar=[]
# while True:
#     print("\nQuyidagi ma'lumotlarni kiriting:", end=' ')
#     kompaniya=input("Kompaniya nomi: ")
#     model=input("Mashina modeli: ")
#     rangi=input("Mashina rangi: ")
#     korobka=input("Korobka: ")
#     yili=input("Ishlab chiqarilgan yili: ")
#     narhi=input("Mashina narhi: ")


#     avtolar.append(avto_info(kompaniya, model, rangi, korobka, yili, narhi))

#     javob=input("Yana ma'lumot kiritasizmi? (yes/no): ")
#     if javob=='no':
#         break

# print("Salonimizdagi avtolar:")
# for avto in avtolar:
#     if avto['price']:
#         price=avto['price']
#     else:
#         price='nomalum'
#     print(f"{avto['color'].title()} {avto['model']}, {avto['type']} korobka, Narhi: {avto['price']}$.")

# print(avtolar)


























