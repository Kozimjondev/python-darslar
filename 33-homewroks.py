
# faylnomi='data/pi_million_digits.txt'

# with open(faylnomi) as file:
#     pi=file.read()

# pi=pi.rstrip()
# pi=pi.replace("\n", '')
# pi=pi.replace(" ", "")

# bdate='4808838'

# print(bdate in pi)


faylnomi='data/pi_million_digits.txt'

with open(faylnomi) as file:
    pi=file.read()

pi=pi.rstrip()
pi=pi.replace("\n", '')
pi=pi.replace(" ", "")   
pi=float(pi)
pi=str(pi)


import pickle

with open('info_pi', 'wb') as file:
    pickle.dump(pi, file)


with open('info_pi', 'rb') as file:
    pi=pickle.load(file)

print(pi)
