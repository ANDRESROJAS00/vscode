
''''''''''
lst = [1, 2]

for v in range(2):
    lst.insert(-1, lst[v])

print(lst)

'''''''''''
'''''''''''
def func1 (a):
    return None
def func2 (a):
    return func1(a) * func1(a)
print(func2(2))
'''''''''''
'''''''''''
x = 1// 2

print(x)
'''''''''''
'''''''''''
def func(a, b):
    return b**a
print(func(b=2, 2))
'''''''''''
'''''''''''
list = [x * x for x in range (5)]
def fun(lst):
    del lst[lst[2]]
    return lst
print(fun(list))
'''''''''''
'''''''''''
x = 1
y= 2

x, y, z = x, x, y
z, y, z = x, y, z

print(x, y, z)
'''''''''''
'''''''''''
a= 1
b=0

a=a^b
b=a^b
a=a^b

print(a,b)
'''''''''''
'''''''''''
def fun(x):
    if x % 2 == 0:
        return 1
    else:
        return 2
print(fun(fun(2)))
'''''''''''
'''''''''''
nums=[1,2,3]
vals = nums
del vals[:]

print(nums)
print(vals)
'''''''''''
'''''''''''
x = int(input())
y = int(input())
x=x%y
x=x%y
y=y%x
print(y)
'''''''''''
'''''''''''
y = input()
x = input()
print(x+y)
'''''''''''
'''''''''''
print('a', 'b', 'c', sep='sep')
'''''''''''
'''''''''''
x = 1//5+1/5
print(x)
'''''''''''
'''''''''''
x = float(input())
y = float(input())

print(y **(1/x))
'''''''''''
'''''''''''
dct = {'uno':'dos', 'tres':'uno', 'dos':'tres'}
v = dct['tres']

for k in range(len(dct)):
    v = dct[v]

print(v)
'''''''''''
'''''''''''
lst = [i for i in range(-1, -2)]
print(lst)
'''''''''''
'''''''''''
def fun(a, b, c=0):

    print(fun)
'''''''''''

'''''''''''
def fun(x, y):
    if x == y:
        return x
    else:
        return fun(x, y-1)
print(fun(0, 3))
'''''''''''

'''''''''''
i = 0

while i < i + 2:
    i += i
    print('*')
else:
    print('*')
'''''''''''
'''''''''''
tup = (1, 2, 4, 8)
tup = tup[-2:-1]
tup = tup[-1]
print(tup)
'''''''''''
'''''''''''
dd = {'1':'0', '0':'1'}

for x in dd.vals():
    print(x, end='')
'''''''''''
'''''''''''
dct = {}
dct['1'] = (1, 2)
dct['2'] = (2, 1)


for x in dct.keys():
    print(dct[x][1], end='')
'''''''''''
'''''''''''
def fun(inp=2, out=3):
    return inp * out
print(fun(out=2))
'''''''''''
'''''''''''
lst = [[x for x in range(3)] for y in range(3)]


for r in range(3):
    for c in range(3):
        if lst[r][c] % 2 != 0:
            print('#')
'''''''''''
'''''''''''
import math
print(dir(math))
'''''''''''
'''''''''''
#archivo a.py

print('a', end='')

import a
print('b' , end='')

print('c', end='')
import a
import b
'''''''''''
'''''''''''
try:
    raise Exception
except:
    print('c')
except BaseException:
    print('a')
except Exception:
    print('b')
'''''''''''
'''''''''''
x = '\\\'
print(len(x))
'''''''''''
'''''''''''
print(chr(ord('p') + 2))
'''''''''''
'''''''''''
print(float('1.3'))
'''''''''''

'''''''''''
class A:
    def __init__(self, v=2):
        self.v = v

    def set(self, v=1):
        self.v += v
        return self.v
    
a = A()
b = a
b.set()
print(a.v)
'''''''''''

'''''''''''
class A:

    A = 1
    def __init__(self):
        self.a = 0

print(hasattr(A, 'a'))

'''''''''''
'''''''''''
class A:
    pass

class B(A):
    pass

class C(B):
    pass
print(issubclass(A,C))
'''''''''''

'''''''''''
class A:
    def __init__(self, v):
        self.__a = v + 1
a = A(0)
print(a.__a)
'''''''''''
'''''''''''
class A:
    def __init__(self):
        pass

a = A(1)
print(hasattr(a, 'A'))
'''''''''''
'''''''''''
class A:
    def a(self):
        print('a')
class B:
    def a(self):
        print('b')
class C(B, A):
    def c(self):
        self.a()

o = C()

o.c()
'''''''''''

'''''''''''
try:
    raise Exception(1, 2, 3)
except Exception as e:
    print(len(e.args))
'''''''''''
'''''''''''
def I(n):
    s = '+'
    for i in range(n):
        s += s
        yield s

for x in I(2):
    print(x)
'''''''''''

'''''''''''
class I:
    def __init__(self):
        self.s = 'abc'
        self.i = 0
    def __init__(self):
        return self
    def __next__(self):
        if self.i == len(self.s):
                raise StopIteration
        v = self.s[self.i]
        self.i += 1
        return v
    
for x in I():
    print(x, end='')
'''''''''''
'''''''''''
def o(p):
    def q():
        return '*' * p
    return q
r = o(1)
s = o(2)
print(r() + s())
'''''''''''

