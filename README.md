#Create Virtualenv
 - python3 -m venv venv

#Activate Virtualenv
 - source venv/bin/activate

#Install requirements
 - pip install -r requirements.txt

#Create Migrations:
 - python manage.py makemigrations
 - python manage.py migrate

#Create .env file on root level
  - touch .env
  - copy variable names from env_example file and put in .env file

#Get Access token and refresh token
  - http://127.0.0.1:8000/api/token/ - for get access token and refresh token
  - http://127.0.0.1:8000/api/token/refresh/ - for update access token using refresh token

#swagger UI:
  - http://127.0.0.1:8000/ - for vendor and purchase order endpoints