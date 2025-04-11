import mysql.connector

conn = mysql.connector.connect(
    user='root',
    unix_socket='/var/run/mysqld/mysqld.sock',
    database='ecommerce'
)
cursor = conn.cursor()

# Helper to create index safely
def create_index_safe(query):
    try:
        cursor.execute(query)
        print(f"✅ Executed: {query}")
    except mysql.connector.errors.ProgrammingError as e:
        if "Duplicate key name" in str(e):
            print(f"⚠️ Index already exists, skipped: {query}")
        else:
            raise

# Scalar index
create_index_safe("CREATE INDEX idx_payment_value ON payments(payment_value);")

# Fulltext index
create_index_safe("CREATE FULLTEXT INDEX idx_product_category_ft ON products(product_category_name);")

conn.commit()
cursor.close()
conn.close()
