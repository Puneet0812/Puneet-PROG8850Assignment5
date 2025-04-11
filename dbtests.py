import mysql.connector
import time

conn = mysql.connector.connect(
    user='root',
    unix_socket='/var/run/mysqld/mysqld.sock',
    database='ecommerce'
)
cursor = conn.cursor()

# Scalar query timing
print("🔍 Running AVG(payment_value) query...")
start = time.time()
cursor.execute("SELECT AVG(payment_value) FROM payments;")
print("✅ AVG Payment Value:", cursor.fetchone())
end = time.time()
print("⏱️ Time taken:", round(end - start, 4), "seconds\n")

# Full-text search using MATCH ... AGAINST
print("🔍 Running full-text search using MATCH() ... AGAINST()...")
start = time.time()
cursor.execute("""
    SELECT * FROM products 
    WHERE MATCH(product_category_name) AGAINST('celular');
""")
results = cursor.fetchall()
end = time.time()
print(f"✅ Found {len(results)} rows matching 'celular'")
print("⏱️ Time taken:", round(end - start, 4), "seconds\n")

# EXPLAIN for scalar query
print("🔎 EXPLAIN for AVG query:")
cursor.execute("EXPLAIN SELECT AVG(payment_value) FROM payments;")
for row in cursor.fetchall():
    print(row)

# EXPLAIN for MATCH ... AGAINST query
print("\n🔎 EXPLAIN for MATCH() ... AGAINST():")
cursor.execute("""
    EXPLAIN SELECT * FROM products 
    WHERE MATCH(product_category_name) AGAINST('celular');
""")
for row in cursor.fetchall():
    print(row)

cursor.close()
conn.close()
