
# print("Yaqin do'stlaringiz ro'yhatini tuzamiz.")
# ismlar=[]
# n=1
# while True:
#     savol=f"{n}-do'stingiz ismini kiriting: "
#     ism=input(savol)
#     ismlar.append(ism)
#     takrorlash=input("Yana ism qo'shasizmi?(ha/yoq) ")
#     n+=1
#     if takrorlash=='yoq':
#         break

# print("Do'stlaringiz ro'yhati:")
# for ism in ismlar:
#     print(ism.title())

# print("Do'stlaringiz yoshini saqlaymiz.")
# dostlar={}
# while True:
#     ism=input("Do'stingiz ismini kiriting: ")
#     yosh=input(f"{ism.title()}ning yoshini kiriting: ")
#     dostlar[ism]=int(yosh)

#     javob=input("Yana ma'lumot qo'shasizmi?(ha/yoq) ")
#     if javob=='yoq':
#         break

# for ism, yosh in dostlar.items():
#     print(f"{ism.title()}ning yoshi {yosh}")

# cars=['lacetti', 'nexia', 'kobalt', 'matiz', 'nexia', 'malibu', 'nexia']
# # cars.remove('nexia')
# # print(cars)
# while 'nexia' in cars:
#     cars.remove('nexia')
# print(cars)



students=['hasan', 'husan', 'olim', 'botir']
baholangan_talabalar={}
while students:
    student=students.pop()
    mark=input(f"{student.title()}ning bahosini kiriting: ")
    print(f"{student.title()} baholandi.")
    baholangan_talabalar[student]=int(mark)

print(students)
print(baholangan_talabalar)



























