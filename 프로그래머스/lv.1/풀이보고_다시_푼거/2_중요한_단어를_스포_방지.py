def solution(message, spoiler_ranges):
    a = list(message)
    result = 0
    # 공백을 기준으로 단어 추출
    message = message.split()
    for i in spoiler_ranges:
        # b = 메시지에서 스포방지 범위를 슬라이스
        b = a[i[0]:i[1] + 1]
        # 스포방지 글자를 "-" 로 치환
        for j in b:
            if j == " ":
                continue
            b[b.index(j)] = "-"
        a[i[0]:i[1] + 1] = b
    # 스포방지 처리된 단어들을 a에 저장
    a = "".join(a).split()
    # 만약 a에 포함된 단어에 "-"가 포함되고 해당 순서의 message 단어가 a에 포함되지 않았다면 결과 +1
    # a의 단어를 원본 메시지의 단어로 치환 (중복방지로 추정)
    # enumerate() -> 묶음 자료형, 문자열에 대하여 (인덱스, 데이터) 쌍을 반환
    for i,j in enumerate(a):
        if "-" in j and not message[i] in a:
            result += 1
            a[i] = message[i]
    print(message)
    print(a)
    return result
    
print(solution("my phone number is 01012345678 and may i have your phone number", [[5, 5], [25, 28], [34, 40], [53, 59]]))