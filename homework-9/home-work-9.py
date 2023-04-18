a = int(input('Введіть яке саме число із послідовності Фібоначі треба вивести: '))

def fib(n):
    a, b = 1, 1
    for i in range(n):
        yield a
        a, b = b, a + b

l = list(fib(a))

print(l[a-1])