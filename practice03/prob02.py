# 문제2. range() 함수와 유사한 frange() 함수를 작성해 보세요.
# frange() 함수는 실수 리스트를 반환합니다.
def frange(val, base=0.0, step=0.1):
    result = []
    val = int(val*10)
    base = int(base * 10)
    step = int(step * 10)
    for i in range(base, val, step):
        result.append(float(i/10))
    return result

print(frange(2))
print(frange(2.0, 1.0))
print(frange(3.0, 1.0, 0.5))
