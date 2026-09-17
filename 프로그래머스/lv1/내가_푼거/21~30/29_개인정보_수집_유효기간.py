def expiration_date(date, term) :
    y, m, d = map(int, date.split("."))
    y = y + ((m + term) // 12 - 1 if (m + term) % 12 == 0 else (m + term) // 12)
    m = (m + term) % 12 if (m + term) % 12 != 0 else 12
    return [y, m, d]


def solution(today, terms, privacies):
    terms_dict = {a.split()[0] : int(a.split()[1]) for a in terms}
    privacies_dict = [[a.split()[0], terms_dict[a.split()[1]]] for a in privacies]
    ex_date = []

    for i in privacies_dict :
        ex_date.append(expiration_date(i[0], i[1]))

    today = list(map(int, today.split(".")))
    answer = []

    for i, x in enumerate(ex_date) :
        y, m, d = x[0], x[1], x[2]
        if y < today[0] :
            answer.append(i + 1)
        elif y == today[0] and m < today[1] :
            answer.append(i + 1)
        elif y == today[0] and m == today[1] and d <= today[2] :
            answer.append(i + 1)
    return answer

# print(solution("2020.01.01", ["Z 3", "D 5"], ["2019.01.01 D", "2019.11.15 Z", "2019.08.02 D", "2019.07.01 D", "2018.12.28 Z"]))