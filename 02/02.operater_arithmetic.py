# 사칙연산
print(2*3)
print(2+3)
print(2-3)
print(2/3)

# // 몫연산자, ** 지수승, % 나머지연산자
print(2//3)
print(2**3)
print(2%3)

# divmod() 함수

t = divmod(2, 3)
print(t, type(t))

# 산술 연산자 우선순위
print(2+3*4)
print(-2+3*4)

# 복합 관계 지원
a = 6
print(0< a and a <10)
print(0<a<10)

# 수치형 이외의 다른 타입 객체 비교
print('abcd' > 'abcc')
print('abcd' == 'abcc')
print((1,2,3) > (1,2,10))
print([1,2,3] > [1,2,10])

# 동질성 비교 == (객체의 내용(값))
# 동일성 비교 is (동일한 객체 유무)
x = 10
y = x
print(x == y)
print(x is y)

x = 10
y = 10
print(x == y)
print(x is y)

l1 = [10, 20, 30]
l2 = [10, 20, 30]
print(l1 == l2)
print(l1 is l2)

l3 = l2
print(l3 == l2)
print(l3 is l2)
