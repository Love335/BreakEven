# TODO: Import neccessary utilities and make the API calls to handle the shuffling of cards.
# Create endpoints that the frontend can access
#
from flask import Flask, render_template
import requests

app = Flask(__name__)


@app.route("/")
def main():
    return render_template("index.html")


@app.route("/api/newdeck")
def get_deck():
    url = "https://deckofcardsapi.com/api/deck/new/"
    response = requests.get(url)
    data = response.json()
    print(data)
    user_id = data["deck_id"]
    print(user_id)
    return data


@app.route("/api/drawcard")
def draw_card():
    url = "https://deckofcardsapi.com/api/deck/iun3e4moglhs/draw/?count=2"
    response = requests.get(url)
    data = response.json()
    print(data)
    return data


if __name__ == "__main__":
    app.run(debug=True, port=5000)
