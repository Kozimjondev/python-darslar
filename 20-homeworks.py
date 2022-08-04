# Foydanaluvchidan ismi, familiyasi, tug'ilgan yili, tug'ilgan joyi, email manzili va telefon raqamini qabul qilib, lug'at ko'rinishida qaytaruvchi funksiya yozing. Lug'atda foydalanuvchu yoshi ham bo'lsin. Ba'zi argumentlarni kiritishni ixtiyoriy qiling (masalan, tel.raqam, el.manzil)

# def foydalanuvchi(ism, familiya, yosh, tjoy, email='', telefon=None):
#     malumot={
#         'name': ism,
#         'last_name': familiya,
#         'age': yosh,
#         'b_date': 2022-yosh,
#         'b_place': tjoy,
#         'mail': email,
#         'phone': telefon
#     }
#     return malumot

# # print(foydalanuvchi('olim', 'olimov', 14, 2005, 'qoqon',))

# # Yuqoridagi funksiyani while yordamida bir necha bor chaqiring, va mijozlar degan ro'yxatni shakllantiring. Ro'yxatdagi mijozlar haqidagi ma'lumotni konsolga chiqaring.
# print("Mijozlar haqida maulumot:")
# while True:
#     mijozlar=[]
#     ism=input("Ismingizni kiriting: ")
#     familiya=input("Familiya: ")
#     yosh=int(input("Yosh: "))
#     tjoy=input("Tugilgan joy: ")
#     email=input("Elektron pochta: ")
#     telefon=input("Telefon raqam: ")
    
#     mijozlar.append(foydalanuvchi(ism, familiya, yosh, tjoy, email, telefon))

#     javob=input("Yana malumot kiritishni hoxlaysizmi?(yes/no): ")
#     if javob=='no':
#         break

# print("Mizojlar ro'yhati:")
# for mijoz in mijozlar:
#     print(f"{mijoz['name'].title()} {mijoz['last_name'].title()}. "
#     f"{mijoz['age']} yoshda, telefoni: {mijoz['phone']}.")



# Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya yozing


# def sonlar(x,y,z):
#     """Uchta son qabul qilib, ulardan eng kattasini qaytaruvchi funksiya"""
#     max=x
#     if y>=max:
#         max=y
#     if z>=max:
#         max=z
#     return max 

# print(sonlar(10,5,9))
# print(sonlar(1000, 2**10, 10**3))


# Foydalanuvchidan aylaning radiusini qabul qilib olib, uning radiusini, diametrini, perimetri va yuzini lug'at ko'rinishida qaytaruvchi funksiya yozing.
# def aylana(radius, pi=3.14):
#     circle={
#         'radius': radius,
#         'diametr': radius*2,
#         'perimetr': 2*pi*radius,
#         'yuza': pi*(radius**2)
#     }
#     return circle

# print(aylana(3))


# Berilgan oraliqdagi tub sonlar ro'yxatini qaytaruvchi funksiya yozing (tub sonlar —faqat birga va o'ziga qoldiqsiz bo'linuvchi, 1 dan katta musbat sonlar)
# def tub_sonlar_top(min, max):
#     tub_sonlar=[]
#     for n in range(min, max+1):
#         tub=True
#         if n==1:
#             tub=False
#         elif n==2:
#             tub=True
#         else:
#             for x  in range(2,n):
#                 if n%x==0:
#                     tub=False
#         if tub:
#             tub_sonlar.append(n)
    
#     return tub_sonlar

# print(tub_sonlar_top(2,109))


# Foydalanuvchidan son qabul qilib, shu son miqdoricha Fibonachchi ketma-ketligidagi sonlar ro'yxatni qaytaruvchi funksiya yozing.  Ta’rif: Har bir hadi o’zidan oldingi ikkita hadning yig’indisiga teng bo’lgan ketma-ketlik Fibonachchi ketma-ketligi deyiladi. Bunda boshlang’ish had ko’pincha 1 deb olinadi.  1, 1, 2, 3, 5, 8, 13, 21, 34, 55,...
def fibonachi(n):
    sonlar=[]
    for x in range(n):
        if x==0 or x==1:
            sonlar.append(1)
        else: 
            sonlar.append(sonlar[x-1]+sonlar[x-2])

    return sonlar

print(fibonachi(10))









