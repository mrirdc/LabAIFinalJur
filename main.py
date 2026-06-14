def my_fun(arg1,*argv):
    print("first argument:",arg1)
    for arg in argv:
        print("next argument through *argv:",arg)


my_fun('hello','welcome','to','python')


def my_func(**kwargs):
    for key, value in kwargs.items():
        print("%s==%s"% (key,value))

my_func(first='B', mid='to',last='C')


fib=lambda n:n if n<=1 else fib(n-1)+fib(n-2)
result=fib(10)
print(result)

def fib(n):
    if n <= 1:
        return n
    return fib(n-1) + fib(n-2)

print(fib(10))


def fun(variable):
    letters=['a','e','i','o','u']
    if variable in letters:
        return True
    else:
        return False


sequence=['g','e','e','j','k','s','p','r']
filtered=filter(fun,sequence)
print('the filtered letters are:')
for s in filtered:
    print(s)

