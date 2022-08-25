# #Talaba klassiga yana bir, fanlar degan xususiyat qo'shing. Bu xususiyat parametr sifatida uzatilmasin va obyekt yaratilganida bo'sh ro'yxatdan iborat bo'lsin (self.fanlar=[])

class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.ism=ism
        self.familiya=familiya
        self.tyil=tyil
        self.fanlar=[]

    def add_fanlar(self,fan):
        return self.fanlar.append(fan)

    def fanga_yozil(self):
        return 


class Fan:
    def __init__(self, math, chemistry, physics, geography):
        self.math=math
        self.chemistry=chemistry
        self.physics=physics
        self.geography=geography

    def get_math(self):
        return self.math

    def get_kimyo(self):
        return self.chemistry

    def get_fizika(self):
        return self.chemistry

    def get_geografiya(self):
        return self.geography


talaba1=Talaba('Olim', 'Olimov', 2000)
print(talaba1.add_fanlar('kimyo'))
fanlar=Fan('matematika', 'kimyo', 'fizika', 'geografiya')

# print(fanlar.get_math())
# print(talaba1.fanlar)















