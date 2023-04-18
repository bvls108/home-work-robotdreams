
class CtxManager:
    def __enter__(self):
        print('==========')

    def __exit__(self, type, value, traceback):
        if value:
            print(value)
        print('==========')
        return True


with CtxManager():
    print(f'Hello!')