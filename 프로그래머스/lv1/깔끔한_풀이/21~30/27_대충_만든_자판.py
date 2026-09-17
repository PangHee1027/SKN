def solution(keymap, targets):
    # 알파벳별 최소 누름 횟수를 저장할 딕셔너리
    key_dict = {}

    # 1. keymap을 순회하며 각 문자의 최소 누름 횟수 계산
    for keys in keymap:
        for idx, char in enumerate(keys):
            # 기존 값과 비교해 더 적게 누르는 횟수로 갱신
            key_dict[char] = min(key_dict.get(char, float('inf')), idx + 1)

    answer = []
    # 2. targets의 문자열들을 확인하며 누름 횟수 합산
    for target in targets:
        total = 0
        for char in target:
            if char in key_dict:
                total += key_dict[char]
            else:
                total = -1  # 작성 불가능한 문자가 있으면 -1 처리 후 중단
                break
        answer.append(total)

    return answer