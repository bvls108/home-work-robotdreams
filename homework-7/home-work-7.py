phonebook = {"Ганна" : 1111, "Марина" : 2222, "Віктор": 3333}

dic = phonebook

def amount(dic):
    print(len(dic))

def add(key, value):
    dic[key] = value
    print(dic)

def delete(key):
    del dic[key]
    print(dic)

def list_f():
    print(dic.keys())

def show(key):
    print(dic[key])

amount(dic)
add("Микола", 5555)
delete("Марина")
list_f()
show("Віктор")