n = int(input())
nums = list(map(int, input().split()))

cnt = 0
for num in nums:
    if num == 1:
        continue

    isFlag = False

    for i in range(2, num):
        if num % i == 0:
            isFlag = True
            break
    
    if isFlag == False:
        cnt += 1
    
print(cnt)