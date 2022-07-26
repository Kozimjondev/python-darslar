# Kamida 5 elementdan iborat ismlar degan ro'yxat tuzing, va ro'yxatdagi har bir ismga takrorlanuvchi xabar yozing
# ismlar=["Diyorbek", "Nozimjon", "Temur", 'Shuhratjon', 'Sarvarbek']
# for ism in ismlar:
#     print(f"{ism} bugun osh bor Uchariqda, kelasizlarmi?")
# print("Kod 5 marta takrorlandi")

# 10 dan 100 gacha bo'lgan toq sonlar ro'yxatini tuzing. Ro'yxatning xar bir elementining kubini yangi qatordan konsolga chiqaring.
# toq_sonlar=list(range(11,100,2))
# for son in toq_sonlar:
#     print(f"{son} ning kubi {son**3} ga teng")

# Foydalanuvchidan 5 ta eng sevimli kinolarini kiritshni so'rang, va kinolar degan ro'yxatga saqlab oling. Natijani konsolga chiqaring.
# kinolar=[]
# for kino in range(5):
#     kinolar.append(input(f"{kino+1}-eng sevimli kino nomini kiriting:"))
# print(kinolar)

# Foydalanuvchidan bugun nechta odam bilan uchrashganini (suhbatlashganini) so'rang, va har bir suhbatlashgan odamning ismini birma-bir so'rab ro'yxatga yozing. Ro'yxatni konsolga chiqaring.
n_people=int(input("Bugun necha kishi bilan suhbat qildingiz?>>>"))
ismlar=[]
for k in range(n_people):
    ismlar.append(input(f"{k+1}-suhbat qilgan odamingiz kim edi:  "))
print(ismlar)

