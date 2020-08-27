#일반적으로 피연산자(operand)는 True 또는 False 값을 가지는 연산
a = 20
print(not a < 20)
print(a < 30 and a !=30)

b = a > 1

# 다른 타입의 객체도 bool 타입으로 형변환이 가능하다
print(bool(10), bool(0))
print(bool(3.14), bool(0.))
print(bool('hello'), bool(''))
print(bool([0,1]), bool([]))
print(bool((0,1)), bool(()))
print(bool({'k1':'v1', 'k2':'v2', 'k3':'v3'}), bool({}))
print(bool(None))

# 논리식의 계산순서
t = True or bool('logical')
print(t)
print(True or 'logical')
print(False or 'logical')
print([] or 'logical')
print([] and 'logical')
print([0,1] or 'logical')

def f():
    print('hello world')
a = 11
a > 10 or f()

if a > 10:
    f()

s1 = ''
s = 'Hello World'
s1 and print(s)