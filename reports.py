import csv
from inventory import load_products
#importing a function to load products from another module

SALES_FILE = 'sales.csv'
# file contains the sales records
def daily_sales_report(date):
    total = 0
    items_sold = []
    try:
        # opening the sales file in read mode
        with open(SALES_FILE, 'r') as file:
            reader = csv.reader(file)
            #iterate the eeach record in the file
            for row in reader:
                #each row must contains:date,product_id,qty,price,amount
                sale_date, pid, qty, price, amount = row
                #checking whether this record matches with the requested date
                if sale_date == date:
                    total += float(amount)
                    #adding the amount to the daily total
                    items_sold.append({'ID': pid, 'Qty': qty, 'Amount': amount})
        return total, items_sold
    except FileNotFoundError:
        #if sales.csv doesn't exist,return empty results
        return 0, []

def low_stock_report(threshold=5):
    products = load_products()
#loading the product data from inventory module
    #FILTERING PRODUCT DATA WHICH CONTAINS STOCK LESS THAN OR EQUAL TO THE THRESHOLD.
    return [prod for prod in products if prod['Stock'] <= threshold]
