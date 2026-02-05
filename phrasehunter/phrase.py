class Phrase:
    """
    Represents a phrase in the Phrase Hunter game.
    Handles display of guessed/unguessed letters and checking for matches.
    """
    
    def __init__(self, phrase):
        """
        Initialize a Phrase object.
        
        Args:
            phrase (str): The phrase to be guessed
        """
        self.phrase = phrase.lower()
    
    def display(self, guesses):
        """
        Display the phrase with guessed letters visible and unguessed letters as underscores.
        Spaces between words are preserved.
        
        Args:
            guesses (list): List of letters that have been guessed
        """
        display_phrase = ""
        for char in self.phrase:
            if char == " ":
                display_phrase += "  "  # Two spaces to make word separation clear
            elif char in guesses:
                display_phrase += char + " "
            else:
                display_phrase += "_ "
        
        print(f"\n{display_phrase.strip()}\n")
    
    def check_letter(self, letter):
        """
        Check if the guessed letter is in the phrase.
        
        Args:
            letter (str): The letter to check
            
        Returns:
            bool: True if the letter is in the phrase, False otherwise
        """
        return letter.lower() in self.phrase
    
    def check_complete(self, guesses):
        """
        Check if all letters in the phrase have been guessed.
        
        Args:
            guesses (list): List of letters that have been guessed
            
        Returns:
            bool: True if the phrase is complete, False otherwise
        """
        for char in self.phrase:
            if char != " " and char not in guesses:
                return False
        return True
