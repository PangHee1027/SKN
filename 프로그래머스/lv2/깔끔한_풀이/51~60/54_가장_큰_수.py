def solution(numbers):
    # 1. 모든 정수를 문자열로 변환
    numbers_str = list(map(str, numbers))
    
    # 2. 3번 반복한 문자열을 기준으로 내림차순 정렬
    numbers_str.sort(reverse=True, key=lambda x: x * 3)
    
    # 3. 정렬 후 가장 큰 요소가 '0'이면 전체가 0이므로 "0" 리턴
    if numbers_str[0] == '0':
        return '0'
    
    return "".join(numbers_str)