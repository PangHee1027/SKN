# 필요한 라이브러리 임포트
import streamlit as st
import pymysql

# 1. 웹 화면 제목 설정
st.title("대륙 및 인구수 조건별 도시 검색")

# 2. PyMySQL을 이용하여 DB 데이터 조회 함수 정의
def get_cities():
    conn = pymysql.connect(
        host='localhost', 
        user='root', 
        password='1234',
        database = 'world', 
        charset='utf8mb4', 
        cursorclass=pymysql.cursors.DictCursor
    )
    
    with conn.cursor() as cursor:
        sql = """
        SELECT C.Name AS 도시명, CO.Name AS 국가명, C.Population AS 인구수
        FROM city C
        INNER JOIN country CO ON C.CountryCode = CO.Code
        WHERE CO.Continent = %s AND C.Population >= %s
        ORDER BY C.Population DESC LIMIT 10;
        """
        cursor.execute(sql, (st.session_state["continent"], st.session_state["min_population"]))
	# list[dict] 반환
        return cursor.fetchall() 
    
    conn.close()

if 'continent' not in st.session_state :
    st.session_state['continent'] = "Asia"

with st.sidebar:
    continent = st.selectbox("대륙선택", ("Asia", "Africa", "Europe", "South America", "Oceania", "Antartica", "North America"))
    st.session_state['continent'] = continent

with st.form(key="search_form"):
    min_population = st.number_input(
        label="최소 인구수를 입력하세요",
        value=0,
        step=100000,
        format="%d"
    )
    st.session_state['min_population'] = min_population
    # 폼 제출 버튼
    submit_button = st.form_submit_button(label="도시 검색 실행")

# 2. 버튼이 클릭되었을 때의 동작 처리
if submit_button:
    # session_state에서 선택된 대륙값 가져오기
    selected_continent = st.session_state["continent"]
    
    # 초록색 성공 박스로 결과 메시지 표시
    st.success(f"{selected_continent} 대륙 / {min_population:,}명 이상 도시 검색 완료!")
    data = get_cities()

    st.table(data)
    # TODO: 데이터베이스(PyMySQL) 조회 및 검색된 도시 테이블(st.dataframe 등) 출력 로직 작성

# 3. 데이터 로드 및 Streamlit 표출

st.divider()

# list[dict] 데이터를 깔끔한 표 형태로 웹에 출력
 