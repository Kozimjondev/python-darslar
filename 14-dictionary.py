car_0={'model':'ferrari','rang':'qizil'}
# print(type(car_0))
# print(car_0['model'])
# print(type(car_0))
# print(car_0['rang'])

# en_uz={'apple':'olma',  'apricot':'o\'rik',  'banana':'banan'}
# print(en_uz['apple'])

# mevalar={'olma':10000,  "o'rik":15000,  'tarvuz':8000}
# print(f"Olma narhi {mevalar['olma']} so'm")

# talaba_0={'ism':'murod olimov',  'yosh':20,  't_yil':2000}
# print(f"{talaba_0['ism'].title()},\
#  {talaba_0['yosh']}-yoshda,\
#  {talaba_0['t_yil']}-yilda tug'ilgan")
# talaba_0['kurs']=4
# talaba_0['fakultet']='informatika'
# print(talaba_0)
# talaba_0['ism']='abdulloh'
# print(talaba_0)

# talaba_1={}
# talaba_1['ism']='qobil karimov'
# talaba_1['kurs']=3
# talaba_1['yosh']=21
# print(talaba_1)
# print(f"{talaba_1['ism'].title()}, {talaba_1['kurs']}-kurs talabasi, {talaba_1['yosh']} yosh")

# talaba_1['kurs']=4
# print(f"{talaba_1['ism'].title()}, {talaba_1['kurs']}-kurs talabasi, {talaba_1['yosh']} yosh")

# talaba_0={'ism':'murod olimov',  'yosh':20,  't_yil':2000}
# del talaba_0['yosh']
# print(talaba_0)

telefonlar={
    'ali':'iphone x',
    'vali':'galaxy s11',
    'karim':'mi 5+',
    'anvar':'nokia 1202'
}
print(telefonlar['ali'])

phone=telefonlar.get('hasan', 'Hasanda telefon yo\'q')
print(phone)










