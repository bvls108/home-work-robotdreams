
class CtxManager:
    def __enter__(self):
        print('==========')

    def __exit__(self, type, value, traceback):
        print('==========')


with CtxManager():
    print(f'Hello!')