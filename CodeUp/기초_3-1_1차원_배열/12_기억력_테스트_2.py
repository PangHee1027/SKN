# 고마워요 제미나이!
# 이건 현재 내 능력 밖이다

import sys

def main():
    # 10,000,001개(최대 N, M 범위)의 비트 상태 저장 (약 1.25MB 사용)
    exist = bytearray(1250001)

    # C 스타일 Fast I/O: 전체 입력을 통째로 바이트로 읽음
    input_bytes = sys.stdin.buffer.read()
    length = len(input_bytes)
    idx = 0

    # Fast Integer Parsing 함수
    def get_int():
        nonlocal idx
        # 공백 및 줄바꿈 건너뛰기
        while idx < length and input_bytes[idx] <= 32:
            idx += 1
        if idx >= length:
            return None
        num = 0
        while idx < length and input_bytes[idx] > 32:
            num = num * 10 + (input_bytes[idx] - 48)
            idx += 1
        return num

    # N 읽기
    n = get_int()
    if n is None:
        return

    # N개의 숫자를 bitset에 기록
    for _ in range(n):
        num = get_int()
        exist[num >> 3] |= (1 << (num & 7))

    # M 읽기
    m = get_int()
    if m is None:
        return

    # M개의 숫자를 확인 후 바로 출력 버퍼에 담아 출력
    out = []
    for _ in range(m):
        num = get_int()
        if exist[num >> 3] & (1 << (num & 7)):
            out.append('1')
        else:
            out.append('0')
            
        # 메모리 절약을 위해 20만개씩 끊어서 바로 출력
        if len(out) >= 200000:
            sys.stdout.write(' '.join(out) + ' ')
            out.clear()

    if out:
        sys.stdout.write(' '.join(out))

if __name__ == '__main__':
    main()