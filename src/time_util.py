import tkinter as tk

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

def convert_seconds_to_full_time(seconds):
    hour = seconds // 3600
    seconds %= 3600
    minute = seconds // 60
    seconds %= 60
    return f'{hour}시간 {minute}분 {seconds}초'

def get_server_time(service):
    chrome_options = Options()
    chrome_options.add_argument("--headless")  # 크롬을 헤드리스 모드로 실행
    chrome_options.add_argument("--disable-gpu")  # GPU 사용 중지 (Linux에서 필수)
    chrome_options.add_argument("--window-size=1920x1080")  # 창 크기를 설정할 수 있음

    time_url = 'https://time.navyism.com/?host=edu.ssafy.com'

    # Chrome 드라이버 실행
    driver = webdriver.Chrome(service=service, options = chrome_options)

    # 웹사이트 열기
    driver.get(time_url)

    time_div = driver.find_element(By.ID, 'time_area')
    current_time = time_div.text.split()
    hour = int(current_time[3][:2])
    minute = int(current_time[4][:2])
    seconds = int(current_time[5][:2])
    return hour * 3600 + minute * 60 + seconds

def show_left_time(left_seconds, show_left_time_event):
    root = tk.Tk()
    root.geometry('300x200')
    root.title('퇴실까지 남은 시간')
    title_label = tk.Label(root, text = '퇴실까지 남은 시간')
    title_label.pack(pady=10)
    left_time_label = tk.Label(root, text = convert_seconds_to_full_time(left_seconds))
    left_time_label.pack(pady=10)

    countdown(left_seconds, left_time_label, root, show_left_time_event)

    root.mainloop()

def countdown(left_seconds, time_label, root, show_left_time_event):
    if left_seconds > 0:
        time_label.config(text=convert_seconds_to_full_time(left_seconds))
        root.after(1000, countdown, left_seconds - 1, time_label, root, show_left_time_event)
    else:
        root.destroy()
        show_left_time_event.set() # Thread 작업이 끝났다는 신호
