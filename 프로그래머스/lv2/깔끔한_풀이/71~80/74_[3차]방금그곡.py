def parse_notes(notes):
    """C#, D# 등의 음을 소문자 단일 문자로 치환하여 1글자로 맞춤"""
    return (notes.replace('C#', 'c')
                 .replace('D#', 'd')
                 .replace('F#', 'f')
                 .replace('G#', 'g')
                 .replace('A#', 'a'))

def solution(m, musicinfos):
    m = parse_notes(m)
    answer = '(None)'
    max_duration = -1  # 재생 시간이 0분인 경우를 대비해 -1로 초기화
    
    for info in musicinfos:
        start_str, end_str, title, notes = info.split(',')
        
        # 시작 시간과 종료 시간을 분 단위로 변환
        start_min = int(start_str[:2]) * 60 + int(start_str[3:])
        end_min = int(end_str[:2]) * 60 + int(end_str[3:])
        duration = end_min - start_min
        
        notes = parse_notes(notes)
        note_len = len(notes)
        
        # 재생된 시간(duration) 동안 실제로 연주된 전체 악보 생성
        played_notes = (notes * (duration // note_len + 1))[:duration]
        
        # 네오가 기억한 멜로디(m)가 연주된 악보에 포함되어 있는지 확인
        if m in played_notes:
            # 조건 1: 재생 시간이 더 긴 음악 우선
            # 조건 2: 재생 시간이 같다면 먼저 입력된 음악 유지 (초과 조건 사용)
            if duration > max_duration:
                max_duration = duration
                answer = title
                
    return answer