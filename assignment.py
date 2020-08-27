#치환문

a = 1
b = a + 1

print(a, b)

# 변수 할당값 오류(연산 방향 오류)
# 1 + a = b

# 세미콜론으로 치환문을 구현할 수 있다.
e = 3.5; f = 5.3
print(e, f)

# 여러 개를 한번에 치환할 수 있다.
e, f = 3.5, 5.3
print(e, f)

# 같은 값을 여러 변수에 할당할 수 있다.
x = 30
y = 30
z = 30
x = y = z = 30
print(x, y, z)

# 동적 타이핑(실행중에 변수의 타입을 결장한다.)
a = 1
print(type(a))
a = 'hello'
print(type(a))

# 확장 치환문
a = 10
# a = a+10
a += 10
print(a)

# swap
c = 5
d = 17
print("before swap:")
print(c, d)
#
t = d
d = c
c = t
print("after swap:")
print(c,d)
#

