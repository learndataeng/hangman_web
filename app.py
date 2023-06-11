#!/usr/bin/env python3.8
# -*- coding: utf-8 -*-
import random
from flask import Flask, session

app = Flask(__name__)

HANGMANPICS = ['''

  +---+
  |   |
      |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
      |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
  |   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|   |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\\  |
      |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\\  |
 /    |
      |
=========''', '''

  +---+
  |   |
  O   |
 /|\\  |
 / \\  |
      |
=========''']


def loadWordList():
    words = ["hangman", "programmers", "data", "engineering", "datawarehouse"]
    """
    try:
        conn = pymysql.connect(host='localhost',
                       user='root', password='keeyonghan',
                       db='test', charset='utf8')
        curs = conn.cursor()
        sql = "select word from test.words"
        curs.execute(sql)
        rows = curs.fetchall()
        for row in rows:
            words.append(row[0])
        conn.close()
    except Exception as e:
        print("Can't read from the word table")
    """
    return words


def getRandomWord(wordList):
    # This function returns a random string from the passed list of strings.
    wordIndex = random.randint(0, len(wordList) - 1)
    return wordList[wordIndex]


def displayBoard(HANGMANPICS, missedLetters, correctLetters, secretWord):
    html = HANGMANPICS[len(missedLetters)]
    html += "\n"
    html += "Missed letters:"
    for letter in missedLetters:
        html += letter
    html += "\n"

    blanks = ''
    for i in range(len(secretWord)):  # replace blanks with correctly guessed letters
        if secretWord[i] in correctLetters:
            blanks += secretWord[i]
        else:
            blanks += '_'

    for letter in blanks:  # show the secret word with spaces in between each letter
        html += letter + " "
    html += "\n"

    return "<h3><pre>" + html + "</pre></h3>"


def getGuess(alreadyGuessed):
    # Returns the letter the player entered. This function makes sure the player
    # entered a single letter, and not something else.
    while True:
        print('Guess a letter.')
        guess = input().lower()
        if len(guess) != 1:
            print('Please enter a single letter.')
        elif guess in alreadyGuessed:
            print('You have already guessed that letter. Choose again.')
        elif guess not in 'abcdefghijklmnopqrstuvwxyz':
            print('Please enter a LETTER.')
        else:
            return guess


def playAgain():
    # This function returns True if the player wants to play again, otherwise it returns False.
    print('Do you want to play again? (yes or no)')
    return input().lower().startswith('y')


# Check if the player has won
def checkCorrectAnswer(correctLetters, secretWord):
    foundAllLetters = True
    for i in range(len(secretWord)):
        if secretWord[i] not in correctLetters:
            foundAllLetters = False
            break
    return foundAllLetters


# Check if player has guessed too many times and lost
def checkWrongAnswer(missedLetters, secretWord):
    # Check if player has guessed too many times and lost
    if len(missedLetters) == len(HANGMANPICS) - 1:
        return True
    return False


@app.route("/")
def main():
    session["words"] = loadWordList()

    """Main application entry point."""
    header = '<h1>H A N G M A N</h1><p>'
    session["missedLetters"] = ''
    session["correctLetters"] = ''
    session["gameSucceeded"] = False
    session["gameFailed"] = False
    session["secretWord"] = getRandomWord(session["words"])

    html = "<center>" + header + displayBoard(
        HANGMANPICS,
        session["missedLetters"],
        session["correctLetters"],
        session["secretWord"]
    ) + "</center>"

    return html


# python3 -m flask run --host=0.0.0.0 --port=4000
app.secret_key = "Python Study"
if __name__ == "__main__":
    app.run()
