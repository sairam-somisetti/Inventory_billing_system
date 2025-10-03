# Inventory_billing_system-A python based console application

A comprehensive Python-based console application for managing inventory, processing sales, and generating business reports.

## 📋 Project Overview

The **Inventory Management System** is a robust console application designed to streamline inventory control and sales management for small to medium-sized businesses. This system provides a complete solution for product management, order processing, billing, and business intelligence through an intuitive menu-driven interface.

Built with modular architecture and CSV-based data persistence, the application offers enterprise-level inventory management capabilities in a lightweight, accessible format perfect for retailers, warehouses, and small businesses.

## 🎯 Project Objectives

### Primary Objectives

#### 1. **Efficient Inventory Control**
- Centralized product database management with real-time stock tracking
- Complete product lifecycle management (CRUD operations)
- Proactive low stock alerts and monitoring

#### 2. **Streamlined Sales Processing**
- Automated order management with stock validation
- Flexible billing system with discount support
- Multiple bill format generation (TXT/CSV)
- Automatic sales logging and inventory updates

#### 3. **Comprehensive Business Intelligence**
- Daily sales reporting and revenue analytics
- Inventory performance metrics and trend analysis
- Data-driven insights for business decision making

### Technical Objectives

#### 4. **Data Integrity & Persistence**
- Reliable CSV-based data storage
- Consistent data management across modules
- Easy backup and export capabilities

#### 5. **User Experience**
- Intuitive console interface for non-technical users
- Robust error handling and input validation
- Fast, responsive operations

## 🏗️ System Architecture

```
Inventory Management System
├── Core Modules
│   ├── inventory.py    - Product management
│   ├── order.py        - Sales processing & billing
│   ├── reports.py      - Analytics & reporting
│   └── main.py         - User interface
├── Data Files
│   ├── products.csv    - Product database
│   └── sales.csv       - Sales records
└── Generated Content
    └── bills/          - Customer bills (auto-created)
```

## 📁 File Structure

### Core Application Files

#### `main.py`
**Purpose**: Main application entry point and user interface
```python
# Key Features:
# - Interactive menu system
# - User input handling
# - Module coordination
# - Error management
```

#### `inventory.py`
**Purpose**: Product management and inventory operations
```python
# Key Functions:
load_products()          # Load product data from CSV
save_products(products)  # Save products to CSV
add_product(pid, name, price, stock)
update_product(pid, **kwargs)
delete_product(pid)
search_product(keyword)
```

#### `order.py`
**Purpose**: Sales processing, billing, and cart management
```python
# Key Functions:
add_to_cart(cart, pid, qty)     # Add items with stock validation
generate_bill(cart, discount)   # Create bill text and data
save_bill(bill_text, bill_data, format)  # Save as TXT/CSV
log_sales(cart, now)            # Record sales transactions
```

#### `reports.py`
**Purpose**: Business intelligence and analytics
```python
# Key Functions:
daily_sales_report(date)        # Sales analysis by date
low_stock_report(threshold)     # Inventory alert system
```

### Data Files

#### `products.csv`
Stores product information in CSV format:
```csv
ID,Name,Price,Stock
123,saiam,2000.0,123
2345,laptop,2000.0,2
```

#### `sales.csv`
Tracks all sales transactions:
```csv
Date,ProductID,Qty,UnitPrice,Amount
```

## 🚀 Features

### 1. Product Management
- **Add New Products**: Complete product registration with ID, name, price, and stock
- **Update Existing Products**: Modify name, price, or stock levels
- **Delete Products**: Remove products from inventory
- **Search Functionality**: Find products by ID or name
- **View All Products**: Complete inventory listing

### 2. Sales & Order Processing
- **Shopping Cart System**: Add multiple products to cart
- **Stock Validation**: Prevent overselling with real-time stock checks
- **Automatic Inventory Updates**: Stock levels adjust automatically after sales
- **Discount Management**: Apply percentage discounts to orders
- **Bill Generation**: Professional bill creation with timestamps

### 3. Reporting & Analytics
- **Daily Sales Reports**: Revenue analysis by specific dates
- **Low Stock Alerts**: Customizable threshold for stock warnings
- **Sales Tracking**: Complete transaction history
- **Inventory Analytics**: Stock level monitoring and reporting

