Pillar = [[]] # 기둥
Bar = [[]] # 보

def checkPillar(x,y):
    if y == 0 or Pillar[x][y-1]: # 아래에 기둥이 있을경우 설치가능
        return True
    if (x > 0 and Bar[x-1][y]) or Bar[x][y] : # 보위에 설치가능 0 이상 , 보가 같은 경우에도 설치가능
        return True
    return False

def checkBar(x,y):
    if Pillar[x][y-1] or Pillar[x+1][y-1]: # 바로밑에 기둥이 있는경우 설치가능 , 오른쪽 아래에 있을 경우에도 설치가능
        return True
    if x > 0 and Bar[x-1][y] and Bar[x+1][y]: # 양옆에 보가 있을경우 설치가능
        return True
    return False

def canDel(x,y):
    for i in range(x-1, x+2):
        for j in range(y, y+2):
            if Pillar[i][j] and checkPillar(i,j) == False: # 기둥이 있으면 존제할수 있는지 본다.
                return False
            if Bar[i][j] and checkBar(i,j) == False:
                return False
     return True



def solution(n, build_frame):
    global Pillar , Bar
    Pillar = [[0 for _ in range(n+1)] for _ in range(n+2)] # 초기회
    Bar = [[0 for _ in range(n+1)] for _ in range(n+2)] # 초기화

    for x, y, kind, cmd in build_frame: # kind 기둥,보를 구분한다. cmd 설치, 삭제 구분
        if kind == 0: # 기둥
            if cmd == 1: # 설치
                if checkPillar(x,y):
                    Pillar[x][y] = 1
            else: # 삭제
                Pillar[x][y] = 0
                if canDel(x,y): # 삭제함수
                    Pillar[x][y] = 1
        else:
            if cmd == 1:
                if checkBar(x,y): # 보를 체크하는 함수
                    Bar[x][y] = 1
            else: # 보를 삭제하는 경우
                Bar[x][y] = 0
                if not canDel(x,y):
                    Bar[x][y] = 1
    ans = []
    for x in range(n+1):
        for y in range(n+1):
            if Pillar[x][y]:
                ans.append([x,y,0])
            if Bar[x][[y]:
                ans.append([x,y,1])
    return ans