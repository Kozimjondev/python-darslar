# from itertools import product
# import math
# uzunlik=lambda pi, r: 2*pi*r
# print(uzunlik(math.pi, 10))

# product=lambda x, y: x**y
# print(product(2,3))



# def daraja(n):
#     return lambda x: x**n

# kvadrat=daraja(2)
# kub=daraja(3)
# daraja4=daraja(4)
# print(f"3 ning kvadrati {kvadrat(3)}, kubi {kub(3)}, 4-darajasi {daraja4(3)}.")

# from math import sqrt
import math

sonlar=list(range(11))
ildizlar=list(map(math.sqrt,sonlar))
# print(ildizlar)

# def daraja2(x):
#     """Berilgan sonning kvadratini qaytaruvchi funksiya"""
#     return x*x

# print(list(map(daraja2, sonlar)))

# kvadratlar=list(map(lambda x: x*x,sonlar))
# print(kvadratlar)

# a=[4, 5, 6, 0]
# b=[7, 8, 9, 0]
# c=[1, 2, 3, 4]
# a_plus_b=list(map(lambda x, y, z: x+y+z, a,b,c))
# print(a_plus_b)

# import random as r
# sonlar=r.sample(range(100),10)

# def juftmi(x):
#     """x juft bo'lsa True, aks holda False qaytaruvchu funksiya"""
#     return x%2==0

# juft_sonlar=list(filter(juftmi,sonlar))
# print(sonlar)
# print(juft_sonlar)



# import random as r
# sonlar=r.sample(range(100), 10)

# juft_sonlar=list(filter(lambda x: x%2==0, sonlar))
# print(sonlar)
# print(juft_sonlar)

mevalar=['olma', 'anor', 'banan', 'uzum', 'anjir', 'shaftoli', 'nok', 'limon']

harf='b'

# mevalar_b=list(filter(lambda meva: meva.startswith(harf), mevalar))
# print(mevalar_b)

mevalar2=list(filter(lambda meva: len(meva)<5, mevalar))
print(mevalar2)


























