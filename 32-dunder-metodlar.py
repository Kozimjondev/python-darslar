class Avto:
    __num_avto = 0
    """Avtomobil klassi"""
    def __init__(self,make,model,rang,yil,narh):
        """Avtomobilning xususiyatlari"""
        self.make = make
        self.model = model
        self.rang = rang
        self.yil = yil
        self.narh = narh
        Avto.__num_avto += 1
    
    def __str__(self):
        return f"Avto: {self.make} {self.model}."

    def __repr__(self):
        return f"Avto: {self.make} {self.model}."

    def __eq__(self,y):
        return self.narh==y.narh

    def __le__(self, y):
        return self.narh<=y.narh

    def __lt__(self, y):
        return self.narh<y.narh

class AvtoSalon:
    def __init__(self, name):
        self.name=name
        self.avtolar=[]

    def __repr__(self):
        return f"{salon1.name} avtosaloni"

    def add_avto(self, *qiymat):
        for avto in qiymat:
            if isinstance(avto, Avto):
                self.avtolar.append(avto)
            else:
                print("Avto kiriting.")

    def __getitem__(self, index):
        return self.avtolar[index]

    def __setitem__(self, index, qiymat):
        self.avtolar[index]=qiymat

    def __len__(self):
        return len(self.avtolar)

    def __call__(self, *qiymat):
        if qiymat:
            for avto in qiymat:
                self.add_avto(avto)
        else:
            return [avto for avto in self.avtolar]

    def __add__(self,y):
        if isinstance(y, AvtoSalon):
            yangi_salon=AvtoSalon(f"{self.name} {y.name}.")
            yangi_salon.avtolar=self.avtolar+y.avtolar
            return yangi_salon
        elif isinstance(y, Avto):
            self.add_avto(y)

    




salon1=AvtoSalon('MaxAvto')
salon2=AvtoSalon('Lider')
# salon1.add_avto(avto1, avto2, avto3)
# salon1[0]=Avto("BMW", 'x7', 'qora', 2021, 50000)
                                                    # print(avto1) # obyekt haqida ma'lumot
                                                    # print(avto1!=avto2)
                                                    # print(avto1<avto2)
                                                    # print(salon1)
avto1 = Avto("GM","Malibu","Qora",2020,40000)
avto2 = Avto("GM", 'Lacetti', 'Oq', 2020, 20000)
avto3 = Avto("Toyota",'Carolla',"Silver",2018, 45000)
avto4 = Avto("Mazda", "6", 'Qizil',2015,35000)
avto5 = Avto("Volkswagen","Polo",'Qora',2015,30000)
avto6 = Avto("Honda","Accord","Oq",2017,42000)
# print(salon1.avtolar)
# print(len(salon1))
# salon1(avto4, avto5, avto6)
# print(salon1())
salon1(avto1, avto2, avto3)
salon2(avto4, avto5, avto6)
salon3=salon1+salon2
# print(salon3.avtolar)
avto7 = Avto("Honda","G7","Oq",2017,42000)
salon1+avto4
print(salon1())


















