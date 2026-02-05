"""
Phrase Hunter Game - Main Entry Point

A word guessing game where players try to guess a hidden phrase
one letter at a time. Players can choose between easy and hard
difficulties and track their win/loss statistics.
"""

from phrasehunter.game import Game


if __name__ == "__main__":
    # Create a new game instance
    game = Game()
    
    # Start the game
    game.start()
