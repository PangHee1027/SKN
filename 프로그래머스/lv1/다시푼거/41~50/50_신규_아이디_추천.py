import re

def solution(new_id):
    # 1단계: 대문자를 소문자로 치환
    new_id = new_id.lower()
    
    # 2단계: 알파벳 소문자, 숫자, 빼기(-), 밑줄(_), 마침표(.)를 제외한 모든 문자 제거
    new_id = re.sub(r'[^a-z0-9-_.]', '', new_id)
    
    # 3단계: 마침표(.)가 2번 이상 연속된 부분을 하나의 마침표(.)로 치환
    new_id = re.sub(r'\.+', '.', new_id)
    
    # 4단계: 처음이나 끝에 위치한 마침표(.) 제거
    new_id = re.sub(r'^\.+|\.+$', '', new_id)
    
    # 5단계: 빈 문자열이면 "a" 대입
    if not new_id:
        new_id = 'a'
        
    # 6단계: 16자 이상이면 15자로 자르고, 끝에 위치한 마침표(.) 제거
    new_id = re.sub(r'\.+$', '', new_id[:15])
    
    # 7단계: 2자 이하라면 길이가 3이 될 때까지 마지막 문자 반복
    if len(new_id) < 3:
        new_id += new_id[-1] * (3 - len(new_id))
        
    return new_id