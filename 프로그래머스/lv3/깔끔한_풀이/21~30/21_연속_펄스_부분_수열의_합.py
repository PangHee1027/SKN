def solution(sequence):
    # 1. 펄스 수열 [1, -1, 1, -1 ...]을 곱한 형태로 변환
    pulsed = [x * -1 if i % 2 else x * 1 for i, x in enumerate(sequence)]
    
    # 2. 카데인 알고리즘을 이용해 최댓값(맥스 서브배열 합)과 최솟값(민 서브배열 합) 구하기
    max_sum = current_max = pulsed[0]
    for num in pulsed[1:]:
        current_max = max(num, current_max + num)
        max_sum = max(max_sum, current_max)
        
    min_sum = current_min = pulsed[0]
    for num in pulsed[1:]:
        current_min = min(num, current_min + num)
        min_sum = min(min_sum, current_min)

    # 3. 두 경우의 절댓값 중 가장 큰 값이 정답
    return max(abs(max_sum), abs(min_sum))