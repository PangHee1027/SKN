import json
import requests
import pandas as pd
import os
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("도서관_정보나루")
url = f"http://data4library.kr/api/loanItemSrch?authKey={api_key}&startDt=2025-01-01&format=json"

# CSV 저장 경로
file_path = "C:\\Users\\playdata2\\work\\SKN\\데이터수집\\오픈API\\2025_2026_20대_인기도서_200위.csv"

data = requests.get(url).text
python_dict = json.loads(data)

# 1. JSON 데이터의 docs 리스트 추출
docs = python_dict["response"]["docs"]

# 2. DB 테이블(book_table) 컬럼명에 맞춰 데이터 매핑
book_list = []
for item in docs:
    book_info = item["doc"]

    # pub_year를 INT 형으로 변환 (데이터가 없을 경우 None 처리)
    pub_year_val = book_info.get("publication_year")
    try:
        pub_year_val = int(pub_year_val) if pub_year_val else None
    except ValueError:
        pub_year_val = None

    book_list.append({
        "no": int(book_info.get("no")),  # 순번 (PRIMARY KEY)
        "ranking": int(book_info.get("ranking")),  # 대출 순위
        "book_name": book_info.get("bookname"),  # 도서명
        "author_name": book_info.get("authors"),  # 저자명
        "publisher": book_info.get("publisher"),  # 출판사
        "pub_year": pub_year_val,  # 출판년도 (INT)
        "isbn13": str(book_info.get("isbn13")),  # 13자리 ISBN
        "addition_symbol": book_info.get("addition_symbol"),  # 부가기호
        "vol": book_info.get("vol"),  # 권
        "class_no": book_info.get("class_no"),  # 주제분류번호
        "class_nm": book_info.get("class_nm"),  # 주제분류명
        "loan_count": int(book_info.get("loan_count", 0)),  # 대출건수
        "cover_url": book_info.get("bookImageURL"),  # 책표지 URL
        "detail_url": book_info.get("bookDtlUrl"),  # 도서상세 URL
    })

# 3. DataFrame 변환
df = pd.DataFrame(book_list)

# 4. CSV 파일 저장 (MySQL Table Data Import Wizard용 euc-kr 지정)
df.to_csv(file_path, index=False, encoding="euc-kr")

print("MySQL book_table 규격에 맞춘 CSV 파일 생성 완료!")