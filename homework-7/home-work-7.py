
dic = {"Ганна" : 1111, "Марина" : 2222, "Віктор": 3333}


def amount(dic):
    print(len(dic))

def add(key, value):
    dic[key] = value
    print("Нові дані записано. Нова телефонна книга:")
    print(dic)

def delete(key):
    del dic[key]


def list_f():
    print(dic.keys())

def show(key):
    print("Інформація за іменем:")
    print(dic[key])

while True:

    key = input("Введіть команду (stats, add, delete, list, show): ")

    if key == "stats":
        print("Кількість записів у телефонній книзі:")
        amount(dic)

    if key == "add":
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
        name_d = input("Введіть ім'я контакту для видалення:")
        while name_d not in dic:
            print("Ім'я контакту не існує")
            name_d = input("Ім'я контакту не існує. Введіть ім'я контакту для видалення або введіть команду stop для введення нової команди")

        if name == "stop":
            continue

        else:
            delete(name_d)
            print(f"Видалено контакт: {name_d}")
            print("Нова телефонна книга:")
            print(dic)

    if key == "list":
        print("Cписок всіх імен в книзі:")
        list_f()

    if key == "show":
        name_show = input("Введіть ім'я за яким має бути виведена детальна інформація:")
        while name_show not in dic:
            print("Ім'я контакту не існує")
            name_show = input("Ім'я контакту не існує. Введіть існуюче ім'я контакту для виведенгня інфо або введіть команду stop для введення нової команди")

        if name == "stop":
            continue

        else:
            show(name_show)







