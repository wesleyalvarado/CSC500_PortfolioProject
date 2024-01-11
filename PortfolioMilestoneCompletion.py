

#ItemsToPurchase class
class ItemToPurchase:
    def __init__(self, item_name="none", item_description="none", item_price=0, item_quantity=0):
        self.item_name = item_name
        self.item_description = item_description
        self.item_price = item_price
        self.item_quantity = item_quantity

#ShoppingCart class
class ShoppingCart:
    def __init__(self, customer_name="none", current_date="December 18, 2023"):
        self.customer_name = customer_name
        self.current_date = current_date
        self.cart_items = []

    def add_item(self, item_to_purchase):
        self.cart_items.append(item_to_purchase)

    def remove_item(self, item_name):
        found = False
        for item in self.cart_items:
            if item.item_name == item_name:
                self.cart_items.remove(item)
                found = True
                break
        if not found:
            print("Item not found in cart. It was not removed.")

    def modify_item(self, modified_item):
        found = False
        for item in self.cart_items:
            if item.item_name == modified_item.item_name:
                item.item_description = modified_item.item_description
                item.item_price = modified_item.item_price
                item.item_quantity = modified_item.item_quantity
                found = True
                break
        if not found:
            print("Item not found in cart. Nothing modified.")

    def get_num_items_in_cart(self):
        num_items = sum(item.item_quantity for item in self.cart_items)
        return num_items

    def get_cost_of_cart(self):
        total_cost = sum(item.item_price * item.item_quantity for item in self.cart_items)
        return total_cost

    def print_total(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        num_items = self.get_num_items_in_cart()
        print(f"Number of Items: {num_items}")

        if num_items == 0:
            print("SHOPPING CART IS EMPTY")
        else:
            for item in self.cart_items:
                print(f"{item.item_name} {item.item_quantity} @ ${item.item_price} = ${item.item_price * item.item_quantity}")

        total_cost = self.get_cost_of_cart()
        print(f"Total: ${total_cost}")

    def print_descriptions(self):
        print(f"{self.customer_name}'s Shopping Cart - {self.current_date}")
        print("Item Descriptions")
        for item in self.cart_items:
            print(f"{item.item_name}: {item.item_description}")


#Part 5: Print_menu implementation
            
def print_menu():
    print("\nMENU")
    print("a - Add item to cart")
    print("r - Remove item from cart")
    print("c - Change item quantity")
    print("i - Output items' descriptions")
#Part 6: Output shopping cart option to Print_menu
    print("o - Output shopping cart")
    print("q - Quit")

def main():
    customer_name = input("Enter customer's full name: ")
    current_date = input("Enter the current date: ")
    shopping_cart = ShoppingCart(customer_name, current_date)

    print(customer_name)
    print(current_date)

    while True:
        print_menu()
        user_choice = input("Choose an option: ")

        if user_choice == 'a':
            # Add item to cart
            item_name = input("Enter the name of the item: ")
            item_description = input("Enter the description of the item: ")
            item_price = float(input("Enter the price of the item: "))
            item_quantity = int(input("Enter the quantity of the item: "))
            item_to_purchase = ItemToPurchase(item_name, item_description, item_price, item_quantity)
            shopping_cart.add_item(item_to_purchase)

        elif user_choice == 'r':
            # Remove item from cart
            item_name = input("Enter the name of the item to remove: ")
            shopping_cart.remove_item(item_name)

        elif user_choice == 'c':
            # Change item quantity
            item_name = input("Enter the name of the item to modify: ")
            item_quantity = int(input("Enter the new quantity of the item: "))
            modified_item = ItemToPurchase(item_name, item_quantity=item_quantity)
            shopping_cart.modify_item(modified_item)

        elif user_choice == 'i':
            # Output items' descriptions
            shopping_cart.print_descriptions()

        elif user_choice == 'o':
            # Output shopping cart
            shopping_cart.print_total()

        elif user_choice == 'q':
            # Quit
            print("Exiting the program. Goodbye!")
            break

        else:
            print("Invalid choice. Please choose a valid option.")

if __name__ == "__main__":
    main()