'''''''''''
def f(par2, par1):
    return par2 + par1


print(f(par2=1, 2))
'''''''''''
'''''''''''
z = 2
y=1 

x=y<z or z> y and y > z or z< y
print(x)
'''''''''''
'''''''''''
str = 'abcdef'

def fun(s):
    del s[2]
    return s
print(fun(str))
'''''''''''
'''''''''''
x,y,z=3,2,1
z,y,x=x,y,z
print(x,y,z)
'''''''''''
'''''''''''
a=True
b=False
a=a or b
b = a and b
a = a or b
print(a, b)
'''''''''''

'''''''''''
def fun(x):
    return 1 if x % 2 != 0 else 2
print(fun(fun(1)))
'''''''''''
'''''''''''
print(len((1, )))
'''''''''''
'''''''''''
d = {1:0, 2:1, 3:2, 0:1}

x = 0

for y in range (len(d)):
    x = d[x]

print(x)
'''''''''''
'''''''''''
y = input()
x = input()

print(x + y) 
'''''''''''
'''''''''''
print("a", "b", "c", sep="'")
'''''''''''
'''''''''''
v = 1 + 1 // 2 + 1 / 2 + 2
print(v)
'''''''''''
'''''''''''
t = (1, )
t = t[0] + t[0]
print(t)
'''''''''''
'''''''''''
x = 16

while x > 0:

    print('*', end='')
    x //= 2
'''''''''''
'''''''''''
d = {'uno':1, 'tres':3, 'dos':2}

for k in sorted(d.values()):
    print(k, end=' ')
'''''''''''

'''''''''''
print(len([i for i in range(0, -2)]))
'''''''''''
'''''''''''
def fun(a, b, c = 0):
    fun(a, b, c=0)

print(fun)
'''''''''''
'''''''''''
lt = [1, 2, 3, 4]

lt = list(map(lambda x: 2*x, 1))
print(lt)
'''''''''''
'''''''''''
i = 4

while i > 0:
    i -= 2
    print('*')
    if i == 2:
        break

else:
    print('*')
'''''''''''
'''''''''''
t = (1, 2, 3, 4)
t = t[-2:-1]
t = t[-1]
print(t)
'''''''''''
'''''''''''
d = {}
d['2'] = [1, 2]
d['1'] = [3, 4]
for x in d.keys():
    print(d[x][1], end = '')
'''''''''''
'''''''''''
def fun(d, k, v):

    d[k]=v
dc = {}
print(fun(dc, '1', 'v'))
'''''''''''
'''''''''''
ls = [[c for c in range (r)] for r in range (3)]
for x in ls:
    if len(x) < 2:
        print()
'''''''''''
'''''''''''
try:
    raise Exception
except BaseException:
    print("a", end='')
else:
    print("b", end='')
finally:
    print("c")
'''''''''''
'''''''''''
class A:
    def __init__(self,name):
        self.name = name
a = A("class")
print(a)
'''''''''''
'''''''''''
try:
    raise Exception
except:
    print('c')
except BaseException:
    print("a")
except Exception:
    print("b")
'''''''''''

'''''''''''
class X:
    pass
class Y(X):
    pass
class Z(Y):
    pass
x = X()
z = Z()

print(isinstance(x, Z), isinstance(z, X))
'''''''''''
'''''''''''
X = '\'
print(len(X))
'''''''''''
'''''''''''
x = """
"""

print(len(x))
'''''''''''
'''''''''''
class Class:
    def __init__(self):
        pass
        
'''''''''''
'''''''''''
class A:
    A = 1
    def __init__(self, v=2):
        self.v = v + A.A
        A.A += 1

    def set(self, v):
        self.v += v
        A.A += 1
        return
    
a = A()
a.set(2)
print(a.v)
'''''''''''
'''''''''''
class A:
    A = 1
    def __init__(self):
        self.a = 0

print(hasattr(A, 'A'))
'''''''''''
'''''''''''
class A:
    pass
class B:
    pass
class C(A,B):
    pass
print(issubclass(C, A) and issubclass(C, B))
'''''''''''
'''''''''''
class A:
    def __init__(self, v):
        self._a = v + 1

a = A(0)
print(a._a)
'''''''''''
'''''''''''
class A:
    def __init__(self):
        pass
    def f(self):
        return 1
    def g():
        return self.f()
    
a = A()
print(a.g())
'''''''''''
'''''''''''
class A:
    def a(self):
        print('a')

class B:
    def a(self):
        print('b')

class C(A, B):
    def c(self):
        self.a()

o = C()

o.c()
'''''''''''

'''''''''''
def I(n):
    s = ''
    for i in range(n):
        s += '*'
        yield s
for x in I(3):
    print(x, end='')
'''''''''''
'''''''''''
def a (x):
    def b():
        return x + x
    return b
x = a('x')
y = a('')
print(x() + y())
'''''''''''