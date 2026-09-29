def solution(n, arr1, arr2):
    answer = []
    for num1, num2 in zip(arr1, arr2):
        # 비트 OR 연산 후 2진수 변환 -> n자리 채우기
        ## 1. | -> 비트 단위 or 연산
        ## 2. bin() -> 숫자를 2진수 형태의 문자열로 반환 ex) 0b1001
        ## 3. [2:] 접두사 0b 제거
        ## 4. zfill(n) n자리 수가되게 앞에 0 추가
        binary_str = bin(num1 | num2)[2:].zfill(n)
        # 1은 '#', 0은 공백으로 변환
        row = binary_str.replace('1', '#').replace('0', ' ')
        answer.append(row)
    return answer