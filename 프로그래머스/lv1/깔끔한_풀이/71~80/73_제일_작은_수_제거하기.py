def solution(arr):
    min_val = min(arr)
    result = [i for i in arr if i != min_val]
    return result if result else [-1]