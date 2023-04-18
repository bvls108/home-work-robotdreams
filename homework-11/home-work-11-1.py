
def decotator_to_func(func):
    def deco_func(*args, **kwargs):
        print(f'Назва функції - {func}')
        result = func(*args, **kwargs)
        from datetime import datetime
        current_datetime = datetime.now()
        print(f"Час виконання функції - {current_datetime}")
        return result
    return deco_func

@decotator_to_func
def hello_world():
    print('Hello world!')

hello_world()