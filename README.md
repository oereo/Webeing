# Webeing Services

Webeing is a platform to provide food and other stuff which is closed with the expired day with the low prices So We can save the Earth, too.

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

-----------------------------
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