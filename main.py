#importing all the necessary functions from various modules.
from inventory import add_product, update_product, delete_product, search_product
from inventory import load_products
from order import add_to_cart, generate_bill, save_bill
from reports import daily_sales_report, low_stock_report

def main_menu():
    while True:
        # displaying the main menu with different options.
        print("1. Add Product")
        print("2. Update Product")
        print("3. Delete Product")
        print("4. Search Product")
        print("5. Show All Products")
        print("6. Create Order")
        print("7. Daily Sales Report")
        print("8. Low Stock Products")
        print("9. Exit")
        # getting user choices.
        choice = input("Pick an option: ")
        #adding new product
        if choice == '1':
            pid = input("Product ID: ")
            name = input("Name: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            add_product(pid, name, price, stock)
            #---update product details---
        elif choice == '2':
            pid = input("Product ID to update: ")
            key = input("Field to update (Name/Price/Stock): ")
            value = input("New value: ")
            if key == "Price":
                value = float(value)
            elif key == "Stock":
                value = int(value)
            update_product(pid, **{key: value})
            #---deleting a new product---
        elif choice == '3':
            pid = input("Product ID to delete: ")
            delete_product(pid)
            #---searching for a product by it's ID or name.
        elif choice == '4':
            keyword = input("Enter product ID or name: ")
            results = search_product(keyword)
            print(results)
            #---display of all products---
        elif choice == '5':
            for prod in load_products():
                print(prod)
                #---creating a new order---
        elif choice == '6':
            cart = []
            while True:
                pid = input("Product ID to add to cart (or 'done'): ")
                if pid == 'done':
                    break
                qty = int(input("Quantity: "))
                if not add_to_cart(cart, pid, qty):
                    print("Not enough stock or invalid product ID.")
                    #apply the discount if given.
            disc = input("Discount (%) (blank for 0): ")
            discount = float(disc) if disc else 0
            #generate and display bill
            bill_text, bill_data = generate_bill(cart, discount)
            print(bill_text)
            #saving bill in chosen format
            fmt = input("Save bill as txt or csv? [txt/csv]: ")
            save_bill(bill_text, bill_data, fmt)
            #---generating the daily sales reports---.
        elif choice == '7':
            date = input("Enter date (YYYY-MM-DD): ")
            total, items = daily_sales_report(date)
            print(f"Total Sales: {total}")
            for item in items:
                print(item)
                #---showing all products with low stock---
        elif choice == '8':
            threshold = int(input("Enter stock threshold: "))
            low_stock = low_stock_report(threshold)
            print("Low Stock Products:")
            for prod in low_stock:
                print(prod)
                # ---exit from the program---
        elif choice == '9':
            break
# ---entry point of the program or function call---
if __name__ == '__main__':
    main_menu()

    
