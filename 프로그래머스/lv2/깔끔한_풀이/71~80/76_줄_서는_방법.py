import math

def solution(n, k):
    # 1. 0-based index로 맞추기 위해 k를 1 감소시킴
    k -= 1
    
    # 2. 1부터 n까지의 숫자를 담은 리스트 생성
    numbers = list(range(1, n + 1))
    answer = []
    
    # 3. 큰 자리수부터 차례대로 결정
    for i in range(n, 0, -1):
        # 현재 자릿수를 제외한 나머지 자리들의 경우의 수 ((i-1)!)
        fact = math.factorial(i - 1)
        
        # 몫은 사용할 숫자의 인덱스, 나머지는 다음 단계로 넘길 k가 됨
        index, k = divmod(k, fact)
        
        # 숫자를 선택하여 결과에 추가하고, 사용한 숫자는 리스트에서 제거
        answer.append(numbers.pop(index))
        
    return answer