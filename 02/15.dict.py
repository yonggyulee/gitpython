# 생성
d = {'basketball': 5, 'baseball': 9}
print(d, type(d))

d2 = {}
print(d2, type(d2))

d3 = dict()
print(d3, type(d3))

d4 = dict(one=1, two=2, three=3, five=5)
print(d4)

d5 = dict([('one',1),('two',2),('three',3),('four', 4)])
print(d5, type(d5))

# index 대신에 key로 값에 접근한다
print(d['basketball'])

# 크기
print(len(d))

# in, not in : 키의 존재 여부
print('soccer' not in d)
print('basketball' in d)

# 다양한 타입의 keyㄹ흘 지원할 수 있다
d6 = {}
print(d6)

d['twenty'] = 20
d[True] = 'true'
d[10] = 10
print(d)

# key는 변경 불가능한 타입의 값을 사용해야 한다.
#d6[[1,2,3]] = 6
d6[(1,2,3)] = 6

# 객체 함수
print("===============객체함수==============")
k = d6.keys()
print(k,type(k))
for key in k:
    print(key)

v = d6.values()
for val in v:
    print(val)

it = d6.items()
for i in it:
    print(it)


phone = {'마이콜':'000-0000-0000', '둘리':'111-1111-1111', '또치': '222-2222-2222'}
print(phone['둘리'])
print(phone.get('둘리'))

# get() 객체 함수를  사용하는 경우 : 값 객체가 없는 경우 None을 반환 받을 수 있게 때문에
# print(phone['도우너'])
v = phone.get('도우너')
if v is None:
    print('도우너 키를 가진 값은 없습니다')

# setdefault()는 get()와 차이점은 존재하지 않는 경우 default 값이 저장된다.
v = phone.setdefault('둘리', '555-5555-5555')
print(v)
v = phone.setdefault('도우너', '555-5555-5555')
print(v)

print(phone)

#pop(),  삭제와 동시에 값을 가져온다.
v = phone.pop('둘리')
print(v)
print(phone)

item = phone.popitem()
print(item)
print(phone)

# clear
phone.clear()
print(phone)

# 조회
d7 = {'c':3,'a':1,'b':2}
for key in d7:
    print(key, end=' ')
else:
    print()

for key in d7.keys():
    print(key, end=' ')
else:
    print()

for key, value in d7.items():
    print(key, value)


