# Tech_Test
School Teacher DBMS

setup
The first thing to do is to clone the repository:

$ git clone https://github.com/akashgusain/Tech_Test.git
$ cd Tech_Test
Create a virtual environment to install dependencies in and activate it:

$ virtualenv2 --no-site-packages env
$ source env/bin/activate
Then install the dependencies:

(env)$ pip install -r requirements.txt
Note the (env) in front of the prompt. This indicates that this terminal session operates in a virtual environment set up by virtualenv2.

Once pip has finished downloading the dependencies:

(env)$ cd Tech_Test
(env)python3 manage.py migrate

Create a superuser:
python3 manage.py createsuperuser and follow instructions
  
(env)$ python manage.py runserver
And navigate to http://127.0.0.1:8000/api/swagger
check all api listed in them 

login for accesing logged in user API's
http://127.0.0.1:8000/admin/login/?next=/admin/
