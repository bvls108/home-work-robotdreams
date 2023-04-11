from datetime import datetime
import json

try:
    file_exception = 'exception.json'
    dic = json.load(open('exception.json','r+'))

except:
    file_exception = 'exception.json'
    dic = {}
    with open(file_exception, 'w') as f:
        json.dump(dic, f)

class InvalidAgeException(Exception):
    "Raised when the input value is less than 18"
    pass

# you need to guess this number
number = 18

try:
    input_num = int(input("Enter a number: "))
    if input_num < number:
        raise InvalidAgeException
    else:
        print("Eligible to Vote")

except InvalidAgeException:
    with open(file_exception, 'r+') as f:
            exception = str(InvalidAgeException)
            current_datetime = str(datetime.now())
            file_contents = json.load(f)
            file_contents[current_datetime] = exception
            print("Дані щодо помилки або винятка (дата отримання та ім'я):")
            print(file_contents)
            with open(file_exception, 'r+') as f:
                json.dump(file_contents, f)