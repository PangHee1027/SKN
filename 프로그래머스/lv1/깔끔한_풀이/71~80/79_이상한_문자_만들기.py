def solution(s):
    answer = []
    idx = 0
    
    for c in s:
        if c == " ":
            answer.append(c)
            idx = 0  # 공백을 만나면 단어 인덱스 리셋
        else:
            # idx가 짝수면 대문자, 홀수면 소문자
            answer.append(c.lower() if idx % 2 else c.upper())
            idx += 1
            
    return "".join(answer)