### 4. Data Management
- **CSV-based Storage**: Simple, accessible data format
- **Automatic Backup**: Data persists between sessions
- **Bill Archiving**: Organized storage of customer bills
- **Sales Logging**: Comprehensive transaction records

## 🛠️ Installation & Usage

### Prerequisites
- Python 3.x
- No external dependencies required

### Setup Instructions

1. **Download all project files** to a single directory:
   ```
   main.py
   inventory.py
   order.py
   reports.py
   products.csv
   sales.csv
   ```

2. **Run the application**:
   ```bash
   python main.py
   ```

3. **Follow the menu prompts** to manage your inventory and process sales.

### Usage Examples

#### Adding a Product
```
1. Add Product
Product ID: 456
Name: Wireless Mouse
Price: 25.99
Stock: 50
```

#### Processing an Order
```
6. Create Order
Product ID to add to cart: 123
Quantity: 2
Product ID to add to cart: done
Discount (%): 10
Save bill as txt or csv? [txt/csv]: txt
```

#### Generating Reports
```
7. Daily Sales Report
Enter date (YYYY-MM-DD): 2024-01-15

8. Low Stock Products  
Enter stock threshold: 5
```

## 🔧 Technical Details

### Data Persistence
- **CSV Files**: All data stored in human-readable CSV format
- **Automatic Saving**: Changes saved immediately after each operation
- **File Validation**: Handles missing files gracefully

### Error Handling
- **Input Validation**: Robust checking of user inputs
- **Stock Validation**: Prevents sales exceeding available inventory
- **File Operations**: Safe file handling with proper exceptions

### Modular Design
- **Separation of Concerns**: Each module handles specific functionality
- **Easy Maintenance**: Independent updates to modules
- **Extensible**: Simple to add new features

## 📊 Output Examples

### Generated Bill (TXT format)
```
Bill Date: 2024-01-15 14:30:25
--------------------------------
saiam (x2): 4000.00
laptop (x1): 2000.00
--------------------------------
Total: 6000.00
Discount: 10%
Total After Discount: 5400.00
--------------------------------
```

### Sales Report
```
Total Sales: 5400.00
{'ID': '123', 'Qty': '2', 'Amount': '4000.0'}
{'ID': '2345', 'Qty': '1', 'Amount': '2000.0'}
```
# screenshots:
<img width="1854" height="962" alt="Image" src="https://github.com/user-attachments/assets/38a63fe8-4f9b-4574-9712-f1250594b4c8" />

<img width="519" height="913" alt="Image" src="https://github.com/user-attachments/assets/0dc1eaae-c25e-43d1-aad9-862391c948fe" />

## 🎯 Business Benefits

### Operational Efficiency
- **Time Savings**: Automated calculations and stock updates
- **Error Reduction**: Minimized manual entry mistakes
- **Process Standardization**: Consistent operations across all transactions

### Financial Management
- **Revenue Tracking**: Complete sales monitoring
- **Inventory Optimization**: Reduced overstocking and stockouts
- **Cost Control**: Better visibility into inventory investment

### Customer Service
- **Fast Checkout**: Quick bill generation
- **Professional Documentation**: Clean, detailed customer bills
- **Accurate Pricing**: Consistent pricing with discount support

## 🔮 Future Enhancements

- User authentication and access control
- Advanced analytics with graphical reports
- Email integration for low stock alerts
- Multi-currency support
- Barcode scanning integration
- Web-based interface
- Mobile application companion

## 📝 License & Contribution
This project is open for educational and commercial use. Developers are encouraged to extend functionality and contribute improvements.
*This Inventory Management System provides a complete, professional solution for businesses seeking to digitalize their inventory and sales processes with a reliable, easy-to-use console application.*

📩 Contact
👨‍💻 Developer: SAIRAM SOMISETTI
📧 Email: somisettisairam@gmail.com
🌐 GitHub: https://github.com/sairam-somisetti
💡 Feel free to fork, contribute, or drop a message if you have ideas to improve this project!
