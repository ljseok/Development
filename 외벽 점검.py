import math
import itertools

def solution(n, weak, dist):
    weakSize = len(weak) # 취약지점의 갯수
    weak = weak + [w + n for w in weak]
    miniCnt = math.inf
    for start in range(weakSize): # 시작위치에서 시도를 함
        for d in itertools.permutations(dist, len(dist)):
            cnt = 1
            pos = start
            for i in range(1, weakSize): # 모든 취약지점 까지 방문
                nextPos = start + i
                diff = weak[nextPos] - weak[pos]
                if diff > d[cnt-1]:
                    pos = nextPos
                    cnt += i
                    if cnt > len(dist):
                        break
            if cnt <= len(dist):
                miniCnt = min(miniCnt, cnt)

    if miniCnt == math.inf:
        return -1
    return miniCnt