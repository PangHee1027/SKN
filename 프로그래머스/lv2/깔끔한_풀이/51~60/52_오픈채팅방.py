def solution(record):
    user_name_dict = {}
    user_actions = []

    # 1. 닉네임 업데이트 및 출력 로그 추출
    for log in record:
        info = log.split()
        action, uid = info[0], info[1]

        if action in ("Enter", "Change"):
            user_name_dict[uid] = info[2]

        if action in ("Enter", "Leave"):
            user_actions.append((action, uid))

    # 2. 메시지 템플릿 매핑
    printer = {"Enter": "님이 들어왔습니다.", "Leave": "님이 나갔습니다."}

    # 3. 리스트 컴프리헨션으로 최종 결과 생성
    return [
        f"{user_name_dict[uid]}{printer[action]}" for action, uid in user_actions
    ]