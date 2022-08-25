
class Shaxs:
    def __init__(self, ism, familiya, passport, tyil):
        """Shaxsning xususiyatlari"""
        self.ism = ism
        self.familiya = familiya
        self.passport = passport
        self.tyil = tyil

    def get_info(self):
        """Shaxs haqida ma'lumot"""
        info=f"{self.ism} {self.familiya}. "
        info+=f"Passport: {self.passport}, {self.tyil}-yilda tug'ilgan."
        return info

    def get_age(self, yil):
        """Shaxsning yoshini qaytaruvchi metod"""
        return yil-self.tyil

class Talaba(Shaxs):
    """Talaba klassi"""
    def __init__(self, ism, familiya, passport, tyil, idraqam, manzil):
        """Talabaning xusuiyatlari"""
        super().__init__(ism, familiya, passport, tyil)
        self.idraqam=idraqam
        self.bosqich=1
        self.manzil=manzil

    def get_id(self):
        """Talabaning id raqami"""
        return self.idraqam

    def get_bosqich(self):
        """Talabaning o'qish bosqichi"""
        return self.bosqich

    def get_info(self):
        """Talaba haqida ma'lumot"""
        info=f"{self.ism} {self.familiya}. "
        info+=f"{self.bosqich}-bosqich talabasi. ID raqami {self.idraqam}."
        return info

class Manzil:
    """Manzilni saqlash uchun klass"""
    def __init__(self, uy, kocha, tuman, viloyat):
        self.uy=uy
        self.kocha=kocha
        self.tuman=tuman
        self.viloyat=viloyat

    def get_manzil(self):
        """Manzilni ko'rish"""
        info=f"{self.uy}-uy, {self.kocha} ko'chasi, {self.tuman} tumani, {self.viloyat} viloyati."
        return info



inson=Shaxs("Olim", "olimov", 'AB1234242', 1999)
# print(inson.get_info())
# print(inson.get_age(2022))

# print(talaba1.get_bosqich())
# print(talaba1.get_age(2022))
# print(talaba1.get_info())

talaba1_manzil=Manzil(65, 'Mustaqillik', 'Bog`dod', 'Farg`ona')
talaba1=Talaba('Ali', 'Valiyev', 'AA1234567', 1997, 6617274, talaba1_manzil)
print(talaba1.manzil.get_manzil())




































