import random

class Game:
    def __init__(self, rounds):
        self.rounds = rounds
        self.computerScore = 0
        self.humanScore = 0

    def generateComputerChoice(self):
        return random.randint(1, 3)

    def viewOptions(self):
        choiceList = ["rock", "paper", "scissors"]
        print("\nSelect one:")
        for option, value in enumerate(choiceList, 1):
            print(f"{option}. {value}")

    def showSelectedOption(self, n):
        match n:
            case 1:
                return "rock"
            case 2:
                return "paper"
            case 3:
                return "scissors"

    def determine_winner(self, human_choice, computer_choice):
        if human_choice == computer_choice:
            return "tie"
        elif (human_choice == 1 and computer_choice == 3) or \
             (human_choice == 2 and computer_choice == 1) or \
             (human_choice == 3 and computer_choice == 2):
            self.humanScore += 1
            return "human"
        else:
            self.computerScore += 1
            return "computer"

    def winnerName(self):
        if self.computerScore == self.humanScore:
            return "The game is a tie."
        elif self.computerScore > self.humanScore:
            return "The computer is the winner."
        else:
            return "The human is the winner."

if __name__ == "__main__":
    rounds = int(input("How many rounds you want to play: "))
    game = Game(rounds)

    for _ in range(game.rounds):
        game.viewOptions()
        human_choice = int(input("Enter your choice (1, 2, or 3): "))
        while human_choice not in [1, 2, 3]:
            print("Invalid choice, please try again.")
            human_choice = int(input("Enter your choice (1, 2, or 3): "))

        computer_choice = game.generateComputerChoice()
        print(f"Computer chose: {game.showSelectedOption(computer_choice)}")
        print(f"You chose: {game.showSelectedOption(human_choice)}")

        winner = game.determine_winner(human_choice, computer_choice)
        if winner == "tie":
            print("It's a tie!")
        elif winner == "human":
            print("You win this round!")
        else:
            print("Computer wins this round!")
    
    print("\n==========================================")
    print("Final Scores:")
    print(f"Computer: {game.computerScore}")
    print(f"Human: {game.humanScore}")
    print(f"Total tie: {rounds-game.computerScore-game.humanScore}")
    print(game.winnerName())
    print("==========================================\n")
