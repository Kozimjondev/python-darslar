# 1-task--------------------
# ismlar=["Diyorbek", "Temur", "Nozimjon"]
# print("Assalomu alaykum "+ismlar[0]+" bugun osh bormi kechga?")
# print("Nima gap "+ismlar[1]+" dota oynayapsanmi charchamay")
# print(ismlar[2]+" yuribsizmi uyda IT o'rganib")
# print(f"{ismlar[0]} va {ismlar[1]} qo'shnilar")

# 2-task--------------------
# sonlar deb nomlangan ro'yxat yarating va ichiga turli sonlarni yuklang (musbat, manfiy, butun, o'nlik)
# sonlar=[10, -20, 7.0, 15.5]
# print(sonlar)
# sonlar[0]=sonlar[0]+15
# sonlar[2]=1_200
# print(sonlar)
# print(sonlar[0]+sonlar[1])
# print(sonlar[2]-sonlar[3])
# print(sonlar[0]*sonlar[3])
# print(sonlar[1]/sonlar[2])

# 3-task----------------
# t_shaxslar va z_shaxslar degan 2 ta ro'yxat yarating va biriga o'zingiz eng ko'p hurmat qilgan tarixiy shaxslarning, ikkinchisiga esa zamonamizdagi tirik bo'lgan shaxslarning ismini kiriting. 
# t_shaxslar=["Amir Temur", "Alisher Navoiy", "Z.M.Bobur", "Mirzo Ulug'bek", "Imom Buxoriy"]
# z_shaxslar=["Alisher Fayz", "Ozodbek", "Yulduz", "Alisher Uzoqov", "Bill Gates"]
# print(t_shaxslar)
# print(z_shaxslar)
# shaxs=t_shaxslar.pop(-1)
# shaxs_z=z_shaxslar.pop(-1)
# print("Men tarixiy shaxslardan "+shaxs+" bilan, zamonaviy shaxslardan esa "+shaxs_z+" bilan suhbat qilishni istar edim")

# 4-task-----------------
# friendsnomli bo'sh ro'yxat tuzing va unga .append() yordamida 5-6 ta mehmonga chaqirmoqchi bo'lgan do'stlaringizni kiriting.
friiends=[]
friiends.append("Diyorbek")
friiends.append("Temur")
friiends.append("Nozimjon")
friiends.append("Shuratjon")
friiends.append("Doniyor")
print("Mehmonga keladigan sinfdoshlar ro'yhati:",friiends)
# Yuqoridagi ro'yxatdan mehmonga kela olmaydigan odamlarni .remove() metodi yordamida o'chrib tashlang. 
friiends.remove("Temur")
print(friiends)
friiends.append("Xurshid")
friiends.insert(0,"Jahongir")
friiends.insert(3,"Zoirjon")
print("\n ",friiends)

# Yangi mehmonlar deb nomlangan bo'sh ro'yxat yarating. .pop() va .append() metodlari yordamida mehmonga kelgan do'stlaringizning ismini friends ro'yxatidan sug'urib olib, mehmonlar ro'yxatiga qo'shing.
mehmonlar=[]
mehmonlar.append(friiends.pop(0))
mehmonlar.append(friiends.pop(3))
mehmonlar.append(friiends.pop(-1))
print("\nKelgan mehmonlar:",mehmonlar)