# yosh=int(input("Yoshingiz nechida?>>>"))
# if yosh<=4:
#     print("Sizga kirish bepul")
# elif yosh<=12:
#     print("sizga kirish 5000 so'm")
# elif yosh<=18:
#     print("sizga kirish 8000 so'm")
# else:
#     print("sizga kirish 10000 so'm")

# 2-usul
# yosh=int(input("Yoshingiz nechida?>>>"))
# if yosh<=4:
#     price="bepul"
# elif yosh<=12:
#     price=5000
# elif yosh<=18:
#     price=8000
# else:
#     price=10000
# print(f"Sizga kirish {price} so'm")

# OR operatori
# kun=input("Bugun qanday kun?>>>")
# if kun.lower()=='shanba' or kun.lower()=='yakshanba':
#     print("Bugun dam olish kuni")
# else:
#     print("Bugun ish kuni")

# AND operatori
# kun=input("Bugun nima kun?>>>")
# temperature=float(input("Harorat necha daraja?>>>"))
# if kun.lower()=='yakshanba' and temperature>=30:
#     print("Bugun kanalga boramiz cho'milgani")
# else:
#     print("Bugun uyda qolamiz")

# AND va OR operatori qatnashgan masala
# kun=input("Bugun qaysi kun?>>>")
# temperature=float(input("Bugun harorat qanday?>>>"))
# if (kun.lower()=='shanba' or kun.lower()=='yakshanba') and temperature>=30:
#     print("Bugun cho'milgani boramiz")
# else:
#     print("Bugun uyda \t qolamiz")

# BOOLEAN ma'mumotlar turi
# narh=15000 # mijoz 15000 so'mga taom sotib oldi
# choy=True # mijoz choy sotib oldi.
# salad=False # mijoz salad sotib olmadi.
# if choy and salad: # agar mijoz choy ham salad ham olgan bo'lsa
#     narh=narh+10000 # taom narhiga 10000 so'm qo'shadi
# elif choy or salad: # agar mijoz choy yoki salad olgan bo'lsa
#     narh=narh+5000 # taom narhiga 5000 so'm qo'shadi
# print(f"Jami {narh} so'm")

# SHARTLARNI KETMA-KET TEKSHIRISH
# narh=15000 # mijoz 15000 so'mga taom sotib oldi
# choy=1
# salad=0
# non=1
# kompot=1
# shirinlik=0
# if choy:
#     print("Mijoz choy sotib oldi")
#     narh=narh+2000

# if salad:
#     print("Mijoz salad sotib oldi")
#     narh=narh+3000

# if non:
#     print("Mijoz non sotib oldi")
#     narh=narh+2000

# if kompot:
#     print("Mijoz kompot sotib oldi")
#     narh=narh+2000

# if shirinlik:
#     print("Mijoz shirinlik sorib oldi")
#     narh=narh+5000
# print(f"Jami {narh} so'm")


# in operatori
# menu=["osh", "kabob", "sho'rva", "mastava", "lag'mon"]
# print("manti" in menu)
# print("osh" in menu)

# menu=["osh", "qazonkabob", "shashlik", "norin", "somsa"]
# ovqat=input("Nima ovqat yeysiz?>>>")
# if ovqat.lower() in menu:
#     print("Buyurtma qabul qilindi")
# else:
#     print("Uzur bizda bunday ovqat yo'q")

# not in operatori
# menu=["osh", 'somsa', 'mastava', 'kabob']
# print('manti' not in menu)
# print('osh' not in menu)

# menu=["osh", "qazonkabob", "shashlik", "norin", "somsa"]
# ovqat=input("Nima ovqat yeysiz?>>>")
# if ovqat.lower() not in menu:
#       print("Uzur bizda bunday ovqat yo'q")
# else:
#       print("Buyurtma qabul qilindi")

# Ikki ro'yxatni solishtirish
menu=["osh", 'somsa', 'mastava', 'kabob', 'norin', 'manti']
buyurtmalar=['osh', 'shashlik', 'somsa', 'lag\'mon']
if buyurtmalar:
    for taom in buyurtmalar:
        if taom in menu:
            print(f"Menuda {taom} bor")
        else:
            print(f"Kechirasiz, menuda {taom} yo'q")
else:
    print("Savatchangiz bo'sh")


# buyurtmala=[]
# if buyurtmala:
#     print(f"Ro'yhatda {len(buyurtmala)} ta taom bor")
# else:
#     print("Ro'yhat bo'sh")

