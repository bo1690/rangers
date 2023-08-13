import datetime
from flask import Flask, render_template


main = Flask(__name__)

@main.route("/")
def hello_world():
    return render_template('home.html', curryear = datetime.datetime.today().year)

if __name__ == "__main__":
    main.run(host="0.0.0.0", debug=True)