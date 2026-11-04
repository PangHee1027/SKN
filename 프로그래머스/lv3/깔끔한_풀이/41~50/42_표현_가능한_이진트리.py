import sys
sys.setrecursionlimit(10000)

def is_binary_tree(s, start, end):
    if start >= end:
        return True
    
    mid = (start + end) // 2
    
    # 부모 노드가 0(더미)인데, 해당 서브트리 구간 내에 1(실제 노드)이 존재한다면 불가능
    if s[mid] == '0':
        for i in range(start, end + 1):
            if s[i] == '1':
                return False
                
    # 왼쪽 서브트리와 오른쪽 서브트리 재귀 탐색 (인덱스 범위만 전달)
    return is_binary_tree(s, start, mid - 1) and is_binary_tree(s, mid + 1, end)

def solution(numbers):
    answer = []
    for number in numbers:
        bin_number = bin(number)[2:]
        n = len(bin_number)
        
        # 포화 이진트리 크기(2^h - 1) 맞추기 위한 패딩
        element = 1 
        while element - 1 < n:
            element *= 2
        bin_number = '0' * (element - 1 - n) + bin_number
        
        # 유효성 검사 수행
        if is_binary_tree(bin_number, 0, len(bin_number) - 1):
            answer.append(1)
        else:
            answer.append(0)

    return answer