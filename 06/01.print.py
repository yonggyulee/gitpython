
# 가변인수
import sys

print('==================== 가변 인수 ==================')
print(1)
print('hello', ' ', 'world')
print('hello ' + 'world')

# sep 기본 인수값
print('==================== sep 기본 인수 값 ==================')
x = 0.2
s = 'hello'
print(str(x) + ' ' + s)
print(x, s)
print(x, s, sep=':')

# end 기본 인수값
print('==================== end 기본 인수 값 ==================')
print('hello world')
print('!!!!!!!!!!!!!!!!!!!!!!')
print('hello world', end='\n')
print('!!!!!!!!!!!!!!!!!!!!!!')
print('hello world', end='')
print('!!!!!!!!!!!!!!!!!!!!!!')


print('==================== file 기본 인수 값 ==================')
print('hello world', file=sys.stdout)
print('error: hello world', file=sys.stderr)

f = open('hello.txt', 'w')
print(type(f))
print('hello world', file=f)
f.close()

#참고