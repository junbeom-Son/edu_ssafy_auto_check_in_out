import tkinter as tk
from tkinter import messagebox

# 버튼 클릭 시 입력 박스의 값 출력하는 함수
def on_button_click():
    email = email_input_box.get()  # 입력 상자의 값 가져오기
    password = password_input_box.get()

    if not email or not password:
        messagebox.showinfo("Alert", '아이디와 비밀번호를 모두 입력하세요')
        return

    file_name = "login_information.txt"
    with open(file_name, 'w') as file:
        file.write(f"{email}\n")
        file.write(f"{password}\n")

    messagebox.showinfo("Information", f"아이디와 비밀번호가 {file_name} 파일에 저장되었습니다.")
    root.quit()

def on_enter_key(event):
    on_button_click()

# 윈도우 생성
root = tk.Tk()
root.title("register ssafy info")
root.geometry('400x300')

# 라벨 추가
email_label = tk.Label(root, text="Enter your email:")
email_label.grid(row=0, column=0, padx=10, pady=10)

# 입력 박스(Entry 위젯) 추가
email_input_box = tk.Entry(root, width=30)  # 가로 크기 30
email_input_box.grid(row=0, column=1, padx=10, pady=10)

# 입력 필드에 Enter 키 이벤트 바인딩
email_input_box.bind('<Return>', on_enter_key)

# 라벨 추가
password_label = tk.Label(root, text="Enter your password:")
password_label.grid(row=1, column=0, padx=10, pady=10)

# 입력 박스(Entry 위젯) 추가
password_input_box = tk.Entry(root, width=30, show='*')  # 가로 크기 30
password_input_box.grid(row=1, column=1, padx=10, pady=10)

# 입력 필드에 Enter 키 이벤트 바인딩
password_input_box.bind('<Return>', on_enter_key)

# 버튼 추가
submit_button = tk.Button(root, text="Submit", command=on_button_click)
submit_button.grid(row=2, column=0, columnspan=2, pady=10)

# 프로그램이 실행될 때 입력 필드로 포커스를 이동
email_input_box.focus_set()

# 메인 루프 실행
root.mainloop()