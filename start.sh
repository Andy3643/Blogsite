export SECRET_KEY="secretkey1"
export SQLALCHEMY_DATABASE_URI='postgresql+psycopg2://moringa:pass123@localhost/personalblog'
export MAIL_USERNAME='pitcheshubapp@gmail.com'
export MAIL_PASSWORD='Get#yourinfo'


python3 manage.py server






python3.9 manage.py db migrate -m ""
python3.9 manage.py db upgrade
