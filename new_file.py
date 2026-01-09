print("<------------ ANURAG CAFE | Menu ------------>\n")

cafe_menu = {
    "Coffee": 2,
    "Tea": 1,
    "Nuddles": 4,
    "Sandwich": 4,
    "Burger": 3,
    "Pizza": 7
}


# Print menu
for key, value in cafe_menu.items():
    print(f"{key} : {value}")

cart = []

def dish_order():
    while True:
        order_item = input(
            "\nEnter dish-name | type 'view cart' | type 'exit': "
        ).strip()

        if order_item.lower() == "exit":
            print("\nThank you for visiting ANURAG CAFE ")
            break

        elif order_item.strip() == "view cart":
            if cart:
                print("\n🛒 Your Cart:")
                for item in cart:
                    print("-", item)
                for item in cart:
                    print("-", item)
            else:
                print("Cart is empty 🛒")
        elif order_item in cafe_menu:
            cart.append(order_item)
            print(f"{order_item} added to cart ")

            choice = input(f"Anything else with your {order_item}? [YES / NO]: ").strip().lower()

            if choice == "yes":
                continue

            elif choice == "no":
                total_bill = 0
                for item in cart:
                    total_bill += cafe_menu[item]

                print("\n BILL SUMMARY")
                for item in cart:
                    print(f"- {item} : ${cafe_menu[item]}")

                print(f"\n Total Bill: ${total_bill}")
                print("\nThank you for visiting ANURAG CAFE ")
                break


            else:
                print("Please type YES or NO only!")

dish_order()

