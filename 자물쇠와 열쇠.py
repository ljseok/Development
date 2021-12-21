def match(array, key, rot, row, col):
    n = len(key) # 열쇠의 크기
    for i in range(n):
        for j in range(n):
            if rot == 0:  #회전각이 0인 경우
                array[row + i][col + j] += key[i][j]
            elif rot == 1: # 시계방향으로 90도 회전
                array[row + i][col +j] += key[n-1 -j][i]
            elif rot == 2: # 시계방향으로 180도 회전
                array[row +i][col + j] += key[n-1 -i][n-1 -j]
            else: # 시계방향으로 270도 회전 == 반시계 방향으로 90도 회전
                array[row + i][col + j] += key[j][n-1 -i]

def check(array, offset, n):
    for i in range(n):
        for j in range(n):
            if array[offset + i][offset +j] != 1:
                return False
    return True

def solution(key, lock):
    offset = len(key)- 1 # 일정한 거리만큼 떨어진 거리

    for row in range(offset + len(lock)): # row위치 옵셋에서 자물쇠 만큼 더한 값
        for col in range(offset + len(lock)): # col위치 옵셋에서 자물쇠 만큼 더한 값
            for rot in range(4): # 열쇠를 돌리는 경우 총 4가지
                array = [[0 for _ in range(58)] for _ in range(58)]

                for i in range(len(lock)): # 자물쇠 복사
                    for j in range(len(lock)):
                        array[offset + i][offset + j] = lock[i][j] # 옵셋 만큼 떨어진 위치에 자물쇠 복사

                match(array, key, rot, row, col) # 복사하기 위한 함수
                if check(array, offset, len(lock)):
                    return True
    return False