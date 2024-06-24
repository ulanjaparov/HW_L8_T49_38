#CW_L8_T49_38

# Задача №49. Решение в группах
# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt. Фамилия, имя, отчество, 
# номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи(Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

# Задача 38: Дополнить телефонный справочник возможностью изменения и удаления данных.
# Пользователь также может ввести имя или фамилию, и Вы должны реализовать функционал для изменения и удаления данных.

def menu():
    print("Телефонный справочник")
    print("1. Вывести все записи")
    print("2. Добавить новую запись")
    print("3. Найти запись")
    print("4. Изменить запись")
    print("5. Удалить запись")
    print("6. Сохранить данные в файл")
    print("7. Загрузить данные из файла")
    print("8. Выход")
    choice = input("Введите номер операции: ")
    return choice

def load_data(file_name):
    try:
        with open(file_name, 'r', encoding='utf-8') as file:
            records = []
            for line in file:
                surname, name, patronymic, phone = line.strip().split(',')
                record = {'Фамилия': surname, 'Имя': name, 'Отчество': patronymic, 'Телефон': phone}
                records.append(record)
        return records
    except FileNotFoundError:
        print(f"Файл '{file_name}' не найден.")
        return []

def save_data(records, file_name):
    with open(file_name, 'w', encoding='utf-8') as file:
        for record in records:
            line = ','.join([record['Фамилия'], record['Имя'], record['Отчество'], record['Телефон']])
            file.write(line + '\n')
    print(f"Данные сохранены в файл '{file_name}'.")

def print_records(records):
    if not records:
        print("Справочник пуст.")
    else:
        for idx, record in enumerate(records, start=1):
            print(f"{idx}. {record['Фамилия']} {record['Имя']} {record['Отчество']}, Телефон: {record['Телефон']}")

def search_record(records, key, value):
    found_records = []
    for record in records:
        if record[key] == value:
            found_records.append(record)
    return found_records

def add_record(records, record):
    records.append(record)
    print("Запись добавлена.")

def update_record(records, key, value):
    for record in records:
        if record[key] == value:
            print(f"Текущие данные: {record}")
            new_phone = input("Введите новый номер телефона: ")
            record['Телефон'] = new_phone
            print("Данные обновлены.")

def delete_record(records, key, value):
    for record in records[:]:  # Используем срез для безопасного удаления во время итерации
        if record[key] == value:
            records.remove(record)
            print("Запись удалена.")

def main():
    file_name = 'phonebook.txt'
    records = load_data(file_name)
    
    while True:
        choice = menu()
        
        if choice == '1':  # Вывести все записи
            print_records(records)
        
        elif choice == '2':  # Добавить новую запись
            surname = input("Введите фамилию: ")
            name = input("Введите имя: ")
            patronymic = input("Введите отчество: ")
            phone = input("Введите номер телефона: ")
            new_record = {'Фамилия': surname, 'Имя': name, 'Отчество': patronymic, 'Телефон': phone}
            add_record(records, new_record)
        
        elif choice == '3':  # Найти запись
            search_key = input("Введите характеристику для поиска (Фамилия, Имя, Отчество или Телефон): ").capitalize()
            search_value = input(f"Введите значение для характеристики '{search_key}': ")
            found_records = search_record(records, search_key, search_value)
            print_records(found_records)
        
        elif choice == '4':  # Изменить запись
            search_key = input("Введите характеристику для поиска (Фамилия, Имя, Отчество или Телефон): ").capitalize()
            search_value = input(f"Введите значение для характеристики '{search_key}': ")
            update_record(records, search_key, search_value)
        
        elif choice == '5':  # Удалить запись
            search_key = input("Введите характеристику для поиска (Фамилия, Имя, Отчество или Телефон): ").capitalize()
            search_value = input(f"Введите значение для характеристики '{search_key}': ")
            delete_record(records, search_key, search_value)
        
        elif choice == '6':  # Сохранить данные в файл
            save_data(records, file_name)
        
        elif choice == '7':  # Загрузить данные из файла
            records = load_data(file_name)
        
        elif choice == '8':  # Выход
            print("Работа завершена.")
            break
        
        else:
            print("Некорректный выбор. Попробуйте еще раз.")

if __name__ == "__main__":
    main()