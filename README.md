# TODO-Calendars
### 달력 형태로 한 눈에 알아볼 수 있는 투두 리스트

---
## 개요
2022년 1학기 클라우드 프로그래밍 프로젝트이다.

## 내용
달력 형태의 메인 페이지에 할 일들을 작성하고, 그 일들을 얼마나 잘 수행했는지 확인하도록 하기 위한 프로젝트이다.
달력의 각 날짜를 클릭하였을 경우 세부적인 내용을 확인하거나 작성할 수 있다.

## 로컬 사용 방법

- Project를 clone한 후 가상 환경인 venv를 활성화시킨다.
- pip install -r requirements.txt를 통해 의존성 모듈을 받아온다.
- python manage.py makemigrations 명령어를 통하여 데이터베이스 마이그레이션을 생성한다.
- 그 후, python manage.py migrate 명령어를 통해 데이터베이스를 마이그레이트한다.
- python manage.py runserver를 통하여 서버를 활성화시킨다.

## 사용 기술
* Django
* KT PaaS-TA

## 플로우 다이어그램
![flow](./static/readme/flow.jpg)