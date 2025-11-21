import psycopg2

class DBFacade_one:
    def __init__(self):
        self.DB_CONNECTION = psycopg2.connect(
            dbname='shop_db',
            user='postgres',
            password='123123',
            host='localhost',
            port=5432
        )
        self.DB_CURSOR = self.DB_CONNECTION.cursor()

        some_query_category = """
            CREATE TABLE IF NOT EXISTS category (
                id SERIAL PRIMARY KEY, 
                name VARCHAR(100),
                category_id NUMERIC(10,2)
            );
        """

        some_query_product = """
            CREATE TABLE IF NOT EXISTS product (
                id SERIAL PRIMARY KEY, 
                price NUMERIC(10,2)
            ) INHERITS(category);
        """

        self.DB_CURSOR.execute(some_query_category)
        self.DB_CURSOR.execute(some_query_product)
        self.DB_CONNECTION.commit()

    def add_category(self, name, category_id):
        query = """
            INSERT INTO category (name, category_id) VALUES (%s, %s);
        """
        self.DB_CURSOR.execute(query, (name, category_id))
        self.DB_CONNECTION.commit()

    def add_product(self, name, category_id, price):
        query = """
            INSERT INTO product (name, category_id, price) VALUES (%s, %s, %s);
        """
        self.DB_CURSOR.execute(query, (name, category_id, price))
        self.DB_CONNECTION.commit()

    def close(self):
        self.DB_CURSOR.close()
        self.DB_CONNECTION.close()


db_facade = DBFacade_one()

while True:
    choice = input("1 = добавить категорию, 2 = добавить продукт, 0 = выход: ")
    if choice == "0":
        break
    elif choice == "1":
        name = input("Введите название категории: ")
        code = float(input("Введите код категории: "))
        db_facade.add_category(name, code)
    elif choice == "2":
        name = input("Введите название продукта: ")
        code = float(input("Введите код категории: "))
        price = float(input("Введите цену: "))
        db_facade.add_product(name, code, price)

db_facade.close()
