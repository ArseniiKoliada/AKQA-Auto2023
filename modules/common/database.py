import sqlite3


class Database():

    def __init__(self):
        self.connection = sqlite3.connect(r'c:/Users/Mine-iac/Desktop/AKQA-Auto2023' + r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()

    def test_connection(self):
        sqlite_select_query = "SELECT sqlite_version();"
        self.cursor.execute(sqlite_select_query)
        record = self.cursor.fetchall()
        print(f"Connected successfully. Sqlite Database version is {record}")

    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record
    
    def insert_products(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES({product_id}, '{name}', '{description}',{qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
            products.description, orders.order_date \
            FROM orders \
            JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record