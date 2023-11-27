from flask import Flask, render_template, flash, jsonify, redirect, url_for
from tic_tac_toe import TicTacToe

app = Flask(__name__)
app.secret_key = "TicTacToe"
game = TicTacToe()

@app.route('/')
def index():
    map = {"O": "⭕️", "X": "❌", "_": "⬜️"}
    return render_template('index.html', board=game.board, map=map)

@app.route('/reset')
def reset():
    game.board = [["_", "_", "_"], ["_", "_", "_"], ["_", "_", "_"]]
    return redirect(url_for("index"))

@app.route('/move/<x>/<y>', methods=['GET', 'POST'])
def move(x, y):
    if game.check_win() or len(game.free_spots()) == 0:
        flash("Game ended. Click 'Reset' button to start new game.")
        return redirect(url_for("index"))

    map = {"O": "⭕️", "X": "❌"}
    if game.make_move(int(x), int(y)):
        winner = game.check_win()
        if winner:
            flash(f"{map[winner]} wins")
        elif len(game.free_spots()) == 0:
            flash("Draw 😭")
    else:
        flash(f"Select a free cell to play!")
    return redirect(url_for("index"))

if __name__ == '__main__':
    app.run(debug=True)