
i1 = 10
i2 = 20
print(hex(id(i1)), hex(id(i2)))

i1 = 1234567890
i2 = 1234567890

print(hex(id(i1)),hex(id(i2)))

i1 = 11
i2 = 10 + 1

print(hex(id(i1)),hex(id(i2)))

s1 = 'hello'
s2 = 'hello'
print(hex(id(s1)),hex(id(s2)))

l1 = [1,2,3]
l2 = [1,2,3]
print(hex(id(l1)),hex(id(l2)))

# is (동일 레퍼런스 비교)
# 불변객체는 is(동일성)과 ==(동질성) 비교 결과가 같다
# 가변객체는 is(동일성)과 ==(동질성) 비교 결과가 다르다 ( list, set, dict )

print(l1 is l2)
print(l1 == l2)

print(s1 is s2)
print(s1 == s2)

# 형변환 함수는 불변환 객체라고 하더라도 새로운 객체를 만든다. (바로 대입하는 = 과는 다르게 작동한다.)
r = range(1,4)
print(r, type(r))
t1 = tuple(r)
print(r is t1)

# slicing 경우에도 불변환 객체라고 하더라도 새로운 객체를 만든다. (바로 대입하는 = 과는 다르게 작동한다.)
t4 = (0, 1, 2, 3)[1:]
print(t1 is t4)
print(t1 == t4)

