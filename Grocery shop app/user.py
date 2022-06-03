import admin as ad
class user:
    user_id={"shankar":"shankar@1122"}
def __init__(self,full_name,phone_no,email,adress,password):
    self.full_name=full_name
    self.phone_no=phone_no
    self.email=email
    self.adress=email
    self.password=password
    user.user_id[self.full_name]= self.password
    self.profile={"Name":name}
    self.orderhistory={}
def login(cls,username,password):
    if cls.user_id.get(username)==password:
       print("your are log in sucessfully")
       return True
    else:
        print("your userid & password invelid")
        return False
def placed_order():
    print("give your order")
    print(ad.show())
    user_choice=int(input("if you want to order select 1.yes or 2.no"))
    if user_choice == 1:
        n=int(input("how many order do you want"))
        x=0
        for i in range(n):
            itemiD= int(input("enter item id here"))
            quan=int(input("enter quantity here"))
            x += ad.food_items[itemiD]["price"]*quan
            again_ask=(input("again you want to order"))
            if again_ask == "yes":
                print(f'''Your item name is {ad.inven[itemid]["ItemName"]}''')
                print(f'''Price of your Item is {ad.inven[itemid]["Price"]}''')
                print(f"This is your quantity {quan}")
                print(f"It costs you {x}INR in total")
                print("You're all set for this order")
                self.orderhistory[itemiD] = {
                    "Item Name": ad.food_items[itemiD]["ItemName"],
                    "Price": ad.food_items[itemiD]["Price"],
                    "Quantity": quan
                }
                final_stock = ad.food_items[itemiD]["Stock"] - quan
                ad.food_items[itemiD]["Stock"] = final_stock
                print("You're order is successfully placed")

            elif again_ask == "NO":
                print("This Order is cancelled!! You can look once more")
            else:
                print("Invalid choice")
        elif  user_choice == 2:
             print("You select 2 option so we cancelled this")
        else:
             print("Enter the invalid choice")

