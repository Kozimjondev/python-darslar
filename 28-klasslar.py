class Talaba:
    def __init__(self, ism, familiya, tyil):
        self.name=ism
        self.familiya=familiya
        self.tyil=tyil

    def get_name(self):
        return self.name.capitalize()

    def describe(self):
        pass

    def get_age(self, yil):
        return yil-self.tyil

    def tanishtir(self):
        return f"Ismim {self.name.capitalize()} {self.familiya.capitalize()}. Tug`ilgan yilim {self.tyil}."

talaba1=Talaba('olim', 'olimov', 2000)
talaba2=Talaba('hasan', 'husanov', 1995)
talaba3=Talaba('ali', 'valiyev', 2004)
# print(talaba1.name.title())
# print(talaba3.familiya.capitalize())
# print(talaba1.tanishtir())
# print(talaba1.get_name())
print(talaba1.get_age(2022))


















