import os
import shutil

try:
    
    task = int(input("Введите номер задачи: "))
    
    if task == 1:
        
        print("\nВведите точную директорию ваших файлов")
        print("Пример: d:/Печенька") 
        data_file = input(f"Ответ: ")
        
        os.chdir(data_file)
        
        print("\nВведите формат файла. (.txt, .csv и тд)")
        format_file = input(f"Ответ: ")
        
        list_files = [f for f in os.listdir() if f.endswith(format_file) and os.path.isfile(f)]
        
        count = 0
        
        if list_files:
            
            for count, file in enumerate(list_files, start = 1):
                print(f"{count}. {file}")
                
            print("\nТребуеться ли скопировать и переместить эти файлы в новую папку? (да/нет)")
            task_one = input("Ответ: ")
                
            if task_one.lower() == "да":
                print("\nВведите название папки")
                folder_name = input("Ответ: ")
                
                if not os.path.exists(folder_name):
                    os.mkdir(folder_name)
                    print(f"Папка с названием {folder_name} успешно создана")
                else:
                    print(f"Так как папка {folder_name} уже существует, файлы будут скопированы туда")
                    
                for file in list_files:
                    shutil.copy(file, os.path.join(folder_name, file))
                print(f"Файлы успешно скопированы в папку {folder_name}")
                
        else:
            print(f"Файлов с форматом {format_file} не существкет в этой директории")
            exit
        
    elif task == 2:
        print()
except (ValueError, MemoryError) as error:
    print(f"Произошла ошибка: {type(error).__name__}")
    print(f"Описание ошибки: {error}")