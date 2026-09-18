import os
import math
import requests
import pandas as pd
from dotenv import load_dotenv

# 1. 환경 변수(.env)에서 API KEY 불러오기
load_dotenv()
API_KEY = os.getenv("서울_열린데이터_광장")

if not API_KEY:
    raise ValueError(".env 파일에 'SEOUL_DATA_API_KEY'가 설정되어 있지 않습니다.")

SERVICE_NAME = "VwsmTrdarSelngQq"
BASE_URL = f"http://openapi.seoul.go.kr:8088/{API_KEY}/json/{SERVICE_NAME}"

# 수집 대상 분기 목록 (2024년 1분기 ~ 2025년 3분기)
TARGET_QUARTERS = [
    "20241", "20242", "20243", "20244",
    "20251", "20252", "20253"
]

def fetch_quarter_data(quarter: str) -> pd.DataFrame:
    """
    특정 분기(quarter)의 전체 데이터를 페이징 처리하여 수집하는 함수
    """
    # 1. 해당 분기의 전체 개수(list_total_count) 확인을 위한 첫 번째 호출
    init_url = f"{BASE_URL}/1/1/{quarter}"
    res = requests.get(init_url)
    data = res.json()
    
    if SERVICE_NAME not in data:
        print(f"[{quarter}] 데이터 요청 실패: {data.get('RESULT', {}).get('MESSAGE', '알 수 없는 오류')}")
        return pd.DataFrame()
    
    total_count = data[SERVICE_NAME]["list_total_count"]
    print(f"[{quarter}] 전체 데이터 건수: {total_count:,}건 수집 시작...")
    
    # 1,000건 단위 페이징 수집
    page_size = 1000
    total_pages = math.ceil(total_count / page_size)
    
    all_rows = []
    for page in range(total_pages):
        start_idx = page * page_size + 1
        end_idx = min((page + 1) * page_size, total_count)
        
        url = f"{BASE_URL}/{start_idx}/{end_idx}/{quarter}"
        response = requests.get(url)
        
        if response.status_code == 200:
            result_json = response.json()
            if SERVICE_NAME in result_json and "row" in result_json[SERVICE_NAME]:
                rows = result_json[SERVICE_NAME]["row"]
                all_rows.extend(rows)
            else:
                print(f"  └ [{quarter}] {start_idx}~{end_idx} 행 수집 중 응답 데이터 없음")
        else:
            print(f"  └ [{quarter}] {start_idx}~{end_idx} HTTP 요청 실패 (Status Code: {response.status_code})")
            
    df_quarter = pd.DataFrame(all_rows)
    return df_quarter

def main():
    all_quarters_df = []
    
    # 2. 지정된 기간 데이터 수집 실행
    for quarter in TARGET_QUARTERS:
        df_q = fetch_quarter_data(quarter)
        if not df_q.empty:
            all_quarters_df.append(df_q)
    
    if not all_quarters_df:
        print("수집된 데이터가 없습니다.")
        return

    # 통합 데이터프레임 생성
    final_df = pd.concat(all_quarters_df, ignore_index=Index) if 'Index' in globals() else pd.concat(all_quarters_df, ignore_index=True)
    
    # CSV 저장
    output_filename = "C:\\Users\\playdata2\\work\\SKN\\데이터수집\\오픈API\\서울시_상권분석서비스_추정매출_상권_20241_20253.csv"
    final_df.to_csv(output_filename, index=False, encoding="utf-8-sig")
    print(f"\n==========================================")
    print(f"데이터 수집 및 파일 저장 완료: {output_filename}")
    print(f"==========================================\n")
    
    # 3. 데이터 검증 실행
    verify_data(output_filename, TARGET_QUARTERS)

def verify_data(file_path: str, expected_quarters: list):
    """
    수집된 CSV 파일을 읽어 분기별 데이터 수집 정상 여부를 검증하는 함수
    """
    print("[데이터 수집 및 저장 검증 결과]")
    df = pd.read_csv(file_path, dtype={'STDR_YYQU_CD': str})
    
    total_rows = len(df)
    print(f"- 저장된 총 데이터 수: {total_rows:,} 행")
    print(f"- 컬럼 수: {len(df.columns)} 개")
    
    # 기준 년분기 코드 컬럼 존재 여부 확인
    quarter_col = "STDR_YYQU_CD"
    if quarter_col not in df.columns:
        print(f"ERR: {quarter_col} 컬럼을 찾을 수 없어 분기별 검증을 진행할 수 없습니다.")
        return
    
    # 분기별 수집 데이터 개수 통계
    quarter_counts = df[quarter_col].value_counts().sort_index()
    
    print("\n[분기별 수집 데이터 건수 요약]")
    for q in expected_quarters:
        count = quarter_counts.get(q, 0)
        status = "정상" if count > 0 else "미수집/데이터없음"
        print(f"  • {q} 분기: {count:,} 건 ({status})")
        
    print("\n[결측치 상위 5개 컬럼]")
    print(df.isnull().sum().sort_values(ascending=False).head(5))

if __name__ == "__main__":
    main()