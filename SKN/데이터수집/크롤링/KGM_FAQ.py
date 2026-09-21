import csv
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def crawl_kgm_faq():
    # 웹드라이버 옵션 설정
    options = webdriver.ChromeOptions()
    # 창을 최대화하여 클릭 요소가 숨지 않도록 설정
    options.add_argument("--start-maximized")
    driver = webdriver.Chrome(options=options)
    
    # KGM FAQ 페이지 URL
    url = "https://www.kg-mobility.com/sr/online-center/faq/detail?searchWord=&categoryCd=300"
    driver.get(url)
    wait = WebDriverWait(driver, 15)
    
    faq_data = []
    order = 1

    try:
        # 1. FAQ 아코디언 리스트 항목들이 로드될 때까지 대기
        wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".accordion-item, .faq-list > div, .accordion")))

        # 2. FAQ 카드/아이템 요소 전체 수집
        items = driver.find_elements(By.CSS_SELECTOR, ".accordion-item, [class*='faq'], [class*='accordion']")
        
        # 실제 FAQ 데이터 아이템만 필터링하기 위한 리스트
        valid_items = []
        for item in items:
            text = item.text.strip()
            # 텍스트가 존재하고 질문 내용이 포함된 요소 구분
            if text and ("카테고리" in text or "차량정비" in text or "구매/영업" in text or "부품" in text or "홈페이지" in text or "기타" in text):
                valid_items.append(item)

        print(f"감지된 FAQ 항목 수: {len(valid_items)}개")

        for item in valid_items:
            try:
                # 카테고리 추출 (태그/클래스 탐색)
                try:
                    category_elem = item.find_element(By.CSS_SELECTOR, "span, .badge, .cate, .category")
                    category = category_elem.text.strip()
                except:
                    category = "일반"

                # 질문 및 클릭 요소 추출
                # 클릭하여 답변을 열어야 하는 버튼/헤더 요소
                click_target = item.find_element(By.CSS_SELECTOR, "button, .accordion-header, a, .title")
                question = click_target.text.strip()

                # 질문 텍스트에서 카테고리명이 겹쳐 들어간 경우 정리
                if category in question and len(question) > len(category):
                    question = question.replace(category, "").strip()

                # JavaScript 클릭으로 아코디언 답변 영역 펼치기
                driver.execute_script("arguments[0].click();", click_target)
                time.sleep(0.4) # 애니메이션 슬라이딩 대기

                # 답변 영역 추출
                try:
                    answer_elem = item.find_element(By.CSS_SELECTOR, ".accordion-body, .accordion-collapse, .ans, .answer, .reply")
                    answer = answer_elem.text.strip()
                except:
                    # 클릭 후 펼쳐진 전체 텍스트에서 질문 및 카테고리를 제외한 부분을 답변으로 처리
                    full_text = item.text.strip()
                    answer = full_text.replace(category, "").replace(question, "").strip()

                if question:
                    faq_data.append({
                        "순번": order,
                        "카테고리": category,
                        "질문": question,
                        "답변": answer
                    })
                    order += 1

            except Exception as e:
                continue

    finally:
        driver.quit()

    # CSV 파일 저장 (utf-8-sig로 저장하여 엑셀 한글 깨짐 방지)
    csv_file_path = "kgm_faq_list.csv"
    fieldnames = ["순번", "카테고리", "질문", "답변"]

    with open(csv_file_path, mode="w", encoding="utf-8-sig", newline="") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(faq_data)

    print(f"성공적으로 총 {len(faq_data)}건의 FAQ 데이터를 '{csv_file_path}'로 저장했습니다.")

if __name__ == "__main__":
    crawl_kgm_faq()