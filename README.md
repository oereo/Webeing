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

$ ./manage.py makemigrations
$ ./manage.py migrate
$ ./manage.py runserver
```





