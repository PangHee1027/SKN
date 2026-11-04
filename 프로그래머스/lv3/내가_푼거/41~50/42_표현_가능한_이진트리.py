import sys
sys.setrecursionlimit(10000)

def is_binary_tree(bin_number) :
    n = len(bin_number)
    if n == 1 :
        return True
    mid = n // 2
    left, right = bin_number[:mid], bin_number[mid + 1 :]
    if bin_number[mid] == '0' :
        if any(x == '1' for x in left) or any(x == '1' for x in right) :
            return False
    return is_binary_tree(left) and is_binary_tree(right)

def solution(numbers):
    answer = []
    for number in numbers :
        bin_number = bin(number)[2:]
        n = len(bin_number)
        element = 1 
        while element - 1 < n :
            element *= 2
        bin_number = '0' * (element - 1 - n) + bin_number
        answer.append(1 if is_binary_tree(bin_number) else 0)

    return answer

print(solution([7, 42, 5])) # [1, 1, 0]
print(solution([63, 111, 95])) # [1, 1, 0]
