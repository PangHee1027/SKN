from itertools import combinations
from collections import Counter

def solution(orders, course):
    answer = []
    
    # 1. course 배열에 있는 각 코스 요리 개수별로 반복문 수행 (예: 2개짜리, 3개짜리 코스 따로 처리)
    for c in course:
        counter = Counter()  # 각 조합의 등장 횟수를 기록할 빈 Counter 객체 생성
        
        # 2. 모든 손님의 주문 내역(orders)을 하나씩 확인
        for order in orders:
            # 각 손님이 주문한 메뉴를 알파벳 순으로 정렬한 뒤, c개짜리 조합(combination)을 모두 만듦
            # (※ 'AC'와 'CA'를 같은 메뉴 조합으로 인식하기 위해 알파벳 정렬이 필수입니다.)
            for comb in combinations(sorted(order), c):
                counter[comb] += 1  # 해당 조합이 등장할 때마다 빈도수를 1씩 증가시킴
                
            # 만약 현재 course 길이에 해당하는 조합이 하나도 만들어지지 않았다면 다음으로 넘어감
            if not counter:
                continue
                
        # 3. 이번 course 길이에서 가장 많이 주문된 횟수(max_count)를 구함
        max_count = max(counter.values())
        
        # 4. 문제 조건: 최소 2명 이상의 손님으로부터 주문된 조합이어야만 코스 후보가 될 수 있음
        if max_count >= 2:
            # Counter에 저장된 모든 조합(comb)과 주문 횟수(count)를 확인
            for comb, count in counter.items():
                # 최다 주문 횟수와 정확히 일치하는 조합만 정답 후보로 선택
                if count == max_count:
                    answer.append("".join(comb))  # 튜플 형태의 조합을 문자열로 변환하여 추가
                    
    # 5. 최종 결과로 수집된 모든 코스 메뉴들을 문제 조건에 맞게 사전 순(오름차순)으로 정렬하여 리턴
    return sorted(answer)