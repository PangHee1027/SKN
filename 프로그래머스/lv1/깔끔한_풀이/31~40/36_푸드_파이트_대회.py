def solution(food):
    # 각 음식을 나누어 몫만큼 배치한 왼쪽 문자열 생성
    left = "".join(str(i) * (f // 2) for i, f in enumerate(food))
    
    # [왼쪽] + [물(0)] + [오른쪽(좌우반전)]
    return left + "0" + left[::-1]