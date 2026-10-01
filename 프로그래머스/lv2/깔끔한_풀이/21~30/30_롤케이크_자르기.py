from collections import Counter

def solution(topping):
    answer = 0
    set1 = set()
    cnt = Counter(topping)  # 1. Counter 자체를 그대로 사용

    for v in topping:
        set1.add(v)
        cnt[v] -= 1
        
        # 2. del 키워드로 깔끔하게 삭제
        if cnt[v] == 0:
            del cnt[v]
            
        if len(set1) == len(cnt):
            answer += 1
        # 3. 철수 가짓수가 동생보다 많아지면 더 이상 같아질 수 없음 (조기 종료)
        elif len(set1) > len(cnt):
            break

    return answer