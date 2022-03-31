'''System module'''
from collections import Counter

# input the number of shoes, list of shoes sizes, number of customers
num_of_shoes = int(input())
inventory = list(map(int, input().split()))
customers = int(input())

# input n lists of space seperated shoe size and price
orders = []
occurence_inventory = Counter(inventory)
TOTAL_SALE = 0
for i in range(int(customers)):
    orders.append(list(input().split()))

    # decrease the inventory count
    occurence_inventory.update({int(orders[i][0]) : -1})

    #check if order is in the inventory
    if int(orders[i][0]) in occurence_inventory.keys():
        if occurence_inventory[int(orders[i][0])] >= 0:
            TOTAL_SALE += int(orders[i][1])

print(TOTAL_SALE)
