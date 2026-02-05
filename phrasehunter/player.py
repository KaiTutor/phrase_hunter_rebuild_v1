class Player:
    """
    Represents a player in the Phrase Hunter game.
    Tracks player name and game statistics.
    """
    
    def __init__(self, name):
        """
        Initialize a Player object.
        
        Args:
            name (str): The player's name
        """
        self.name = name
        self.stats = {
            "easy": {"wins": 0, "losses": 0},
            "hard": {"wins": 0, "losses": 0}
        }
    
    def update_stats(self, difficulty, outcome):
        """
        Update the player's statistics based on game outcome.
        
        Args:
            difficulty (str): The difficulty level ('easy' or 'hard')
            outcome (str): The game outcome ('win' or 'loss')
        """
        if outcome in ["win", "wins"]:
            self.stats[difficulty]["wins"] += 1
        elif outcome in ["loss", "losses"]:
            self.stats[difficulty]["losses"] += 1
    
    def display_stats(self):
        """
        Display the player's current statistics.
        """
        print(f"\n{'='*50}")
        print(f"Stats for {self.name}:")
        print(f"{'='*50}")
        
        for difficulty in ["easy", "hard"]:
            wins = self.stats[difficulty]["wins"]
            losses = self.stats[difficulty]["losses"]
            total = wins + losses
            
            print(f"\n{difficulty.upper()} Mode:")
            print(f"  Wins: {wins}")
            print(f"  Losses: {losses}")
            print(f"  Total Games: {total}")
            
            if total > 0:
                win_rate = (wins / total) * 100
                print(f"  Win Rate: {win_rate:.1f}%")
        
        print(f"{'='*50}\n")
