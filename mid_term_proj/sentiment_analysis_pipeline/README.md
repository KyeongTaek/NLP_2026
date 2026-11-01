# 📦 감성 분석 파이프라인 설계 프로젝트 (도메인 맞춤형)

## 1. 프로젝트 개요 (Overview)
* **주제:** 배달 음식 서비스 리뷰 감성 분석 파이프라인 설계 및 도메인 전이 탐색
* **배정 도메인:** 
  * **주 도메인 (Train/Valid/Test):** 배달 음식 서비스 리뷰
  * **전이 도메인 (Domain Transfer):** 택배·배송 서비스 리뷰
* **작성자:** 임경택 (2021040032)

---

## 2. 디렉토리 구조 (Directory Structure)
```text
├── notebooks/midterm_analysis.ipynb          # 전체 파이프라인 및 분석 코드가 포함된 주피터 노트북
├── midterm_analysis_report.pdf     # 과제 제출용 해석 보고서
└── README.md                       # 프로젝트 설명서 (본 문서)
```

---

## 3. 파이프라인 핵심 설계 (Pipeline Architecture)
* **Split First 원칙 준수:** 전처리나 벡터화를 수행하기 전, 원시 텍스트 상태에서 `train_test_split`을 두 번 적용하여 **Train(60%) / Validation(20%) / Test(20%)**로 Stratified 분할을 수행했습니다.
* **정보 누수(Data Leakage) 차단:** `scikit-learn Pipeline`을 활용하여 `TfidfVectorizer`(공백 토큰화, n-gram=(1,2))와 분류 모델을 하나로 캡슐화했습니다.
* **규칙 기반 Baseline (`improved_rule_score`):**
  * 배달 음식 도메인 맞춤형 감성 사전(Lexicon) 구축 (핵심 어휘 10개 이상 및 극성 점수 ±1, ±2 부여)
  * 부정어(`않`, `못` 등) 포함 시 점수 부호 반전 규칙(`improved_rule_score`) 적용
* **공정한 모델 비교 및 선정:** 
  * `MultinomialNB`와 `LogisticRegression`을 동일한 조건에서 비교
  * 클래스 불균형과 양측 성능 균형을 고려하여 **`macro-F1`을 최적 모델 선정 기준**으로 채택

---

## 4. 주요 분석 결과 (Key Results & Analysis)
* **Validation 오류 분석 (3가지 유형):**
  1. **용어 미탐 (OOV):** 공백 토큰화(`str.split`) 및 어휘 사전에 등록되지 않은 활용형 단어(`불어서`, `없고` 등)로 인한 인식 실패
  2. **부정어 처리 한계:** 부정어(`안`)가 수식하는 대상과 멀리 떨어져 있어 정확한 반전이 일어나지 않는 현상
  3. **문맥 해석 한계:** 복합 문맥(`빠져 있었어요`)에서 단편적 어휘 조합으로 인한 오판
* **Test 세트 평가 및 비즈니스적 위험:**
  * `TEST_EVALUATED` 플래그를 통한 단일 평가 보장
  * **비즈니스적 관점:** 긍정 누락(TN/FN)보다 **부정 리뷰를 놓쳐 서비스 개선 기회를 잃는 것(FP)**이 더 치명적이므로, 이에 대한 혼동행렬(Confusion Matrix) 해석 수행
* **전이 도메인 탐색 (Domain Transfer):**
  * 주 도메인 모델을 택배·배송 서비스 리뷰에 적용했을 때 발생하는 성능 저하 분석
  * 핵심 미등록 어휘(`상차 대기` 등) 소실로 인해 모델의 예측 확률이 `0.5` 부근으로 수렴하며 혼란을 겪는 현상(OOV 및 어휘 중복도 관점) 해석

---

## 5. 실행 방법 (How to Run)
1. Python 환경 및 필수 라이브러리 설치 (`pandas`, `scikit-learn`, `numpy`)
2. `midterm_analysis.ipynb` 파일 실행 (`SEED = 42` 고정으로 재현성 보장)
