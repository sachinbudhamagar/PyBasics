print("Welcome! I'm restaurant bot. Here's our menu")

def print_menu():
    """Prints the menu options."""
    print("-" * 44)
    print("1: Sandwich")
    print("2: Burger")
    print("3: Pizza")
    print("4: Noodles")
    print("5: Pasta")
    print("6: Coffee")
    print("7: Lemonade")
    print("8: Exit")
    print()

def get_food_name(order):
    """Returns the food name based on the order number."""
    menu = {
        1: "Sandwich",
        2: "Burger",
        3: "Pizza",
        4: "Noodles",
        5: "Pasta",
        6: "Coffee",
        7: "Lemonade"
    }
    return menu.get(order, "")

def print_final_order(order_items):
    """Prints the final order summary."""
    if order_items:
        print("Thank you for your order. Here's your order summary:")
        for item in order_items:
            print(item)
        print("Thank you for your order. Enjoy your meal!")
    else:
        print("Your order is empty! Thank you for visiting.")

def bot():
    order_items = []

    while True:
        print_menu()

        try:
            order = int(input("Enter number you would like to order: "))

            if 1 <= order <= 7:
                food = get_food_name(order)
                order_items.append(food)
                print(f"{food} is added to your order")
                print("-" * 40)
                print()

                while True:
                    add_more = input("Would you like to add another order? y/n: ").lower()
                    if add_more == "y":
                        break
                    elif add_more == "n":
                        print_final_order(order_items)
                        return
                    else:
                        print("Invalid input! Enter 'y' or 'n'.")
                        continue

            elif order == 8:
                print_final_order(order_items)
                return

            else:
                print("Invalid input. Please enter a number between 1-8.")
                print()

        except ValueError:
            print("Invalid input. Please enter a valid number between 1-8.")
            print()

if __name__ == "__main__":
    bot()