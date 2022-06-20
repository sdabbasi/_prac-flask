# set a virtual environment
# pip install virtualenv
# pip install flask
# to run the flask app, activate the prepared venv
# set environment variable FLASK_APP:
#   in powershell use: $env:FLASK_APP="flaskblog.py"
#   in linux use: export FLASK_APP=flaskblog.py
# also can set environment variable FLASK_DEBUG=1
# then: flask run
# --------
# instead of the above method, can run the app as usual by using __name__ variable.


from flask import Flask

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return "<h1>Home Page!</h1>"

@app.route("/about")
def about():
    return "<h1>About Page!</h1>"

if __name__== '__main__':
    app.run(debug=True)