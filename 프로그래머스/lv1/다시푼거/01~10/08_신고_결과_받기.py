def solution(id_list, report, k):
    report = set(report)
    report_count = {id : 0 for id in id_list}
    report_user = {id : [] for id in id_list}
    
    for r in report :
        a, b = r.split()
        report_count[b] += 1
        report_user[a].append(b)
    
    return [sum(1 for y in report_user[x] if report_count[y] >= k) for x in id_list]