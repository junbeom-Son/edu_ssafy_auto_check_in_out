import os

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time

def logout(userId, userPassword, service):
    # Chrome 드라이버 실행
    driver = webdriver.Chrome(service=service)

    # 웹사이트 열기
    driver.get('https://edu.ssafy.com')

    # 로그인 예제 코드 (요소 아이디는 실제 사용 중인 웹사이트에 맞춰 변경해야 함)
    username_input_box = driver.find_element(By.ID, 'userId')
    password_input_box = driver.find_element(By.ID, 'userPwd')

    username_input_box.send_keys(userId)
    password_input_box.send_keys(userPassword)

    # 로그인 버튼 클릭
    login_button = driver.find_element(By.CSS_SELECTOR, 'div.form-btn a')
    login_button.click()

    # 퇴실 체크 버튼 클릭
    check_out_button = driver.find_element(By.ID, 'checkOut')
    check_out_button.click()

    # 확인 버튼 클릭
    ok_button = driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-md.btn-primary.pop-event-close')
    ok_button.click()

    # 시간 체크
    check_out_button = driver.find_element(By.ID, 'checkOut')
    check_out_time = check_out_button.find_element(By.CSS_SELECTOR, '.t1').text
    driver.quit()
    return check_out_time


with open('login_information.txt', 'r', encoding='utf-8') as file:
    content = file.read()

userId, userPassword = content.split()

# 크롬 경로 설정
driver_path = 'chromedriver.exe'
service = Service(driver_path)

check_out_time = logout(userId, userPassword, service)
print(f'퇴실 체크 시간: {check_out_time}')

# 페이지 로딩 대기
time.sleep(1)
    
# Windows에서 컴퓨터 종료
os.system("shutdown /s /t 0")