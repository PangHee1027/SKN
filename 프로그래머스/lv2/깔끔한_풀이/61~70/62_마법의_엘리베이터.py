def solution(storey):
  answer = 0

  while storey > 0:
    # 몫(다음 자릿수들)과 나머지(현재 1의 자릿수)를 동시에 추출
    storey, cur = divmod(storey, 10)

    if cur < 5:
      answer += cur
    elif cur > 5:
      answer += 10 - cur
      storey += 1  # 올림 발생
    else:  # cur == 5 인 경우
      # 다음 자릿수가 5 이상이면 올림을 해주는 것이 다음 연산에서 돌을 아낄 수 있음
      if storey % 10 >= 5:
        storey += 1
      answer += 5

  return answer