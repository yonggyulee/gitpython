#global, local 심벌테이블 확인
g_a = 1
g_b = 'hello'



def f():
    l_a = 3
    l_b = '둘리'
    print(locals())

def g():
    print(g_a)

a = (1,2,3,'hello')
f()
g()


print(globals())

# 사용자 정의 함수
f.n = 'hello'
print(f.__dict__)

# 사용자 정의 클래스
class MyClass:
    def __init__(self):
        self.i = 10
        self.j = 10
    a = 10
    b = 11

MyClass.c = 12

print(MyClass.__dict__)

# 내장함수
# 내장함수는 symbol table이 없다.
# 확장을 할 수 없다.
# print.z = 12              #error
# print(print.__dict__)     #error

# 내장 클래스
# 내장함수는 symbol table이 있다.
# 확장은 할 수 없다.
print(str.__dict__)
# str.z = 15                #error

# 사용자 정의 클래스로 생성된 객체
o = MyClass()
o.k = 30
print(o.__dict__)

# 내장 클래스로 생성된 객체
#
# g_a.z = 10
# print(g_a.__dict__)