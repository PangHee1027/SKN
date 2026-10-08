def solution(sequence, k):
    left, right = 0, 1
    answer = [0, len(sequence)]
    cur_len = len(sequence) + 1
    sum_of_list = sequence[0]
    while left < right <= len(sequence) :
        if sum_of_list < k :
            if right < len(sequence) :
                sum_of_list += sequence[right]
                right += 1
            else :
                sum_of_list -= sequence[left]
                left += 1
        elif sum_of_list > k :
            sum_of_list -= sequence[left]
            left += 1
        else :
            if cur_len > right - left :
                answer = [left, right - 1]
                cur_len = right - left
            sum_of_list -= sequence[left]
            left += 1
        
        # print(sequence[left:right], left, right, sum_of_list, answer)
    return answer

print(solution([1, 2, 3, 4, 5], 7))
print(solution([1, 1, 1, 2, 3, 4, 5], 5))
print(solution([2, 2, 2, 2, 2], 6))