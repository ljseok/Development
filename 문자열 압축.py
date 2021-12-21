
def solution(s):
    answer = len(s)

    for i in range(1, int(len(s)/2)+1):
        pos = 0 # 어느위치에서 문자열 처리 하는지
        length = len(s) # 문자열의 길이만큼 초기화

        while pos + i <= len(s): # 문자열 끝까지 반복
            unit = s[pos:pos+i] # pos pos+i
            pos += i
            count = 0
            while pos + i <= length: # length를 넘어가면 안된다.
                if unit == s[pos:pos+i]: # 포지션의 압축길이 만큼 읽어왔을때
                    count += 1
                    pos += i
                else:
                    break
                if count > 0: # 압축 된것이므로
                    length -= i * count

                    if count < 9:
                        length += 1
                    elif count < 99:
                        length += 2
                    elif count < 990:
                        length += 3
                    else:
                        length += 4
        answer = min(answer, length)


    return answer
