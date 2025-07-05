print( 'welcome to Shreyas AI restaurant')
chosen_items = []
option = input("do you want to 'eat' or 'takeaway'? ").lower()
if option == 'takeaway':
    while True:
        print("sorry but we dont do takeaways , its a fine dine gourmet AI restaurant")
        exit_q = input("pls click 'enter' to exit ").lower
        exit()
    

elif option == 'eat':
    print  ("pls have a seat" )
    print("these are the items available ")
    items={
         1:"pizza",
         2:"breadsticks",
         3:"pasta",
         4:"burger",
         5:"cake",
         6:"chips"}
    for item in items.items():
        print(item)



    while True:
        menu=input("which item do you want? ")
        if menu == "1" :
            print("pizza")
            chosen_items.append("pizza")

        elif menu == "2":
            print("breadsticks")
            chosen_items.append("breadsticks")
        elif menu=="3":
            print("pasta")
            chosen_items.append("pasta")

        elif menu=="4":
            print("oh! i am very sorry but we dont have burger right now  ")

        elif menu=="5":
            print("cake")
            chosen_items.append("cake")

        elif menu=="6":
            print("chips")
            chosen_items.append("chips")
        if menu == "no":
            print("thanks for ordering")
            break
        else:
             print("choose again")

        option_2=input("do you want to order more , 'yes'/'no' ").lower()

        if option_2 != "yes":
            print("thanks for ordering  , you will surely like it" )
            break

if chosen_items:
            print("\nYou selected:")
            for item in chosen_items:
                print( "-",item)
else:
    print("\nYou didn’t pick any items.")

from collections import Counter


if chosen_items:
    counts = Counter(chosen_items)
    item_units = {}

    print("\nHow many pieces of each item do you want sir/mam? ")
    for item in counts:
        while True:
            qty = input(f"{item.capitalize()}: ")
            if qty.isdigit() and int(qty) > 0:
                item_units[item] = int(qty)
                break
            print("Please enter a positive whole number.")

    print("\nYour final order:")
    for item, qty in item_units.items():
        print(f"{qty} × {item}")
else:
    print("\nYou didn’t pick any items.")
ask=input("thankyou for ordering before proceeding do you want to 'delete' , 'modify' or 'add' item? ").lower()
if ask== 'delete':
    ask_2=input("which item do you want to delete? ").lower()
    if ask_2 in item_units:
        while True:
            ask_3 = input(f"How many units of {ask_2} to delete? ")
            if ask_3.isdigit() and int(ask_3) > 0:
                units_to_remove = int(ask_3)
                break
            print("Please enter a positive whole number.")

        current_qty = item_units[ask_2]

        if units_to_remove >= current_qty:
            del item_units[ask_2]
            print(f"{ask_2} deleted.")
        else:
            item_units[ask_2] = current_qty - units_to_remove
            print(f"Removed {units_to_remove} × {ask_2}.  "
                  f"Remaining: {item_units[ask_2]}")
            print(item_units,'')

    else:
        print("Item not found.")

if ask =='add':
    ask_4=input("which item do you want to add? ").strip().lower()

    if ask_4 in item_units:
        while True:
            ask_5 = input(f"How many units of {ask_4} to add? ")
            if ask_5.isdigit() and int(ask_5) > 0:
                item_units[ask_4] += int(ask_5)
                break
            print("please enter a positive whole number ")
        print(f"{ask_5}*{ask_4} added ",
              f"new total: {item_units[ask_4]} {chosen_items}")
    else:
        while True:
            ask_6=input(f"{ask_4} was not in your order "
                    f"how many units to add? ")
            if ask_6.isdigit()and int(ask_6) > 0:
                item_units[ask_4] = int(ask_6)
                break
            print("Please enter a positive whole number.")

        print(f"{item_units[ask_4]} × {ask_4} added to your order.")
        print(f"new total:{item_units[ask_4]} {ask_4},{chosen_items}")

        
exit_q=input("pls click 'enter' to exit ").lower

















