def solution(id_list, report, k):
    # 와 이걸 이렇게 할수 있구나, 이거 몰라서 고생했네
    answer = [0] * len(id_list)    
    reports = {x : 0 for x in id_list}
    # 한 사람이 같은 사람 여러번 신고한 걸 제거하려고 set 사용함
    report = set(report)

    for r in report:
        # 신고당한 사람의 신고 수 + 1
        reports[r.split()[1]] += 1

    for r in report:
        # 피신고자가 제한 횟수 이상 신고당했다면
        if reports[r.split()[1]] >= k:
            # 그 사람을 신고한 사람에게 신고처리 메일 +1
            # index() = 해당 데이터가 처음 나타난 인덱스를 반환
            answer[id_list.index(r.split()[0])] += 1

    return answer
