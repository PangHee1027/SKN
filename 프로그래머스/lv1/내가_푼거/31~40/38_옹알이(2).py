def solution(babbling):
    baby_word = ["aya", "ye", "woo", "ma"]
    answer = 0
    for i in babbling :
        last_word = ""
        while True :
            current_word = [i[:2], i[:3]]
            if current_word == last_word :
                break
            if current_word[0] in baby_word or current_word[1] in baby_word :
                i = i[len(current_word):]
                continue
            break
        else :
            answer += 1
    return answer
            

print(solution(["ayaye", "uuu", "yeye", "yemawoo", "ayaayaa"]))