# 문제8.문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을 작성하세요.
s1 = input('입력> ')

def reverse(s):
    t = ''
    for i in range(len(s)-1,-1,-1):
        t += s[i]
    return t

print('결과> ' + reverse(s1))