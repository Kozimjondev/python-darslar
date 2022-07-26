# mehmonlar=['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# print("Salom", mehmonlar[0])
# print("Salom", mehmonlar[1])

# FOR tsikli
# mehmonlar=['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:
#     print("Salom", mehmon)
#     print("Hayr", mehmon )
    
# mehmonlar=['Ali', 'Vali', 'Hasan', 'Husan', 'Olim']
# for mehmon in mehmonlar:    
#     print(f"Hurmatli {mehmon}, sizni 1-avgust kuni tug'ilgan kunimga taklif qilaman.")
#     print("Hurmat bilan, Palonchiyevlar oilasi")

# for YORDAMIDA SONLI RO'YXATLAR BILAN ISHLASH
# sonlar=list(range(1,11))
# for son in sonlar:
#     print(f"{son} ning kvadrati {son**2} ga teng")

# sonlar=list(range(11))
# sonlar_kvadrati=[]
# for son in sonlar:
#     sonlar_kvadrati.append(son**2)
# print(sonlar)
# print(sonlar_kvadrati)

# for operatori va input() funktsiyasini jamlab, ro'yxatni foydalanuvchidan olingan qiymatlar bilan to'ldirish mumkin:
dostlar=[]
print("5ta eng yaqin do'stingiz kim?")
for n in range(5):
    dostlar.append(input(f"{n+1}-do'stingizni ismini kiriting:"))
print(dostlar)

