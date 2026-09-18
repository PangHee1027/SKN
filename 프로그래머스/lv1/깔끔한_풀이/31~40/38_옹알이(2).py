def solution(babbling):
    answer = 0
    baby_words = ["aya", "ye", "woo", "ma"]

    for b in babbling:
        # 연속된 발음이 포함되어 있으면 건너뜀
        if any(word * 2 in b for word in baby_words):
            continue

        # 발음할 수 있는 단어를 공백(' ')으로 대체 (단어가 이어져서 잘못 결합되는 것 방지)
        for word in baby_words:
            b = b.replace(word, " ")

        # 공백을 모두 제거했을 때 빈 문자열만 남으면 발음 가능한 단어
        if b.strip() == "":
            answer += 1

    return answer