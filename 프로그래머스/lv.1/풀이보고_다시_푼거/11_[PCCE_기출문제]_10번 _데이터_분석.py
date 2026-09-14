def solution(data, ext, val_ext, sort_by):
    # 나는 match-case로 풀었는데 이걸 딕셔너리로 만들어서 처리를 간단하게 함
    column_idx = {"code": 0, "date": 1, "maximum": 2, "remain": 3}
    # data에서 ext의값 기준으로 val_ext 보다 큰것을 filter()로 걸러냄
    # lamda 이거 익숙해져야 할 듯
    # filter() 조건에 맞는 값만 포함된 것을 반환
    # 위의 처리한 것을 sort_by의 값을 기준으로 정렬
    return sorted(filter(lambda x:x[column_idx[ext]] < val_ext,data),key=lambda x:x[column_idx[sort_by]])
