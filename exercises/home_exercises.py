L = ['aa']
L.extend('bb')
print(L)

str = 'A'
n = 10
print(f'{str = } \n{n = }')
print(f'{n % 2 = }')

n = [4, 1]
print(sorted(n))
print(n)
print(n.sort())
print(n)

print(*['* ' * i for i in range(2)],
      *['* ' * i for i in range(2, 0, -1)], sep='\n')

print(20 + -+20)


class C: ...


print(C.__class__)

# Разделяем строку на слова
s = 'Py thon'.split()
print(s)  # ['Py', 'thon']

# Создаем список длин слов
L = [len(w) for w in s]
print(L)  # [2, 4]

# Создаем словарь из слов и их длин
d = dict(zip(s, L))
print(d)  # {'Py': 2, 'thon': 4}

# Печатаем каждую пару ключ-значение из словаря
for k, v in d.items():
    print(k, v)
    # Py 2
    # thon 4

L = [3, 1]
print(L)
n = L, L.sort()
print(n)


class A: pass


A.num = 1
ob = A()
print(ob.num)


class C1:
    def f(self, v):
        self.d = v

    def ff(self):
        print(self.d)


class C2(C1):
    def ff(self):
        print(self.d, '.')


n = C1()
m = C2()

n.f('A')
m.f(1)

m.ff()
n.ff()

n = 'a1_b2_c3'
d = []
c = []
symbols = []
for i in list(n):
    if i.isdigit():
        d.append(i)
    elif i.isalpha():
        c.append(i)
    else:
        symbols.append(i)
print(''.join(d))
print(''.join(c))
print(''.join(symbols))

L1 = [1, 3, 5, 6]
L2 = [2, 3, 4, 6]
L3 = list(set(L1) & set(L2))
print(L3)


class A:
    def f(self):
        return self.ff()

    def ff(self):
        return 'a'


class B(A):
    def ff(self):
        return 'b'


ob_1 = A()
ob_2 = B()

print(ob_1.ff(), ob_2.ff())


class Text:
    def str(self, s):
        self.s = s

    s = 'ccaa'


t = Text()
t.str('aacc')
print(Text.s)
print(t.str)


class A:
    def f(self, n):
        self.n = 10
        n = 12


a = A()
a.f(11)
print(a.n)


# class A:
#     ...
# a = A()
# a.n = 10
# print(A.n)

class A:
    n = 1


class B(A):
    n = 2


a = B()
a.n = 3
b = B()
print(a.n, b.n)


class A:
    n = 10


x = A()
print(x.n)
A.n = 11
print(x.n, A.n)
x.n = 20
print(x.n, A.n)


class A:
    def __init__(self):
        a = 1
        self.a = 5

    def f(self, b):
        self.a = b
        a = 4


n = A()
n.f(2)

print(n.a)


class A:
    def __init__(self):
        self.n = 10

    def f(self, m):
        n = m


a = A()
a.f(11)
print(a.n)

L1 = [1, 4]
L2 = [5, 4]
L3 = [n + m for n, m in zip(L1, L2)]
print(L3)
print('###')
# {*()} return set()
print('@@@')

# s = 'a\nb\c'
# print(len(s))

m = print
m('jopa')


def f(L):
    n = len(L) != len(set(L))
    return n


print(f([1, 2]))
print(f([1, 2, 2, 4]))

t = (0, True, False)
n = all(t)
print(n)


class A:
    n = 10


class B(A):
    pass


class C(A):
    pass


B.n = 11
print(A.n, B.n, C.n)

print(len(''.split()))
print(len(''.split(' ')))


class A:
    n = 10


class B(A):
    pass


print(B.n)


class A:
    def __init__(self, n):
        self.n = n
        n = 10


m = A(11)
print(m.n)

L = [1]
L.append(L)
print(L)

L = ['ab']
print(dict(L))

# t = (1, [2])
# t[1].append(3)
# print(t)
# t[0].append(0)
# print(t)
# (1, [2, 3])
# t[0].append(0)
#     ^^^^^^^^^^^
# AttributeError: 'int' object has no attribute 'append'

L = ['a', 'b']
for i in L:
    if i == 'c':
        print(i)
        break
    else:
        print(i)

n = {x: x * x for x in range(1, 3)}
print(n)

print('###############################################################')
surprise = ['a', 'b' 'c']
print(surprise)
print('###############################################################')


def f_1(n):
    return n.upper()


print(f_1('j'))
f_2 = f_1
del f_1
print(f_2('k'))
print('###############################################################')
x = ['x', 'x']
x = [x + x for x in x]
print(x)
print('###############################################################')
List1 = [1, 2]
L2 = [3, 4, 5]
for a, b in zip(List1, L2):
    print(a, b)
print('###############################################################')
d = {'a': 1}
print(list(d.items()))
print('###############################################################')
t = [(1, 2), (3, 4)]
for (a, b) in t:
    print(a, b)
