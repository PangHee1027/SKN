import streamlit as st
import pandas as pd
from sqlalchemy import create_engine
import plotly.express as px
import pymysql
from urllib.parse import quote_plus  # 비밀번호 특수문자 처리용
import math  # 페이지 계산용

# ---------------------------------------------------------
# 0. 페이지 기본 설정 (앱 전체에서 단 한 번만 호출)
# ---------------------------------------------------------
st.set_page_config(
    page_title="차량 통합 정보 및 FAQ 시스템",
    page_icon="🚗",
    layout="wide"
)

st.markdown("""
    <style>
    /* 전체 폰트 및 부드러운 자간 설정 */
    html, body, [class*="css"] {
        letter-spacing: -0.01em;
    }
    
    /* 카드 및 입력 요소 모서리 둥글게 */
    div[data-testid="stExpander"], 
    div[data-baseweb="select"] > div,
    button[kind="secondary"],
    button[kind="primary"] {
        border-radius: 8px !important;
    }
    
    /* 버튼 호버 및 액티브 스타일 */
    button[kind="primary"] {
        font-weight: 600;
    }
    </style>
""", unsafe_allow_html=True)

# 세션 상태 초기화 (페이지 번호 관리용)
if 'current_page' not in st.session_state:
    st.session_state.current_page = 1

def reset_page():
    """조건 변경 시 1페이지로 초기화"""
    st.session_state.current_page = 1

# ---------------------------------------------------------
# 사이드바 메뉴 구성
# ---------------------------------------------------------
st.sidebar.title("🚘 메뉴 선택")
menu = st.sidebar.radio(
    "원하는 서비스를 선택하세요",
    ["자동차 등록현황", "FAQ"]
)

st.sidebar.divider()


