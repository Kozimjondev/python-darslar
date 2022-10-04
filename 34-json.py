# import json

# x=10
# x_json=json.dumps(x)
# # print(x_json)
# # print(type(x_json))


# m= True
# m_json=json.dumps(m)

# # print(m)
# # print(m_json)


# sonlar=(12, 9, 10, 5)
# sonlar_json=json.dumps(sonlar)

# # print(sonlar_json)


# bemor={
#     'ism': "Alijon Valiyev",
#     "yosh": 30,
#     "oila": True,
#     "farzandlar": ("Ahmad", "Ahad"),
#     "allergiya": None,
#     "dorilar": [
#         {'nomi': "Anolgin", 'miqdori': 0.5},
#         {'nomi': "Panadol", 'miqdori': 1.2}
#     ]
# }

# # bemor_json=json.dumps(bemor)
# # print(bemor_json)
# # print(type(bemor_json))


# bemor_json=json.dumps(bemor, indent=4)
# # print(bemor_json)
# print(bemor.keys())
# print(bemor['dorilar'])


# with open('bemor.json', 'w') as f:
#     json.dump(bemor, f)

# with open('sonlar.json', 'w') as f:
#     json.dump(sonlar, f)

# bemor2=json.loads(bemor_json)
# print(type(bemor2))

# sonlar2=json.loads(sonlar_json)
# print(type(sonlar2))

# filename='bemor.json'
# with open(filename) as f:
#     bemor=json.load(f)

# print(type(bemor))

















