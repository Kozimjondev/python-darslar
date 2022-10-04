import random

n=100
numbers=list(range(1,n+1))
x=numbers.pop(random.randint(1,n+1))
print(x)

# 1-yechim.
# numbers2=list(range(1,n+1))
# print(sum(numbers2)-sum(numbers))


# 2-yechim
# for i in range(1,n+1):
#     if i not in numbers:
#         print(i)
#         break


# 3-optimal yechim
summa=n*(n+1)/2
print(summa-sum(numbers))









