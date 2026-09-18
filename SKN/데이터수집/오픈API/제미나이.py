import pandas as pd
import requests


def fetch_popular_books(auth_key):
    # API 요청 URL[cite: 1, 2]
    url = "http://data4library.kr/api/loanItemSrch"

    # API 요청 파라미터 설정
    params = {
        "authKey": auth_key,  # 발급받은 인증키[cite: 1, 2]
        "startDt": "2025-01-01",  # 검색 시작일[cite: 1, 2]
        "endDt": "2026-06-30",  # 검색 종료일[cite: 1, 2]
        "age": "20",  # 20대 대상
        "pageNo": "1",  # 첫 번째 페이지[cite: 1, 2, 3]
        "pageSize": "200",  # 상위 200개 출력[cite: 1, 2, 3]
        "format": "json",  # JSON 응답 포맷 지정
    }

    try:
        # API 호출[cite: 1, 2]
        response = requests.get(url, params=params)
        response.raise_for_status()

        data = response.json()

        # 도서 목록 추출 (response -> docs)[cite: 1, 3]
        docs = data.get("response", {}).get("docs", [])

        if not docs:
            print("수집된 데이터가 없거나 인증키를 확인해야 합니다.")
            return

        book_list = []
        for item in docs:
            doc = item.get("doc", {})
            # 매뉴얼 항목 매핑[cite: 1, 2, 3]
            book_info = {
                "순번": doc.get("no"),
                "순위": doc.get("ranking"),
                "도서명": doc.get("bookname"),
                "저자명": doc.get("authors"),
                "출판사": doc.get("publisher"),
                "출판년도": doc.get("publication_year"),
                "ISBN13": doc.get("isbn13"),
                "ISBN부가기호": doc.get("addition_symbol"),
                "권": doc.get("vol"),
                "주제분류코드": doc.get("class_no"),
                "주제분류명": doc.get("class_nm"),
                "대출건수": doc.get("loan_count"),
                "책표지URL": doc.get("bookImageURL"),
                "상세페이지URL": doc.get("bookDtlUrl"),
            }
            book_list.append(book_info)

        # 데이터프레임 생성 및 CSV 저장
        df = pd.DataFrame(book_list)
        output_file = "C:\\Users\\playdata2\\work\\SKN\\데이터수집\\오픈API\\popular_books_20s_2025_2026.csv"

        # utf-8-sig 인코딩으로 저장하여 Excel에서 한글 깨짐 방지
        df.to_csv(output_file, index=False, encoding="euc-kr")
        print(
            f"수집 완료: 총 {len(df)}건의 도서 정보가 '{output_file}'로 저장되었습니다."
        )

    except requests.exceptions.RequestException as e:
        print(f"API 요청 중 네트워크/HTTP 오류 발생: {e}")
    except Exception as e:
        print(f"데이터 처리 중 오류 발생: {e}")


if __name__ == "__main__":
    # 도서관 정보나루에서 발급받은 본인의 인증키(authKey)로 변경해주세요.[cite: 1, 2]
    AUTH_KEY = "b519ff70dc2780e49abc0ccd2280bd792f809ef8435a852aaa390e4890f4bfbd"
    fetch_popular_books(AUTH_KEY)