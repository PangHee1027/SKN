import math

def solution(r1, r2):
    answer = 0
    
    # 1사분면(x가 1부터 r2까지)을 기준으로 탐색합니다.
    for x in range(1, r2 + 1):
        # 1. 큰 원(r2) 안에서 가능한 최대 y 좌표
        y2 = math.isqrt(r2 ** 2 - x ** 2)
        
        # 2. 작은 원(r1) 안에서 제외해야 하는 최대 y 좌표 (최소 시작점 구하기)
        if x < r1:
            val = r1 ** 2 - x ** 2
            y1 = math.isqrt(val)
            # 만약 나누어떨어지지 않는다면(완전제곱수가 아니라면), 
            # 올림(ceil) 처리를 해주어야 안쪽 원 바깥부터 시작하게 됩니다.
            if y1 ** 2 != val:
                y1 += 1
        else:
            # x가 r1보다 크거나 같으면 작은 원의 영향권 밖이므로 y는 0부터 시작
            y1 = 0
            
        # 3. 현재 x 좌표에서 두 원 사이에 존재하는 y 좌표의 개수 누적
        answer += (y2 - y1 + 1)
        
    # 4개 사분면(x, y 부호 조합)이 모두 같으므로 전체 결과에 4를 곱해줍니다.
    return answer * 4