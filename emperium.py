import psycopg2

class DBFacade:
    def __init__(self):
        self.DB_CONECTION = psycopg2.connect(
            dbname = "emperium",
            user='postgres',
            password='123123',
            host='localhost',
            port=5432
        )
        self.DB_CURSOR = self.DB_CONECTION.cursor()
        
        some_query = """
            CREATE TABLE IF NOT EXISTS expenses(
                id SERIAL PRIMARY KEY,
                unit_name VARCHAR(100),
                resource VARCHAR(100),
                amount NUMERIC(10, 2),
                battle VARCHAR(100)
            )
        """
        
        self.DB_CURSOR.execute(some_query)
        self.DB_CONECTION.commit()
        
    def add_execute(self, unit_name, resource, amount, battle):
        add_execute_table = """
        INSERT INTO expenses (unit_name, resource, amount, battle)
        VALUES (%s, %s, %s, %s)
        """
        self.DB_CURSOR.execute(add_execute_table, (unit_name, resource, amount, battle))
        self.DB_CONECTION.commit()
        
    def serach_execute(self, unit_name = None, battle = None):
        select = "SELECT * FROM expenses WHERE TRUE"
        
        data = []
        
        if unit_name:
            select += " AND unit_name = %s"
            data.append(unit_name)
        if battle:
            select += " AND battle = %s"
            data.append(battle)
            
        self.DB_CURSOR.execute(select, data)        
        results = self.DB_CURSOR.fetchall()
        return results
    
    def show_all(self):
        self.DB_CURSOR.execute("SELECT * FROM expenses")
        return self.DB_CURSOR.fetchall()
    
    def close(self):
        self.DB_CURSOR.close()
        self.DB_CONECTION.close()
        
def data_open():
    
    db = DBFacade()
    
    while True:
        print("\n--- Терминал ---")
        print("Добро пожаловать в терминал адептус администратум")
        print("Что желаете сделать?")
        
        print("\n 1. Добавить расход")
        print("2. Поиск расходов")
        print("3. Показать все расходы")
        print("4. Выход из терминала")
        
        task = int(input("\nВыберите вариант ответа: "))
        
        try:
            if task == 1:
                print("\nВведите название подразделения")
                unit = input("Ответ: ")
                
                print("\nВведите название ресурса")
                resource = input("Ответ: ")

                print("\nВведите количетсво затраченного ресурса")
                amount = float(input("Ответ: "))
                
                print("\nВведите мество битвы")
                battle = input("Ответ: ")
                
                db.add_execute(unit, resource, amount, battle)
                
            elif task == 2:
                print("Введите название подразделения")
                unit = input("Ответ: ")
                
                print("\nВведите мество битвы")
                battle = input("Ответ: ")
                
                result = db.serach_execute(
                    unit_name= unit if unit else None,
                    battle= battle if battle else None,
                    )
                
                for row in result:
                    print(row)
                    
            elif task == 3:
                print("\nВсе рассходы в текущий момент:")
                result = db.show_all()
                
                for row in result:
                    print(row)
                    
            elif task == 4:
                db.close()
                
                print("\n Терминал завершил свою работу")
                break
            
            else:
                print("Ошибка!")
        except ValueError as error:
            print(f"Ошибка {type(error).__name__}: ошибка ввода значения.")
