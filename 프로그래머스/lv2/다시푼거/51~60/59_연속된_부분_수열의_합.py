def solution(sequence, k) :
    n = len(sequence)
    left, right = 0, 1
    sum_s = sequence[0]
    answer = [0, n + 1]
    cur_len = n + 1
    
    while left < right <= n :
        if sum_s == k :
            if cur_len > right - left :
                cur_len = right - left
                answer = [left, right - 1]
            sum_s -= sequence[left]
            left += 1
        elif sum_s > k :
            sum_s -= sequence[left]
            left += 1
        else :
            if right < n :
                sum_s += sequence[right]
                right += 1
            else :
                sum_s -= sequence[left]
                left += 1

    return answer