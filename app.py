from boggle import Boggle
from flask import Flask, render_template, request, jsonify, session
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)
app.debug = True
app.config['SECRET_KEY'] = 'secret'

toolbar = DebugToolbarExtension(app)

boggle_game = Boggle()
# board = boggle_game.make_board()

@app.route('/')
def show_board():
   """Show game board"""
   board = boggle_game.make_board()
   session['board'] = board
   return render_template('index.html', board=board)

@app.route('/check-word')
def check_word():
   """Check if word is in dictionary"""

   word = request.args.get('word') 
   board = session['board']
   # print(board)
   response = boggle_game.check_valid_word(board, word)
   return jsonify({'result': response})

@app.route('/post-score', methods=["POST"])
def show_score():
   """Receive score, show final score"""

   score = request.json['score']

   highscore = session.get('highscore', 0)
   session['highscore'] = max(score, highscore)

   nplays = session.get('nplays', 0)
   session['nplays'] = nplays + 1

   return jsonify(brokeRecord=score > highscore)


