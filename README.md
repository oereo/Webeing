# Webeing Services

Webeing is a platform to provide food and other stuff which is closed with the expired day with the low prices So We can save the Earth, too.

## Contributor
- Likelion in Chungang University

## Branch structure

### Main branch
* Master branch : It is Manage only the state that can be distributed
* Develop branch : It is Used to merge branches for feature development

### Secondary branch

* Feature branch : Branch to develop the function ex)feature/profile
* Fix branch : Branch to fix the function ex)fix/profile

## Guide

```console
$ git clone https://github.com/oereo/Algorithm_for_CodingTest.git
$ git pull origin develop
$ python -m venv myvenv
$ source myvenv/scripts/activate  mac) source myvenv/bin/activate
$ cd Webeing
$ pip install -r requirements.txt

$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py runserver
```

## Commit rule
```console
git commit -m "text"
```

|Keyword|Description|
|:---:|:---|
|[ADD]|코드나 테스트, 예제, 문서 등의 추가가 있을 때 사용|
|[fix]|올바르지 않은 로직을 고친 경우에 사용|
|[REMOVE]|코드의 삭제가 있을 때 사용|
|[UPDATE]|개정이나 버전 업데이트가 있을 때 사용|
|[CORRECT]|주로 문법의 오류나 타입의 변경, 이름 변경 등에 사용|

## Convention
#### 1. test.py 작성
- 기능에 대한 validation을 할 수 있는 test code를 작성
- 기능에 대한 문제가 날만한 test code를 작성

#### 2. method
- CRUD 순서로 함수 작성

#### 3. import
- module을 import 해야될 때는 무조건 알파벳 순서로 정리

#### 4. python
- class, function 간의 간격은 무조건 2줄
- def (method)의 경우에 간격은 무조건 1줄

#### 5. comments
- 로직, class, function에 대한 설명의 주석 작성
- 사용이 안되는 코드의 주석은 무조건 삭제하고 pull request

## Merge Rule
- merge는 확실하게 된 pull request만 할 것
- 에러나 convention이 잘 지켜지지 않았을 경우 코드리뷰를 하거나 보고 수정을 할 것 
