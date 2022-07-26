# cars=['bmw', 'audio', 'volvo', 'mercedez benz', 'tesla', 'general motors']
# cars.sort()
# print(cars)

# agar ro'yhatda katta harf bilan boshlangan qiymat bo'lsa, katta harf kichik harfdan 1-keladi
# cars=['bmw', 'audio', 'volvo', 'Nexia', 'mercedez benz', 'tesla', 'general motors']
# cars.sort()
# print(cars)

# cars=['bmw', 'audio', 'volvo', 'Nexia', 'mercedez benz', 'tesla', 'general motors']
# cars.sort(reverse=True)
# print(cars)

# mehmonlar=['Odil', 'Avaz', 'Hamid', 'Temur', 'Mamur']
# print(sorted(mehmonlar))
# print(mehmonlar)
# print(sorted(mehmonlar, reverse=True))

# sonlar=[12, 100, 55, 7.7, -16, 146, -5]
# sonlar.sort(reverse=True)
# print(sonlar)
# print(sorted(sonlar, reverse=True))

# fruits=['banana', 'pear', 'apple', 'lemon', 'peach']
# fruits.reverse()
# print(fruits)

# fruits=['banana', 'peach', 'apple', 'pear', 'lemon', 'grapes']
# uzunlik=len(fruits)
# print(uzunlik)
# print("Elementlar soni:", len(fruits))

# sonlar=list(range(10))
# print(sonlar)
# juft_sonlar=list(range(0,20,2))
# toq_sonlar=list(range(1,20,2))
# print(juft_sonlar)
# print(toq_sonlar)
# print(max(juft_sonlar))
# print(min(juft_sonlar))

# SONLI RO'YHATLAR USTIDA SODDA AMALLAR!
# narhlar = [12000, 22500, 23456, 9800, 5600, 9934, 32874]
# arzon=min(narhlar)
# qimmat=max(narhlar)
# jami=sum(narhlar)
# print("Eng arzon narx:",arzon,". Eng qimmat narx:",qimmat,". Umumiy summa:",jami,".")

# RO'YHATNI KESISH
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars=cars[0:4]
# print(my_cars)
# his_cars=cars[3:6]
# print(his_cars)

# RO'YHATDAN NUSXA OLISH
# cars = ['bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi']
# my_cars=cars[:]
# my_cars[0]='lacetti'
# print(cars)
# print(my_cars)

# TUPLES
cars = ('bmw','mercedes benz', 'volvo', 'general motors', 'tesla', 'audi')
cars=list(cars)
cars.append('tico')
cars.remove('bmw')
cars[1]='tracker'
cars=tuple(cars)
print(cars)