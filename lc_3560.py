import random

'''
Min log transport cost:
You have two logs and three trucks. Each truck can hold a log of k length. Cut off the excess for the third truck to hold. The cost is (log - offcut) * (offcut) and, if necessary, (log2 - offcut2) * (offcut2)
'''

k = random.randint(2, 10**5)
x = random.randint(1, k*3)
y = random.randint(1, x)
z = x - y
m = y
n = z
first_truckload = max(m, n)
second_truckload = min(m, n)
if second_truckload > k:
    offcut1 = first_truckload - k
    offcut2 = second_truckload - k
    total_cost = (offcut2 * (second_truckload - offcut2)) + (offcut1 * (first_truckload - offcut1))
elif first_truckload > k:
    offcut1 = first_truckload - k
    total_cost = offcut1 * (first_truckload - offcut1)
else:
    total_cost = 0
print(total_cost)