
results = []

numbers = [1,2,3,4,5,6,7,8]

for n in numbers:
    result = n*n
    results.append(result)

print(results)

results = [num*num for num in numbers]
print(results)

# 문자열 리스트에서 길이가 2이하인 문자열만 새로운 리스트에 담기
strings = [ 'a', 'as', 'bat', 'car', 'dove', 'python' ]

results = []
for s in strings:
    if len(s) <= 2:
        results.append(s)
print(results)

results = [s for s in strings if len(s) <= 2]
print(results)

# 1 ~ 100 사이에 수 중의 짝수 리스트 만들기
results = [n for n in range(1,101) if n % 2 == 0]
print(results)

# 1 ~ 100 사이에 3, 6, 9 가 들어 있는
#results = [n for n in range(1,101) if (n % 10) % 3 == 0 or ((n//10) % 10) % 3 == 0 ]
#print(results)
results = [n for n in range(1,101) if str(n).count('6') > 0 or str(n).count('3') > 0 or str(n).count('9') > 0]
print(results)

# 문자열 리스트에서 각각의 문자열의 길이를 담은 리스트 만들기
results = [len(s) for s in strings]
print(results)

# set comprehension
s = {s for s in strings if len(s) <= 2}
print(s)

# dict comprehension
d = {s:len(s) for s in strings}
print(d)

#