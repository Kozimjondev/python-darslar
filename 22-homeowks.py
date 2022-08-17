# Istalgancha sonlarni qabul qilib, ularning ko'paytmasini qaytaruvchi funksiya yozing
def kopaytir(*sonlar):
    kopaytma=1
    for son in sonlar:
        kopaytma*=son
    return kopaytma

print(kopaytir(1,2,3,4))
print(kopaytir(10,2,10,3))

# Talabalar haqidagi ma'lumotlarini lug'at ko'rinishida qaytaruvchi funksiya yozing. Talabaning ismi va familiyasi majburiy argument, qolgan ma'lumotlar esa ixtiyoriy ko'rinishda istalgancha berilishi mumkin bo'lsin.
def talaba_info(ism, familiya, **malumotlar):
    malumotlar['ism']=ism
    malumotlar['familiya']=familiya
    return malumotlar

talaba1=talaba_info('olim', 'olimov', tyil=1999, tjoy='qoqon shahri', hobby='futbol oynash')
print(talaba1)








