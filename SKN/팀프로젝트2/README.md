# 🎵 Music Streaming Service Churn Prediction System
> 로그 시퀀스 기반 데이터 누수 방지 및 ML/DL 하이브리드 모델링을 통한 사용자 이탈 예측 프로젝트

---

## 📌 Project Overview
본 프로젝트는 음악 스트리밍 서비스 사용자들의 행동 로그(Log) 데이터를 기반으로 **사용자 이탈(Churn)**을 예측하는 End-to-End 머신러닝/딥러닝 파이프라인을 구축하는 것을 목표로 합니다.

특히, 기존 모델링 과정에서 빈번하게 발생하는 **데이터 누수(Data Leakage)** 문제를 차단하기 위해 원본 로그 시퀀스 단계에서부터 정밀한 필터링 및 시퀀스 패딩 방식을 도입하였으며, 정형 데이터(ML)와 비정형 시퀀스 데이터(DL)를 결합한 하이브리드 접근법을 적용하였습니다.

---

## 🛠️ Tech Stack & Architecture
- **Language**: Python 3.10+
- **Data Processing**: Pandas, NumPy, PyArrow (Parquet)
- **Visualization**: Matplotlib, Seaborn, Plotly
- **Machine Learning**: XGBoost, LightGBM, CatBoost, Scikit-learn
- **Deep Learning**: PyTorch (LSTM / Transformer-based Sequence Models)
- **Model Evaluation**: ROC-AUC, F1-Score, PR-AUC, SHAP (XAI)

---

## 🚀 Phase Details (1 ~ 6 Phase Workflow)

```
[Phase 1] Data Preprocessing & Validation
       ↓
[Phase 2] Feature Engineering Pipeline (Leakage Prevention)
       ↓
[Phase 3] Exploratory Data Analysis (EDA)
       ↓
[Phase 4] Machine Learning Modeling & Calibration
       ↓
[Phase 5] Deep Learning Sequence Modeling
       ↓
[Phase 6] Hybrid Ensemble & Model Interpretation (SHAP)
```

---

### 🟢 Phase 1: Data Preprocessing & Validation
- **목적**: 대용량 비정형 사용자 이벤트 로그 데이터의 정제 및 기초 검증
- **주요 작업**:
  - 로그 데이터(Parquet) 로드 및 결측치, 중복 레코드 처리
  - 타임스탬프(`ts`) 단위 정형화 및 유저 단위 정렬
  - 데이터 타입 최적화 및 메타데이터 정제

---

### 🟢 Phase 2: Feature Engineering Pipeline
- **목적**: 데이터 누수 없는 정형/시퀀스 피처 추출 파이프라인 구축
- **주요 작업**:
  - **데이터 누수(Leakage) 차단**: AUC 1.0을 유발하는 결정적 이탈 페이지(`Cancel`, `Cancellation Confirmation`, `Submit Downgrade` 등) 로그 사전 제거
  - **정형 피처 생성**: 가입 기간(`tenure_days`), 총 재생 곡 수, 썸즈업/다운, 플레이리스트 추가 횟수, 에러/도움말 요청 빈도 계산
  - **시퀀스 피처 추출**: 유저별 최근 N개(예: 50개) 페이지 이동 경로 추출 및 정수 인코딩(Vocabulary Mapping)
  - **Loop Padding 기법 적용**: 활동량이 적은 유저의 시퀀스 길이를 채울 때 `0` 패딩 대신 기존 시퀀스를 반복(Loop) 채움으로써 시퀀스 길이로 인한 leakage 차단
  - **출력 데이터 저장**: `ml_tabular_features.parquet`, `dl_sequence_tensors.npy`, `y_labels.npy`

---

### 🟢 Phase 3: Exploratory Data Analysis (EDA)
- **목적**: 타겟 라벨 불균형 및 피처별 이탈 유저/유지 유저 간 행동 특성 비교
- **주요 작업**:
  - 타겟 변수(`is_churn`) 클래스 불균형 확인 (유지 ~77.5% vs 이탈 ~22.5%)
  - Plotly/Seaborn 기반의 정형 피처 분포 분석 (Boxplot, Violin plot)
  - 주요 페이지 이용 빈도 및 가입 기간에 따른 이탈율 차이 시각화

---

### 🟢 Phase 4: Machine Learning Modeling
- **목적**: 정형 피처 기반의 트리 계열 머신러닝 모델 구축 및 최적화
- **주요 작업**:
  - LightGBM, XGBoost, CatBoost 모델 학습 및 교차 검증(Stratified K-Fold)
  - 클래스 불균형 대응을 위한 `scale_pos_weight` 조정 및 하이퍼파라미터 튜닝
  - 확률 보정(Probability Calibration) 및 Decision Threshold 최적화

---

### 🟢 Phase 5: Deep Learning Sequence Modeling
- **목적**: 유저의 시간순 페이지 이동 로그(시퀀스) 패턴 학습
- **주요 작업**:
  - PyTorch 기반 `Dataset` 및 `DataLoader` 구현
  - LSTM / GRU / Transformer Encoder 기반의 시퀀스 분류 모델 설계
  - Embedding Layer를 활용한 페이지 ID 고차원 벡터화
  - Focal Loss / Weighted BCE Loss를 통한 불균형 학습 개선

---

### 🟢 Phase 6: Hybrid Ensemble & XAI (Model Interpretation)
- **목적**: ML 및 DL 예측값 앙상블 및 이탈 요인 해석가능성 확보
- **주요 작업**:
  - ML(LightGBM/CatBoost) 예측 확률과 DL(Sequence Model) 예측 확률의 Soft Voting 앙상블
  - ROC-AUC, F1-Score, PR-AUC 기반 최종 성능 평가
  - **SHAP (SHapley Additive exPlanations)** 분석을 통한 유저 이탈 주요 피처 기여도 해석 및 비즈니스 인사이트 도출

---

## 📊 Key Results & Artifacts

| Output File | Description |
| :--- | :--- |
| `ml_tabular_features.parquet` | Leakage가 제거된 유저별 정형 집계 피처 |
| `dl_sequence_tensors.npy` | Loop Padding이 적용된 최근 50개 페이지 시퀀스 텐서 |
| `y_labels.npy` | 유저별 이탈 여부 라벨 (0: 유지, 1: 이탈) |
| `models/` | 학습된 ML / DL 최적 모델 가중치 |

---

## 💡 How to Run
```bash
# 1. 환경 설정 및 패키지 설치
pip install -r requirements.txt

# 2. Phase 1 & 2: 전처리 및 피처 엔지니어링 실행
python src/phase2_feature_engineering.py

# 3. Phase 4 & 5: ML / DL 모델 학습
python src/phase4_train_ml.py
python src/phase5_train_dl.py

# 4. Phase 6: 앙상블 및 SHAP 분석
python src/phase6_ensemble_and_explain.py
```