#global, local 심벌테이블 확인
g_a = 1
g_b = 'hello'



def f():
    print(g_a)
    l_a = 3
    l_b = '둘리'
    print(locals())

def g():
    print(g_a)

f()
g()
print(globals())