# Tech_Test
School Teacher DBMS

setup

Download Python from official website
https://www.python.org/downloads/


Clone the repository:

$ git clone https://github.com/akashgusain/Tech_Test.git

$ cd Tech_Test

Create a virtual environment to install dependencies in and activate it:

Virtual Env installation

https://virtualenv.pypa.io/en/latest/installation.html

$ virtualenv venv

$ source env/bin/activate

Then install the dependencies:

(env)$ pip install -r requirements.txt

Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv.

Once pip has finished downloading the dependencies:

(env)$ cd Tech_Test (you have to be inside Tech_Test main folder where manage.py file is there )

(env)python3 manage.py migrate

Create a superuser:

python3 manage.py createsuperuser and follow instructions on screen to add your credentials
  
(env)$ python manage.py runserver

And navigate to http://127.0.0.1:8000/api/swagger

check all api listed in the Swagger UI

login for accesing logged in user API's (Djano Rest api are Browsable API - https://www.django-rest-framework.org/topics/browsable-api/#the-browsable-api)

http://127.0.0.1:8000/admin/login/?next=/admin/

http://127.0.0.1:8000/api/teachers/

Teachers to filtered by first letter of last name or by subject

http://127.0.0.1:8000/api/teachers/?search=l

search paramaters can be used 
