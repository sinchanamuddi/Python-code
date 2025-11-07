# Hotel Billing System

# The menu is stored in a dictionary with item names as keys and prices as values.
menu = {
    'tea': 15.00,
    'coffee': 20.00,
    'samosa': 10.00,
    'idli': 30.00,
    'dosa': 40.00,
    'vada': 25.00,
    'poori': 50.00,
    'paratha': 35.00,
    'biryani': 120.00,
    'veg noodles': 90.00,
    'chicken tikka': 150.00
}

def generate_bill():
    """Generates a hotel bill by taking a user's order."""
    print("Welcome to our Hotel! 🏨")
    print("\n---------------- MENU ----------------")
    for item, price in menu.items():
        print(f"{item.ljust(15)}: ₹{price:.2f}")
    print("--------------------------------------")

    order = {}
    
    while True:
        item_name = input("\nEnter item name (or 'done' to finish): ").lower()
        if item_name == 'done':
            break

        if item_name in menu:
            try:
                quantity = int(input(f"Enter quantity for {item_name}: "))
                if quantity > 0:
                    order[item_name] = order.get(item_name, 0) + quantity
                    print(f"{quantity} x {item_name} added to your order.")
                else:
                    print("Invalid quantity. Please enter a positive number.")
            except ValueError:
                print("Invalid input. Please enter a number for quantity.")
        else:
            print("Sorry, that item is not on the menu. Please try again.")

    if not order:
        print("\nNo items were ordered. Thank you for visiting! 😊")
        return

    # Calculate total cost, tax, and grand total
    total_cost = sum(menu[item] * quantity for item, quantity in order.items())
    tax_rate = 0.05  # 5% tax
    tax_amount = total_cost * tax_rate
    grand_total = total_cost + tax_amount

    # Print the final bill
    print("\n----------------- BILL -----------------")
    print("Item              Qty   Price   Total")
    print("----------------------------------------")
    for item, quantity in order.items():
        price = menu[item]
        total = price * quantity
        print(f"{item.ljust(18)}{str(quantity).ljust(4)}{f'₹{price:.2f}'.ljust(8)}{f'₹{total:.2f}'}")

    print("----------------------------------------")
    print(f"Subtotal:                 ₹{total_cost:.2f}")
    print(f"Tax ({tax_rate * 100}%):              ₹{tax_amount:.2f}")
    print("----------------------------------------")
    print(f"Grand Total:              ₹{grand_total:.2f}")
    print("----------------------------------------")
    print("Thank you for your visit! Have a great day! 😊")

# Run the program
if __name__ == "__main__":
    generate_bill()
