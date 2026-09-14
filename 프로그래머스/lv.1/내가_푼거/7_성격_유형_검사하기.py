mbti = [["R", "T"], ["C", "F"], ["J", "M"], ["A", "N"]]
survey_list = {"RT" : [3, 2, 1, 0, -1, -2, -3],
               "TR" : [-3, -2, -1, 0, 1, 2, 3],
               "CF" : [3, 2, 1, 0, -1, -2, -3],
               "FC" : [-3, -2, -1, 0, 1, 2, 3],
               "JM" : [3, 2, 1, 0, -1, -2, -3],
               "MJ" : [-3, -2, -1, 0, 1, 2, 3],
               "AN" : [3, 2, 1, 0, -1, -2, -3],
               "NA" : [-3, -2, -1, 0, 1, 2, 3],
               }
mbti_score = {"R" : 0, "C" : 0, "J" : 0, "A" : 0}

def solution(survey, choices):
    for i in range(len(survey)) :
        if "R" in survey[i] :
            mbti_score["R"] += survey_list[survey[i]][choices[i] - 1]
        elif "F" in survey[i] :
            mbti_score["C"] += survey_list[survey[i]][choices[i] - 1]
        elif "J" in survey[i] :
                mbti_score["J"] += survey_list[survey[i]][choices[i] - 1]
        elif "A" in survey[i] :
                mbti_score["A"] += survey_list[survey[i]][choices[i] - 1]
    answer = ''
    answer += "R" if mbti_score["R"] >= 0 else "T"
    answer += "C" if mbti_score["C"] >= 0 else "F"
    answer += "J" if mbti_score["J"] >= 0 else "M"
    answer += "A" if mbti_score["A"] >= 0 else "N"

    return answer
