This project for PROG8850 Assignment 5 showcases a complete end-to-end database automation workflow using Ansible, Python, and MySQL. The objective was to automate the creation of a database schema, load CSV datasets from a Brazilian e-commerce archive, optimize query performance, and analyze the effects of indexing on query execution.

All tasks are fully orchestrated using a single Ansible playbook (up.yaml) which handles database and table creation, data ingestion from CSV files, index creation, and query performance testing. Python scripts (loaddata_all.py, create_indexes.py, and dbtests.py) are integrated within the playbook to modularize data loading, indexing, and performance analysis.

The database includes five key tables: orders, customers, order_items, payments, and products. Data from these tables is loaded from the official Kaggle dataset provided by Olist. After loading, a scalar index was created on payments(payment_value) to optimize aggregation queries, and a FULLTEXT index was created on products(product_category_name) to support full-text search with MATCH() ... AGAINST().

Query performance was timed and analyzed using Python. EXPLAIN plans before and after indexing were compared, showing clear improvements. For example, full table scans (ALL) were reduced to index-based lookups (index, ref) as a result of indexing.

The entire pipeline was tested in GitHub Codespaces using Python 3.12 and MySQL 8.0 over a UNIX socket. Execution was verified through screenshots of successful Ansible playbook runs, SHOW INDEX confirmations, and EXPLAIN output.

This project highlights the importance of database automation and indexing in real-world data pipelines, providing a practical example of how DevOps tools like Ansible can integrate seamlessly with Python and SQL-based workflows to ensure repeatable, scalable deployments.

