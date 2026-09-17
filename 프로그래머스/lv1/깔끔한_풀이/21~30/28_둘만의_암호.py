import string

def solution(s, skip, index):
    # skip을 제외한 알파벳만 남긴 리스트 생성 (전역변수 문제 해결)
    valid_alphabets = [ch for ch in string.ascii_lowercase if ch not in set(skip)]
    n = len(valid_alphabets)
    
    # 각 알파벳의 인덱스 매핑 (조회 성능 최적화)
    char_to_idx = {ch: i for i, ch in enumerate(valid_alphabets)}
    
    answer = []
    for ch in s:
        # 현재 위치에서 index만큼 이동 후 나머지 연산
        new_idx = (char_to_idx[ch] + index) % n
        answer.append(valid_alphabets[new_idx])
        
    return "".join(answer)