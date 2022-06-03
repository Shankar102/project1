admin_key={"shankar":"shankar@1234"}
food_items={1:{'itemName' : 'glucos', 'itemiD': 1, 'Quanity': '200ml', 'Price': '45', 'Stock': 25},
            2:{'itemName' : 'meggie', 'itemiD': 2, 'Quanity': '4pices', 'Price': '67', 'Stock': 65},
            3:{'itemName' : 'coffee', 'itemiD': 3, 'Quanity': '250gm', 'Price': '320', 'Stock': 80}}
def  add_items():
    itemname=int(input("enter the food itemname"))
    iD =int(input("enter the food iD"))
    quanity=int(input("enter the food quanity"))
    price=int(input("enter the food price"))
    stock=int(input("enter the food stock"))
    add_items[itemiD] ={
    "itemName" :itemname,
    "itemiD": itemid,
    "Quanity": quanity,
    "Price": price,
    "Stock": stock
    }
    print("this is"+itemname+"order successfully")
    return food_items
def edit_food_items():
    edit=int(input("which item you want to edit"))
    a=int(input("enter the food itemname"))
    c=int(input("enter the food quanity"))
    d=int(input("enter the food price"))
    e=int(input("enter the food stock"))
    food_item[edit][itemName]=a
    food_item[edit][Quanity]=c
    food_item[edit][Price]=d
    food_item[edit][stock]=e
    print("edit done")
    return food_items
def show():
    print("show the inventory")
    for i in food_items:
         print("total item",food_items[i],["itemName"])
         print("total item",food_items[i],["Quanity"])
         print("total item",food_items[i],["Price"])
         print("total item",food_items[i],["Stock"])
         print("********your fooditem edit successful**************")
     
def remove():
    d=int(input("remove item"))
    food_items.pop(d)
    print=("Remove all food items")
    return food_items
