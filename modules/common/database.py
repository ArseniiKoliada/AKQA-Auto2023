import sqlite3


class Database():

    # class constructor which initializes connection to the database file 
    #   and creates a cursor to execute queries and fetch results
    def __init__(self):
        self.connection = sqlite3.connect(r'c:/Users/Mine-iac/Desktop/AKQA-Auto2023' + r'/become_qa_auto.db')
        self.cursor = self.connection.cursor()

    # display SQLite version and "connected successfully" message
    def test_connection(self):
        # query the SQLite version
        sqlite_select_query = "SELECT sqlite_version();"
        # execute the query
        self.cursor.execute(sqlite_select_query)
        # fetch all rows from query
        record = self.cursor.fetchall()
        print(f"Connected successfully. Sqlite Database version is {record}")

    # select all users from customers table
    def get_all_users(self):
        query = "SELECT name, address, city FROM customers"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    #display address information about a person with certain name
    def get_user_address_by_name(self, name):
        query = f"SELECT address, city, postalCode, country FROM customers WHERE name = '{name}'"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record

    # change quantity of a product with selected id
    def update_product_qnt_by_id(self, product_id, qnt):
        query = f"UPDATE products SET quantity = {qnt} WHERE id = {product_id}"
        self.cursor.execute(query)
        # commit the changes, used when performing requests other than SELECT, 
        #   i.e., that make changes to the database
        # no return statement as there's nothing to display
        self.connection.commit()

    # display the quantity of a product with selected id
    def select_product_qnt_by_id(self, product_id):
        query = f"SELECT quantity FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        record = self.cursor.fetchall()

        return record
    
    # add a new product into the table
    def insert_products(self, product_id, name, description, qnt):
        query = f"INSERT OR REPLACE INTO products (id, name, description, quantity) \
            VALUES({product_id}, '{name}', '{description}',{qnt})"
        self.cursor.execute(query)
        self.connection.commit()

    # delete product by id
    def delete_product_by_id(self, product_id):
        query = f"DELETE FROM products WHERE id = {product_id}"
        self.cursor.execute(query)
        self.connection.commit()

    # display what customer ordered what product
    def get_detailed_orders(self):
        query = "SELECT orders.id, customers.name, products.name, \
            products.description, orders.order_date \
            FROM orders \
            JOIN customers ON orders.customer_id = customers.id \
            JOIN products ON orders.product_id = products.id"
        self.cursor.execute(query)
        record = self.cursor.fetchall()
        return record
