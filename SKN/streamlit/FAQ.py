import streamlit as st
import pymysql
import pandas as pd

# 페이지 기본 설정
st.set_page_config(
    page_title="차량 FAQ 조회 시스템",
    page_icon="🚗",
    layout="wide"
)

# ---------------------------------------------------------
# 1. MySQL 데이터베이스 연결 함수
# ---------------------------------------------------------
# DB 접속 정보를 본인의 환경에 맞게 수정하세요.
DB_CONFIG = {
    'host': 'localhost',
    'port': 3306,
    'user': 'root',          # MySQL 사용자명
    'password': '1234',  # MySQL 비밀번호
    'db': 'vehiclesdb',       # 데이터베이스명
    'charset': 'utf8mb4'
}

@st.cache_resource
def get_connection():
    """데이터베이스 연결 생성"""
    return pymysql.connect(**DB_CONFIG)

def fetch_data(query, params=None):
    """SQL 쿼리를 실행하여 DataFrame으로 반환"""
    try:
        conn = get_connection()
        conn.ping(reconnect=True)  # 연결 끊김 방지
        with conn.cursor(pymysql.cursors.DictCursor) as cursor:
            cursor.execute(query, params or ())
            result = cursor.fetchall()
            return pd.DataFrame(result)
    except Exception as e:
        st.error(f"데이터베이스 오류가 발생했습니다: {e}")
        return pd.DataFrame()


# ---------------------------------------------------------
# 2. 메인 화면 레이아웃 및 UX
# ---------------------------------------------------------
st.title("🚗 차량 제조사별 FAQ 검색")
st.caption("현대자동차 및 기아의 FAQ 정보를 조회할 수 있는 페이지입니다.")
st.divider()

# 메인 화면에 2개 컬럼 생성 (제조사 선택 / 카테고리 선택)
col1, col2 = st.columns([1, 2])

with col1:
    # 제조사 선택
    manufacturer = st.radio(
        "🚘 **제조사를 선택하세요**",
        options=["현대자동차", "기아"],
        horizontal=True
    )

# 선택된 제조사에 따라 테이블명 지정
table_name = "hyundai_faq" if manufacturer == "현대자동차" else "kia_faq"

# 해당 테이블의 컬럼 목록 확인 쿼리
columns_df = fetch_data(f"SHOW COLUMNS FROM {table_name}")

if not columns_df.empty:
    column_list = columns_df['Field'].tolist()

    # 테이블 구조 파악 (Major_Category 유무 확인)
    has_major = 'Major_Category' in column_list
    has_category = 'Category' in column_list

    with col2:
        # 카테고리 드롭다운 선택
        if has_major:
            # 첫 번째 이미지 형태의 테이블 (Major_Category, M_Category 존재)
            major_categories_df = fetch_data(f"SELECT DISTINCT Major_Category FROM {table_name} WHERE Major_Category IS NOT NULL")
            categories = ["전체"] + major_categories_df['Major_Category'].tolist() if not major_categories_df.empty else ["전체"]
            selected_category = st.selectbox("📂 **카테고리 선택**", categories)

        elif has_category:
            # 두 번째 이미지 형태의 테이블 (Category 존재)
            categories_df = fetch_data(f"SELECT DISTINCT Category FROM {table_name} WHERE Category IS NOT NULL")
            categories = ["전체"] + categories_df['Category'].tolist() if not categories_df.empty else ["전체"]
            selected_category = st.selectbox("📂 **카테고리 선택**", categories)
        else:
            selected_category = "전체"

    st.divider()

    # ---------------------------------------------------------
    # 3. FAQ 데이터 조회 및 표시
    # ---------------------------------------------------------
    # SQL 조건문 구성
    where_clause = ""
    params = []

    if selected_category != "전체":
        if has_major:
            where_clause = "WHERE Major_Category = %s"
            params.append(selected_category)
        elif has_category:
            where_clause = "WHERE Category = %s"
            params.append(selected_category)

    query = f"SELECT * FROM {table_name} {where_clause} ORDER BY FAQ_id ASC"
    faq_data = fetch_data(query, params)

    # 결과 출력
    st.subheader(f"📌 {manufacturer} FAQ 목록 (총 {len(faq_data)}건)")

    if faq_data.empty:
        st.info("해당 조건에 맞는 FAQ 데이터가 없습니다.")
    else:
        for idx, row in faq_data.iterrows():
            # 카테고리 태그 표시 설정
            cat_tag = ""
            if has_major and pd.notna(row.get('Major_Category')):
                m_cat = f" > {row['M_Category']}" if pd.notna(row.get('M_Category')) else ""
                cat_tag = f"[{row['Major_Category']}{m_cat}] "
            elif has_category and pd.notna(row.get('Category')):
                cat_tag = f"[{row['Category']}] "

            question_text = f"Q{idx + 1}. {cat_tag}{row['Question']}"

            # 질문 클릭 시 답변이 펼쳐지는 Accordion(Expander) 형태
            with st.expander(question_text):
                st.markdown(f"**A.** {row['Answer']}")

else:
    st.warning(f"'{table_name}' 테이블 정보를 불러올 수 없습니다. DB 및 테이블 이름을 확인해 주세요.")