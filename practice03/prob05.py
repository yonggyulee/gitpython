# 문제5. 선택정렬(제자리 정렬 알고리즘)을 적용하는 코드를 완성하세요.
# 문제에 주어진 배열 [ 5, 9, 3, 8, 60, 20, 1 ] 를 크기 순서대로 정렬하여 다음과 같은 출력이 되도록 완성하는 문제입니다.
arr = [5, 9, 3, 8, 60, 20, 1]

print('Before Sort....')
print(arr)


for i in range(len(arr)-1):
    max = i
    for j in range(i+1,len(arr)):
        if arr[max] < arr[j]:
            max = j
    arr[i], arr[max] = arr[max], arr[i]

print('After Sort....')
print(arr)