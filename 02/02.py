# 부울(bool) 참이나 거짓을 나타내는 것
# True, False 두 값(리터럴)만 가진다.

a = 1
print(a>1)

b =  a>1
print(b, type(b))

# 연산식에서 int 값(0,1)으로 평가된다.
print(b + 1)
print(True*False)

# int
a = 0x20
print(a, type(a))
b = 0b10001
print(b, type(b))
c = 0o10001
print(c, type(c))

# 3.x에서는 int, long 합쳐졌다. 따라서 표현범위가 무한대이다.
e = 2**1024
print(e, type(e))
print(e.bit_length())

# 변환 함수
print(oct(38))
print(bin(38))
print(hex(38))

a = 1.2
print(a, type(a))

# is_integer 함수는 float 객체가 저장한 값으로 정수인지 실수인지 확인이 가능하다.
b = 2.0
print(type(b))
print(b.is_integer())

c = 3e3
print(c)
c = 0.2e-4
print(c)
