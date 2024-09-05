# 목적
SSAFY 교육생들의 로그인 로그아웃을 조금 더 편하게 하기 위함

# 기능
- 한 번의 클릭으로 자동 입실 체크
- 한 번의 클릭으로 자동 퇴실 체크

# 미리 설정해야 할 사항
1. 실행파일(auto_login.exe or auto_logout.exe)과 같은 경로에 login_information.txt 생성
2. login_information.txt에 edussafy 로그인 이메일과 비밀번호를 엔터로 분리해서 저장
이메일이 aaa@naver.com이고 비밀번호가 abcdefg인 경우 다음과 같이 설정

![image](https://github.com/user-attachments/assets/54f17a0d-c089-4e7f-91a6-28ec6f946bc7)

# 사용법
login_information.txt에 이메일과 비밀번호를 설정한 뒤 진행해야 됩니다.
## 입실 체크
auto_login.exe 클릭
가만히 기다리면 크롬이 켜지고 알아서 입실체크 진행 후 프로그램 종료

## 퇴실 체크 - 버전 3개
### 1) 18시에 퇴실이 되고 컴퓨터 종료
auto_logout.exe 클릭
18시 이전에 클릭하면 계속해서 퇴실 체크 진행 반복
18시가 된 경우 정상 적으로 퇴실 체크를 확인하고 컴퓨터 자동종료 -> 칼퇴 가능
### 2) 18시에 퇴실 체크만하고 컴퓨터 종료 X
checkout_now_power_off.exe 클릭
18시 이전에 클릭하면 계속해서 퇴실 체크 진행 반복
18시가 된 경우 정상 적으로 퇴실 체크를 확인하고 프로그램 종료
### 3) 시간과 관계없이 그냥 지금 퇴실 체크 후 컴퓨터 종료
checkout_now.exe 클릭
자동으로 퇴실체크가 되고 컴퓨터 종료 -> 조퇴 시 사용

# 유의 사항
본인 컴퓨터의 Chrome 버전과 해당 패키지에 있는 Chrome Driver의 버전이 일치하지 않는 경우
Chrome Driver의 버전을 맞춰서 새로 설치 필요
