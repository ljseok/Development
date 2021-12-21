from operator import itemgetter

def solution(food_times, k):
    foods = []
    n = len(food_times) # 음식의 총 개수
    for i in range(n):
        foods.append((food_times[i], i+1)) # 시간과 음식번호

    foods.sort()
    pretime = 0 # 이전의 음식을 먹는 시간
    for i, food in enumerate(foods):
        diff = food[0] - pretime # 높이
        if diff != 0: # 높이차가 0이 아니라면
            spend = diff * n # 소비한 시간 = 높이 * 갯수
            if spend <= k:
                k -= spend # 한번에 뺄수 있다
                pretime = food[0]
            else: # 한번에 뺄수 없다면
                k %= n
                sublist = sorted(foods[i:], key = itemgetter(i))
                return sublist[k][1]
        n -= 1

        answer = 0
        return answer