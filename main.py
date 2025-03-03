# Define the function to print the menu
def print_menu():
    print("\nTaco Palace Menu")
    print("1. Taco")
    print("2. Burrito")
    print("3. Nachos")
    print("4. Water")
    print("5. Soft Drink")
    print("6. Quit")

# Define the function to get the price of what the customer orders
def get_price(selection):
    if selection == 1:
        return 3.50 # Taco price
    elif selection == 2:
        return 7.50 # Burrito price
    elif selection == 3:
        return 6.75 # Nachos price
    elif selection == 4:
        return 2.00 # Water price
    elif selection == 5:
        return 2.50 # Soft Drink Price
    else:
        return 0.00 # Quit or no price

# Main program loop
def taco_palace():
    # Welcome message
    print("Welcome to Taco Palace, please view the menu below and enter the number that represents your selection.")

    # Initialize the list to store ordered item and total cost
    ordered_items = []
    total_cost = 0.00

    while True:
        # Call the function to print the menu
        print_menu()

        # Get user input for selection
        try:
            user_input = int(input("User entered: "))
        except ValueError:
            print("Invalid input, please enter a number.")
            continue

        # If the user selects quit (option 6), exit the loop
        if user_input == 6:
            break

        # Process user selection
        if user_input in [1, 2, 3, 4, 5]: # Valid food/drink option
            # Get price and add it to the total
            price = get_price(user_input)
            total_cost += price

            # Add the item to the ordered items list
            if user_input == 1:
                ordered_items.append("Taco")
                print("You ordered a Taco")
            elif user_input == 2:
                ordered_items.append("Burrito")
                print("You ordered a Burrito")
            elif user_input == 3:
                ordered_items.append("Nachos")
                print("You ordered Nachos")
            elif user_input == 4:
                ordered_items.append("Water")
                print("You ordered Water")
            elif user_input == 5:
                ordered_items.append("Soft Drink")
                print("You ordered a Soft Drink")
        else:
            print("Invalid selection, please select a number between 1 and 6.")

    # Once user quits, display their order
    print("\nYour order:")
    print(f"You ordered: {', '.join(ordered_items)}")
    print(f"Your total is: ${total_cost:.2f}")

# Run the Taco Palace program
taco_palace()