# =========================================================
# 1. [페이지 1] 자동차 등록현황
# =========================================================
if menu == "자동차 등록현황":
    st.title("🚗 월별/시도별 차량 등록 현황")

    # 대한민국 주요 시도별 위경도 좌표 매핑 사전
    REGION_COORDS = {
        '서울': (37.5665, 126.9780), '서울특별시': (37.5665, 126.9780),
        '경기': (37.4138, 127.5183), '경기도': (37.4138, 127.5183),
        '인천': (37.4563, 126.7052), '인천광역시': (37.4563, 126.7052),
        '강원': (37.8228, 128.1555), '강원도': (37.8228, 128.1555), '강원특별자치도': (37.8228, 128.1555),
        '충북': (36.6357, 127.4912), '충청북도': (36.6357, 127.4912),
        '충남': (36.5184, 126.8000), '충청남도': (36.5184, 126.8000),
        '대전': (36.3504, 127.3845), '대전광역시': (36.3504, 127.3845),
        '세종': (36.4800, 127.2890), '세종특별자치시': (36.4800, 127.2890),
        '전북': (35.7175, 127.1530), '전라북도': (35.7175, 127.1530), '전북특별자치도': (35.7175, 127.1530),
        '전남': (34.8679, 126.9910), '전라남도': (34.8679, 126.9910),
        '광주': (35.1595, 126.8526), '광주광역시': (35.1595, 126.8526),
        '경북': (36.5760, 128.5056), '경상북도': (36.5760, 128.5056),
        '경남': (35.4606, 128.2132), '경상남도': (35.4606, 128.2132),
        '대구': (35.8714, 128.6014), '대구광역시': (35.8714, 128.6014),
        '울산': (35.5384, 129.3114), '울산광역시': (35.5384, 129.3114),
        '부산': (35.1796, 129.0756), '부산광역시': (35.1796, 129.0756),
        '제주': (33.4996, 126.5312), '제주도': (33.4996, 126.5312), '제주특별자치도': (33.4996, 126.5312)
    }

    # SQLAlchemy DB 연결 함수
    @st.cache_resource
    def get_sqlalchemy_engine():
        user = "root"
        raw_password = "1234"  # 👈 본인 DB 비밀번호로 수정
        password = quote_plus(raw_password)
        host = "localhost"
        port = "3306"
        database = "vehiclesdb"
        
        return create_engine(f"mysql+pymysql://{user}:{password}@{host}:{port}/{database}")

    # 데이터 로드 함수
    @st.cache_data
    def load_vehicle_data():
        engine = get_sqlalchemy_engine()
        query = "SELECT base_ym, region, bus_count, passenger_car_count, special_car_count FROM cars"
        df = pd.read_sql(query, engine)
        
        df['base_ym'] = df['base_ym'].astype(str)
        df['year'] = df['base_ym'].str[:4]
        df['month'] = df['base_ym'].str[4:6]
        
        df['total_count'] = df['passenger_car_count'] + df['bus_count'] + df['special_car_count']
        
        national_df = df.groupby('base_ym', as_index=False)[
            ['passenger_car_count', 'bus_count', 'special_car_count', 'total_count']
        ].sum()
        national_df['region'] = '전국'
        national_df['year'] = national_df['base_ym'].str[:4]
        national_df['month'] = national_df['base_ym'].str[4:6]
        
        full_df = pd.concat([df, national_df], ignore_index=True)
        return full_df

    try:
        df = load_vehicle_data()
    except Exception as e:
        st.error(f"데이터베이스 연결 중 오류가 발생했습니다: {e}")
        st.stop()

    type_map = {
        'passenger_car_count': '승용차',
        'bus_count': '승합차',
        'special_car_count': '특수차량',
        'total_count': '총합'
    }

    # 메인 화면 상단 - 조회 조건 설정 패널
    with st.expander("🔍 **조회 조건 설정**", expanded=True):
        col_mode, col_type = st.columns([1, 2])
        
        with col_mode:
            view_mode = st.radio("분석 기준 선택", ["월별 보기", "지역별 보기"], horizontal=True)
            
        with col_type:
            vehicle_options = ['승용차', '승합차', '특수차량', '총합']
            selected_vehicle_types = st.multiselect(
                "표시할 차량 종류 선택",
                options=vehicle_options,
                default=['승용차']
            )
            
        col_sub1, col_sub2 = st.columns(2)
        
        if view_mode == "월별 보기":
            with col_sub1:
                available_years = sorted(df['year'].unique(), reverse=True)
                selected_year = st.selectbox("연도 선택", available_years)
            with col_sub2:
                available_months = sorted(df[df['year'] == selected_year]['month'].unique())
                selected_month = st.selectbox("월 선택", available_months)
            selected_ym = f"{selected_year}{selected_month}"
            
        else:
            with col_sub1:
                all_regions = sorted([r for r in df['region'].unique() if r != '전국'])
                available_regions = ['전국'] + all_regions
                # -----------------------------------------------------
                # [수정 포인트 1] 단일 선택 -> 다중 선택(multiselect) 변경
                # -----------------------------------------------------
                default_region_selection = ['전국'] if '전국' in available_regions else [available_regions[0]]
                selected_regions = st.multiselect(
                    "지역/전국 선택 (다중 선택 가능)",
                    available_regions,
                    default=default_region_selection
                )
            with col_sub2:
                year_options = ["전체 연도"] + sorted(df['year'].unique(), reverse=True)
                selected_year_filter = st.selectbox("연도 필터", year_options)

    st.divider()

    if not selected_vehicle_types:
        st.warning("⚠️ 상단 조회 조건에서 하나 이상의 차량 종류를 선택해 주세요.")
    else:
        if view_mode == "월별 보기":
            st.subheader(f"📅 {selected_year}년 {selected_month}월 기준 - 시도별 및 전국 차량 등록 현황")
            
            ym_df = df[df['base_ym'] == selected_ym].sort_values(by='total_count', ascending=True)
            
            melted_df = ym_df.melt(
                id_vars=['region'],
                value_vars=['passenger_car_count', 'bus_count', 'special_car_count', 'total_count'],
                var_name='vehicle_type',
                value_name='count'
            )
            melted_df['vehicle_type'] = melted_df['vehicle_type'].map(type_map)
            filtered_melted_df = melted_df[melted_df['vehicle_type'].isin(selected_vehicle_types)]
            
            fig_bar = px.bar(
                filtered_melted_df,
                y='region',
                x='count',
                color='vehicle_type',
                barmode='group',
                orientation='h',
                title=f"📊 {selected_year}년 {selected_month}월 시도별 및 전국 차량 등록 수 ({', '.join(selected_vehicle_types)})",
                labels={'region': '지역/전국', 'count': '차량 수', 'vehicle_type': '차량 종류'}
            )
            fig_bar.update_layout(height=500, yaxis={'categoryorder': 'total ascending'})
            st.plotly_chart(fig_bar, use_container_width=True)
            
            st.divider()
            st.markdown(f"### 📌 {selected_year}년 {selected_month}월 지역별 점유율 및 지도 분포도")
            
            col_left, col_right = st.columns(2)
            
            regional_only = ym_df[ym_df['region'] != '전국'].copy()
            col_mapping = {'승용차': 'passenger_car_count', '승합차': 'bus_count', '특수차량': 'special_car_count', '총합': 'total_count'}
            selected_cols = [col_mapping[vt] for vt in selected_vehicle_types if vt in col_mapping]
            regional_only['selected_sum'] = regional_only[selected_cols].sum(axis=1)
            
            with col_left:
                fig_pie = px.pie(
                    regional_only,
                    values='selected_sum',
                    names='region',
                    title=f"🍕 지역별 차량 점유율 비율 (%) - {', '.join(selected_vehicle_types)}",
                    hole=0.35
                )
                fig_pie.update_traces(textposition='inside', textinfo='percent+label')
                fig_pie.update_layout(height=500)
                st.plotly_chart(fig_pie, use_container_width=True)
                
            with col_right:
                regional_only['lat'] = regional_only['region'].map(lambda r: REGION_COORDS.get(r, (None, None))[0])
                regional_only['lon'] = regional_only['region'].map(lambda r: REGION_COORDS.get(r, (None, None))[1])
                
                map_data = regional_only.dropna(subset=['lat', 'lon'])
                
                map_func = getattr(px, 'scatter_map', getattr(px, 'scatter_mapbox', None))
                style_param = 'map_style' if hasattr(px, 'scatter_map') else 'mapbox_style'
                
                map_kwargs = {
                    'data_frame': map_data,
                    'lat': 'lat',
                    'lon': 'lon',
                    'size': 'selected_sum',
                    'color': 'selected_sum',
                    'color_continuous_scale': px.colors.cyclical.IceFire,
                    'hover_name': 'region',
                    'hover_data': {'selected_sum': ':,', 'lat': False, 'lon': False},
                    'size_max': 70,
                    'zoom': 5.8,
                    'center': {"lat": 35.8, "lon": 127.8},
                    'title': f"🗺️ 대한민국 지역별 차량 분포도 - {', '.join(selected_vehicle_types)}",
                    'labels': {'selected_sum': '선택 차량 수'}
                }
                map_kwargs[style_param] = "open-street-map"
                
                fig_map = map_func(**map_kwargs)
                fig_map.update_layout(height=500, margin={"r":0,"t":40,"l":0,"b":0})
                st.plotly_chart(fig_map, use_container_width=True)
                
            with st.expander("원본 데이터 보기"):
                st.dataframe(ym_df[['region', 'passenger_car_count', 'bus_count', 'special_car_count', 'total_count']].sort_values(by='total_count', ascending=False))

        elif view_mode == "지역별 보기":
            # -----------------------------------------------------
            # [수정 포인트 2] 지역 미선택 시 방어 로직 추가
            # -----------------------------------------------------
            if not selected_regions:
                st.warning("⚠️ 상단 조회 조건에서 하나 이상의 지역을 선택해 주세요.")
            else:
                region_title = ", ".join(selected_regions)
                st.subheader(f"📍 [{region_title}] 기준 - 시간순 차량 등록 추이")
                
                # -----------------------------------------------------
                # [수정 포인트 3] isin()을 사용하여 다중 지역 필터링
                # -----------------------------------------------------
                filtered_df = df[df['region'].isin(selected_regions)]
                if selected_year_filter != "전체 연도":
                    filtered_df = filtered_df[filtered_df['year'] == selected_year_filter]
                    
                filtered_df = filtered_df.sort_values(by='base_ym', ascending=True)
                
                melted_df = filtered_df.melt(
                    id_vars=['base_ym', 'region'],
                    value_vars=['passenger_car_count', 'bus_count', 'special_car_count', 'total_count'],
                    var_name='vehicle_type',
                    value_name='count'
                )
                melted_df['vehicle_type'] = melted_df['vehicle_type'].map(type_map)
                filtered_melted_df = melted_df[melted_df['vehicle_type'].isin(selected_vehicle_types)]
                
                # -----------------------------------------------------
                # [수정 포인트 4] Plotly 다중 지역 비교형 막대 그래프 구성
                # -----------------------------------------------------
                fig = px.bar(
                    filtered_melted_df,
                    x='base_ym',
                    y='count',
                    color='region',          # 지역별로 색상을 다르게 표현
                    pattern_shape='vehicle_type' if len(selected_vehicle_types) > 1 else None,
                    barmode='group',
                    title=f"[{region_title}] 시간순 차량 등록 추이 ({', '.join(selected_vehicle_types)})",
                    labels={'base_ym': '연월(base_ym)', 'count': '차량 수', 'vehicle_type': '차량 종류', 'region': '지역'}
                )
                fig.update_layout(height=600, xaxis_type='category')
                st.plotly_chart(fig, use_container_width=True)
                
                with st.expander("원본 데이터 보기"):
                    st.dataframe(filtered_df[['base_ym', 'region', 'passenger_car_count', 'bus_count', 'special_car_count', 'total_count']])


