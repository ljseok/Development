from itertools import combinations

n = int(input()) # 복도의 크기를 입력받는다

corridor = [] # 복도
teacher = [] # 선생님 위치
space = [] # 빈 공간

for i in range(n):
    corridor.append(list(input().split())) # 복도의 정보 입력받기
    for j in range(n):
        if corridor[i][j] == 'T': # T가 위치하면 선생님이 있으므로
            teacher.append((i,j))
        if corridor[i][j] == 'X': # 빈공간 이라면
            space.append((i,j))

def observe(x,y,direct): # 상,하,좌,우 학생 감시 함수
    if direct == 0:
        while y >= 0: # 왼쪽방향 감시
            if corridor[x][y] == 'S': # 학생이 있는 경우
                return True
            if corridor[x][y] == 'O': # 장애물이 있는 경우
                return False
            y -= 1

    if direct == 1:
        while y < n: # 오른쪽방향 감시
            if corridor[x][y] == 'S':
                return True
            if corridor[x][y] == 'O':
                return False
            y += 1

    if direct == 2: # 위쪽 방향 감시
        while x >= 0:
            if corridor[x][y] == 'S':
                return True
            if corridor[x][y] == 'O':
                return False
            x -= 1

    if direct == 3: # 아래쪽 방향 감시
        while x < n:
            if corridor[x][y] == 'S':
                return True
            if corridor[x][y] == 'O':
                return False
            x += 1

def block(): # 장애물 설치후 학생검사 함수
    for x , y in teacher:
        for i in range(4): # 상,하,죄,우 방향 확인
            if observe(x,y,i):
                return True
    return False

find = False

for data in combinations(space, 3): # 빈공간에서 3개를 뽑는 경우의 수 확인
    for x, y in data:
        corridor[x][y] = 'O' # 장애물 설치

    if not block(): # 학생이 감지되지 않았을 경우
        find = True
        break

    for x, y in data:
        corridor[x][y] = 'X' # 장애물 제거

if find == True:
    print('YES')
else:
    print('NO')










