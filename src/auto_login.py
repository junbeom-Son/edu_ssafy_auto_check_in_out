from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

with open('login_information.txt', 'r', encoding='utf-8') as file:
    content = file.read()

userId, userPassword = content.split()

# 크롬 경로 설정
driver_path = 'chromedriver.exe'
service = Service(driver_path)

# Chrome 드라이버 실행
driver = webdriver.Chrome(service=service)

# 웹사이트 열기
driver.get('https://edu.ssafy.com')

# 로그인 예제 코드 (요소 아이디는 실제 사용 중인 웹사이트에 맞춰 변경해야 함)
username = driver.find_element(By.ID, 'userId')
password = driver.find_element(By.ID, 'userPwd')

username.send_keys(userId)
password.send_keys(userPassword)

# 로그인 버튼 클릭
login_button = driver.find_element(By.CSS_SELECTOR, 'div.form-btn a')
login_button.click()

# 입실 체크 버튼 클릭
check_in_button = driver.find_element(By.ID, 'checkIn')
check_in_button.click()

# 페이지 로딩 대기
time.sleep(3)