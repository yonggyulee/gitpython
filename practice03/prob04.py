# 문제4 구구단 중에 특정 곱셈을 만들고 그 답을 선택하는 프로그램을 작성하는 문제입니다.
# 답을 포함하여 9개의 정수가 아래와 같은 형태로 출력되고 사용자는 답을 골라 입력하게 됩니다. 프로그램은 정답 여부를 다시 출력합니다.
import random

x = random.randrange(2,10)
y = random.randrange(2,10)
correct_answer = x*y

print('{0} X {1} = ?'.format(x, y))
print()

correct_turn = random.randrange(9)

ex_list = []
for i in range(9):
    while True:
        ex = random.randrange(2,10)*random.randrange(2,10)
        if ex != correct_answer:
            break
    if i == correct_turn:
        ex = correct_answer
    print(ex, end='\t')
    if (i%3) == 2:
        print()

while True:
    answer = int(input('answer: '))
    if answer == correct_answer:
        print('정답')
        break
    else:
        print('틀렸습니다. 다시 한번 생각해보세요.')



