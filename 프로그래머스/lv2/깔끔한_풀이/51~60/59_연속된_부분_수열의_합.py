def solution(sequence, k):
    answer = []
    min_len = float('inf')
    
    left = 0
    sum_of_list = 0
    
    for right in range(len(sequence)):
        sum_of_list += sequence[right]
        
        while sum_of_list > k:
            sum_of_list -= sequence[left]
            left += 1
            
        if sum_of_list == k:
            length = right - left + 1
            if length < min_len:
                min_len = length
                answer = [left, right]
                
                # 길이가 1인 수열을 찾으면 최단 길이이자 가장 앞선 인덱스이므로 즉시 반환
                if min_len == 1:
                    return answer
                
    return answer