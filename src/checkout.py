import os
import tkinter as tk
import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from tkinter import messagebox

def checkout_on_edu_ssafy(email, password, service):
    # Chrome 드라이버 실행
    driver = webdriver.Chrome(service=service)

    # 웹사이트 열기
    driver.get('https://edu.ssafy.com')

    # 로그인 예제 코드 (요소 아이디는 실제 사용 중인 웹사이트에 맞춰 변경해야 함)
    username_input_box = driver.find_element(By.ID, 'userId')
    password_input_box = driver.find_element(By.ID, 'userPwd')

    username_input_box.send_keys(email)
    password_input_box.send_keys(password)

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

def get_server_time(service):
    time_url = 'https://time.navyism.com/?host=edu.ssafy.com'

    # Chrome 드라이버 실행
    driver = webdriver.Chrome(service=service)

    # 웹사이트 열기
    driver.get(time_url)

    time_div = driver.find_element(By.ID, 'time_area')
    current_time = time_div.text.split()
    hour = int(current_time[3][:2])
    minute = int(current_time[4][:2])
    seconds = int(current_time[5][:2])
    return hour * 3600 + minute * 60 + seconds

def convert_seconds_to_full_time(seconds):
    hour = seconds // 3600
    seconds %= 3600
    minute = seconds // 60
    seconds %= 60
    return f'{hour}시간 {minute}분 {seconds}초'

def countdown(left_seconds, time_label, root):
    if left_seconds > 0:
        time_label.config(text=convert_seconds_to_full_time(left_seconds))
        root.after(1000, countdown, left_seconds - 1, time_label, root)

def show_left_time(left_seconds):
    root = tk.Tk()
    root.geometry('300x200')
    root.title('퇴실까지 남은 시간')
    title_label = tk.Label(root, text = '퇴실까지 남은 시간')
    title_label.pack(pady=10)
    left_time_label = tk.Label(root, text = convert_seconds_to_full_time(left_seconds))
    left_time_label.pack(pady=10)
    countdown(left_seconds, left_time_label, root)


def checkout(root, email, password, termination_option, checkout_time):

    root.destroy()
    # 크롬 경로 설정
    driver_path = 'chromedriver.exe'
    service = Service(driver_path)

    # 현재 시간을 초로 환산한 시간
    current_time_of_seconds = get_server_time(service)

    # 퇴실 체크 시간을 초로 환산한 시간
    checkout_time_of_seconds = checkout_time * 3600

    left_seconds = checkout_time_of_seconds - current_time_of_seconds

    show_left_time(max(left_seconds, 0))

    while True:
        tried_checkout_time = checkout_on_edu_ssafy(email, password, service)
        
        hour, minute = tried_checkout_time.split(":")
        hour = int(hour)
        print(f'퇴실 체크 시간: {tried_checkout_time}')
        if hour < checkout_time:
            print(f'{checkout_time}시 이전에 퇴실 체크를 시도하였습니다. 다시 퇴실체크를 진행합니다.')
            
        else:
            print('정상적으로 퇴실체크 되었습니다.')
            time.sleep(1)
            break
    
    if termination_option:
        # Windows에서 컴퓨터 종료
        os.system("shutdown /s /t 0")

def main():
    login_information_file = 'login_information.txt'
    register_userinfo_file = 'register_userinfo.exe'
    if not os.path.exists(login_information_file):
        messagebox.showinfo("Alert", f'{login_information_file}가 존재하지 않습니다. {register_userinfo_file}파일을 먼저 실행해 유저 정보를 등록하세요')
        return
    
    with open('login_information.txt', 'r', encoding='utf-8') as file:
        content = file.read()
    
    userEmail, userPassword = content.split()

    # 윈도우 생성
    root = tk.Tk()
    root.title("register ssafy info")
    root.geometry('400x300')

    # 선택된 값을 저장할 변수
    termination_options = ['즉시 종료', '종료 안함']

    termination_option = tk.StringVar(value = termination_options[0])  # StringVar로 숫자 값 관리

    termination_label = tk.Label(root, text="퇴실체크 후 컴퓨터 종료 여부")
    termination_label.pack(pady=10)
    for option in termination_options:
        # 라디오 버튼 생성
        radio_button = tk.Radiobutton(root, text=option, variable=termination_option, value=option)

        # 라디오 버튼 배치
        radio_button.pack(pady=5)

    checkout_time_label = tk.Label(root, text="퇴실체크 시간 설정")
    checkout_time_label.pack(pady=10)
    checkout_time_options = [['18:00', 18], ['14:00', 14], ['즉시', 0]]
    checkout_time = tk.IntVar(value = checkout_time_options[0][1])
    for time_str, time_value in checkout_time_options:
        # 라디오 버튼 생성
        radio_button = tk.Radiobutton(root, text=time_str, variable=checkout_time, value=time_value)

        # 라디오 버튼 배치
        radio_button.pack(pady=2)

    checkout_button = tk.Button(root, text='퇴실 체크', command=lambda: 
                                checkout(root, userEmail, userPassword, termination_option.get() == termination_options[0], checkout_time.get()))
    checkout_button.pack(pady=10)
    
    root.mainloop()

main()