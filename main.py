import datetime
from flask import Flask, render_template, jsonify

PLAYERS = [
  {
    'id:':1,
    'name': 'Jack Butland',
    'position': 'Goalkeeper',
    'country': 'England'
  },
    {
    'id:':2,
    'name': 'Connor Goldson',
    'position': 'Defender',
    'country': 'England'
  },
    {
    'id:':3,
    'name': 'Todd Cantwell',
    'position': 'Midfielder',
    'country': 'England'
  },
    {
    'id:':4,
    'name': 'Danilo',
    'position': 'Forward',
    'country': 'Brazil'
  }
]

main = Flask(__name__)

@main.route("/")
def hello_world():
    return render_template('home.html', players=PLAYERS, curryear = datetime.datetime.today().year)

##API - NOT DOING ANYTHING WITH IT AT THE MOMENT
@main.route("/api/players")
def list_players():
  return jsonify(PLAYERS)

if __name__ == "__main__":
    main.run(host="0.0.0.0", debug=True)