def solution(clothes):
    category_counts = {}
    for _, category in clothes:
        category_counts[category] = category_counts.get(category, 0) + 1
        
    answer = 1
    for count in category_counts.values():
        answer *= (count + 1)
        
    return answer - 1