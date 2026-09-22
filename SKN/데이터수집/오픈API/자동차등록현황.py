import os
import pandas as pd
import requests
from dotenv import load_dotenv

load_dotenv()

# 1. API 요청 URL 및 파라미터 설정 (5년치 범위: 202109 ~ 202608)
url = "http://stat.molit.go.kr/portal/openapi/service/rest/getList.do"

params = {
    "key": os.getenv("국토교통부"),  # 발급받은 OPEN API 인증키
    "form_id": "5498",  # 자동차등록대수현황 시도별
    "style_num": "2",
    "start_dt": "202109",  # 시작연월 (5년 전)
    "end_dt": "202608",    # 종료연월 (최신)
}

# 2. API 호출
response = requests.get(url, params=params)

# 3. 데이터 확인 및 가공 후 CSV 저장
if response.status_code == 200:
    data = response.json()

    # API 응답 상태 확인
    status_code = data.get("result_status", {}).get("status_code")

    if status_code == "INFO-000":
        # formList 추출 및 DataFrame 생성
        form_list = data["result_data"]["formList"]
        df = pd.DataFrame(form_list)

        # 수치형 데이터 변환 및 결측치 처리
        num_cols = ["승합>계", "승용>계", "특수>계"]
        for col in num_cols:
            df[col] = pd.to_numeric(df[col], errors="coerce").fillna(0)

        # 월(date) 및 시도명(시도명) 기준 그룹화 및 합계 집계
        grouped_df = df.groupby(["date", "시도명"], as_index=False)[num_cols].sum()

        # 컬럼명 정리
        grouped_df.rename(
            columns={
                "date": "기준월",
                "시도명": "시도",
                "승합>계": "승합차",
                "승용>계": "승용차",
                "특수>계": "특수차",
            },
            inplace=True,
        )

        # 열 및 행 정렬 (기준월 오름차순, 시도별 정렬)
        grouped_df = grouped_df[["기준월", "시도", "승합차", "승용차", "특수차"]]
        grouped_df.sort_values(by=["기준월", "시도"], ascending=[True, True], inplace=True)

        # CSV 파일 저장 (utf-8-sig 사용으로 엑셀 한글 깨짐 방지)
        file_name = "C:/Users/playdata2/work/SKN/데이터수집/오픈API/시도별_월별_자동차등록대수_5년치.csv"
        grouped_df.to_csv(file_name, index=False, encoding="euc-kr")

        print(f"성공적으로 '{file_name}' 파일로 저장되었습니다.")
    else:
        print(f"API 오류: {data.get('result_status', {}).get('message')}")
else:
    print(f"HTTP 요청 실패 (상태 코드: {response.status_code})")