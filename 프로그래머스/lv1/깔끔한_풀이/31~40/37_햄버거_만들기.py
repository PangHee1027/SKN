def solution(ingredient):
    stack = []
    answer = 0

    for item in ingredient:
        stack.append(item)
        
        # 스택 끝 4개의 재료가 [빵, 야채, 고기, 빵] 순서인지 확인
        if stack[-4:] == [1, 2, 3, 1]:
            answer += 1
            # 햄버거 완성 재료 4개 제거 (pop 4회)
            del stack[-4:]

    return answer