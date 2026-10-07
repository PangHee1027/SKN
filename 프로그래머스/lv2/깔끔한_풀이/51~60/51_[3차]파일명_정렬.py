import re

def solution(files):
    # 정렬 기준을 만들어주는 키 함수 정의
    def sort_key(file):
        # re.split()으로 파일명을 (HEAD, NUMBER, TAIL)로 분리
        # r'(\d{1,5})' : 1~5자리의 연속된 숫자를 캡처 그룹()으로 묶어 분리 기준으로 사용
        # maxsplit=1    : 첫 번째로 일치하는 숫자 패턴에서 딱 1번만 split 수행
        parts = re.split(r"(\d{1,5})", file, maxsplit=1)

        # parts[0] -> HEAD (대소문자 구분이 없으므로 소문자로 통일)
        # parts[1] -> NUMBER (문자열 '012'를 정수 12로 변환하여 숫자 크기로 비교)
        return (parts[0].lower(), int(parts[1]))

    # 파이썬의 sorted()는 기본적으로 입력 순서를 보장하는 '안정 정렬(Stable Sort)'입니다.
    # 따라서 (HEAD 소문자, NUMBER 정수) 튜플을 기준으로 정렬하면 조건 1, 2, 3이 모두 만족됩니다.
    return sorted(files, key=sort_key)