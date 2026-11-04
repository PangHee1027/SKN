def solution(n, build_frame):
    def possible(answer):
        for x, y, a in answer:
            if a == 0:  # 기둥인 경우
                # 1. 바닥 위에 있거나
                # 2. 보의 한쪽 끝 부분 위에 있거나
                # 3. 다른 기둥 위에 있는 경우
                if y == 0 or (x - 1, y, 1) in answer or (x, y, 1) in answer or (x, y - 1, 0) in answer:
                    continue
                return False
            else:  # 보인 경우
                # 1. 한쪽 끝 부분이 기둥 위에 있거나
                # 2. 양쪽 끝 부분이 다른 보와 동시에 연결되어 있는 경우
                if (x, y - 1, 0) in answer or (x + 1, y - 1, 0) in answer or ((x - 1, y, 1) in answer and (x + 1, y, 1) in answer):
                    continue
                return False
        return True

    answer = []
    
    for x, y, a, b in build_frame:
        if b == 1:  # 설치
            answer.append((x, y, a))
            if not possible(answer):  # 조건에 맞지 않으면 취소
                answer.pop()
        else:  # 삭제
            answer.remove((x, y, a))
            if not possible(answer):  # 조건에 맞지 않으면 원상복구
                answer.append((x, y, a))
                
    return sorted(answer)