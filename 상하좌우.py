n = 5
x,y = 1,1
plans=['R','R','R','U','D','D']

dx=[0,0,-1,1] # L= 0,-1 R= 0,1 U= -1,0 D= 1,0
dy=[-1,1,0,0]

move=['L','R','U','D']

for plan in plans:
    for i in range(len(move)):
        if plan == move[i]:
            nx = x + dx[i] # 어느 방향으로 갈것인지
            ny = y + dy[i]
    if nx < 1 or ny < 1 or nx > n or ny > n: # 공간을 벗어나는 경우 무시한다.
        continue
    x,y = nx,ny
print(x, y)