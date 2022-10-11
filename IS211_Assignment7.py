import random
import os
class Player:
    def __init__(self, name):
        self.name = name
        self.score = 0
        self.turn = 0

    def roll(self):
        x = random.randint(1, 6)
        if(x == 1):
            print("You rolled a 1, your turn is over, and you got 0 points for this round!")
            self.turn = 0
            return 0
        else:
            self.turn += x
        
    def hold(self):
        print("You have chosen to hold, your turn is over, and you got " + str(self.turn) + " points for this round!")
        self.score += self.turn
        self.turn = 0

    def __str__(self):
        return self.name + " Previous Score: " + str(self.score) + " and Current Round Score: " + str(self.turn)
    
class Game:
    def __init__(self, player1, player2):
        self.player1 = player1
        self.player2 = player2
        self.turn = 1

    def play(self):
        while(self.player1.score < 100 and self.player2.score < 100):
            if(self.turn == 1):
                print("It is " + self.player1.name + "'s turn")
                x = input("Would you like to roll (r) or hold (h)? ")
                os.system("clear")
                if(x == "r"):
                    self.player1.roll()
                    if(self.player1.turn == 0):
                        self.turn = 2
                elif(x == "h"):
                    self.player1.hold()
                    self.turn = 2
                else:
                    print("Invalid input")
                print(self.player1)
                print(self.player2)
            else:

                print("It is " + self.player2.name + "'s turn")
                x = input("Would you like to roll (r) or hold (h)? ")
                os.system("clear")

                if(x == "r"):
                    self.player2.roll()
                    if(self.player2.turn == 0):
                        self.turn = 1
                elif(x == "h"):
                    self.player2.hold()
                    self.turn = 1
                else:
                    print("Invalid input")
                print(self.player1)
                print(self.player2)

        
        if(self.player1.score >= 100):
            print(self.player1.name + " wins!")
        else:
            print(self.player2.name + " wins!")
            
def main():
    player1 = Player(input("What is the name of player 1? \n"))
    player2 = Player(input("What is the name of player 2? \n"))
    os.system("clear")
    game = Game(player1, player2)
    game.play()

if __name__ == "__main__":
    main()
    
