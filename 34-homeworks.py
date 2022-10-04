from fileinput import filename
import json

# Ushbu o'zgaruvchini JSON ko'rinishida saqlang va JSON matnini konsolga chiqaring: 
data = {"Model" : "Malibu", "Rang" : "Qora", "Yil":2020, "Narh":40000}
data_json=json.dumps(data)
# print(data_json)
# print(type(data_json))


# Ushbu JSON matnni ko'chirib oling, va talabaning ismi va familiyasini  konsolga chiqaring: 
talaba_json = """{"ism":"Hasan","familiya":"Husanov","tyil":2000}"""
# print(type(talaba_json))
talaba=json.loads(talaba_json)
# print(f"{talaba['ism']} {talaba['familiya']}")


# Yuqoridagi ikki o'zgaruvchini alohida JSON fayllarga saqlang.

with open('data.json', 'w') as f:
    json.dump(data, f)

with open('talaba.json', 'w') as f:
    json.dump(talaba, f)


# Quyidagi JSON faylni yuklab oling. Faylda 3 ta talabaning ism va familiyasi saqlangan. Ularning har birini alohida qatordan "Ism Familiya, n-kurs, Fakultet talabasi" ko'rinishida konsolga chiqaring.
filename='students.json'
with open(filename) as f:
    students=json.load(f)

# print(students)
# print(students['student'][0]['name'])

# print(f"{students['student'][0]['name']} {students['student'][0]['lastname']}. {students['student'][0]['year']}-kurs, {students['student'][0]['faculty']} fakultet talabasi.")

# print(f"{students['student'][1]['name']} {students['student'][1]['lastname']}. {students['student'][1]['year']}-kurs, {students['student'][1]['faculty']} fakultet talabasi.")

# print(f"{students['student'][2]['name']} {students['student'][2]['lastname']}. {students['student'][2]['year']}-kurs, {students['student'][2]['faculty']} fakultet talabasi.")

filename2='api-result.json'
with open(filename2) as f:
    piton=json.load(f)

print(piton.keys())

print(f"{piton['query']['pages']['13801']['title']}. {piton['query']['pages']['13801']['extract']}")















