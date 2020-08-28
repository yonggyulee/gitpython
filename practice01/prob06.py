#문제6. 키보드에서 정수로 된 돈의 액수를 입력 받아 오만 원권, 만원 권, 오천 원권, 천원 권, 500원짜리 동전, 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전 각 몇 개로 변환 되는지 작성하시오.
money = input("금액:")
print(money, type(money))
money = int(money)
value = 50000
a = 5
for i in range(10):
    print('%d원 : %d개' % (value, money//value))
    money %= value
    a = 5 * ((i+1) % 2) + 2 * (i % 2)
    value /= a

# 방법2
moneys = [ 50000, 10000, 5000, 1000, 500, 100, 50, 10, 5, 1]
