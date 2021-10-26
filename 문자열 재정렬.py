data = input() # 데이터 입력
result = [] # 결과를 저장할 배열
value = 0 # 숫자

for i in data:
    if i.isalpha(): # 문자가 알파벳이면
        result.append(i) # 결과리스트에 저장
    else: # 숫자라면
        value += int(i) # 더한다

result.sort() # 오름차순으로 정렬

if value !=0: # 숫자가 존재한다면
    result.append(str(value))

print(' '.join(result))