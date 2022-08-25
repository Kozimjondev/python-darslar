# file=open('data/pi.txt')
# PI=file.read()



# # print(type(file))
# print(PI)
# file.close()


# with open('data/pi.txt') as file:
#     pi=file.read()
    # print(pi)

# print(pi)

# filename='data/talabalar.txt'
# with open(filename) as file:
#     for line in file:
#         print(line)

# with open(filename) as file:
#     talabalar=file.readlines()

# print(talabalar)

# talabalar=[talaba.rstrip() for talaba in talabalar]
# print(talabalar)

# faylnomi='data/yangi_fayl.txt'
# ism='Olim Olimov'
# tyil=2004
# with open(faylnomi, 'w') as file:
#     file.write(ism+'\n')
#     file.write(str(tyil)+'\n')
#     print(faylnomi)


# faylnomi='data/yangi_fayl.txt'

# with open(faylnomi, 'a') as file:
#     file.write("Alijon ALiyev"+'\n')
#     file.write(str(2000))


import pickle

talaba1 = {'ism':'hasan', 'familiya':'husanov', 'tyil':2003, 'kurs': 2}
talaba2 = {'ism':'alijon', 'familiya':'valiyev', 'tyil':2004, 'kurs': 1}

with open('data/info_pickle', 'wb') as file:
    pickle.dump(talaba1, file)
    pickle.dump(talaba2, file)


with open('data/info_pickle', 'rb') as file:
    talaba1=pickle.load(file)
    talaba2=pickle.load(file)

print(talaba2)











