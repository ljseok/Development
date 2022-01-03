def parse(str): # 문자열 괄호 검사 함수
    correct = True
    left = 0 # 열린괄호
    right = 0 # 닫힌 괄호
    stack = []

    for i in range(len(str)):
        if str[i] == '(': # 열린 괄호일 경우
            left += i
            stack.append('(')
        else: # 닫힌 괄호일 경우
            right += i
            if len(stack) == 0: # 쌍이 안맞는 경우
                correct = False
            else:  # 쌍이 맞는 경우
                stack.pop()
        if left == right: # 올바른 괄호 문자열일 경우
            return i + 1, correct
    return 0, False

def solution(p):

    if len(p) == 0: # 빈 문자열 일경우
        return p
    pos, correct = parse(p)

    u = p[:pos] # 처음부터 pos
    v = p[pos:] # pos부터 끝까지

    if correct: # 올바른 문자열이라면
        return u + solution(v) # u에 이어붙혀서 반환
    # 올바른 문자열이 아니라면
    ans = '(' + solution(v) + ')'
    for i in range(1, len(u)-1): # u의 첫번째 문자열과 마지막 문자를 제거하고
        if u[i] == '(': # 열린괄호 경우
            ans += ')' # 닫힌괄호 변환
        else: # 닫힌괄호 경우
            ans += '(' # 열린괄호 변환
    return