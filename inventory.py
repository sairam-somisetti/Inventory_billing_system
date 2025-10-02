import csv
import os

PRODUCTS_FILE = 'products.csv'

def load_products():
    products = []
    if os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, mode='r', newline='') as file:
            reader = csv.DictReader(file)
            for row in reader:
                row['Price'] = float(row['Price'])
                row['Stock'] = int(row['Stock'])
                products.append(row)
    return products

def save_products(products):
    with open(PRODUCTS_FILE, mode='w', newline='') as file:
        writer = csv.DictWriter(file, fieldnames=['ID', 'Name', 'Price', 'Stock'])
        writer.writeheader()
        for prod in products:
            writer.writerow(prod)

def add_product(pid, name, price, stock):
    products = load_products()
    products.append({'ID': pid, 'Name': name, 'Price': float(price), 'Stock': int(stock)})
    save_products(products)

def update_product(pid, **kwargs):
    products = load_products()
    for prod in products:
        if prod['ID'] == pid:
            for key, value in kwargs.items():
                if key in prod:
                    prod[key] = value
    save_products(products)

def delete_product(pid):
    products = [prod for prod in load_products() if prod['ID'] != pid]
    save_products(products)

def search_product(keyword):
    results = []
    for prod in load_products():
        if keyword.lower() in prod['Name'].lower() or keyword == prod['ID']:
            results.append(prod)
    return results