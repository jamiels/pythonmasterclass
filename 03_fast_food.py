def display_menu(menu):
    print("Food Menu")
    for n in range(0,len(menu)):
        print(n+1,':',menu[n])
    itemNo = int(input("Enter item number: "))
    if itemNo = len(menu) + 1:
        return -1
    return itemNo


shopping_cart = []
is_still_shopping = True
menu = ('Burgers','Pizza','Fried Chicken','Wings')

while is_still_shopping:
    if display_menu(menu) == -1:
        is_still_shopping = False
    else:
        shopping_cart.append(menu[itemNo-1])

    
print("you ordered:", shopping_cart)

