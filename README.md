## To Run, Environment needs to be activated
```
python -m pip install virtualenv
python -m virtualenv venv
venv\Scripts\lib\activate
pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```