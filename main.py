import datetime
from flask import Flask, render_template

PLAYERS = [
  {
    'id:':1,
    'name': 'Jack Butland',
    'position': 'Goalkeeper'
  },
    {
    'id:':2,
    'name': 'Connor Goldson',
    'position': 'Defender'
  },
    {
    'id:':3,
    'name': 'Todd Cantwell',
    'position': 'Midfielder'
  },
    {
    'id:':4,
    'name': 'Danilo',
    'position': 'Forward'
  }
]

main = Flask(__name__)

@main.route("/")
def hello_world():
    return render_template('home.html', players=PLAYERS, curryear = datetime.datetime.today().year)

if __name__ == "__main__":
    main.run(host="0.0.0.0", debug=True)