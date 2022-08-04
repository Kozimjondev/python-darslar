# Foydalanuvchidan buyurtma qabul qiluvchi dastur yozing. Mahsulotlar nomini birma-bir qabul qilib, yangi ro'yxatga joylang.
# savat=[]
# while True:
#     savol=input("Buyurtmani kiriting: ")
#     savat.append(savol)
#     javob=input("Yana mahsulot qo'shasizmi? (ha/yoq)")
#     if javob=='yoq':
#         break

# print(savat)

# e-bozor uchun mahsulotlar va ularning narhlari lug'atini shakllantiruvchi dastur yozing. Foydalanuvchidan lug'atga bir nechta elementlar (mahsulot va uning narhi) kiritishni so'rang.
# print("Mahsulot va ularning narhlarini chiqaruvchi dastur.")
# e_bozor={}
# while True:
#     mahsulot=input("Mahsulot nomini kiriting: ")
#     narh=input(f"{mahsulot.title()}ning narhini kiriting: ")
#     e_bozor[mahsulot]=int(narh)

#     javob=input("Yana malumot qoshasizmi?(ha/yoq): ")
#     if javob=='yoq':
#         break

# print(e_bozor)

# Yuqoridagi ikki dasturni jamlaymiz. Foydalanuvchi buyurtmasi ro'yxatidagi har bir mahsulotni e-bozordagi mahsulotlar bilan solishitiring (tayyor ro'yxat ishlatishingiz mumkin). Agar mahsuot e-bozorda mavjud bo'lsa mahuslot narhini chiqaring, aks holda "Bizda bu mahsulot yo'q" degan xabarni kor'sating.
# e_bozor={'non':3000 , 'cola': 5000, 'pishiriqlar': 10000, 'fanta': 5000, 'sut': 6000, 'qatiq': 8000, 'tuxum': 2000}
# buyurtma=[]
# while True:
#     savol=input("Buyurtma kiriting: ")
#     buyurtma.append(savol)
#     if savol in e_bozor:
#         print(f"{savol.title()}ning narhi {e_bozor[savol]} so'm")
#     else:
#         print("Bizda bunday mahsulot yoq")

buyurtmalar = ['olma','anjir','uzum','qovun']
mahsulotlar = {'olma':20000,
               'shaftoli':25000,
               'tarvuz':18000,
               'uzum':22000}

while buyurtmalar:
    buyurtma = buyurtmalar.pop()
    if buyurtma in mahsulotlar:
        narh = mahsulotlar[buyurtma]
        print(f"{buyurtma.title()} - {narh} so'm")
    else:
        print(f"Bizda {buyurtma} yo'q")
















