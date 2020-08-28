# 생성
t = () # 공튜플
print(t, type(t))

t = (1, )   # 항목이 하나인 tuple을 생성할 때는 반드시 콤마를 사용한다.
print(t, type(t))

print('\n======================sequence 타입 특징============================')
# 인덱싱 (sequence  타입 특징)
t = (1,2,3)
print(t[0], t[1], t[2], t[-1], t[-2], t[-3])

# slicing
print(t[1:3])
print(t[:])

# 반복(sequence 타입 특징)
t1 = t*2
print(t1)

# 연결
t3 = t + (4,5,6)
print(t3)

# 길이
print(len(t3))

# in, not in
print(4 in t3)
print(10 not in t3)

# 튜플은 변경 불가(immotable)
try:
    t4 = ('apple', 'banana', 10, 20)
    54[2] = 90
except TypeError as te:
    print('튜플은 변경 불가 -- immotable')

# 튜플을 이용한 여러 값의 대입
x, y, z = 10, 20, 30
print(x, y, z)

# 튜플을 이용한 여러 값의 치환
x, y = 10, 20
print(x, y)

x, y = y, x
print(x, y )

# 객체 함수
print('\n======================객체 함수============================')
t5 = (20, 30, 40, 50, 20)
print(t5.index(50))
print(t5.count(20))

# 변환 tuple -> set
s = set(t5)
print(s)

# 변환 tuple -> list, list -> tuple
l = list(t5)
l.insert(0, 10)
print(l)

t5 = tuple(l)
print(t5)

t5 = tuple(set(t5))
print(t5)

