# task_auth

just run following commands to run the application.

git clone https://github.com/rishi-nstarx/task_auth.git
cd auth_project
docker-compose build
docker-compose up

Then go to inside web_app container's and run following commands;

python manage.py makemigrations auth_app
python manage.py migrate

After all this your application will run.
