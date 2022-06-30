## Django rest api versioning
- This project help to understand how versioning flow is works in django rest api. You can use serializer according to version. You can prefer [django documentation](https://www.django-rest-framework.org/api-guide/versioning/) for more info.

## Project setup
## 1. Create virtual environment

    python3 -m venv venv

## 2. Activate virutal environment

### For windows
    source <virtual_environment_dir>/venv/Scripts/activate

### For ubuntu
    source <virtual_environment_dir>/venv/bin/activate


## 3. Install python dependencies
    pip3 install -r requirements.txt

## 4. Run project

### Run migrations
    python manage.py makemigrations
    python manage.py migrate

### Run django server
    python manage.py runserver

### Create super user
    python manage.py createsuperuser

## 5. Visit below two urls
    - Category V1: http://127.0.0.1:8000/v1/category/

<img width="1192" alt="Category v1" src="https://user-images.githubusercontent.com/25084128/176759567-e820e9c2-d723-4460-a7bd-da611f3a134e.png">

    - Category V2: http://127.0.0.1:8000/v2/category/

<img width="1194" alt="Category v2" src="https://user-images.githubusercontent.com/25084128/176759457-13f7a66b-322a-43ff-8b80-67c26e97290c.png">
