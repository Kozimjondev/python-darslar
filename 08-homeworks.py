# O'zingizga ma'lum davlatlarning ro'yxatini tuzing va ro'yxatni konsolga chiqaring
countries=['the USA', 'the UK', 'Canada', 'Australia', 'South Korea', 'Japan']
# print(countries)

# Ro'yxatning uzunligini konsolga chiqaring
print(len(countries))

# sorted() funktsiyasi yordamida ro'yxatni tartiblangan holda konsolga chiqaring
print(sorted(countries))

# sorted() yordamida ro'yxatni teskari tartibda konsolga chiqaring
print(sorted(countries, reverse=True))

# Asl ro'yxatni qaytadan konsolga chiqarin
print(countries)

# reverse() metodi yordamida ro'yxatni ortidan boshlab chiqaring
countries.reverse()
print(countries)

# sort() metodi yordamida ro'yxatni avval alifbo bo'yicha, keyin esa alifboga teskari tartibda konsolga chiqaring.
# countries.sort()
countries.sort(reverse=True)
print(countries)

# 120 dan 1200 gacha bo'lgan juft sonlar ro'yxatini tuzing
numbers=list(range(120,1200,2))

# Ro'yxatdagi sonlar yig'indisini hisoblang va konsolga chiqaring
print(sum(numbers))

# Ro'yxatdagi eng katta va eng kichik son o'rtasidagi ayirmani hisoblang va konsolga chiqaring
print(max(numbers)-min(numbers))

# Ro'yxatdagi elementlar sonini hisoblang
print(len(numbers))

# Ro'yxatning boshidan, o'rtasidan va oxiridan 20 ta qiymatni konsolga chiqaring
print(numbers[0:20])
print(numbers[-20:])
print(numbers[260:280])

# taomlar degan ro'yxat yarating va ichiga istalgan 5ta taomni kiriting
taomlar=['mastava', 'osh', 'sho\'rva', 'manti', 'xonim']

# nonushta degan yangi ro'yxatga taomlardan nusxa oling
nonushta=taomlar[:]

# Yangi ro'yxatda faqat nonushtaga yeyiladigan taomlarni qoldiring, va qo'shimcha 2 ta taom qo'shing
nonushta.remove('osh')
nonushta.remove("sho'rva")
nonushta.append('qovurilgan tuxum')
nonushta.append('kolbasa')

# Ikkala ro'yxatni ham (taomlar va nonushta) konsolga chiqaring
print(taomlar)
print(nonushta)

# Yuqoridagi nonushta ro'yxatini o'zgarmas ro'yxatga aylantiring va nonushta[0] = "qaymoq va non" deb qiymat berib ko'ring.
nonushta=tuple(nonushta)
nonushta[0]="qaymoq va non" # Tuple paytida ro'yhatni o'zgartirib bo'lmaydi
print(nonushta)