# Web sahifangiz uchun foydalanuvchi (user) klassini tuzing. Klassning xususiyatlari sifatida odatda ijtimoiy tarmoqlar talab qiladigan ma'lumotlarni kiriting (ism, foydalanuvchi ismi, email, va hokazo)
class User:
    def __init__(self, ism, familiya, email):
        self.name=ism
        self.surname=familiya
        self.email=email

    def get_name(self):
        return self.name

    def get_surname(self):
        return self.surname

    def get_mail(self):
        return self.email


user1=User('Olim', 'Olimov', 'developer.0829@gmail.com')
print(user1.get_name())
print(user1.get_mail())

        


















