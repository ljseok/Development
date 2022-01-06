import math
import itertools

def solution(n, weak, dist): # 외벽의 길이 , 취약지점 , 이동할수 있는 거리
    weakSize = len(weak)
    weak = weak + [w + n for w in weak] # 두배만큼 증가
    miniCnt = math.inf
    for st in range(weakSize): # 시작위치에서 조사
        for d in itertools.permutations(dist, len(dist)):
            cnt = 1 # 친구
            pos = st
            for i in range(1, weakSize):
                next = st + i
                diff = weak[next] - weak[pos]
                if diff > d[cnt-1]:
                    pos = next
                    cnt += 1
                    if cnt > len(dist):
                        break
            if cnt <= len(dist):
                miniCnt = min(miniCnt, cnt)
    if miniCnt == math.inf:
        return -1
    return miniCnt