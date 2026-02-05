# Phrase Hunter Game

A word guessing game built with Python using Object-Oriented Programming principles.

## Description

Phrase Hunter is a console-based game where players try to guess a hidden phrase one letter at a time. Players have 5 lives and must guess all letters in the phrase before running out of lives.

## Features

- **Two Difficulty Levels:**
  - Easy: 3-4 word phrases
  - Hard: Longer, more challenging phrases

- **Player Statistics:**
  - Track wins and losses for each difficulty
  - View win rate and total games played

- **Game Mechanics:**
  - 5 lives per game
  - Clear visual feedback for guessed/unguessed letters
  - Input validation
  - Play multiple rounds with the same player

## Project Structure

```
phrase-hunter/
│
├── app.py                    # Main entry point
│
└── phrasehunter/            # Game package
    ├── __init__.py          # Package initializer
    ├── phrase.py            # Phrase class
    ├── player.py            # Player class
    ├── game.py              # Game class (main controller)
    └── all_phrases.py       # Phrase lists
```

## How to Run

1. Make sure you have Python 3.x installed
2. Navigate to the project directory
3. Run the game:
   ```bash
   python app.py
   ```

## How to Play

1. Enter your name when prompted
2. Choose a difficulty level (Easy or Hard)
3. Guess letters one at a time
4. Try to complete the phrase before running out of lives
5. View your statistics after each game
6. Choose to play again or quit

## Game Rules

- You have 5 lives (incorrect guesses)
- Only single letters (a-z) are accepted
- Spaces between words are clearly visible
- Each letter can only be guessed once
- Win by guessing all letters in the phrase
- Lose by running out of lives

## Classes

### Phrase Class (`phrase.py`)
- Manages the phrase to be guessed
- Displays guessed/unguessed letters
- Checks if letters exist in the phrase
- Checks if the phrase is complete

### Player Class (`player.py`)
- Stores player name
- Tracks win/loss statistics for each difficulty
- Updates and displays statistics

### Game Class (`game.py`)
- Main game controller
- Manages game flow and state
- Handles user input and validation
- Controls game loop

## Example Gameplay

```
==================================================
  WELCOME TO PHRASE HUNTER!
==================================================

Guess the phrase one letter at a time.
You have 5 lives. Lose them all and it's game over!
==================================================

Please enter your name: Alex

Hello, Alex! Let's play!

Select difficulty:
  1. Easy (3-4 word phrases)
  2. Hard (longer phrases)

Enter 1 for Easy or 2 for Hard: 1

You selected EASY mode!

Here's your phrase:

_ _ _ _ _  _ _  _ _ _ _

Guess a letter: e

Correct! The letter 'e' is in the phrase!

_ _ _ e _  _ _  _ _ _ e

Guess a letter:
```

## Requirements

- Python 3.x
- No external dependencies required

## License

This project is created for educational purposes.
