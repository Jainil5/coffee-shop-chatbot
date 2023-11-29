from items_list import items
import re

def order(text):
    order = []
    prices = []
    total = 0
    for item in items:
        search = re.findall(item, text)
        for value in search:
            if value not in order:
                order.append(value)
    order_items = " , ".join(order).upper()
    for i in order:
        prices.append(int(items.get(i)))
    for i in prices:
        total += int(i)
    output = f"""
    ORDER PLACED .\n
    ITEMS  :  {order_items} .\n
    BILL :  {total} $ .\n  
    Type  'Cancel order'  to  cancel  the  order .
    """    
    return output


# text = " I want a black coffee and americano"

# print(order(text))            