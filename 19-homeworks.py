# Foydalanuvchi ismi va yoshini so'rab, uning tug'ilgan yilini hisoblaydigan funksiya yozing.
# def tugilgan_yil(ism,yosh,j_yil=2022):
#     """Foydalanuvchi tugilgan yilini hisoblaydigan dastur"""
#     print(f"{ism.title()} {j_yil-yosh}-yilda tavallud topgan.")

# tugilgan_yil('olim', 23)


# Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing.
# def son(n):
#     """Foydalanuvchidan son olib, uning kvadrati va kubini konsolga chiqaruvchi funksiya yozing. """
#     print(f"{n} sonning kvadrati {n**2} ga teng.\n"
#     f"{n} sonning kubi {n**3} ga teng")

# son(2)


# Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing.

# def son(n):
#     """Foydalanuvchidan son olib, son juft yoki toqligini konsolga chiqaruvchi funksiya yozing."""
#     if n%2==0:
#         print(f"{n} juft son.")
#     else:
#         print(f"{n} toq son.")

# son(12)


# Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring.
# def sonlar(n, k):
#     """Foydalanuvchidan ikkita son olib, ulardan kattasini konsolga chiqaruvchi funksiya yozing. Agar sonlar teng bo'lsa "Sonlar teng" degan xabarni chiqaring."""
#     if n>k:
#         print(n)
#     elif k>n:
#         print(k)
#     elif k==n:
#         print("Sonlar teng")

# sonlar(4, 11)
# sonlar(12, 7)
# sonlar(5, 5)

# Foydalanuvchidan x va y sonlarini olib, (x**y)ni konsolga chiqaruvchi funksiya yozing.
# def numbers(x, y):
#     """Foydalanuvchidan x va y sonlarini olib, (x**y)ni konsolga chiqaruvchi funksiya yozing."""
#     print(f"{x} ning {y}-darajasi {x**y} ga teng ")

# numbers(3, 5)


# Yuqoridagi funksiyada y uchun 2 standart qiymatini bering.
# def numbers(x, y=2):
#     """Foydalanuvchidan x va y sonlarini olib, (x**y)ni konsolga chiqaruvchi funksiya yozing.
#      Yuqoridagi funksiyada y uchun 2 standart qiymatini bering."""
#     print(f"{x} ning {y}-darajasi {x**y} ga teng")

# numbers(5)


# Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring.
def bolinish_alomatlari(son):
    """Foydalanuvchidan son qabul qilib, sonni 2 dan 10 gacha bo'lgan sonlarga qoldiqsiz bo'linishini tekshiruvchi funksiya yozing. Natijalarni konsolga chiqaring."""
    for n in range(2,11):
        if son%n==0:
            print(f"{son} {n} ga qoldiqsiz bo'linadi")

bolinish_alomatlari(70)

















