from collections import Counter

def make_multiset(s):
    # 소문자 변환 후 알파벳 2글자인 경우만 리스트로 반환
    s = s.lower()
    return [s[i:i+2] for i in range(len(s) - 1) if s[i:i+2].isalpha()]

def solution(str1, str2):
    # 1. 두 문자열을 다중집합(Counter)으로 변환
    c1 = Counter(make_multiset(str1))
    c2 = Counter(make_multiset(str2))
    
    # 2. Counter의 다중집합 연산자(&, |)를 활용해 교집합, 합집합 계산
    intersection = sum((c1 & c2).values())
    union = sum((c1 | c2).values())
    
    # 3. 모두 공집합인 경우 (합집합이 0인 경우) 예외 처리
    if union == 0:
        return 65536
        
    # 4. 자카드 유사도 계산 후 65536 곱한 정수부 반환
    return int(intersection / union * 65536)