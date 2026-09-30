def solution(people, limit):
    people.sort()
    left, right = 0, len(people) - 1
    boats = 0
    
    while left <= right:
        # 가장 가벼운 사람 + 가장 무거운 사람 <= limit 이면 가벼운 사람도 같이 탑승
        if people[left] + people[right] <= limit:
            left += 1
        # 무거운 사람은 무조건 보트에 탑승
        right -= 1
        boats += 1
        
    return boats