input_data = input()
row = int(input_data[1])  # x위치 좌표
col = int(ord(input_data[0])) - int(ord('a')) + 1 # Y위치 좌표

steps = [(-2,1),(-2,-1),(1,2),(-1,2),(2,1),(2,-1),(1,-2),(-1,-2)] # 나이트가 이동할수 있는 8가지 방향

result = 0
for step in steps:
    next_row = row+step[0] # X위치확인
    next_column = col+step[1] # Y위치확인

    if next_row>=1 and next_row <=8 and next_column >=1 and next_column<=8: # 이동이 가능하다면 result 증가
        result+=1

print(result)


