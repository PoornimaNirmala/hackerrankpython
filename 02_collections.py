"""System module."""
from collections import OrderedDict

def orders_list(count_orders):
    """input orders"""
    #use the OrderedDict to order the list
    order_list = OrderedDict()
    for _ in range(0,count_orders):
        #input each order
        order = input().split()
        if len(order) > 2:
            item_name = order[0] +""+ order[1]
        else:
            item_name = order[0]
        #update the price for duplicate orders
        if item_name in order_list.keys():
            updated_price = int(order_list[item_name]) + int(order[-1])
            order_list[item_name] = updated_price
        else:
            order_list[item_name] = order[-1]
    #print the updated items
    for key,value in order_list.items():
        print(key,value)
orders_list(int(input()))
