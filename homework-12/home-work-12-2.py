from datetime import datetime
import json

try:
    file_calling = 'func_callings.json'
    dic = json.load(open('func_callings.json','r+'))

except:
    file_calling = 'func_callings.json'
    dic = {}
    with open(file_calling, 'w') as f:
        json.dump(dic, f)

def decotator_to_func(func):
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

@decotator_to_func
def say_hello():
    print("Hello!")

say_hello()