# 기본 인수값
def incr(a, b = 1):
    return a + b

# 오류
# def incr(a=1, b):
#       return a+b


print(incr(10))
print(incr(10,5))
print(incr(10, b=5))

print('====키워드 인수====')
def area_rect(width, height):
    return width*height

print(area_rect(10, 20))
print(area_rect(width=10, height=20))
print(area_rect(height=20, width=10))
#print(area_rect(width=10, 20))

print('====가변 인수====')
def vargs(a, *args):
    print(a, args)

vargs(10)
vargs(10, 20, 30)

def _print(*args, sep=' ', end='newline'):
    for c in args:
        print(c, end='')
        print(sep, end='')
    print(end=end)

_print(10)
_print(10,20,30,end='\t')
_print(10,20,30,end='\n')
_print(10,20,30,sep=':',end='\t')
print(10,20,30,sep=':')

# 정의되지 않은 키워드 인수 처리하기
def area(width, height, **args):
    print(width, height)
    print(args)


area(10, 20)
area(10, 20, depth=10,dimension=10)
# 에러
# area(10,20, depth=10, 3)

def g(a, b, *args, **kw):
    print(a, b)
    print(args)
    print(kw)

g(10, 20)
g(10, 20, 30)
g(10, 20, c=60)
g(10, 20, 30, 40, 50, c=60, d=70)

def f(a):
    return a*a


print('==튜플/사전 파라미터==')
def h(name, age, height):
    print(name, age, height)

name = '둘리'
age = 10
height = 150
t = ('둘리', 10, 1)
h('둘리', 10, 1)
h(*t)

d = {'name':'둘리', 'age':10, 'height':150}
h(**d)