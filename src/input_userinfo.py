	# 사용자로부터 아이디와 비밀번호를 입력받습니다.
user_id = input("아이디를 입력하세요: ")
password = input("비밀번호를 입력하세요: ")

# 파일 이름을 설정합니다.
file_name = "login_information.txt"

# 파일을 쓰기 모드로 열어 아이디와 비밀번호를 각각 줄을 바꿔서 기록합니다.
with open(file_name, 'w') as file:
    file.write(f"{user_id}\n")
    file.write(f"{password}\n")

print(f"아이디와 비밀번호가 {file_name} 파일에 저장되었습니다.")