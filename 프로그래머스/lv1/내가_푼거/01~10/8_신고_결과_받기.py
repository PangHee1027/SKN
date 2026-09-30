def solution(id_list, report, k):
    report_dict = {}
    user_report_count = {}
    answer = []

    for i in report :
        a, b = i.split()
        if not report_dict.get(a) :
            report_dict[a] = [b] 
        else :
            report_dict[a].append(b)
            report_dict[a] = list(set(report_dict[a]))

    for value in report_dict.values() :
        for i in value :
            if not user_report_count.get(i) :
                user_report_count[i] = 1
            else :
                user_report_count[i] += 1

    for i in id_list :
        count = 0
        if report_dict.get(i) :
            for j in report_dict[i] :
                if user_report_count[j] >= k :
                    count += 1
        answer.append(count)
    
    return answer

# print(solution(	["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
