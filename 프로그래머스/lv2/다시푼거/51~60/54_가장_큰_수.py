def solution(numbers):
    if not max(numbers) :
        return '0'
    
    numbers = list(map(str, numbers))
    numbers.sort(reverse = True, key = lambda x : x * 3)
    
    return ''.join(numbers)