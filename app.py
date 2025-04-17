from flask import Flask, request, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/wordle_game", methods=["GET", "POST"])
def wordle_game():
    return render_template("wordle_game.html")

if __name__ == "__main__":
    app.run()