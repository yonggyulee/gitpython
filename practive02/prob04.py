#문제4 반복문을 이용하여 369게임에서 박수를 쳐야 하는 경우의 수를 순서대로 화면에 출력해보세요. 1부터 99까지만 실행하세요.

count = 0
for n in range(1,100):
    clab = 0
    clab += str(n).count('3')
    clab += str(n).count('6')
    clab += str(n).count('9')
    if clab > 0:
        print('{0} '.format(n) + '짝'*clab)
        count += 1
print('총 객수 : {0}'.format(count))

