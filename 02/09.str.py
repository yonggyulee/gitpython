
# 한 줄 문자열
s1 = ''
str1 = 'Hello World'
str2 = "Hello World"
print(type(s1), type(str1),type(str2))
print(isinstance(s1,str))

# 여러 줄 문자열
str3 = '''ABC
DEF
가나다라마바사
아자차카타파하'''
print(str3)

# 여러 줄 주석 -> 여러 줄 문자열
'''
주석1
주석2
주석3
'''

# escape
print("Hello\nWorld\n")
print("Hello\"World\"")
print("She\'s mom")
print("She's mom")
print("둘리\t0000-00000-0000")

print("===============문자열 연산===============")
s1 = 'First String'
s2 = 'Second String'

# 반복
s3 = s1*3
print(s3)

#
s4 = s1 + ' ' + s2
print(s4)
s5 = 'Hello' + '-' + 'world'
s6 = 'Hello''-''world'
print(s5)
print(s6)

# 문자열 객체와 정수 객체는 연결(+) 연산을 할 수 없다.
# print('Hello' + 5) : error
print('Hello' + str(5))

# 인덱싱(sequence 타입이 가지는특징)
print(s1[0], s1[1], s1[2])
print(s1[-12], s1[-11], s1[-10])


# slicing(sequence 타입이 가지는특징)
s7 = s1[2:5]
print(s7)
print(s1[2:])

# len() 함수(sequence 타입이 가지는특징)
print(len(s1))

# in, not in 연산(sequence 타입이 가지는특징)
print('s' in s2)
print('s' not in s2)


print("===============포맷팅===============")
# tuple

print('name: %s, age: %d' % ('둘리', 10))

# dict
print("name: %(name)s, age: %(age)d" % {'name':'둘리', 'age':10})

# format() 함수
name = '마이콜'
age = 30
print('name: ' + format(name, 's') + ', age: ' + format(age, 'd'))

#format() 객체 함수
print("name : {0}, age: {1}".format(name,age))
print("name: {n}, age: {a}".format_map({'n': name,'a': age}))
print("=============== 객체함수 ===============")
s8 = 'i like Python'
print(s8.upper())
print(s8.lower())
print(s8.swapcase())
print(s8.capitalize())
print(s8.title())
print(s8.isdigit())
s9 = '12345689'
print(s9.isdigit())
s9 = 'i Like Python. I Like Java Also'
print(s9.count('Like'))
print(s9.find('Like'))
print(s9.find('Like', 5))
print(s9.find('JavaScript'))
print(s9.rfind('Like'))
print(s9.startswith('i Like', 2))
print(s9.endswith('Also'))
# index()는 발견하지 못하면 예외가 발생한다.
try:
    print(s9.index('Like'))
    s9.rindex('JavaScript')

except ValueError as ex:
    pass
    print('index()는 발견하지 못하면 예외가 발생한다.')
    #예외
    # 1. 로그를 남긴다.
    # 2. 사용자한테 사과

# 편집과 치환
s10 = '     spam and ham'
print('=================' + s10.strip() + '===============')
print('=================' + s10.rstrip() + '===============')
print('=================' + s10.lstrip() + '===============')

s11 = '<><abc><><defg><>'
print('=================' + s11.strip('<>') + '===============')

s12 = 'Hello Java Java Java'
print('=================' + s12.replace('Java','Python') + '===============')

#정렬
s13= 'King and Queen'
print('---' + s13.center(30)+ '---')
print('---' + s13.ljust(30)+ '---')
print('---' + s13.rjust(30)+ '---')

#분리
s14 = 'spam and ham'
t=s14.split(' and ')
print(t, type(t))
s15 = 'one:two:three:four'
t=s15.split(':',2)
print(t)
t=s15.rsplit(':',2)
print(t)

lines = '''1st line
2nd line
3rd line
4th line'''

t = lines.split('\n')
print(t)

t = lines.splitlines()
print(t)

# 병합
s16 = '&'.join(t)
print(s16)

# 판별
print('1234'.isdigit())
print('abcd'.isalpha())
print('1234'.isalpha())
print('abcd'.isdigit())
print('abcd'.islower())
print('abcd'.isupper())
print(' '.isspace())
print(''.isspace())
print('\n'.isspace())
print('\t'.isspace())

# '0' 채우기
number = 234
print(str(number).zfill(5))


# str 객체는 변경할 수 없다. (불변성, immutable)
# s10 = 'hello'
# s10[0] = 't'
# print(s10)

# cf list는 변경 가능하다(mutable)
l1 = ['hello', 'world']
print(l1)
l1[0] = 'HELLO'
print(l1)
l1.append('Python')
print(l1)