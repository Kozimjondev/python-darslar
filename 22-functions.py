
# def avto_info(kompaniya, model, rangi, korobka, yili, narhi=None):
#     avto={
#         'kompaniya': kompaniya,
#         'model': model,
#         'rang': rangi,
#         'korobka': korobka,
#         'yil': yili,
#         'narh': narhi
#     }
#     return avto

# avto1=avto_info('GM', 'malibu', 'qora', 'avtomat', 2018)
# avto2=avto_info('GM', 'lacetti', 'oq', 'avtomat', 2015, 20000)
# avtolar=[avto1, avto2]
# # print("Onlayn bozordagi avtomashinalar: ")
# # for avto in avtolar:
# #     if avto['price']:
# #         price=avto['price']
# #     else:
# #         price="Nomalum"
# #     print(f"{avto['color'].title()} {avto['model']}. Narhi: {price}.")
# print(avto1)

def summa(*sonlar):
    """Kiritilgan sonlar funksiyasini hisoblaydigan dastur"""
    yigindi=0
    for son in sonlar:
        yigindi+=son
    return yigindi

print(summa(1,2,3,4,5))



























