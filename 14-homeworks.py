# otam (onam, akam, ukam, va hokazo) degan lug'at yarating va lug'atga shu inson haqida kamida 3 ta m'alumot kiriting (ismi, tu'gilgan yili, shahri, manzili va hokazo). Lug'atdagi ma'lumotni matn shaklida konsolga chiqaring :Otamning ismi Mavlutdin, 1954-yilda, Samarqand viloyatida tug'ilgan.
# oila={'otam':'Nasirdinov Azimjon', 't_yil':1965, 'manzil':'Govhona qishlog\'i',\
#     'onam':'Nasirdinova Xabibaxon', 't_yil1':1967, 'manzil_1':'Konizar qishlog\'i',\
#         'k_opam':'Nazarova Gulbahor', 't_yil2':1991, 'manzil_2':'Mustaqillik ko\'chasi, 65-uy' 
#      }
# print(f"Otamning ismi {oila['otam']}, {oila['t_yil']}-yilda {oila['manzil']}da tug'ilgan.")
# print(f"Onamning ismi {oila['onam']}, {oila['t_yil1']}-yilda {oila['manzil_1']}da tug'ilgan.")
# print(f"Opamning ismi {oila['k_opam']}, {oila['t_yil2']}-yilda {oila['manzil_2']}da tug'ilgan.")

# Oila a'zolaringizning sevimli taomlari lug'atini tuzing. Lug'atda kamida 5 ta ism-taom jufltigi bo'lsin. Kamida uch kishining sevimli taomini konsolga chiqaring: Alining sevimli taomi osh.
# taomlar={
#     'otam':'osh',
#     'onam':'makron',
#     'k_opam':'kabob',
#     'kch_opam':'manti',
#     'men':'lag\'mon'
# }
# print(f"Otamning sevimli taomi {taomlar['otam']}.")
# print(f"Onamning sevimli taomi {taomlar['onam']}.")
# print(f"Mening sevimli taomim {taomlar['men']}.")

# Python izohli lu'gati tuzing: Lug'atga shu kunga qadar o'rgangan 10 ta so'z (atamani) kiriting (masalan integer, float, string, if, else va hokazo) va har birining qisqacha tarjimasini yozing.
dictionary_py={
    'integer': 'Faqat butun sonlarni qabul qiladi',
    'string': 'Matn ko\'rinishidagi ma\'lumotni qabul qiladi va ekranga chiqaradi',
    'float': "O'nli kasr ko'rinishidagi sonlarni qabul qiladi va ekranga chiqaradi",
    'if': "agar deb tarjima qilinadi va ikki narsadan birini bajarish talab etilganda qo'llaniladi",
    'else': "if sharti bajarilmaganda ishlaydi",
    'list': "Ro'yhat",
    'tuple': "O'zgarmas ro'yhat",
    'boolean': "true yoki false qiymat qabul qiladi"
}
# Foydalanuvchidan biror so'z kiritishni so'rang va so'zning tarjimasini yuqoridagi lug'atdan chiqarib bering. Agar so'z lu'gatda mavjud bo'lmasa, "Bunda so'z mavjud emas" degan xabarni chiqaring.
# kalit=input("Kalit so'zni kiriting:  ").lower()
# print(dictionary_py.get(kalit, 'Bunday so\'z mavjud emas'))

# Yuqoridagi vazifani if-else yordamida qiling va natijani ham foydalanuvchiga tushunarli ko'rinishda chiqaring.
kalit=input("Kalit so'zini kiriting:  ").lower()
if kalit in dictionary_py:
    print(dictionary_py[kalit])
else:
    print("Bunday so'z mavjud emas")

# 2-usul
kalit=input("Kalit so'zini kiriting:  ").lower()
tarjima=dictionary_py.get(kalit)
if tarjima==None:
    print("Bunday so'z mavjud emas")
else:
    print(tarjima)























