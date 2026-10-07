def solution(record):
    user_name_dict = {}
    user_action = []
    answer = []

    for log in record :
        log_info = log.split(" ")
        action, uid, username = log_info[0], log_info[1], log_info[2] if len(log_info) == 3 else ""
        user_action.append([uid, action])
        if action == "Enter" or action == "Change":
            user_name_dict[uid] = username
    
    for uid, action in user_action :
        match action :
            case "Enter" :
                answer.append(f"{user_name_dict[uid]}님이 들어왔습니다.")
            case "Change" :
                continue
            case "Leave" :
                answer.append(f"{user_name_dict[uid]}님이 나갔습니다.")
    
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))