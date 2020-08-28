# 1 ~ 10 합을 구하기
s = 0
# for n in range(1,11):
#   s += n
# print(s)

s, count = 0,1
while count < 10:
    print(count)
    s += count
    count+=1
print(s)

#break
#for n in range(10):
#    if n > 5 :
#        break
#    print(n, end=' ')

i = 0
while i <10:
    if i>5:
        break
    print(i,end=' ')
    i+=1

print('\n===============================================')


# 무한루프
i = 0
while True:
    print('infinite loop')
    if i >5:
        break
    i+=1