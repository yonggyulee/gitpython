# for 반복문
# for o in [sequence 객체] :
for i in [10, 20, 30, 40]:
    result = i**2
    print(result, end=' ')
else:
    print("\n---------------------------------")


a = ['cat', 'cow', 'tiger']
for animal in a:
    print(animal, end= ' ')
else:
    print("\n---------------------------------")

# 복합 자료형을 for문에서 사용하는 경우
l = [('둘림', 10),('마이콜', 30),('또치', 11)]

for t in l:
    print('이름: %s, 나이: %d' % t)
else:
    print("\n---------------------------------")

# 10번 반복하는 loop
for i in range(1,11):
    print(i, end=' ')
else:
    print("\n---------------------------------")

# 1 ~ 10 합을 구하기
sum = 0;
for i in range(1,11):
    sum +=i
else:
    print(sum)
print("\n---------------------------------")

# break
for n in range(10):
    if n > 5 :
        break
    print(n, end=' ')
else:
    print("\n----------------정상 루프 종료----------------")
print("\n--------------------------------")

for n in range(10):
    if n > 5 :
        continue
    print(n, end=' ')
else:
    print("\n---------------정상 루프 종료-----------------")


