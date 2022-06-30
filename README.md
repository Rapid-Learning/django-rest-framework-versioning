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
    - http://127.0.0.1:8000/v1/category/
    <img width="1194" alt="Category v1" src="https://user-images.githubusercontent.com/25084128/176759216-21051d8c-771b-4dda-9954-74514164a194.png">

    - http://127.0.0.1:8000/v2/category/
    <img width="1192" alt="Category v2" src="https://user-images.githubusercontent.com/25084128/176759295-15de2f06-9450-4219-a9ef-6d6a4aa0b6b4.png">
