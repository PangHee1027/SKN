def to_days(date_str):
    # 날짜 문자열("YYYY.MM.DD")을 총 일수(Day)로 변환
    y, m, d = map(int, date_str.split("."))
    return y * 12 * 28 + m * 28 + d

def solution(today, terms, privacies):
    # 1. 약관별 유효기간을 '일 수'로 변환해 저장
    terms_dict = {t.split()[0]: int(t.split()[1]) * 28 for t in terms}
    
    # 2. 오늘 날짜를 일 수로 변환
    today_days = to_days(today)
    
    answer = []
    # 3. 각 개인정보의 만료 일수와 오늘 날짜 비교
    for i, p in enumerate(privacies):
        date_str, term_type = p.split()
        expire_days = to_days(date_str) + terms_dict[term_type]
        
        # 만료 일수가 오늘 날짜보다 작거나 같으면 이미 만료된 정보
        if expire_days <= today_days:
            answer.append(i + 1)
            
    return answer