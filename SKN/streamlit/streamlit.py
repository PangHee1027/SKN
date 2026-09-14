import streamlit as st

# 1. 페이지 기본 설정 (가장 처음에 호출해야 함)
st.set_page_config(
    page_title="Streamlit 세션 상태 종합 대시보드",
    page_icon="🚀",
    layout="wide"
)

# 2. st.session_state 초기화 (테마 및 방명록 데이터 관리)
if 'theme_mode' not in st.session_state:
    st.session_state['theme_mode'] = "라이트 모드"

if 'agree_terms' not in st.session_state:
    st.session_state['agree_terms'] = False

# 방명록 데이터를 session_state로 관리 (초기 더미 데이터 포함)
if 'messages' not in st.session_state:
    st.session_state['messages'] = [
        {"id": 1, "name": "홍길동", "hobby": "코딩", "message": "스트림릿 정말 신기하고 재밌네요!"},
        {"id": 2, "name": "김철수", "hobby": "독서", "message": "파이썬만으로 웹이 만들어져요."}
    ]

# 3. 사이드바 구성 (session_state를 활용한 값 동기화)
with st.sidebar:
    st.header("⚙️ 대시보드 설정")
    st.write("사이드바 영역입니다.")
    
    st.session_state['theme_mode'] = st.radio(
        "모드 선택", 
        ["라이트 모드", "다크 모드"],
        index=0 if st.session_state['theme_mode'] == "라이트 모드" else 1
    )
    
    st.session_state['agree_terms'] = st.checkbox(
        "이용 약관에 동의합니다.", 
        value=st.session_state['agree_terms']
    )
    
    st.markdown("---")
    st.info("💡 팁: 방명록 데이터가 st.session_state에 안전하게 저장되어 새로고침 후에도 유지됩니다.")

# 4. 세션 상태에 저장된 모드 값에 따른 실시간 CSS 주입
if st.session_state['theme_mode'] == "다크 모드":
    dark_css = """
    <style>
        .stApp {
            background-color: #0e1117;
            color: #ffffff;
        }
        [data-testid="stSidebar"] {
            background-color: #262730;
            color: #ffffff;
        }
        h1, h2, h3, h4, h5, h6, p, span, label {
            color: #ffffff !important;
        }
    </style>
    """
    st.markdown(dark_css, unsafe_allow_html=True)

# 5. 메인 타이틀 및 소개
st.title("🚀 Streamlit 세션 상태 종합 대시보드")
st.subheader("st.session_state로 방명록 데이터와 상태를 완벽히 관리합니다.")
st.caption("작성자: 파이썬 학습자 | 세션 기반 방명록 CRUD 예제")

# 6. 컬럼 레이아웃 (상단 지표 영역)
col1, col2, col3 = st.columns(3)

with col1:
    st.metric(label="총 방명록 수", value=f"{len(st.session_state['messages'])}개", delta="+1")

with col2:
    st.metric(label="현재 테마", value=st.session_state['theme_mode'], delta="Active")

with col3:
    st.metric(label="만족도 점수", value="98점", delta="+5점")

st.markdown("---")

# 7. 탭 레이아웃 구성
tab1, tab2, tab3 = st.tabs(["📝 방명록 남기기 / 관리", "📊 데이터 확인 (Table/Chart)", "📖 상세 도움말 (Expander)"])

# [탭 1] 입력 폼 및 st.session_state 활용 방명록 추가/삭제 구현
with tab1:
    st.header("방명록 남기기 및 관리")
    
    # 2단 분할 레이아웃 (왼쪽: 등록 폼 / 오른쪽: 삭제 관리)
    form_col, manage_col = st.columns(2)
    
    with form_col:
        st.subheader("✍️ 새 방명록 작성")
        with st.form(key='guestbook_form'):
            input_name = st.text_input("이름을 입력하세요", max_chars=10)
            input_hobby = st.selectbox("관심 있는 분야는 무엇인가요?", ["코딩", "독서", "운동", "여행", "기타"])
            input_msg = st.text_input("남기고 싶은 한마디를 적어주세요")
            
            submit_button = st.form_submit_button(label="방명록 등록하기")
            
            if submit_button:
                if input_name and input_msg:
                    if st.session_state['agree_terms']:
                        # 고유 ID 생성 (가장 최근 ID + 1 혹은 리스트 길이 기반)
                        new_id = st.session_state['messages'][-1]["id"] + 1 if st.session_state['messages'] else 1
                        
                        # st.session_state 리스트에 새로운 딕셔너리 데이터 추가 (Create)
                        new_entry = {"id": new_id, "name": input_name, "hobby": input_hobby, "message": input_msg}
                        st.session_state['messages'].append(new_entry)
                        
                        st.success(f"{input_name}님, 방명록이 성공적으로 등록되었습니다!")
                    else:
                        st.warning("사이드바에서 이용 약관에 먼저 동의해 주세요.")
                else:
                    st.error("이름과 메시지를 모두 입력해 주세요.")
                    
    with manage_col:
        st.subheader("🗑️ 방명록 삭제 관리")
        if len(st.session_state['messages']) > 0:
            # 삭제할 방명록 선택 옵션 생성 (ID와 작성자 이름 표시)
            delete_options = {f"[{item['id']}] {item['name']} - {item['message']}": item['id'] for item in st.session_state['messages']}
            selected_target = st.selectbox("삭제할 방명록을 선택하세요", options=list(delete_options.keys()))
            
            if st.button("선택한 방명록 삭제"):
                target_id = delete_options[selected_target]
                # st.session_state 리스트에서 해당 ID를 제외한 항목만 다시 필터링하여 저장 (Delete)
                st.session_state['messages'] = [item for item in st.session_state['messages'] if item['id'] != target_id]
                st.success("선택하신 방명록이 삭제되었습니다!")
                st.rerun() # 화면을 즉시 새로고침하여 반영
        else:
            st.info("삭제할 방명록이 없습니다.")

# [탭 2] st.session_state 데이터를 기반으로 표출
with tab2:
    st.header("등록된 방명록 목록")
    
    if len(st.session_state['messages']) > 0:
        # st.session_state에 저장된 리스트를 테이블로 바로 시각화
        st.table(st.session_state['messages'])
        
        st.subheader("📈 관심 분야별 통계 (샘플 차트)")
        chart_data = {"코딩": 5, "독서": 3, "운동": 4, "여행": 2}
        st.bar_chart(chart_data)
    else:
        st.info("아직 등록된 방명록이 없습니다.")

# [탭 3] 익스팬더 활용
with tab3:
    st.header("자주 묻는 질문 (FAQ)")
    
    with st.expander("Q. 방명록 데이터는 어디에 저장되나요?"):
        st.write("서버의 데이터베이스가 아니라 **`st.session_state['messages']`**라는 세션 메모리 리스트에 안전하게 저장됩니다.")
        
    with st.expander("Q. 방명록을 삭제하면 어떻게 반영되나요?"):
        st.write("리스트 컴프리헨션을 이용해 선택한 ID를 `st.session_state['messages']`에서 실시간으로 필터링 제거한 뒤 `st.rerun()`을 호출하여 즉시 화면을 갱신합니다.")

# 8. 화면 하단 푸터 작성
st.markdown("---")
st.caption("Copyright 2026. Streamlit Study All rights reserved.")