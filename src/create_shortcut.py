import os
import sys
from win32com.client import Dispatch
import ctypes  # 메시지 박스를 사용하기 위한 라이브러리

def create_shortcut(exe_relative_path, shortcut_name, shortcut_dir):
    # PyInstaller로 빌드된 실행 파일의 실제 위치를 기준으로 exe 파일 경로 설정
    script_dir = os.path.dirname(sys.executable)
    exe_path = os.path.abspath(os.path.join(script_dir, exe_relative_path))

    # 쉘 객체 생성
    shell = Dispatch('WScript.Shell')

    # 바로가기 경로 설정
    shortcut_path = os.path.join(shortcut_dir, f"{shortcut_name}.lnk")
    
    # 바로가기 파일 생성
    shortcut = shell.CreateShortCut(shortcut_path)
    shortcut.Targetpath = exe_path  # exe 파일 경로
    shortcut.WorkingDirectory = os.path.dirname(exe_path)  # 작업 디렉토리
    shortcut.save()  # 저장

    # 성공 메시지 출력
    if os.path.exists(shortcut_path):
        message = f"시작 프로그램에 추가 완료: {shortcut_path}"
    else:
        message = "바로가기 생성 실패"

    # 메시지 박스로 결과 출력
    ctypes.windll.user32.MessageBoxW(0, message, "바로가기 생성", 1)

# 예시 사용법
exe_relative_path = r"checkin.exe"  # 상대 경로
shortcut_name = "EduSSAFYCheckinApp"  # 바로가기 이름
startup_directory = r"C:\ProgramData\Microsoft\Windows\Start Menu\Programs\StartUp"  # 바로가기 생성 경로

create_shortcut(exe_relative_path, shortcut_name, startup_directory)
