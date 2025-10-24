import os
import shutil

def rename_file(file_path, file, file_new_name):
    
    path_one = os.path.join(file_path, file) #Исходный путь
    path_two = os.path.join(file_path, file_new_name) #Новый путь
    
    shutil.copy(path_one, path_two)

try:
    
    task = int(input("Введите номер задачи: "))
    
    if task == 1:
        
        print("\nВведите точную директорию ваших файлов")
        print("Пример: d:/Печенька") 
        data_file = input(f"Ответ: ")
        
        directory = os.chdir(data_file) # Директория
        
        print("\nВведите формат файла. (.txt, .csv и тд)")
        format_file = input(f"Ответ: ")
        
        list_files = [f for f in os.listdir() if f.endswith(format_file) and os.path.isfile(f)] # 1 перебирает все файлы в директории. 2 Ищет все файлы с таким форматом
        
        count = 0 #кол-во файлов
        
        total_size_file = 0 #Размер файлов
        
        if list_files:
            
            for count, file in enumerate(list_files, start = 1):
                print(f"{count}. {file}")
                
            print("\nТребуеться ли скопировать и переместить эти файлы в новую папку? (да/нет)")
            task_one = input("Ответ: ")
                
            if task_one.lower() == "да":
                print("\nВведите название папки")
                folder_name = input("Ответ: ")
                
                if not os.path.exists(folder_name):
                    os.mkdir(folder_name) #Создает папку, не может создавать файлы. Для создания файлов надо: with open ("""w+")
                    print(f"Папка с названием {folder_name} успешно создана")
                    
                else:
                    print(f"Так как папка {folder_name} уже существует, файлы будут скопированы туда")
                    
                for file in list_files:
                    shutil.copy(file, os.path.join(folder_name, file))#1 Исходный файл в указанной директории, 2 Путь к папке 3 окончательное имя файлан
                    
                print(f"Файлы успешно скопированы в папку {folder_name}")
                
                print(f"\nНужно ли изменить имя файла. (да/нет)")
                task_two = input("Ответ: ")
                if task_two.lower() == "да":
                    print("\nВы хотите изменить название файла в директории/дочерних папках? (1/2)")
                    task_three = int(input("Ответ: "))
                    if task_three == 1:
                        print("\nВведите полное название файла.")
                        print("Пример: name.exe")
                        name_file = input("Ответ: ")
                        if not os.path.isfile(name_file):
                            raise Exception(f"Файл {name_file} не существует.")
                        elif os.path.isfile(name_file):
                            print(("\nВведите новое полное название файла: "))
                            new_name_file = input("Ответ: ")
                            shutil.copy(name_file, new_name_file)
                        os.remove(name_file)
            else:
                print("Дальше нет пути.")
                
        else:
            print(f"Файлов с форматом {format_file} не существкет в этой директории")
            exit
        
    elif task == 2:
        print()
except (ValueError, MemoryError) as error:
    print(f"Произошла ошибка: {type(error).__name__}")
    print(f"Описание ошибки: {error}")

