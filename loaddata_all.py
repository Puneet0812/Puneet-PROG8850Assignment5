import mysql.connector
import csv

def sanitize(value):
    return value if value.strip() else None

# Connect via Unix socket as root
conn = mysql.connector.connect(
    user='root',
    unix_socket='/var/run/mysqld/mysqld.sock',
    database='ecommerce'
)
cursor = conn.cursor()

### 1. Load customers
with open("data/olist_customers_dataset.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        cursor.execute("""
            INSERT INTO customers (
                customer_id, customer_unique_id, customer_zip_code_prefix,
                customer_city, customer_state
            ) VALUES (%s, %s, %s, %s, %s)
        """, row)

print("✅ Customers loaded.")

### 2. Load orders
with open("data/olist_orders_dataset.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        cursor.execute("""
            INSERT INTO orders (
                order_id, customer_id, order_status, order_purchase_timestamp,
                order_approved_at, order_delivered_carrier_date,
                order_delivered_customer_date, order_estimated_delivery_date
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)
        """, [sanitize(val) for val in row])

print("✅ Orders loaded.")

### 3. Load order_items
with open("data/olist_order_items_dataset.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        cursor.execute("""
            INSERT INTO order_items (
                order_id, order_item_id, product_id, seller_id,
                shipping_limit_date, price, freight_value
            ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """, [sanitize(val) for val in row])

print("✅ Order Items loaded.")

### 4. Load payments
with open("data/olist_order_payments_dataset.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        cursor.execute("""
            INSERT INTO payments (
                order_id, payment_sequential, payment_type,
                payment_installments, payment_value
            ) VALUES (%s, %s, %s, %s, %s)
        """, [sanitize(val) for val in row])

print("✅ Payments loaded.")

### 5. Load products
with open("data/olist_products_dataset.csv", "r", encoding="utf-8") as file:
    reader = csv.reader(file)
    next(reader)
    for row in reader:
        cursor.execute("""
            INSERT INTO products (
                product_id, product_category_name, product_name_length,
                product_description_length, product_photos_qty,
                product_weight_g, product_length_cm,
                product_height_cm, product_width_cm
            ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)
        """, [sanitize(val) for val in row])

print("✅ Products loaded.")

conn.commit()
cursor.close()
conn.close()
print("🎉 All data loaded successfully into ecommerce DB.")
