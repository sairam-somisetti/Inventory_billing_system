import csv
from inventory import load_products

SALES_FILE = 'sales.csv'

def daily_sales_report(date):
    total = 0
    items_sold = []
    try:
        with open(SALES_FILE, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                sale_date, pid, qty, price, amount = row
                if sale_date == date:
                    total += float(amount)
                    items_sold.append({'ID': pid, 'Qty': qty, 'Amount': amount})
        return total, items_sold
    except FileNotFoundError:
        return 0, []

def low_stock_report(threshold=5):
    products = load_products()
    return [prod for prod in products if prod['Stock'] <= threshold]