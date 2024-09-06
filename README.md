# 목적

SSAFY 교육생들의 로그인 로그아웃을 조금 더 편하게 하기 위함

# 유의 사항

- 본인 컴퓨터의 Chrome 버전과 해당 패키지에 있는 Chrome Driver의 버전이 일치하지 않는 경우 Chrome Driver의 버전을 맞춰서 새로 설치 필요
- 실행파일(.exe)이 Chrome Driver와 같은 경로상에 존재해야 실행 가능
- 수정 필요 시 src 디렉토리 내부의 소스코드를 직접 변경할 수 있으며 소스코드 직접 실행시에도 Chrome Driver파일들과 같은 경로에서 실행 필수(혹은 Chrome driver 경로 설정)

# 기능

- 한 번의 클릭으로 자동 입실 체크
- 한 번의 클릭으로 자동 퇴실 체크

# 사용법

## 사용자 정보 등록

register_userinfo.exe 클릭
1. edu ssafy 이메일과 비밀번호를 입력
2. enter키 or submit 버튼 클릭
3. user_info.txt 생성


![유저 정보 등록](https://github.com/user-attachments/assets/f261939a-0a95-4e0c-b4b1-cf186d40930f)


## 입실 체크

checkin.exe 클릭
가만히 기다리면 크롬이 켜지고 알아서 입실체크 진행 후 프로그램 종료

## 퇴실 체크 - 버전 3개
checkout.exe 클릭
### 유저 정보가 없는 경우 
![유저 정보가 없는 경우](https://github.com/user-attachments/assets/76bfe84f-0ff0-4a03-a1fc-f2f7bf9ce24e)

유저 정보가 없는 경우 register_userinfo.exe를 실행하라는 경고 창이 뜹니다.

### 퇴실 옵션 선택
![checkout 실행](https://github.com/user-attachments/assets/6498a8be-6256-490e-8924-ffe221c02d9e)

(지정된 시간까지 반복 퇴실 진행)

1. 퇴실 체크 이후 컴퓨터 종료 여부 지정(default 즉시 종료)
- 즉시 종료 : 퇴실 체크가 정상적으로 종료되면 컴퓨터 즉시 종료
- 종료 안함 : 퇴실 체크가 정상적으로 종료되면 프로그램만 종료
2. 퇴실 시간 선택(default 18시)
18시 / 14시 / 즉시
- 18시 or 14시 선택: 해당 시간이 될때까지 계속해서 퇴실 체크 진행
  ex) 18시를 선택하고 17시 58분에 프로그램을 실행하면 18시까지 반복 퇴실체크 진행 -> 18시가 기록되는 순간 프로그램 종료
- 즉시 : 현재시간과 무관하게 퇴실 체크 한 번 진행(조퇴 시 사용)


# Contributor
|[이찬진](https://github.com/jinchandol)|
|:---:|
|<img src="https://github.com/user-attachments/assets/27aebf0b-5fe6-45ce-9061-2ce1fbc21401" width="150" height="200">|
|서울 11기|
