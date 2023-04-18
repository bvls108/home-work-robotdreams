import json

try:
    filename = 'phonebook.json'
    dic = json.load(open('phonebook.json','r+'))

except:
    filename = 'phonebook.json'
    dic = {"Ann" : 1111, "Paul" : 2222, "Andrew": 3333}
    with open(filename, 'w') as f:
        json.dump(dic, f)

def stats():
    with open(filename, 'r+') as f:
        file_contents = json.load(f)
        print(len(file_contents))
    print("Кількість записів у телефонній книзі:")

def add(key, value):
    with open(filename, 'r+') as f:
        file_contents = json.load(f)
        file_contents[key] = value
        print("Нові дані записано. Нова телефонна книга:")
        print(file_contents)
        with open(filename, 'w') as f:
            json.dump(file_contents, f)

def delete(key):
    with open(filename, 'r+') as f:
        file_contents = json.load(f)
        del file_contents[key]
        print(f"Видалено контакт: {name_d}")
        print("Нова телефонна книга:")
        print(file_contents)
        with open(filename, 'w') as f:
            json.dump(file_contents, f)

def list_f():
    with open(filename, 'r') as f:
        file_contents = json.load(f)
        print("Cписок всіх імен в книзі:")
        print(file_contents.keys())

def show(key):
    with open(filename, 'r') as f:
        file_contents = json.load(f)
        print("Інформація за іменем:")
        print(file_contents[key])

while True:

    key = input("Введіть команду (stats, add, delete, list, show): ")

    if key == "stats":
        stats()

    if key == "add":
        name = input("Введіть ім'я нового контакту:")
        if name in dic:
            print("Дане ім'я контакту вже існує.")
            name = input("Дане ім'я контакту вже існує. Введіть нове ім'я контакту або введіть команду stop для введення нової команди")

        elif name == "stop":
            continue

        else:
            number = input("Нове ім'я контакту записано. Введіть номер нового контакту:")
            add(name, number)

    if key == "delete":
        name_d = input("Введіть ім'я контакту для видалення:")
        with open(filename, 'r') as f:
            file_contents = json.load(f)
        if name_d not in file_contents:
            print("Ім'я контакту не існує")
            name_d = input("Ім'я контакту не існує. Введіть ім'я контакту для видалення або введіть команду stop для введення нової команди")

        elif name_d == "stop":
            continue

        else:
            delete(name_d)

    if key == "list":
        list_f()

    if key == "show":
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