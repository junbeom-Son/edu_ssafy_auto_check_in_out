import threading
import tkinter as tk

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from tkinter import messagebox

import time
import os
import login_util
import time_util

def login(driver, userEmail, userPassword):
    login_path = 'https://edu.ssafy.com/comm/login/SecurityLoginForm.do'
    # 로그인 예제 코드 (요소 아이디는 실제 사용 중인 웹사이트에 맞춰 변경해야 함)
    username = driver.find_element(By.ID, 'userId')
    password = driver.find_element(By.ID, 'userPwd')

    username.send_keys(userEmail)
    password.send_keys(userPassword)

    # 로그인 버튼 클릭
    login_button = driver.find_element(By.CSS_SELECTOR, 'div.form-btn a')
    login_button.click()

    # 현재 URL 가져오기
    current_url = driver.current_url
    if login_path == current_url:
        return False
    return True

def checked_in(driver):
    try:
        checked_in_span = driver.find_element(By.CSS_SELECTOR, 'div.state.inRoomEnd')
        return True
    except NoSuchElementException:
        return False

def show_message(message, root):
    messagebox.showinfo("Information", message)
    root.destroy()

def checkin(service, userEmail, userPassword, register_userinfo_file):
    # Chrome 드라이버 실행
    driver = webdriver.Chrome(service=service)

    # 웹사이트 열기
    driver.get('https://edu.ssafy.com')

    # 로그인 시도, 실패 시 프로그램 종료
    if not login(driver, userEmail, userPassword):
        messagebox.showinfo("Alert", f'로그인 정보가 잘못 되었습니다.\n{register_userinfo_file}파일을 다시 실행해 유저 정보를 갱신하세요.')
        return

    if checked_in(driver):
        tmp_root = tk.Tk()
        tmp_root.after(0, lambda: show_message('이미 입실 체크 했습니다.', tmp_root))

        tmp_root.mainloop()
        return

    # 입실 체크 버튼 클릭
    try:
        check_in_button = driver.find_element(By.ID, 'checkIn')
        check_in_button.click()
    except NoSuchElementException:
        tmp_root = tk.Tk()
        tmp_root.after(0, lambda: show_message('입실체크는 강의장에서만 가능합니다.', tmp_root))

        tmp_root.mainloop()
        return

    # 페이지 로딩 대기
    time.sleep(1)
    messagebox.showinfo("Information", '정상적으로 로그인 되었습니다.')

def main():
    login_information_file = 'login_information.txt'
    register_userinfo_file = 'register_userinfo.exe'
    if not os.path.exists(login_information_file):
        messagebox.showinfo("Alert", f'{login_information_file}가 존재하지 않습니다. {register_userinfo_file}파일을 먼저 실행해 유저 정보를 등록하세요')
        return

    userEmail, userPassword = login_util.get_user_info()

    # 크롬 경로 설정
    driver_path = 'chromedriver.exe'
    service = Service(driver_path)

    # 현재 시간을 초로 환산한 시간
    current_time_of_seconds = time_util.get_server_time(service)

    # 입실 체크 시간을 초로 환산한 시간
    checkout_time_of_seconds = 8 * 3600 + 1800 # 8시 30분

    left_seconds = checkout_time_of_seconds - current_time_of_seconds

    # 이벤트 객체 생성
    show_left_time_event = threading.Event()

    # 카운트다운을 별도 스레드에서 실행
    show_left_time_thread = threading.Thread(target=time_util.show_left_time,
                                             args=(max(left_seconds, 0), show_left_time_event))
    show_left_time_thread.start()

    # 카운트다운이 끝날 때까지 대기
    show_left_time_event.wait()

    # 카운트다운 완료 후 로직 실행
    checkin(service, userEmail, userPassword, register_userinfo_file)

main()