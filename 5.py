import random
var = 1

switch = [1,2,3,4,5,6]
numbers = list(range(-10, 10))

for i in range(1,21):
    switching = random.choice(switch)

    if switching == 1:
        random.shuffle(numbers)
        print(f'Чи більша змінна за вибране число, яким є число {numbers[0]}?.')
        try1 = var > numbers[0]
        print(try1)
        if try1 == True:
            print ("Змінна справді більша за вибране число")
        else:
            print ("Змінна не є більша за вибране число")
        print('----------')


    if switching == 2:
        random.shuffle(numbers)
        print(f'Чи менша змінна за вибране число, яким є число {numbers[0]}?.')
        try2 = var < numbers[0]
        print(try2)
        if try2 == True:
            print ("Змінна справді менша за вибране число")
        else:
            print ("Змінна не є менша за вибране число")
        print('----------')

    if switching == 3:
        random.shuffle(numbers)
        print(f'Чи змінна більша або дорівнює вибраному числу, яким є число {numbers[0]}?.')
        try3 = var >= numbers[0]
        print(try3)
        if try3 == True:
            print ("Змінна справді більша або дорівнює вибраному числу")
        else:
            print ("Змінна не є більша і не дорівнює вибраному числу")
        print('----------')


    if switching == 4:
        random.shuffle(numbers)
        print(f'Чи змінна менша або дорівнює вибраному числу, яким є число {numbers[0]}?.')
        try4 = var <= numbers[0]
        print(try4)
        if try4 == True:
            print ("Змінна справді менша або дорівнює вибраному числу")
        else:
            print ("Змінна не є менша і не дорівнює вибраному числу")
        print('----------')


    if switching == 5:
        random.shuffle(numbers)
        print(f'Чи змінна не дорівнює вибраному числу, яким є число {numbers[0]}?.')
        try5 = var != numbers[0]
        print(try5)
        if try5 == True:
            print ("Змінна справді не дорівнює вибраному числу")
        else:
            print ("Змінна насправді дорівнює вибраному числу")
        print('----------')


    if switching == 6:
        random.shuffle(numbers)
        print(f'Чи змінна дорівнює вибраному числу, яким є число {numbers[0]}?.')
        try6 = var == numbers[0]
        print(try6)
        if try6 == True:
            print ("Змінна справді дорівнює вибраному числу")
        else:
            print ("Змінна насправді не дорівнює вибраному числу")
        print('----------')

