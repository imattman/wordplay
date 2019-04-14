#!/usr/bin/env python3

from flask import Flask, jsonify, render_template, request
import pathlib
import wordplay

word_file = pathlib.Path(__file__).parent / 'sowpods.txt'
print("loading word_file:", word_file)
word_list = wordplay.load_lexicon_file(word_file)
lexicon = wordplay.Lexicon(word_list)
app = Flask(__name__)


@app.route("/")
def hello():
    return render_template('index.html',
                           letters=['qwerty', 'asdf'],
                           words=['apple', 'wombat', 'xylophone'],
                           missing=['cray cray', 'woozle', 'nerfherder'])


@app.route("/api/v1/score")
def score_letters_query():
    return score_letters(request.args.get('l'))


@app.route("/api/v1/score/<letters>")
def score_letters(letters):
    letters = letters.strip().lower()
    score = wordplay.score_word(letters)
    result = {'letters': sorted(list(letters)),
              'score': score}
    return jsonify(result)


@app.route("/api/v1/words/<word>")
def lookup_word(word):
    word = word.strip().lower()
    if word not in lexicon:
        # return better-than-nothing message along with HTTP 404 NOT FOUND
        return jsonify({'message': f"'{word}' not found in lexicon"}), 404

    score, word = lexicon[word]
    return jsonify({'word': word, 'score': score})


@app.route("/api/v1/matches/<letters>")
def find_matches(letters):
    letters = letters.strip().lower()
    return jsonify({'message': 'not yet implemented'})


def main():
    app.run(debug=True)


if __name__ == "__main__":
    main()
