# Avto degan yangi klass yarating. Unga avtomobillarga doir bo'lgan bir nechta xususiyatlar (model, rang, korobka, narh va hokazo) qo'shing. Ayrim xususiyatlarga standart qiymat bering (masalan, kilometer=0).

class Avto:
    def __init__(self, model, rang, korobka, narh):
        self.model=model
        self.color=rang
        self.type=korobka
        self.cost=narh
        self.kilometr=0

     # Avto ga oid obyektning xususiyatlarini qaytaradigan metodlar yozing

    def get_car(self):
        """Avtomobilning nomini qaytaruvchi metod"""
        return self.model.capitalize()
    
    def get_colour(self):
        """Avtomobilning rangini qaytaruvchi funksiya."""
        return self.color

    def get_type(self):
        """Avtomobilning qanday turini qaytaruvchi metod"""
        return self.type
    
    def get_cost(self):
        """Avtomobilning narhini qaytaruvchi metod"""
        return self.cost

    def update_km(self, kilometr):
        self.kilometr=kilometr
    
    # get_info() metodi avti haqida to'liq ma'lumotni matn ko'rinishida qaytarsin.
    def get_info(self):
        return f"{avto1.color.capitalize()} {avto1.model}. {avto1.type.capitalize()} korobka, narhi {avto1.cost}$, yurilgan kilometri {avto1.kilometr}."
    


avto1=Avto('lacetti', 'qora', 'avtomat', 30000)
# print(avto1.get_car())
print(avto1.get_info())

# Yangi, Avtosalon degan klass yarating va kerakli xususiyatlar bilan to'ldiring (salon nomi, manzili, sotuvdagi avtomobillar va hokazo)
class Avtosalon:
    def __init__(self, nomi, manzili, avtomobillar):
        self.name=nomi
        self.location=manzili
        self.cars=avtomobillar
        self.cars_numbers=0

    def add_car(self,car):
        self.cars.append(car)
        self.cars_numbers+=1

    def get_cars(self):
        return self.cars

    def get_info(self):
        return f"{avto1.name} avto saloniga qarashli mashinalar, {avto1.location} shahrida joylashgan va bu yerda {avto1.cars[0]}, {avto1.cars[1]}, {avto1.cars[2]} mashinalari sotuvda bor."


avto1=Avtosalon('GM', 'Toshkent',['matiz', 'nexia', 'lacetti'])

# print(avto1.get_cars())
# avto1.add_car('kobalt')
# print(avto1.get_cars())
# print(avto1.get_info())
# print(avto1.cars_numbers)
# print(dir(avto1))
# def see_methods(klass):
#     return [method for method in dir(klass) if method.startswith('__') is False]

# print(see_methods(avto1))
# print(avto1.__dict__)





















