# yosh=input("Yoshingizni kiriting:")
# try:
#     yosh=int(yosh)
# except:
#     print("Butun son kiriting.")
# else:
#     print(f"Siz {2022-yosh}-yilda tug`ilgansiz.")

# x, y=5, 10
# try:
#     y/(x-5)
# except ZeroDivisionError:
#     print("0 ga bolish mumkin emas.")

# IndexError
# mevalar=['olma', 'nok', 'anor', 'anjir']
# try:
#     print(mevalar[1])
# except IndexError:
#     print(f"Ro`yhatda {len(mevalar)} ta mevalar bor xolos.")

# FileNotFoundError
# filename='data.txt' # bunday fayl mavjud emas.
# try:
#     with open(filename) as f:
#         text=f.read()
# except FileNotFoundError:
#     print(f'{filename} mavjud emas.')

# n=input("Butun son kiriting: ")
# try:
#     n=int(n)
#     x=20/n
# except ValueError:
#     print("Butun son kiritmadingiz.")
# except ZeroDivisionError:
#     print("0 ga bo`lib bolmaydi.")
# else:
#     print(f"x={x}")

while True:
    n=input("Yoshingizni kiriting: ")
    if n.isdigit():
        n=int(n)
        break

print(f"Siz {2022-n} yilda tugilgansiz.")





























