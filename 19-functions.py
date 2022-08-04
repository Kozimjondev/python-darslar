
# def salom_ber():
#     """Salom beruvchi funksiya"""
#     print("Assalomu alaykum.")

# salom_ber()

# def salom_ber(ism):
#     """ Foydalanuvchi ismini qabul qilib, unga salom beruvchi funksiya."""
#     print(f"Assalomu alaykum, hurmatli {ism.title()}")

# salom_ber(ism='ali')
# print(salom_ber.__doc__)

# def toliq_ism(ism, familiya):
#     """Foydalanuvchi ism va familiyasini chiqaruvchi dastur"""
#     print(f"Foydalanuvchi ismi: {ism.title()}\n"
#     f"Foydalanuvchi familiyasi: {familiya.title()}")

# toliq_ism(ism='olim', familiya='alijonov')
# toliq_ism(familiya='karimov', ism='ali')


# def yosh_hisobla(ism, tugilgan_yil):
#     """Foydalanuvchi yoshini hisoblaydigan dastur."""
#     print(f"{ism.title()} {2022-tugilgan_yil} yoshda.")

# yosh_hisobla(tugilgan_yil=1991, ism='jasur')
# yosh_hisobla('javlon', 1985)

def yosh_hisobla(tugilgan_yil, joriy_yil=2022):
    """Foydalanuvchi yoshini hisoblaydigan dastur."""
    print(f"Siz {joriy_yil-tugilgan_yil} yoshdasiz.")

yosh_hisobla(1965, 2022)



















