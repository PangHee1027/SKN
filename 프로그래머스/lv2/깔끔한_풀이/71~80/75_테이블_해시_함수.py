def solution(data, col, row_begin, row_end):
    # 1. 튜플을 이용해 한번에 정렬 (col번째 기준 오름차순, 첫 번째 컬럼 기준 내림차순)
    data.sort(key=lambda x: (x[col - 1], -x[0]))
    
    answer = 0
    
    # 2. row_begin부터 row_end까지 순회 (행 번호 i는 1부터 시작)
    for i in range(row_begin, row_end + 1):
        row = data[i - 1]
        
        # 3. 원본 데이터를 변경하지 않고, i로 나눈 나머지들의 합을 구함
        s_i = sum(val % i for val in row)
        
        # 4. bitwise XOR 누적
        answer ^= s_i
        
    return answer