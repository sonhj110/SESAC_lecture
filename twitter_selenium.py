from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import time

options=Options()
# options.add_experimental_option('detach', True) #브라우저 바로꺼짐 방지

driver = webdriver.Chrome(ChromeDriverManager().install(), options=options)
driver.get('https://twitter.com/i/flow/login')
driver.implicitly_wait(10) # 사이트가 뜰때까지 기다려주는 명령어

# 아이디 입력
driver.find_element(By.CSS_SELECTOR, 'input.r-30o5oe').send_keys('saessag64830')
time.sleep(1)

# 다음 버튼 클릭
divcls = 'css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-ywje51 r-usiww2 r-2yi16 r-1qi8awa r-1ny4l3l r-ymttw5 r-o7ynqc r-6416eg r-lrvibr r-13qz1uu'
divcls = divcls.replace(' ', '.')
driver.find_element(By.CSS_SELECTOR, f'div.{divcls}').click()
time.sleep(2)

# 패스워드 입력
pwcls = "r-30o5oe r-1niwhzg r-17gur6a r-1yadl64 r-deolkf r-homxoj r-poiln3 r-7cikom r-1ny4l3l r-t60dpp r-1dz5y72 r-fdjqy7 r-13qz1uu"
pwcls = pwcls.replace(' ', '.')
driver.find_element(By.CSS_SELECTOR, f'input.{pwcls}').send_keys('pass123word')
time.sleep(1)

# 로그인 버튼 클릭
logincls = 'css-18t94o4 css-1dbjc4n r-sdzlij r-1phboty r-rs99b7 r-19yznuf r-64el8z r-1ny4l3l r-1dye5f7 r-o7ynqc r-6416eg r-lrvibr'
logincls = logincls.replace(' ', '.')
driver.find_element(By.CSS_SELECTOR, f'div.{logincls}').click()
time.sleep(2)

for cookie in driver.get_cookies() :
    print(cookie['name'])
    print(cookie['value'])

time.sleep(5)