def convert_date(date) :
    y, m, d = map(int, date.split('.'))
    return 12 * 28 * (y - 1) + 28 * (m - 1) + d

def solution(today, terms, privacies) :
    today = convert_date(today)
    term_dict = {}
    for i, term in enumerate(terms) :
        policy, duration = term.split()
        term_dict[policy] = int(duration) * 28
    
    answer = []
    for i, privacy in enumerate(privacies) :
        date, policy = privacy.split()
        limit = convert_date(date) + term_dict[policy] - 1
        if limit < today :
            answer.append(i + 1)
    return answer