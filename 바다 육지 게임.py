n,m = map(int,input().split())

d = [[0] * m for _ in range(n)] # 방문한 위치를 저장하기 위한 맵을 생성하여 0으로 초기화
x,y,direct = map(int,input().split()) # x좌표 , y좌표 , 뱡향 입력받기
d[x][y] = 1 # 현재 좌표는 방문처리

array = [] # 전체 맵 정보를 입력받기
for i in range(n):
    array.append(list(map(int,input().split())))
# 북,동,남,서 방향
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def trun_left(): # 왼쪽으로 회전시키는 함수정의
    global direct
    direct -= 1
    if direct == -1:
        direct = 3

count = 1
turntime = 0
while True:
    trun_left() # 왼쪽으로 회전
    nx = x + dx[direct]
    ny = y + dy[direct]

    # 왼쪽으로 회전한이후에 가보지 않은칸이 존재할 경우 --> 이동

    if d[nx][ny] == 0 and array[nx][ny] == 0:
        d[nx][ny] = 1
        x = nx
        y = ny
        count += 1
        turntime = 0
        continue

    # 회전한 이후에 모두 가본 칸이거나 바다인 경우
    else:
        turntime += 1
    # 4방향 모두 갈수 없는 경우
    if turntime == 4:
        nx = x - dx[direct]
        ny = y - dy[direct]

        # 뒤로가기
        if array[nx][ny] == 0:
            x = nx
            y = ny
        # 뒤가 바다로 막혀있을때
        else:
            break
        turntime = 0

print(count)
