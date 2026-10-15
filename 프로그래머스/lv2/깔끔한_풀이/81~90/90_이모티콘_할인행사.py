from itertools import product

def solution(users, emoticons):
    # 인덱스별 실제 할인율 (10%, 20%, 30%, 40%)
    discounts = [10, 20, 30, 40]
    
    max_subscribe = 0
    max_income = 0
    
    # 가능한 모든 할인율 조합 탐색
    for discount_rates in product(range(4), repeat=len(emoticons)):
        cur_subscribe = 0
        cur_income = 0
        
        for hope_rate, budget in users:
            cost = 0
            for emoticon, rate_idx in zip(emoticons, discount_rates):
                # 현재 이모티콘의 할인율이 유저의 희망 할인율 이상이면 구매
                if discounts[rate_idx] >= hope_rate:
                    # 정수 연산을 이용한 할인 가격 계산 (부동소수점 오차 방지)
                    cost += emoticon * (100 - discounts[rate_idx]) // 100
            
            # 총 비용이 예산 이상이면 플러스 서비스 가입, 미만이면 매출 합산
            if cost >= budget:
                cur_subscribe += 1
            else:
                cur_income += cost
                
        # 최적의 결과 갱신 (1순위: 가입자 수 최대, 2순위: 판매액 최대)
        if cur_subscribe > max_subscribe:
            max_subscribe = cur_subscribe
            max_income = cur_income
        elif cur_subscribe == max_subscribe and cur_income > max_income:
            max_income = cur_income
            
    return [max_subscribe, max_income]