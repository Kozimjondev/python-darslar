class Talaba:
    def __init__(self, ism, familiya, id_raqam):
        self.ism=ism
        self.familiya=familiya
        self.id=id_raqam

    def __repr__(self):
        return f"{self.ism} {self.familiya}"

    def __lt__(self,y):
        return self.id<y.id

    def __eq__(self, y):
        return self.id==y.id



class Fan:
    def __init__(self, fan_nomi):
        self.nomi=fan_nomi
        self.talabalar=[]

    def __repr__(self):
        return f"{self.nomi.capitalize()} fani"

    def add_students(self, *talabalar):
        for talaba in talabalar:
            if isinstance(talaba, Talaba):
                self.talabalar.append(talaba)

    def __getitem__(self, index):
        return self.talabalar[index]

    def __setitem__(self, index, value):
        if isinstance(value, Talaba):
            self.talabalar[index]=value

    def __len__(self):
        return len(self.talabalar)

    def __add__(self,talaba):
        if isinstance(talaba, Talaba):
            self.add_students(talaba)

    def __call__(self,*value):
        if value:
            for talaba in value:
                self.add_students(talaba)
        else:
            return [talaba for talaba in self.talabalar]

    def __sub__(self, qiymat):
        pass


      


        
    

talaba1=Talaba('Olim', "Olimov", 6621401)
talaba2=Talaba("Ali", 'Valiyev', 9851580)
talaba3=Talaba("Ikrom", 'Tojiyev', 7643680)
fan1=Fan('matematika')

# print(talaba1<talaba2)
# print(talaba1==talaba2)
# print(talaba2)

# print(fan1)

fan1.add_students(talaba1, talaba2, talaba3)
# print(fan1.talabalar)

# print(fan1[0])
fan1[0]=Talaba("Diyorbek", 'Xalimov', 5566111)
# print(fan1[0])

# print(len(fan1))

talaba4=Talaba('Islom', 'Ibrohim', 4232111)

print(fan1())

fan1+talaba4

print(fan1())




















