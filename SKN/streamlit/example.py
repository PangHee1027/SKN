import numpy as np
import pandas as pd
import streamlit as st

# 1. 타이틀 및 텍스트 출력
st.title("Streamlit 기본 예제")
st.write("Streamlit을 이용해 빠르고 쉽게 웹 애플리케이션을 만들 수 있습니다.")

# 2. 사용자 입력 위젯 (텍스트 입력 및 슬라이더)
user_name = st.text_input("이름을 입력해주세요:", "홍길동")
st.write(f"안녕하세요, {user_name}님!")

age = st.slider("나이를 선택하세요:", 1, 100, 25)
st.write(f"선택하신 나이는 {age}세입니다.")

# 3. 데이터프레임 생성 및 출력
st.subheader("랜덤 데이터프레임 표시")
df = pd.DataFrame(
    np.random.randn(10, 3), columns=["A열", "B열", "C열"]  # 10행 3열의 랜덤 데이터
)
st.dataframe(df)

# 4. 차트 시각화
st.subheader("라인 차트 시각화")
st.line_chart(df)