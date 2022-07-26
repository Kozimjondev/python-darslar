# Foydalanuvchidan juft son kiritishni so'rang. Agar foydalanuvchi juft son kiritsa "Rahmat!", agar toq son kiritsa "Bu son juft emas" degan xabarni chiqaring.
# n=float(input("Juft son kiriting\n>>>>"))
# if n%2:
#     print("Bu juft son emas")
# else:
#     print("Rahmat")

# Foydalanuvchi yoshini so'rang, va muzeyga kirish uchun chipta narhini quyidagicha chiqaring:
# yosh=int(input("Yoshingiz nechida?>>>"))
# if yosh<4 or yosh>60:
#     print(" Chipta narxi bepul")
# elif yosh<18:
#     print("Chipta narxi 10000 so'm")
# else:
#     print("Chipta narxi 20000 so'm")

# 2-usul
# age=int(input("What is your age?>>>"))
# if age<4 or age>60:
#     price=0
# elif age<18:
#     price=10
# else:
#     price=20
# print(f"The price of the ticket is {price}$")

# Foydalanuvchidan ikita son kiritishni so'rang, sonlarni solishtiring va ularning teng yoki katta/kichikligi haqida xabarni chiqaring
# a=float(input("Birinchi sonni kiriting>>>"))
# b=float(input("Ikkinchi sonni kiriting>>>"))
# if a>b:
#     print("a soni b sonidan katta")
# elif a==b:
#     print(f"{a} = {b}")
# elif a<b:
#     print(f"{b} soni {a} sonidan katta")
#     print("b>a")

# mahsulotlar degan ro'yxat yarating va kamida 10 ta turli mahsulotni kiriting. Yangi, savat degan bo'sh ro'yxat yarating va foydalanuvchidan savatga kamida 5 ta mahsulot kiritishni so'rang. Savatdagi elementlarni, mahsulotlar ro'yxati bilan solishtiring va qaysi biri ro'yxatda bo'lsa "Mahsulot do'konimizda bor" aks holda, "Mahsulot do'konimizda yo'q" degan xabarlarni chiqaring.
# mahsulotlar=["non", 'guruch', 'olma', 'banan', 'anor', 'cola', 'sabzi', 'kartoshka', 'go\'sht', 'nok']
# savat=[]
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni qo'shing>>>"))

# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         print(f"Do'konimizda {mahsulot} bor")
#     else:
#         print(f"Do'konimizda {mahsulot} yo'q")

# Yuqoridagi dasturni quyidagicha o'zgartiring: foydalanuvchidan 5 ta mahsulot kiritishni so'rang. Foydalanuvchi so'ragan va do'konda bor mahsulotlarni yang, bor_mahsulotlar degan ro'yxatga, do'konda yo'q mahsulotlarni esa mavjud_emas degan ro'yxatga qo'shing.  Agar mavjud_emas ro'yxati bo'sh bo'lsa, "Siz so'ragan barcha mahsulotlar do'konimizda bor" degan xabarni, aks holda esa "Quyidagi mahsulotlar do'konimizda yo'q: ....." degan xabarni chiqaring.
# mahsulotlar=["non", 'guruch', 'olma', 'banan', 'anor', 'cola', 'sabzi', 'kartoshka', 'go\'sht', 'nok']
# savat=[]
# for n in range(5):
#     savat.append(input(f"Savatga {n+1}-mahsulotni kiriting:  "))

# bor_mahsulotlar=[]
# mavjud_emas=[]
# for mahsulot in savat:
#     if mahsulot in mahsulotlar:
#         bor_mahsulotlar.append(mahsulot)
#     else:
#         mavjud_emas.append(mahsulot)

# if mavjud_emas:
#     print("Do'konimizda quyidagi mahsulotlar yo'q:")
#     for mahsulot in mavjud_emas:
#         print(mahsulot)
# else:
#     print("Do'konimizda hamma mahsulotlar bor")

# foydalanuvchilar degan ro'yxat tuzing, va kamida 5 ta login qo'shing. Foydalanuvchidan yangi login tanlashni so'rang va foydalanuvchi kiritgan loginni foydalanuvchilar degan ro'yxatning tarkibi bilan solishtiring. Agar ro'yxatda bunday login mavjud bo'lsa, "Login band, yangi login tanlang!" aks holda "Xush kelibsiz, foydalanuvchi!" xabarini chiqaring.
# foydalanuvchilar=['Anvar', 'Hasan', "Husan", "Kozimjon", "Diyorbek"]
# login=input("Yangi login tanlang:  ")
# if login.capitalize() in foydalanuvchilar:
#     print("Login band, boshqa login tanlang!")
# else:
#     print(f"Xush kelibsiz! {login.title()}")

# Foydalanuvchidan biror butun son kiritishni so'rang. Foydalanuvchi kiritgan sonni 2 da 10 gacha bo'lgan sonlardan qay biriga qoldiqsiz bo'linishini konsolga chiqaring. 
a=int(input("Butun son kiriting:  "))
for n in range(2,11):
    if  not (a%n):
        print(f"{a} soni {n} soniga qoldiqsiz bo'linadi")























