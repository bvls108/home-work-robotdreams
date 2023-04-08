import json

dic = {"Ann" : 1111, "Paul" : 2222, "Andrew": 3333}

call = {}

file_calling = 'func_callings.json'

filename = 'phonebook.json'

with open(filename, 'w') as f:
    json.dump(dic, f)

with open(file_calling, 'w') as f2:
    json.dump(call, f2)

def decotator_to_func(func):
    from datetime import datetime
    func_name = str(func)
    current_datetime = str(datetime.now())
    with open(file_calling, 'r+') as f:
        file_contents = json.load(f)
        file_contents[current_datetime] = func_name
        print("Дані щодо виконаних функції (дата виконання та ім'я функції):")
        print(file_contents)
        with open(file_calling, 'r+') as f:
            json.dump(file_contents, f)
    return func

while True:

    key = input("Введіть команду (stats, add, delete, list, show): ")

    if key == "stats":
        @decotator_to_func
        def stats(dic):
            with open(filename, 'r') as f:
                file_contents = json.load(f)
                print(len(file_contents))
        print("Кількість записів у телефонній книзі:")
        stats(dic)

    if key == "add":
        @decotator_to_func
        def add(key, value):
            with open(filename, 'r+') as f:
                file_contents = json.load(f)
                file_contents[key] = value
                print("Нові дані записано. Нова телефонна книга:")
                print(file_contents)
                with open(filename, 'w') as f:
                    json.dump(file_contents, f)
        name = input("Введіть ім'я нового контакту:")
        while name in dic:
            print("Дане ім'я контакту вже існує.")
            name = input("Дане ім'я контакту вже існує. Введіть нове ім'я контакту або введіть команду stop для введення нової команди")

        if name == "stop":
            continue

        else:
            number = input("Нове ім'я контакту записано. Введіть номер нового контакту:")
            add(name, number)

    if key == "delete":
        @decotator_to_func
        def delete(key):
            with open(filename, 'r+') as f:
                file_contents = json.load(f)
                del file_contents[key]
                print(f"Видалено контакт: {name_d}")
                print("Нова телефонна книга:")
                print(file_contents)
                with open(filename, 'w') as f:
                    json.dump(file_contents, f)
        name_d = input("Введіть ім'я контакту для видалення:")
        with open(filename, 'r') as f:
            file_contents = json.load(f)
        while name_d not in file_contents:
            print("Ім'я контакту не існує")
            name_d = input("Ім'я контакту не існує. Введіть ім'я контакту для видалення або введіть команду stop для введення нової команди")

        if name_d == "stop":
            continue

        else:
            delete(name_d)

    if key == "list":
        @decotator_to_func
        def list_f():
            with open(filename, 'r') as f:
                file_contents = json.load(f)
                print(file_contents.keys())
        print("Cписок всіх імен в книзі:")
        list_f()

    if key == "show":
        @decotator_to_func
        def show(key):
            with open(filename, 'r') as f:
                file_contents = json.load(f)
                print("Інформація за іменем:")
                print(file_contents[key])
        name_show = input("Введіть ім'я за яким має бути виведена детальна інформація:")
        with open(filename, 'r') as f:
            file_contents = json.load(f)
        while name_show not in file_contents:
            print("Ім'я контакту не існує")
            name_show = input("Ім'я контакту не існує. Введіть існуюче ім'я контакту для виведенгня інфо або введіть команду stop для введення нової команди")

        if name_show == "stop":
            continue

        else:
            show(name_show)