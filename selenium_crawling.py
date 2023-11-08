# 기본 개념
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options=Options()
options.add_experimental_option('detach', True) #브라우저 바로꺼짐 방지

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://n.news.naver.com/mnews/article/003/0012194486?sid=105')
driver.implicitly_wait(10) # 사이트가 뜰때까지 기다려주는 명령어
# time.sleep(10) # 그냥 10초 멈추는 명령어

# for li in driver.find_elements(By.CSS_SELECTOR, 'li.u_likeit_list') :
#     print(li.find_element(By.CSS_SELECTOR, '.u_likeit_list_name').text)
#     print(li.find_element(By.CSS_SELECTOR, '.u_likeit_list_count').text)

driver.find_element(By.CSS_SELECTOR, '.Nicon_search').click() # 클릭함
driver.find_element(By.CSS_SELECTOR, '.u_it._search_input').send_keys('지드래곤') # 검색창에 검색어 입력
driver.find_element(By.CSS_SELECTOR, '.u_hssbt_us._total_search_btn').click() # 검색 버튼 클릭
