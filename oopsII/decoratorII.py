def outer(func):
    def inner ():
        print('login')
        func()
        print('logout')
    return inner
@outer
def task():
    print('like')
task()
#program successfully executed