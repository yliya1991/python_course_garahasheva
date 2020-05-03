from flask import Flask, request
from requirements import fun_requirements
from users_mail import user_list
from astronauts import astronauts_space
from mean import mean

app = Flask (__name__)


@app.route ('/')
def start():
    return ''


@app.route ('/requirements/')
def requirements():
    return fun_requirements ( )


@app.route ('/generate-users/')
def users():
    count = int(request.args['count'])
    return user_list(count)


@app.route ('/space/')
def astronauts():
    return str(astronauts_space ( ))


@app.route ('/mean/')
def height_weight():
    return mean()


if __name__ == '__main__':
    app.run (port=5000)
