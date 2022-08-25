class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.name=ism
        self.familiya=familiya
        self.tyil=tyil
        self.bosqich=1

    def set_bosqich(self, bosqich):
        """Talabaning kursini yangilovchi metod."""
        self.bosqich=bosqich

    def update_bosqich(self):
        """Talabaning bosqichini bittaga ko`pyatirish."""
        self.bosqich+=1

    def get_info(self):
        """Talaba haqida ma'lumot."""
        print(f"{talaba1.name} {talaba1.familiya}. {talaba1.bosqich}-bosqich talabasi.")

# talaba1=Talaba('Alijon', 'Valiyev', 1998)
# talaba2=Talaba("Hasan", "Husanov", 1999)
# # print(talaba1.name)
# # print(talaba1.bosqich)
# # talaba1.bosqich=2
# # print(talaba1.bosqich)
# talaba1.set_bosqich(2)
# print(talaba1.get_info())
# talaba1.update_bosqich()
# print(talaba1.get_info())

class Fan():
    """Fan nomi klass."""
    def __init__(self, nomi):
        self.nomi=nomi
        self.talabalar_soni=0
        self.talabalar=[]

    def add_student(self, talaba):
        """Fanga talabalar qo`shish."""
        self.talabalar.append(talaba)
        self.talabalar_soni+=1

    def get_name(self):
        return self.nomi

    def get_students(self):
        return [talaba.get_info() for talaba in self.talabalar]


matem=Fan('Oliy matematika')

talaba1=Talaba('Alijon', 'Valiyev', 1998)
talaba2=Talaba("Hasan", "Husanov", 1999)
talaba3=Talaba("Akrom", "Boriyev", 2000)
matem.add_student(talaba1)
matem.add_student(talaba2)
matem.add_student(talaba3)
# print(matem.talabalar_soni)
print(matem.talabalar)

# print(matem.talabalar[0].get_info())
# print(matem.get_students())

# print(dir(Talaba))

# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]

# print(see_methods(Talaba))
# print(talaba1.__dict__.values())




















