def solution(sequence):
    if len(sequence) < 3 :
        return max(abs(max(sequence)), abs(min(sequence)))
    
    sequence = [x * -1 if i % 2 else x * 1 for i, x in enumerate(sequence)]
    current_sum = max_sum = sequence[0]
    for num in sequence[1:]:
        current_sum = max(num, current_sum + num)
        max_sum = max(max_sum, current_sum)
    current_sum = min_sum = sequence[0]
    for num in sequence[1:]:
        current_sum = min(num, current_sum + num)
        min_sum = min(min_sum, current_sum)

    return max(abs(max_sum), abs(min_sum))

print(solution([2, 3, -6, 1, 3, -1, 2, 4])) # 10