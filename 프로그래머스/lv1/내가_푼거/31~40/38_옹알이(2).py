def solution(babbling):
    baby_word = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in babbling :
        last_word = ""
        can_speak = True
        while can_speak and len(i) != 0 :
            current_word = [i[:2], i[:3]]
            if last_word in current_word  :
                can_speak = False
                break
            if current_word[0] in baby_word :
                i = i[len(current_word[0]):]
                last_word = current_word[0]
                continue
            elif current_word[1] in baby_word :
                i = i[len(current_word[1]):]
                last_word = current_word[0]
                continue
            else :
                can_speak = False
        if can_speak :
            answer += 1
    return answer       

# print(solution(["aya", "yee", "u", "maa"]))