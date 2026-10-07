def solution(numbers):
    if not max(numbers) :
        return "0"
    numbers_str = list(map(str, numbers))
    numbers_str.sort(reverse = True, key = lambda x : x * 3)
    
    return "".join(numbers_str)

print(solution([3, 30, 34, 5, 9]))