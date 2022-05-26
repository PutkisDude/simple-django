# simple-django
Simple Ticket System

## Features
CRUD
- C: Create Ticket
- R: Read Tickets
- U: Update Tickets
- D: Delete Tickets

## Requirements
    django==3.2

## Installation

1. Install virtualenv (sudo apt-get install virtualenv) and git (sudo apt-get install git)
2. Make a new directory
    - mkdir django
    - cd django
3. Create and activate a virtual environment
    - virtualenv env/ -p python3 --system-site-packages
    - source env/bin/activate
4. Install Django
    - which pip (make you sure you are in virtualenv)
    - echo "django==3.2" > requirements.txt
    - pip install -r requirements.txt
5. Create a new directory
    - mkdir ticketsystem
    - cd ticketsystem
6. Clone this repository
    - git clone URL (TBH)
7. Change SECRET_KEY (./ticketsystem/settings.py line 23)
8. Makemigrations and migrate
    - ./manage.py makemigrations
    - ./manage.py migrate
9. Create a superuser
    - ./manage.py createsuperuser
10. Run server
    - ./manage.py runserver
11. Login via admin panel or http://127.0.0.1:8000/accounts/login/ with super user
12. Open ListView:  http://127.0.0.1:8000

