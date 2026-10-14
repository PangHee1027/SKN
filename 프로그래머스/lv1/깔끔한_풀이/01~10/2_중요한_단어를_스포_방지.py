def solution(message, spoiler_ranges):
    # 1. 문자열 조작을 쉽게 하기 위해 원본 메시지를 개별 문자의 리스트로 변환합니다.
    a = list(message)
    result = 0
    
    # 2. 원본 메시지를 공백 기준으로 나누어 단어 단위의 리스트로 만듭니다. (나중에 중요한 단어 중복 체크 및 원본 단어 비교용)
    message = message.split()
    
    # 3. 주어진 스포 방지 구간([start, end])들을 하나씩 순회합니다.
    for i in spoiler_ranges:
        # 3-1. 리스트 a에서 해당 스포 방지 범위에 해당하는 부분을 슬라이싱합니다. (i[0]: 시작 인덱스, i[1]+1: 끝 인덱스)
        b = a[i[0]:i[1] + 1]
        
        # 3-2. 슬라이싱한 범위 내의 글자들을 순회하며 공백을 제외한 모든 글자를 "-"로 치환합니다.
        for j in b:
            if j == " ":
                continue
            b[b.index(j)] = "-"
            
        # 3-3. 스포 방지 처리된 부분(b)을 다시 전체 문자열 리스트 a의 해당 위치에 반영합니다.
        a[i[0]:i[1] + 1] = b
        
    # 4. 스포 방지 처리된 문자열(a)을 다시 공백 기준으로 나누어 단어 단위 리스트로 변환합니다.
    #    (이 시점에서 스포된 단어들은 일부 또는 전체 문자가 "-"로 변환되어 있습니다.)
    a = "".join(a).split()
    
    # 5. 스포 방지 처리된 단어 리스트(a)를 순회하며 중요한 단어인지 판별합니다.
    for i, j in enumerate(a):
        # 5-1. 단어에 "-"가 포함되어 있고(스포 방지 구간에 속함),
        #      동시에 아직 결과에 반영(중요한 단어로 카운트되어 원본 단어로 복구)되지 않아
        #      원본 메시지의 해당 단어(message[i])가 아직 a에 포함되어 있지 않은 경우
        if "-" in j and not message[i] in a:
            result += 1  # 중요한 단어 개수 1 증가
            a[i] = message[i]  # 이전에 공개된 스포 방지 단어와 중복 체크를 방지하기 위해 원본 단어로 치환
    print(a)
    print(message)
    return result
    
print(solution("my phone number is 01012345678 and may i have your phone number", [[5, 5], [25, 28], [34, 40], [53, 59]]))