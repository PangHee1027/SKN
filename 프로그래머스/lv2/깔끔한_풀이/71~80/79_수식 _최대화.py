from collections import deque
import re

def solution(expression):
    # 1. 정규표현식을 이용해 수식 문자열을 숫자와 연산자 토큰으로 분리
    # - r'(\d+|\D)': 연속된 숫자(\d+) 또는 숫자가 아닌 문자(\D, 즉 +, -, *)를 각각 매칭
    # - 숫자는 int형으로 변환하고, 연산자는 문자열 그대로 유지하여 리스트 생성
    tokens = [int(x) if x.isdigit() else x for x in re.findall(r'(\d+|\D)', expression)]
    
    # 2. 3개의 연산자(+, -, *)로 만들 수 있는 모든 우선순위 조합 (총 3! = 6가지)
    operations = [
        ("+", "-", "*"), ("+", "*", "-"), 
        ("-", "+", "*"), ("-", "*", "+"), 
        ("*", "-", "+"), ("*", "+", "-")
    ]
    
    max_val = 0  # 모든 연산 결과의 절댓값 중 최댓값을 저장할 변수
    
    # 3. 6가지 연산자 우선순위 조합을 각각 시뮬레이션
    for op_priority in operations:
        current_tokens = list(tokens)  # 원본 토큰 리스트를 보존하기 위해 복사해서 사용
        
        # 현재 우선순위 조합에 포함된 연산자를 순서대로 하나씩 처리 (예: +, -, * 순서)
        for op in op_priority:
            # 덱(deque)을 활용해 순서대로 토큰을 꺼내며 계산 진행
            q = deque(current_tokens)
            next_q = deque()  # 이번 단계에서 연산이 끝난 결과나 다음 대상 토큰들을 임시로 담을 덱
            
            # 4. 덱을 순회하며 현재 연산자(op)를 찾아 먼저 계산
            while q:
                item = q.popleft()
                
                # 현재 처리해야 할 연산자(op)를 만난 경우
                if item == op:
                    # [핵심 로직]
                    # - 왼쪽 피연산자: 이미 계산되어 next_q의 맨 뒤에 쌓여 있는 결과값
                    left = next_q.pop()
                    # - 오른쪽 피연산자: 아직 처리되지 않은 q의 맨 앞에 남아 있는 값
                    right = q.popleft()
                    
                    # 연산자 종류에 따라 실제 산술 연산 수행
                    if op == "+":
                        res = left + right
                    elif op == "-":
                        res = left - right
                    else:
                        res = left * right
                        
                    # 계산된 결과값을 다음 덱(next_q)에 추가
                    next_q.append(res)
                else:
                    # 연산자가 아니거나, 현재 순위의 연산자가 아니라면 그대로 다음 덱으로 넘김
                    next_q.append(item)
                    
            # 이번 우선순위 연산이 모두 끝난 수식 리스트로 갱신
            current_tokens = list(next_q)
            
        # 모든 연산자 우선순위 처리가 완료되면 최종 결과값(current_tokens[0])의 절댓값 계산
        # 기존 최댓값(max_val)과 비교하여 더 큰 값을 갱신
        max_val = max(max_val, abs(current_tokens[0]))
        
    # 5. 모든 조합 중 가장 큰 우승 상금 금액 반환
    return max_val