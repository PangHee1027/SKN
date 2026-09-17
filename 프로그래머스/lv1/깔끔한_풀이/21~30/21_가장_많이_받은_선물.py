def solution(friends, gifts):
    # 1. 친구 이름(문자열)을 2차원 배열의 인덱스(정수 0 ~ N-1)로 매핑
    f = {v: i for i, v in enumerate(friends)}
    l = len(friends)  # 전체 친구 수
    
    p = [0] * l       # p[i]: i번 친구의 선물 지수 (준 선물 - 받은 선물)
    answer = [0] * l  # answer[i]: i번 친구가 다음 달에 받을 선물 개수
    
    # gr[i][j]: i번 친구가 j번 친구에게 준 선물 개수를 저장할 2차원 배열 초기화
    gr = [[0] * l for i in range(l)]
    
    # 2. 주고받은 선물 내역(gifts)을 바탕으로 행렬(gr) 채우기
    for i in gifts:
        a, b = i.split()   # a: 준 사람, b: 받은 사람
        gr[f[a]][f[b]] += 1 # f[a]행 f[b]열의 카운트 1 증가
        
    # 3. 각 친구의 선물 지수(p) 계산
    for i in range(l):
        # sum(gr[i]): i번 친구가 준 총 선물 수 (행의 합)
        # sum([k[i] for k in gr]): i번 친구가 받은 총 선물 수 (열의 합)
        p[i] = sum(gr[i]) - sum([k[i] for k in gr])

    # 4. 모든 친구 쌍(i, j)을 비교하여 다음 달에 받을 선물 개수 집계
    for i in range(l):
        for j in range(l):
            # i가 j에게 준 선물이 더 많은 경우 -> i가 선물 1개 받음
            if gr[i][j] > gr[j][i]:
                answer[i] += 1
            # 주고받은 수가 같거나 전혀 없는 경우 -> 선물 지수(p) 비교
            elif gr[i][j] == gr[j][i]:
                if p[i] > p[j]:  # i의 선물 지수가 더 크면 i가 선물 1개 받음
                    answer[i] += 1
                    
    # 5. 다음 달에 가장 많은 선물을 받는 친구의 선물 개수 반환
    return max(answer)