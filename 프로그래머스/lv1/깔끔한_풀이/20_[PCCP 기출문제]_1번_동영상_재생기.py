# 4번이나 반복하는데 함수를 쓸 생각을 안했음
def to_seconds(time_str):
    m, s = map(int, time_str.split(":"))
    return m * 60 + s

def solution(video_len, pos, op_start, op_end, commands):
    # 1. 모든 시간 입력을 초(초 단위 정수)로 변환
    video_len = to_seconds(video_len)
    pos = to_seconds(pos)
    op_start = to_seconds(op_start)
    op_end = to_seconds(op_end)

    # 2. 시작 위치가 오프닝 구간인 경우 처리
    if op_start <= pos <= op_end:
        pos = op_end

    # 3. 명령어 수행
    for c in commands:
        if c == "prev":
            # 굳이 중첩 조건문을 쓸 필요가 없구만
            pos = max(0, pos - 10)
        elif c == "next":
            pos = min(video_len, pos + 10)
        
        # 이동 후 오프닝 구간 체크
        if op_start <= pos <= op_end:
            pos = op_end

    # 4. "mm:ss" 포맷 변환 후 반환
    return f"{pos // 60:02d}:{pos % 60:02d}"