import math
from colorama import init, Fore, Style
import random

#Печеньки любите?

readln = {
   
   "1" : ["Вы выбрали задачу №1"],
   "2" : ["Вы выбрали задачу №2"],
   "3" : ["Вы выбрали задачу №3"],
   "4" : ["Вы выбрали задачу №4"],
   "5" : ["Вы выбрали задачу №5"]
}

char = len(readln.keys())

try:
   print(Fore.GREEN + "Доступное количество задач: " + str(char) + Style.RESET_ALL)
   task = int(input(Fore.YELLOW + "Введите какую задачу хотите выбрать: " + Style.RESET_ALL))

   if task == 1:
      
      print(readln["1"][0])
      
      a = float(input("Введите значение a: "))
      b = float(input("Введите значение b: "))
      x = float(input("Введите значение x: "))

      a_char = (a**2 / 3) + ((a**2 + 4) / b) + math.sqrt(4 * (math.sqrt(a**2 + 4))**4)

      b_char = math.cos(x) + math.sin(x)

      c_char = math.pow(math.cos(2 * x), 2)**(1/3) + math.sin(2 * x - 1)**2

      d_char = 5 * x + 3 * x**2 + math.sqrt(1 + math.sin(x)**2)

      print("Результаты вычислений: ")
      print("Вывод a: ", a_char)
      print("Вывод b: ", b_char)
      print("Вывод c: ", c_char)
      print("Вывод d: ", d_char)
   
   elif task == 2:
      
      print(readln["2"][0])
      
      s_char = float(input("Введите сумму кредита: "))
      i_char = float(input("Введите годовую процентную ставку : "))
      n_char = int(input("Введите срок кредита в месяцах : "))

      #100 - перевод в проценты
      #12 - месячная оплата

      p_char = i_char / 100 / 12
      
      #Вывод по формуле
      
      m_char = (s_char * p_char * (1 + p_char) ** n_char) / ((1 + p_char) ** n_char - 1)
      
      total_pyment_m_n = m_char * n_char #Годовая оплата
      
      overpayment_t_s = total_pyment_m_n - s_char #Переплата, теперь ты должен печеньки)
      
      print(Fore.GREEN + f"Ежемесячный платёж: {str(round(m_char, 2))} Бел. руб" + Style.RESET_ALL)
      print(Fore.GREEN + f"Годовая оплата: {str(round(total_pyment_m_n, 2))} Бел. руб" + Style.RESET_ALL)
      print(Fore.GREEN + f"Годовая переплата: {str(round(overpayment_t_s, 2))} Бел. руб" + Style.RESET_ALL)
      
      print("Сколько хотите дать печенек?")
      
      cookie = float(input("Кол-во печенек: "))
      
      if cookie == 1:
         print(Fore.GREEN + f"Спасибо за печеньку :)" + Style.RESET_ALL)
         
      elif cookie >= 10:
         print(Fore.GREEN + f"ПЕЧЕНЬКИИИИИИИИ! :3" + Style.RESET_ALL)
         
      elif cookie >= 2 == 9:
         print(Fore.GREEN + f"Спасибо за печеньки :3"  + Style.RESET_ALL)
         
      else:
         print(Fore.RED + f"Где печеньки!" + Style.RESET_ALL)
         
   elif task == 3:
      
      print(readln["3"][0])
      
      count_try = 0
      
      pi = 3.14
      
      while True:
      
         r = float(input("Введите радиус орбиты планеты (млн. км.): "))
         v = float(input("Орбитальная скорость (км/ч): "))
         
         count_try += 1
         
         resoult = round((2*r*pi)/ v, 2) #Формула
         
         if count_try == 1:
            
            l_one = resoult
            l_one_name = "У первой планеты длинее год"
            
            print(f"Длина года на планете: {l_one}")
         elif count_try == 2:
            
            l_two = resoult
            l_two_name = "У первой планеты длинее год"
            
            print(f"Длина года на планете: {l_two}")
         else:
            print("STOP!")
         
            
         again_try = input("Повторить ввод? (да/вывод): ").lower()
         
         if again_try != "да":
            if "l_two" not in locals():
               
               print(f"Введена только одна планета.")
               print(f"Длина года: {l_one}")
               
            else:
               if l_one >= l_two:
                  print(l_one_name)
               else:
                  print(l_two_name)
            break
         
   elif task == 4:
      
      print(readln["4"][0])
      
      place = {
         
         "Школа" : ["Тут ограничение до 5 км/ч", 5],
         "Двор" : ["Тут ограничение до 20 км/ч", 20],
         
      }
      
      char_place = len(place.keys())
      
      user_speed = float(input("Введите скорость: "))
      
      print(f"Доступное количество мест: {str(char_place)}")
      print(f"Название мест: {list(place.keys())}")
      
      user_place = int(input("Введите место езды: "))
      
      if user_place == 1:
         
         print(place["Школа"][0])
         if user_speed <= place["Школа"][1]:
            print(f"Соблюдение скоростного режима.")
            
         elif user_speed >= place ["Школа"][1] * 2:
            print(f"Лишение прав + штраф!")
            
         elif user_speed >= place ["Школа"][1]:
            print(f"Штраф!")   
            
      elif user_place == 2:
         
         print(place["Двор"][0])
         
         if user_speed <= place["Двор"][1]:
            print(f"Соблюдение скоростного режима.")
            
         elif user_speed >= place ["Двор"][1] * 2:
            print(f"Лишение прав + штраф!")
            
         elif user_speed >= place ["Двор"][1]:
            print(f"Штраф!")
            
   elif task == 5:
      
      shop_list = {
         
         "Milk" : "Eat",
         "Hot-dog" : "Eat",
         "Cookie" : "Eat",
         "Toy" : "Other",
         "Book" : "Other",
         "TV" : "Other",
         
      }
      
      def can_return_list(item, days):
            category_list = shop_list.get(item)
         
            if category_list == "Eat":
               return "Еда возврату не подлежит, ОСОБЕННО ПОСРОЧКА!"
            if days <= 14:
               return "Товар можно вернуть бесплатно :3"
            elif days <= 30:
               return "Плати деньги, если хочешь вернуть!"
            else:
               return "Потрачено!"
      
      print("Консультант: Есть ли у вас чек на товар?")
      cheack = input("Проверить наличие чека? (да/нет): ")
      cheack_list = random.choices([True, False], weights=[0.7, 0.2])[0]
      
      #забыл у lower добавить скобки и 5 минут парился почему посстоянно выдает False
      if cheack_list == True and cheack.lower() == "да":
         print("Вы нашли чек.")
         
         print("Товары в чеке.")
            
         for name in shop_list :
            print("-", name)

         item = input("Название товара который требуется вернуть: ")
         days = int(input("Сколько дней прошло с покупки? "))
            
         resoult_list = can_return_list(item, days)
         print("Консультант: ", resoult_list)

      else:
         print("Вы не нашли чек.")
         print("Консультант: Без чека возврат не делаем.")
           
except ValueError:
   print("Мисье, тут все некоректно, давай по новой!")
   
