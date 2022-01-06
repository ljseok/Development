from itertools import combinations

n,m = map(int,input().split()) # 도시의 갯수 , 치킨 집 수 입력
chicken = []
home = []

for i in range(n):
    data = list(map(int, input().split()))
    for j in range(n):
        if data[j] == 1: # 일반집일 경우
            home.append((i,j))
        if data[j] == 2: # 치킨집인 경우
            chicken.append((i,j))

combi = list(combinations(chicken, m)) # 치킨집 중에서 m개의 조합을 뽑는 경우 계산

def sum(chicken_dist):
    result = 0

    for ax,ay in home: # 모든 집에 대해서
        temp = 1e9
        for bx,by in chicken_dist: # 가장 가까운 치킨집의 거리를 계산
            temp = min(temp, abs(ax - bx) + abs(ay - by))
        result += temp
    return result

result = 1e9

for chicken_dist in combi:
    result = min(result, sum(chicken_dist))

print(result)