print('###############################################################')
L = ['A', 'B']
for n, m in enumerate(L):
    print(f'{m}-{n}')
print('##############################################################')
n = "10"
m = n.isnumeric()
print(m)
print('###############################################################')
m = ['a', 'b', 'c'][1]
print(m)
print('###############################################################')
a = ['a', 'b']
b = ['b', 'a']
n = {'a': 1, 'b': 2}
m = {'b': 2, 'a': 1}
print(a == b)
print(n == m)
print('###############################################################')


def f(n):
    n = 10


n = 9
print(f(n))
print('###############################################################')


def f(n):
    n = 10
    return n


n = 9
f(n)
print(n)
print('###############################################################')


def f(n):
    n = 10


n = 9
f(n)
print(n)
print('###############################################################')


def f(n, L):
    n = 21
    L[1] = 'a'


n = 1
L = ['a', 'b', 'b']

f(n, L)
print(n, L)
print('###############################################################')
n = 77


def f():
    global n
    n += 3
    return n


print(f())
print('###############################################################')
# L = [1, 2]
# def f():
#     L += 3
#
# print(f())
#  L += 3
#     ^
# UnboundLocalError: cannot access local variable 'L' where it is not associated with a value
#
# Process finished with exit code 1
L = [1, 2]


def f():
    global L
    L += [3]


f()
print(L)  # Выведет: [1, 2, 3]

print('###############################################################')
d = {'a': 1, '!': 0}
for k in d:
    print(k, d[k])

print('###############################################################')
d = {'a': 1}
for k in d:
    print(d[k])
print('###############################################################')
print('Python', end='')
print('Coder')
print('###############################################################')
L1 = [1, 2]
L2 = [3, 4]
L3, L4 = L1[:], L2
del L2[0:1]
del L3[1]
del L1[:]
print(L1, L2, L3, L4)
print('###############################################################')


def f(L):
    return list(filter(None, L))


L = [0, 1, 2, '', None]
print(f(L))
print('###############################################################')


def f(a=[]):
    print(a)
    a.append('a')


f()
print('###############################################################')
t = ('code')
for c in t:
    print(c)
print('###############################################################')
print([] == [])
print([] is [])
print('###############################################################')
r = 3
for i in range(3):
    for c in range(r - i):
        print('*', end='')
    print()
print('###############################################################')
L = [1, 2, 'a', 'b', 3]
count = 0
for i in L:
    if type(i) == int:
        continue
    count += 1
print(count)
print('###############################################################')
for _ in 'python coder':
    pass
print(_)
print('###############################################################')
print(*range(1, 4))
print('###############################################################')


def f(r):
    for i in range(r):
        n = ' ' * (r - i - 1) + '*' * (2 * i + 1)
        print(n)


f(3)
print('###############################################################')


def f(n, r=[]):
    r.append(n)
    print(r)


f('a')
f('b')
print('###############################################################')


def f(*n):
    print(n)


f([3], [3])
print('###############################################################')
print(1 == 1.0)
print(1.0 == 01.00)
print(not not not not True)
print('###############################################################')


def f(n):
    if n == None:
        print([])
    else:
        print(())


f(())
print('###############################################################')
n = None


def fn(n):
    if n is None:
        print('-> None')
    elif n:
        print('-> True')
    else:
        print('-> False')


fn(n)
print('###############################################################')
for n in range(2, -1, -1):
    print(n, end='')
print('###############################################################')
a = [1]
b = a
c = b
c.insert(1, 0)
print(c)
print(a)

print('###############################################################')


def f():
    s = 'Coder'


s = f()
print(s)

print('###############################################################')
a = [1, 2]
b = a
a.clear()
print(b)
print('###############################################################')
n = [1, 3, 2]
n.reverse()
print(n)
print('###############################################################')


def process_user_info(**user_info):
    print(user_info)


process_user_info(name='Alice', age=30, city='New York')
process_user_info(name='Ariya', age=5, city='Rishon LeZion')

print('###############################################################')


def f(**a):
    print(a)


f(a=1, b=2, c=4, d='kaka')
print('**###############################################################')


def f(*a):
    print(a)


f(a)
f(0, 1, 2, 4, 'kaka')
print('*###############################################################')


def f(**a):
    print(a)


f()
print('**###############################################################')
# def f(a, *b, c):
#     print(a, b, c)
# f(1, 2, 3)
# print('###############################################################')
# print('###############################################################')
# print('###############################################################')
# print('###############################################################')
# print('###############################################################')
# print('###############################################################')
# print('###############################################################')
# print('###############################################################')
# print('###############################################################')
# print('###############################################################')
# print('###############################################################')
# print('###############################################################')
# print('###############################################################')
# print('###############################################################')
# print('###############################################################')
# print('###############################################################')
# print('###############################################################')
# print('###############################################################')
# print('###############################################################')
# print('###############################################################')
# print('###############################################################')
# print('###############################################################')
