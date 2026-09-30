def solution(elements):
    ll = len(elements)  # 수열의 전체 길이를 변수에 저장
    res = set()         # 부분 수열의 합을 중복 없이 저장할 집합(set) 생성

    # 1. 수열의 시작점(i)을 0번 인덱스부터 마지막 인덱스까지 순회
    for i in range(ll):
        ssum = elements[i]  # 시작 원소 하나만 포함한 합으로 초기화 (길이 1인 부분 수열)
        res.add(ssum)       # 길이 1인 부분 수열의 합을 집합에 추가
        
        # 2. 시작점(i) 다음 위치부터 (길이-1)개의 원소를 하나씩 늘려가며 더함
        for j in range(i + 1, i + ll):
            # 원형 수열 처리를 위해 인덱스를 (j % ll)로 순환
            # 이전 합(ssum)에 다음 원소 하나만 더해서 연속 부분 수열의 합을 갱신 ($O(1)$ 연산)
            ssum += elements[j % ll]
            res.add(ssum)   # 갱신된 길이의 부분 수열 합을 집합에 추가
            
    # 중복이 제거된 모든 부분 수열 합의 개수를 반환
    return len(res)