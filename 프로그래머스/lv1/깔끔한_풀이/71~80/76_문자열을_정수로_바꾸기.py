# 알고리즘 공부용
def solution(s):
    result = 0
    # 부호 확인
    sign = -1 if s[0] == '-' else 1
    
    # 맨 앞이 부호(+, -)인 경우 숫자는 index 1부터 시작
    start_idx = 1 if s[0] in ['+', '-'] else 0
    
    # 각 자릿수 숫자를 10씩 곱해가며 누적
    for char in s[start_idx:]:
        result = result * 10 + int(char)
        
    return result * sign