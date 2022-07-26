# Yangi cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] degan ro'yxat tuzing, ro'yxat elementlarining birinchi harfini katta qilib konsolga chqaring. GM uchun ikkala harfni katta qiling
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia']
# for car in cars:
#     if car=='gm':
#         print(car.upper())
#     else:
#         print(car.title())

# Yuqoridagi mashqni teng emas (!=) operatori yordamida bajaring.
# cars = ['toyota', 'mazda', 'hyundai', 'gm', 'kia'] 
# for car in cars:
#     if car!='gm':
#         print(car.title())
#     else:
#         print(car.upper())

# Foydalanuvchi login ismini so'rang. Agar login admin bo'lsa, "Xush kelibsiz, Admin. Foydalanuvchilar ro'yxatini ko'rasizmi?" xabarini konsolga chiqaring. Aks holda, "Xush kelibsiz, {foydalanuvchi_ismi}!"  matnini konsolga chiqaring.
# login=input("Loginga ismningizni kirita olasizmi?>>>")
# if login.lower()=="kozimjon":
#     print("Xush kelibsiz, admin. Foydalanuvchilar ro'yxatini ko'rasizmi?")
# else:
#     print(f"Xush kelibsiz, {login.title()}")

# Foydalanuvchidan 2 ta son kiritishni so'rang. Agar ikki son bir-biriga teng bo'lsa, "Sonlar teng" ekan degan yozuvni konsolga chiqaring.
# x=float(input("Birinchi sonni kiriting:  "))
# y=float(input("Ikkinchi sonni kiriting:  "))
# if x==y: print(f"Sonlar teng: {x}={y}")

# Foydalanuvchidan istalgan son kiritishni so'rang. Agar son manfiy bo'lsa konsolga "Manfiy son", agar musbat bo'lsa "Musbat son" degan xabarni chiqaring.
# son=float(input("Istalgan son kiriting:  "))
# if son>0:
#     print(f"{son}-musbat son")
# else:
#     print(f"{son}-manfiy son")

# Foydalanuvchidan son kiritishni so'rang, agar son musbat bo'lsa uning ildizini hisoblab konsolga chiqaring. Agar son manfiy bo'lsa, "Musbat son kiriting" degan xabarni chiqaring. 
son=float(input("Istalgan son kiriting:  "))
if son>0:
    print(son**(1/2))
else:
    print("Musbat son kiriting!")



