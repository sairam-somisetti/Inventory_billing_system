import csv
import datetime
import os
from inventory import load_products, save_products

SALES_FILE = 'sales.csv'
BILLS_DIR = 'bills'

def add_to_cart(cart, pid, qty):
    products = load_products()
    for prod in products:
        if prod['ID'] == pid and prod['Stock'] >= qty:
            cart.append({'ID': prod['ID'], 'Name': prod['Name'], 'Price': prod['Price'], 'Qty': qty})
            prod['Stock'] -= qty
            save_products(products)
            return True
    return False

def generate_bill(cart, discount=0):
    total = sum(item['Price'] * item['Qty'] for item in cart)
    total_after_discount = total * (1 - discount/100)
    now = datetime.datetime.now()
    bill_text = []
    bill_text.append(f'Bill Date: {now.strftime("%Y-%m-%d %H:%M:%S")}')
    bill_text.append('--------------------------------')
    for item in cart:
        bill_text.append(f"{item['Name']} (x{item['Qty']}): {item['Price'] * item['Qty']:.2f}")
    bill_text.append('--------------------------------')
    bill_text.append(f"Total: {total:.2f}")
    if discount > 0:
        bill_text.append(f"Discount: {discount}%")
        bill_text.append(f"Total After Discount: {total_after_discount:.2f}")
    bill_text.append('--------------------------------')
    bill_data = {
        'date': now.strftime("%Y-%m-%d"),
        'items': cart,
        'total': total_after_discount
    }
    log_sales(cart, now)
    return ''.join(bill_text), bill_data

def save_bill(bill_text, bill_data, format='txt'):
    if not os.path.exists(BILLS_DIR):
        os.makedirs(BILLS_DIR)
    timestamp = datetime.datetime.now().strftime("%Y%m%d_%H%M%S")
    filename = f"{BILLS_DIR}/bill_{timestamp}.{format}"
    if format == 'txt':
        with open(filename, 'w') as f:
            f.write(bill_text)
    elif format == 'csv':
        with open(filename, 'w', newline='') as f:
            writer = csv.writer(f)
            writer.writerow(['Product', 'Qty', 'Unit Price', 'Total'])
            for item in bill_data['items']:
                writer.writerow([item['Name'], item['Qty'], item['Price'], item['Price']*item['Qty']])
            writer.writerow(['Total', '', '', bill_data['total']])
    return filename

def log_sales(cart, now):
    with open(SALES_FILE, 'a', newline='') as file:
        writer = csv.writer(file)
        for item in cart:
            writer.writerow([now.strftime("%Y-%m-%d"), item['ID'], item['Qty'], item['Price'], item['Price']*item['Qty']])