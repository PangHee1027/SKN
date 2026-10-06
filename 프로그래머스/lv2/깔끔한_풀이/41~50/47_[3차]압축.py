import string

def solution(msg):
    # 1. A-Z 사전을 dict로 초기화 ('A': 1, 'B': 2, ..., 'Z': 26)
    dictionary = {char: i + 1 for i, char in enumerate(string.ascii_uppercase)}
    next_index = 27
    
    answer = []
    i = 0
    
    while i < len(msg):
        w = msg[i]
        
        # 사전에 있는 가장 긴 문자열 w 찾기
        while i + 1 < len(msg) and (w + msg[i + 1]) in dictionary:
            i += 1
            w += msg[i]
            
        # 2. w의 색인 번호 출력
        answer.append(dictionary[w])
        
        # 3. 사전에 다음 글자(c)를 포함한 w+c 등록
        if i + 1 < len(msg):
            dictionary[w + msg[i + 1]] = next_index
            next_index += 1
            
        # 다음 글자로 이동
        i += 1
        
    return answer