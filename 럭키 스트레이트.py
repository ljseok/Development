n = input()
length = len(n) # 점수값의 총 자릿수
summary = 0

for i in range(length // 2): # 왼쪽부분 자릿수 합
    summary += int(n[i])

for i in range(length // 2, length): # 오른쪽 부분 자릿수 합
    summary -= int(n[i])

if summary == 0:
    print("LUCKY")
else:
    print("NO")
