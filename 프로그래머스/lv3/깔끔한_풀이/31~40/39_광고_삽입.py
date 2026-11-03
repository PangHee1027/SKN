def convert_time(str_time):
    hour, minute, second = map(int, str_time.split(":"))
    return hour * 3600 + minute * 60 + second


def solution(play_time, adv_time, logs):
    play_time = convert_time(play_time)
    adv_time = convert_time(adv_time)

    play_time_prefix = [0] * (play_time + 2)
    for log in logs:
        log_start, log_end = map(convert_time, log.split("-"))
        play_time_prefix[log_start] += 1
        play_time_prefix[log_end] -= 1

    # 누적합 1회: 각 초당 시청 중인 사람 수
    for i in range(1, play_time + 2):
        play_time_prefix[i] += play_time_prefix[i - 1]

    # 누적합 2회: 누적 재생 시간 계산
    for i in range(1, play_time + 2):
        play_time_prefix[i] += play_time_prefix[i - 1]

    best_time = 0
    max_view_time = 0

    # 슬라이딩 윈도우로 최적의 광고 시작 시각 탐색
    for start_time in range(0, play_time - adv_time + 1):
        end_time = start_time + adv_time
        cur_view_time = play_time_prefix[end_time - 1]

        if start_time > 0:
            cur_view_time -= play_time_prefix[start_time - 1]

        if cur_view_time > max_view_time:
            best_time = start_time
            max_view_time = cur_view_time

    hour = best_time // 3600
    minute = (best_time % 3600) // 60
    second = best_time % 60

    return f"{hour:02d}:{minute:02d}:{second:02d}"