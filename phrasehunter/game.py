import random
from phrasehunter.phrase import Phrase
from phrasehunter.player import Player
from phrasehunter import all_phrases


class Game:
    """
    Main game controller for Phrase Hunter.
    Manages game flow, user input, and game state.
    """
    
    def __init__(self):
        """Initialize a new Game instance."""
        self.player = None
        self.difficulty = None
        self.active_phrase = None
        self.guesses = []
        self.missed = 0
        self.max_misses = 5
    
    def start(self):
        """
        Start the game by setting up and running the main game loop.
        """
        self.welcome()
        self.setup_player()
        self.game_loop()
    
    def welcome(self):
        """Display a welcome message to the player."""
        print("\n" + "="*50)
        print("  WELCOME TO PHRASE HUNTER!")
        print("="*50)
        print("\nGuess the phrase one letter at a time.")
        print("You have 5 lives. Lose them all and it's game over!")
        print("="*50 + "\n")
    
    def setup_player(self):
        """Prompt for player name and create a Player instance."""
        name = input("Please enter your name: ").strip()
        while not name:
            print("Name cannot be empty!")
            name = input("Please enter your name: ").strip()
        
        self.player = Player(name)
        print(f"\nHello, {self.player.name}! Let's play!\n")
    
    def select_difficulty(self):
        """Ask the user to select a difficulty level."""
        print("Select difficulty:")
        print("  1. Easy (3-4 word phrases)")
        print("  2. Hard (longer phrases)")
        
        while True:
            choice = input("\nEnter 1 for Easy or 2 for Hard: ").strip()
            
            if choice == "1":
                self.difficulty = "easy"
                break
            elif choice == "2":
                self.difficulty = "hard"
                break
            else:
                print("Invalid choice! Please enter 1 or 2.")
        
        print(f"\nYou selected {self.difficulty.upper()} mode!\n")
    
    def select_phrase(self):
        """Select a random phrase based on the chosen difficulty."""
        if self.difficulty == "easy":
            phrases = all_phrases.easy
        else:
            phrases = all_phrases.hard
        
        random_phrase = random.choice(phrases)
        self.active_phrase = Phrase(random_phrase)
    
    def get_guess(self):
        """
        Get a letter guess from the user and validate it.
        
        Returns:
            str: A valid single letter guess
        """
        while True:
            guess = input("Guess a letter: ").strip().lower()
            
            # Validate input
            if len(guess) != 1:
                print("Please enter only one character!")
                continue
            
            if not guess.isalpha():
                print("Please enter a letter (a-z)!")
                continue
            
            if guess in self.guesses:
                print(f"You already guessed '{guess}'. Try a different letter!")
                continue
            
            return guess
    
    def process_guess(self, guess):
        """
        Process a player's guess and update game state.
        
        Args:
            guess (str): The letter guessed by the player
        """
        self.guesses.append(guess)
        
        if self.active_phrase.check_letter(guess):
            print(f"\nCorrect! The letter '{guess}' is in the phrase!\n")
        else:
            self.missed += 1
            remaining = self.max_misses - self.missed
            
            if remaining > 0:
                print(f"\nSorry! The letter '{guess}' is not in the phrase.")
                print(f"You have {remaining} out of {self.max_misses} lives remaining!\n")
            else:
                print(f"\nSorry! The letter '{guess}' is not in the phrase.")
    
    def check_game_over(self):
        """
        Check if the game has ended (win or loss).
        
        Returns:
            bool: True if game is over, False otherwise
        """
        # Check for loss
        if self.missed >= self.max_misses:
            return True
        
        # Check for win
        if self.active_phrase.check_complete(self.guesses):
            return True
        
        return False
    
    def display_result(self):
        """Display the game result and update player stats."""
        print("\n" + "="*50)
        
        if self.active_phrase.check_complete(self.guesses):
            print("  CONGRATULATIONS! YOU WIN!")
            print("="*50)
            print(f"\nYou successfully guessed the phrase: '{self.active_phrase.phrase}'")
            self.player.update_stats(self.difficulty, "win")
        else:
            print("  GAME OVER - YOU LOST!")
            print("="*50)
            print(f"\nThe phrase was: '{self.active_phrase.phrase}'")
            print("Better luck next time!")
            self.player.update_stats(self.difficulty, "loss")
        
        # Display updated stats
        self.player.display_stats()
    
    def reset_game(self):
        """Reset the game state for a new round."""
        self.difficulty = None
        self.active_phrase = None
        self.guesses = []
        self.missed = 0
    
    def play_again(self):
        """
        Ask if the player wants to play again.
        
        Returns:
            bool: True if player wants to play again, False otherwise
        """
        while True:
            choice = input("Would you like to play again? (yes/no): ").strip().lower()
            
            if choice in ["yes", "y"]:
                return True
            elif choice in ["no", "n"]:
                return False
            else:
                print("Please enter 'yes' or 'no'.")
    
    def goodbye(self):
        """Display a goodbye message."""
        print("\n" + "="*50)
        print(f"  Thanks for playing, {self.player.name}!")
        print("="*50)
        print("\nSee you next time! 👋\n")
    
    def game_loop(self):
        """Main game loop that controls the flow of the game."""
        playing = True
        
        while playing:
            # Setup new game
            self.select_difficulty()
            self.select_phrase()
            
            # Display initial phrase
            print("Here's your phrase:")
            self.active_phrase.display(self.guesses)
            
            # Play game
            while not self.check_game_over():
                guess = self.get_guess()
                self.process_guess(guess)
                self.active_phrase.display(self.guesses)
            
            # Display result
            self.display_result()
            
            # Check if player wants to play again
            if self.play_again():
                self.reset_game()
                print("\n" + "="*50)
                print("  NEW GAME!")
                print("="*50 + "\n")
            else:
                playing = False
        
        self.goodbye()
