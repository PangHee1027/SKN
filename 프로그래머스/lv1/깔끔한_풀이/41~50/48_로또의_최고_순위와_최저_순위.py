def solution(lottos, win_nums):
    # 순위 표 (0개/1개 맞춤 -> 6등, 2개 -> 5등, ..., 6개 -> 1등)
    rank = [6, 6, 5, 4, 3, 2, 1]

    # 0의 개수와 일치하는 번호 수
    zero_count = lottos.count(0)
    match_count = len(set(lottos) & set(win_nums))

    # [최고 순위, 최저 순위]
    return [rank[match_count + zero_count], rank[match_count]]