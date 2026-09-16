def solution(survey, choices):

    my_dict = {"RT":0,"CF":0,"JM":0,"AN":0}
    # zip = 묶음 자료형들을 하나의 튜플로 묶음
    # 해봤던 생각인데, zip() 함수를 몰라서 못했음
    for A,B in zip(survey,choices):
        if A not in my_dict.keys():
            # 만약 A 가 리스트의 없다면, A를 뒤집음
            # 슬라이싱으로 문자열 뒤집기도 해본적 없는 생각임
            A = A[::-1]
            # B - 4 == B의 값을 -3 ~ 3까지로 만듬
            # 이 경우 뒤집은 상태 (원래 값의 반대)임으로 값에 -를 해줌
            my_dict[A] -= B-4
        else:
            my_dict[A] += B-4

    result = ""
    for name in my_dict.keys():
        # 앞에 성향이 더 강하면 앞에거
        if my_dict[name] > 0:
            result += name[1]
        # 뒤에 성향이 더 강하면 뒤에거
        elif my_dict[name] < 0:
            result += name[0]
        # 같다면 사전 순 앞에 거
        else:
            result += sorted(name)[0]

    return result