# =========================================================
# 2. [페이지 2] FAQ 검색 (하단 < 1 2 3 > 버튼 방식 적용)
# =========================================================
elif menu == "FAQ":
    # DB 접속 정보 설정
    DB_CONFIG = {
        'host': 'localhost',
        'port': 3306,
        'user': 'root',          # MySQL 사용자명
        'password': '1234',      # MySQL 비밀번호
        'db': 'vehiclesdb',       # 데이터베이스명
        'charset': 'utf8mb4'
    }

    @st.cache_resource
    def get_pymysql_connection():
        """데이터베이스 연결 생성"""
        return pymysql.connect(**DB_CONFIG)

    def fetch_data(query, params=None):
        """SQL 쿼리를 실행하여 DataFrame으로 반환"""
        try:
            conn = get_pymysql_connection()
            conn.ping(reconnect=True)  # 연결 끊김 방지
            with conn.cursor(pymysql.cursors.DictCursor) as cursor:
                cursor.execute(query, params or ())
                result = cursor.fetchall()
                return pd.DataFrame(result)
        except Exception as e:
            st.error(f"데이터베이스 오류가 발생했습니다: {e}")
            return pd.DataFrame()

    st.title("🚗 차량 제조사별 FAQ 검색")
    st.caption("현대자동차 및 기아의 FAQ 정보를 조회할 수 있는 페이지입니다.")
    st.divider()

    # 메인 화면 컬럼 생성 (제조사 선택 / 카테고리 선택)
    col1, col2 = st.columns([1, 2])

    with col1:
        manufacturer = st.radio(
            "🚘 **제조사를 선택하세요**",
            options=["현대자동차", "기아"],
            horizontal=True,
            on_change=reset_page  # 제조사 변경 시 1페이지로 이동
        )

    # 테이블명 지정
    table_name = "hyundai_faq" if manufacturer == "현대자동차" else "kia_faq"

    # 테이블 컬럼 목록 확인
    columns_df = fetch_data(f"SHOW COLUMNS FROM {table_name}")

    if not columns_df.empty:
        column_list = columns_df['Field'].tolist()

        has_major = 'Major_Category' in column_list
        has_category = 'Category' in column_list

        with col2:
            if has_major:
                major_categories_df = fetch_data(f"SELECT DISTINCT Major_Category FROM {table_name} WHERE Major_Category IS NOT NULL")
                categories = ["전체"] + major_categories_df['Major_Category'].tolist() if not major_categories_df.empty else ["전체"]
                selected_category = st.selectbox("📂 **카테고리 선택**", categories, on_change=reset_page)

            elif has_category:
                categories_df = fetch_data(f"SELECT DISTINCT Category FROM {table_name} WHERE Category IS NOT NULL")
                categories = ["전체"] + categories_df['Category'].tolist() if not categories_df.empty else ["전체"]
                selected_category = st.selectbox("📂 **카테고리 선택**", categories, on_change=reset_page)
            else:
                selected_category = "전체"

        st.divider()

        # SQL 조건문 및 조회
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
        total_items = len(faq_data)
        st.subheader(f"📌 {manufacturer} FAQ 목록 (총 {total_items}건)")

        if faq_data.empty:
            st.info("해당 조건에 맞는 FAQ 데이터가 없습니다.")
        else:
            ITEMS_PER_PAGE = 10
            total_pages = math.ceil(total_items / ITEMS_PER_PAGE)

            # 현재 저장된 페이지 범위를 벗어나지 않도록 안전장치
            if st.session_state.current_page > total_pages:
                st.session_state.current_page = 1

            # -----------------------------------------------------
            # [질문 목록 출력] (10개 슬라이싱)
            # -----------------------------------------------------
            start_idx = (st.session_state.current_page - 1) * ITEMS_PER_PAGE
            end_idx = start_idx + ITEMS_PER_PAGE
            page_data = faq_data.iloc[start_idx:end_idx]

            for current_idx, row in page_data.iterrows():
                cat_tag = ""
                if has_major and pd.notna(row.get('Major_Category')):
                    m_cat = f" > {row['M_Category']}" if pd.notna(row.get('M_Category')) else ""
                    cat_tag = f"[{row['Major_Category']}{m_cat}] "
                elif has_category and pd.notna(row.get('Category')):
                    cat_tag = f"[{row['Category']}] "

                question_text = f"Q{current_idx + 1}. {cat_tag}{row['Question']}"

                with st.expander(question_text):
                    st.markdown(f"**A.** {row['Answer']}")

            st.divider()

            # -----------------------------------------------------
            # [하단 페이지네이션 UI: < 1 2 3 4 5 > 버튼 형태]
            # -----------------------------------------------------
            PAGE_WINDOW = 5
            current_window = (st.session_state.current_page - 1) // PAGE_WINDOW
            start_page = current_window * PAGE_WINDOW + 1
            end_page = min(start_page + PAGE_WINDOW - 1, total_pages)

            nav_cols = st.columns([2] + [1] * (end_page - start_page + 3) + [2])
            
            col_idx = 1

            # 이전('<') 버튼
            with nav_cols[col_idx]:
                if st.button("◀", disabled=(st.session_state.current_page == 1), use_container_width=True):
                    st.session_state.current_page -= 1
                    st.rerun()
            col_idx += 1

            # 숫자로 된 페이지 버튼들 (1, 2, 3...)
            for p in range(start_page, end_page + 1):
                with nav_cols[col_idx]:
                    btn_type = "primary" if p == st.session_state.current_page else "secondary"
                    if st.button(str(p), key=f"btn_page_{p}", type=btn_type, use_container_width=True):
                        st.session_state.current_page = p
                        st.rerun()
                col_idx += 1

            # 다음('>') 버튼
            with nav_cols[col_idx]:
                if st.button("▶", disabled=(st.session_state.current_page == total_pages), use_container_width=True):
                    st.session_state.current_page += 1
                    st.rerun()

            # 하단 안내 문구
            st.caption(f"<div style='text-align: center; margin-top: 5px;'>현재페이지: {st.session_state.current_page} / 전체 {total_pages} 페이지 (총 {total_items}건)</div>", unsafe_allow_html=True)

    else:
        st.warning(f"'{table_name}' 테이블 정보를 불러올 수 없습니다. DB 및 테이블 이름을 확인해 주세요.")