import random


class Player:
    def __init__(self, name):
        self.name = name
        self.turn_total = 0
        self.total_score = 0

    def roll_die(self):
        return random.randint(1, 6)


class Die:
    @staticmethod
    def roll():
        return random.randint(1, 6)


class PigGame:
    def __init__(self, player1, player2):
        self.players = [player1, player2]
        self.current_player = random.choice(self.players)
        self.other_player = next(p for p in self.players if p != self.current_player)
        self.die = Die()

    def switch_players(self):
        self.current_player, self.other_player = self.other_player, self.current_player

    def display_game_state(self):
        print(f"{self.current_player.name}'s turn:")
        print(f"Current turn total: {self.current_player.turn_total}")
        print(f"Total score: {self.current_player.total_score}")

    def play_turn(self):
        while True:
            decision = input("Enter 'r' to roll or 'h' to hold: ").lower()

            if decision == 'r':
                roll_result = self.die.roll()
                print(f"Rolled a {roll_result}")

                if roll_result == 1:
                    print("Turn total reset to 0. Switching to the other player's turn.")
                    self.current_player.turn_total = 0
                    self.switch_players()
                    break
                else:
                    self.current_player.turn_total += roll_result
                    self.display_game_state()

            elif decision == 'h':
                self.current_player.total_score += self.current_player.turn_total
                print(f"{self.current_player.name} holds. Turn total added to total score.")
                self.current_player.turn_total = 0
                self.display_game_state()
                self.switch_players()
                break

            else:
                print("Invalid input. Please enter 'r' or 'h'.")

    def play_game(self):
        while max(player.total_score for player in self.players) < 100:
            self.play_turn()

        print(f"{self.current_player.name} wins with a total score of {self.current_player.total_score}!")


if __name__ == "__main__":
    # Set a random seed for consistency in testing
    random.seed(0)

    # Create two players
    player1 = Player("Player 1")
    player2 = Player("Player 2")

    # Create a PigGame instance and start the game
    game = PigGame(player1, player2)
    game.play_game()
