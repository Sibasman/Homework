try:
    print("Метод решеня по обычному def или через __init__? (1-4)")
    task = int(input("Ответ: "))
    if task == 1:
        
        class Item:
            def __init__(self, name, name_shop, price_item):
                self.name = name
                self.name_shop = name_shop
                self.price_item = price_item
            
        items = [
            Item("Печеньки", "Копеечка", 10),
            Item("Веб разработчик на Python", "IT Academy", 1041),
        ]
        
        for count, i in enumerate(items, start =1):
            print(f"{count}. Товар: \"{i.name}\" находиться в {i.name_shop} и стоит {i.price_item} руб")
            
            
    elif task == 2:
        
        class Item:
            def __init__(self, name, name_shop, price_item):
                self.__name = name
                self.__name_shop = name_shop
                self.__price_item = price_item
                
            def get_name(self):
                return self.__name
            
            def get_name_shop(self):
                return self.__name_shop
            
            def get_price_item(self):
                return self.__price_item
            
        class Warehouse(Item):
            def __init__(self, index_item, name, name_shop, price_item):
                super().__init__(name, name_shop, price_item)
                self.__index_item = index_item
                
            def get_index_item(self):
                return self.__index_item
                
        items_warehouse = [
            Warehouse("636F6F6B6965", "Cookie", "Shop", 2.50),
            Warehouse("62616E616E61", "Banana", "Shop", 3.90),
            Warehouse("436172", "Car", "Car Dealer", 99999.20)
        ]
        
        print("Как вы метод решения вы хотите вывести.")
        print("Вывод информации по идексу/названию, сортировка по названию/магазину/цене, операция по сложению цен товара.")
        print("(1а,1б,2а,2б,2в,3)")
        task_new = str(input("Ответ: "))
        
        if task_new.lower() == "1а":
            print("Введите индекс товара.")
            
            search_index = input("Ответ: ")
            found_item = [i for i in items_warehouse if i.get_index_item() == search_index]
            
            if found_item:
                for i in found_item:
                    print("Товар найдет.")
                    print(f"Товар: {i.get_index_item()} с названием \"{i.get_name()}\" находиться в {i.get_name_shop()} и стоит {i.get_price_item()} руб.")
            else:
                print(f"Товар с этим индексом не найдет в базе склада.")
            
        elif task_new.lower() == "1б":
            print("Введите название товара.")
            
            search_name = input("Ответ: ")
            found_item = [i for i in items_warehouse if i.get_name() == search_name]
            
            if found_item:
                for i in found_item:
                    print("Товар найден.")
                    print(f"Товар: {i.get_index_item()} с названием \"{i.get_name()}\" находиться в {i.get_name_shop()} и стоит {i.get_price_item()} руб.")
            else:
                print("Товар с этим названием не найден в базе склада.")
            
        elif task_new.lower() == "2а":
            items_warehouse_sort = sorted(items_warehouse, key= lambda item: item.get_name())
            
            for count, i in enumerate(items_warehouse_sort, start=1):
                print(f"{count}. Товар: {i.get_index_item()} \"{i.get_name()}\" находиться в {i.get_name_shop()} и стоит {i.get_price_item()} руб.")
                
        elif task_new.lower() == "2б":
            items_warehouse_sort = sorted(items_warehouse, key= lambda item: item.get_name_shop())
            
            for count, i in enumerate(items_warehouse_sort, start= 1):
                print(f"{count}. Товар: {i.get_index_item()} \"{i.get_name()}\" находиться в {i.get_name_shop()} и стоит {i.get_price_item()} руб.")
        
        elif task_new.lower() == "2в":
            items_warehouse_sort = sorted(items_warehouse, key= lambda item: item.get_price_item())
            
            for count, i in enumerate(items_warehouse_sort, start= 1):
                print(f"{count}. Товар: {i.get_index_item()} \"{i.get_name()}\" находиться в {i.get_name_shop()} и стоит {i.get_price_item()} руб.")
                
        elif task_new.lower() == "3":
            total_price = sum(item.get_price_item() for item in items_warehouse)
            print(f"Общая сумма всех товаров на складе: {total_price:.2f} руб.")
        
    elif task == 3:
        class PcheloSlon:
            def __init__(self, bee, elephant):
                self.bee = bee
                self.elephant = elephant
                
            def fly(self):
                return self.bee >= self.elephant
            
            def trumpet(self):
                return "tu-tu-doo-doo" if self.elephant >= self.bee else "wzzz"
            
            def eat(self, meal, value):
                if meal =="nectar":
                    self.bee = self.bee + value
                elif meal == "grass":
                    self.elephant = self.elephant + value
                else:
                    print("Ошибка, некоректный ввод")
                    
            def status(self):
                print(f"Bee: {self.bee}, Elephant: {self.elephant}")
        
        pcheloslon_init = PcheloSlon(60,40)
        
        pcheloslon_init.eat("nectar", 10)
        pcheloslon_init.status() 
        print(pcheloslon_init.fly())         
        print(pcheloslon_init.trumpet())
    
    elif task == 4:
        class Bus:
            def __init__(self, max_seats, max_speed):
                self.speed = 0
                self.max_speed = max_speed
                self.max_seats = max_seats
                self.seats = [None] * max_seats 
                
                self.passengers = []  #Список людей
            
            @property
            def free_seats(self):
                return len(self.passengers) < self.max_seats
            
            @property
            def free_seats_info(self):
                free = self.max_seats - len(self.passengers)
                if free > 0:
                    return f"Доступны свободные места: {free}"
                elif free == 0:
                    return "Все места заняты"
                else:
                    return f"Переполнено на {abs(free)} человек(а)"
                
            def boadr(self, name):
                if self.free_seats:
                    for i in range(self.max_seats):
                        if self.seats[i] is None:
                            self.seats[i] = name
                            return(f"{name} сел на место {i + 1}")
                else:
                    return("Нет свободных мест")
            
            def exit(self, name):
                if name in self.seats:
                    index = self.seats.index(name)
                    self.seats[index] = None
                    return(f"{name} испарился")
                else:
                    return(f"{name} являеться призраком?")
                
            def change_speed(self, delta):
                old_speed = self.speed
                self.speed = max(0, min(self.speed + delta, self.max_speed))
                print(f"Скорость автобуса: {self.speed} км/ч")
                
                if self.speed > old_speed:
                    print("Привыешнии скорости")
                elif self.speed == 0:
                    print("Вы совершили аварию :)")
                else:
                    print("Скорость изменена")
            
            @property
            def speed_info(self):
                return f"Текущая скорость: {self.speed} км/ч"
            
            def status(self):
                print(f"Скорость автобуса: {self.speed} км/ч")
                print("Места:")
                for i, seat in enumerate(self.seats, start= 1):
                    print(f" {i}: {seat if seat else 'свободно'}")
        
        max_speed = 80
                    
        bus = Bus(4, max_speed)
        
        bus.change_speed(60)
        
        bus.boadr("Сын маминой подруги")
        bus.boadr("Рандомный чувак")
        bus.boadr("Сидрович")
        
        bus.status()
        
        print("\nВы ходите посадит или высадить человека (1/2)")
        print("Или изменить скорость скорость? (3)")
        bus_task = int(input("Ответ: "))
        if bus_task == 1:
            print("\nИмя человека: ")
            bus_name = input("Ответ: ")
            bus.boadr(bus_name)
            bus.status()
        elif bus_task == 2:
            print("\n Имя человека: ")
            bus_name = input("Ответ: ")
            bus.exit(bus_name)
            bus.status()
        elif bus_task == 3:
            print(f"\n{bus.speed_info}")
            print(f"Максимальная скорость: {max_speed} км/ч")
            print("Изменение скорости, что бы понизить добавьте к значению минус")
            
            bus_speed = int(input("Ответ: "))
            bus.change_speed(bus_speed)
            
except ValueError as error:
    print(f"Ошибка: {type(error).__name__}.")
    print(f"Неправильный ввод.")
