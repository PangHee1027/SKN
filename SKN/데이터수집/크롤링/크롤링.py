from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Chrome()

url = "https://product.kyobobook.co.kr/detail/S000001925800"

driver.get(url)

selector = "#bookBasicInfo > section > div.border-t-1 > table > tbody > tr:nth-child(3) > td > div > span"

element = driver.find_element(By.CSS_SELECTOR, selector)

page_info = element.text

print(f"도서 쪽수 : {page_info}")
