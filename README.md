# django-course
keeping notes/class projects in this folder

Creates a virtual enviroment
python -m venv ./venv

deactivate to leave virtual enviroment

to launch the virtual enviroment absolute path to the activate batch script

C:/Users/crash/OneDrive/Desktop/django-course/btre_project/venv/Scripts/activate.bat

To start project
django-admin startproject btre .

Command to runserver:
python manage.py runserver

To create a new app 
python manage.py startapp name-of-new-folder

ex: python manage.py startapp pages

Create a static fold in the project folder and update the settings for static folders to 

STATIC_ROOT= os.path.join(BASE_DIR, 'static')
STATIC_URL = '/static/'
STATICFILES_DIRs= [
    os.path.join(BASE_DIR, 'btre/static')
]

There will be two files after running this command. One that was made in btre and one added to the root directory

run the command 
python manage.py collectionstatic 

if you want to break the base.html page up more create a partials folder

format {%include '{folder_name/{file_name}}' %}

ex: {% include 'partials/_footer.html}