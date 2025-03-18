#here first we are creating a menu using the dictionay
menu={
    'Pizza':100,
    'Chai':80,
    'Biscuit':20,
    'Coffee':30,
    'Burger':100,
    'Pasta':200
    }
#THIS IS A GREETING LINE
print("Hey welcome to our cafe")

#displaying the menu
print("Pizza:Rs 100\nChai:Rs 80\nBiscuit:Rs 20\nCoffee:Rs 30\nBurger:Rs 100\nPasta:Rs 200")

#after displaying the menu we are giving a variable which consists the total of the order

order_total=0
#taking the item 1
item_1=input("ENTER THE ITEM THAT YOU WANT TO ORDER:")
if item_1 in menu:
    order_total+=menu[item_1]
    print(f"The item {item_1} has been added to your order ")
else:
    print("the item that has been ordered is not in our menu please refer the menu")
#if the customer wants to add another item to the order list
another_item=input("Do you want another item ?(Yes/no)")
if another_item == "Yes":
    item_2=input("ENTER THE ITEM THAT YOU WANT TO ORDER:")
    if item_2 in menu:
        order_total+=menu[item_2]
        print(f"The item {item_2} has been added to your order")
    else:
        print("the item that has been ordered is not in our menu please refer the menu")
print (f"the total of the order is{order_total}") 
        
