# Day_13_05_PythonDecorator.py


def f_7(a, b):
    return a + b, a * b     # pack


def f_8(*args):             # pack, 가변 매개 변수
    # print(args, type(args))
    print(*args)            # itertools.chain()


f_8()
f_8(1)
f_8(1, 2)
f_8(1, 2, 'hello')

print([1, 3, 5])
print(*[1, 3, 5])
print(1, 3, 5)


