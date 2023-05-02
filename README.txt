#making a virtual environement
python -m venv venv

#activating a virtual environement
venv\scripts\activate

python -m pip install --upgrade pip

pip install django

django-admin startproject store_project

cd store_project

python manage.py startapp store

python manage.py runserver

python manage.py migrate

#if the base diferences:
python manage.py makemigrations
python manage.py migrate

#making admin
python manage.py createsuperuser
Arthur
a@a.com
54312

#working with library
pip install pillow