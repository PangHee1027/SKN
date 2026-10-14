def solution(s):
    min_len = len(s)
    max_compression = len(s) // 2

    for i in range(1, max_compression + 1):
        cur_len = 0
        prev = s[0:i]
        count = 1

        # i 크기만큼씩 잘라서 비교
        for j in range(i, len(s), i):
            curr = s[j:j + i]
            if prev == curr:
                count += 1
            else:
                # 이전 문자열 길이 + 반복 횟수 자릿수 추가 (2 이상일 때만)
                cur_len += len(prev)
                if count > 1:
                    cur_len += len(str(count))
                prev = curr
                count = 1

        # 마지막에 남은 문자열 처리
        cur_len += len(prev)
        if count > 1:
            cur_len += len(str(count))

        min_len = min(min_len, cur_len)

    return min_len