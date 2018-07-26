import board
from tkinter import *
import time
import random

player1Turn = True
player1var = 1
player2var = 1

class BoardGUI:

    #constructor
    def __init__(self):

        #initialize global variables
        global player1Turn
        global player1var
        global player2var

        #initialize the GUI frame
        self.root = Tk()

        #set the canvas height and width
        self.canvas_height = 1000
        self.canvas_width = 800

        #set the square size
        self.square_size = 80

        #create a container for the whole display
        self.myContainer1 = Frame(self.root)
        #add the container to the frame
        self.myContainer1.pack()

        #set player1 turn when start game
        player1Turn = True

        #create a canvas
        self.w = Canvas(self.myContainer1, height = self.canvas_height, width = self.canvas_width)
        self.background = PhotoImage(file = "smolboard.png")
        self.w.create_image(0, 0, anchor="nw", image = self.background)

        #add button to roll dice
        self.diceButton = Button(self.root, text="ROLL DICE", bg="lightblue", command=self.rollDice)
        self.diceButton.place(x=365, y=880)


        #add the canvas to the frame
        self.w.pack()

        for x in range(10):
            for y in range(10):
                #alternate squares
                if (y+x)%2 == 0:
                    self.w.create_rectangle(x*self.square_size, y*self.square_size, self.square_size*(x+1), self.square_size*(y+1))#, fill = "#9AECDB") #light
                else:
                    self.w.create_rectangle(x*self.square_size, y*self.square_size, self.square_size*(x+1), self.square_size*(y+1))#, fill = "#c0392b") #dark

                #numbering on board
                #if y%2 == 0:
                #    self.w.create_text(self.square_size*(x+1)-(self.square_size/2), self.square_size*(y+1)-(self.square_size/2), text ="%d" % (100-((x) + (y*10))))
                #elif y%2 != 0:
                #    self.w.create_text(self.square_size*(x+1)-(self.square_size/2), self.square_size*(y+1)-(self.square_size/2), text ="%d" % (100-(10-(x+1) + (y*10))))


        #use picture as background
        #self.background = PhotoImage(file = "smolboard.png")
        #self.background_label = Label(self.root, image=self.background)
        #self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

        #this command updates the GUI every 10 ms
        #calls the drawPieces() function every 10 ms
        self.root.after(10, self.rollDice)
        self.root.mainloop()



    #this function is for the rolling of dice
    def rollDice(self):

        #initialize global variables
        global player1Turn
        global player1var
        global player2var

        #text to show which player's turn
        #if player1Turn == True:
        #    player1_turn = "It is Player 1's turn"
        #    self.w.create_text(350, 820, anchor="nw", text=player1_turn)
        #elif player1Turn == False:
        #    player2_turn = "It is Player 2's turn"
        #    self.w.create_text(350, 820, anchor="nw", text=player2_turn)

        #delete text when start loop
        self.w.delete("roll_dice")
        self.w.delete("player1_turn")
        self.w.delete("player2_turn")

        #random dice throw
        dice = random.randint(1,6)
        rollText = "You rolled %s" % dice
        self.w.create_text(365, 820, anchor="nw", text=rollText, tag="roll_dice")

        #player movement based on dice
        if player1Turn == True:
            player1_turn = "It is Player 2's turn"
            self.w.create_text(350, 850, anchor="nw", text=player1_turn, tag="player1_turn")
            player1var = player1var + dice
            player1Turn = False

        elif player1Turn == False:
            player2_turn = "It is Player 1's turn"
            self.w.create_text(350, 850, anchor="nw", text=player2_turn, tag="player2_turn")
            player2var = player2var + dice
            player1Turn = True

        else:
            pass

        ##### PLAYER 1 #####
        ##### ESCALATORS #####
        if player1var == 2:
            player1var = 37
        elif player1var == 4:
            player1var = 14
        elif player1var == 9:
            player1var = 31
        elif player1var == 21:
            player1var = 42
        elif player1var == 28:
            player1var = 84
        elif player1var == 51:
            player1var = 67
        elif player1var == 72:
            player1var = 91
        elif player1var == 80:
            player1var = 99
        ##### EELS #####
        elif player1var == 17:
            player1var = 7
        elif player1var == 54:
            player1var = 34
        elif player1var == 62:
            player1var = 19
        elif player1var == 64:
            player1var = 60
        elif player1var == 87:
            player1var = 36
        elif player1var == 93:
            player1var = 73
        elif player1var == 95:
            player1var = 75
        elif player1var == 98:
            player1var = 79

        ##### PLAYER 2 #####
        ##### ESCALATORS #####
        if player2var == 2:
            player2var = 37
        elif player2var == 4:
            player2var = 14
        elif player2var == 9:
            player2var = 31
        elif player2var == 21:
            player2var = 42
        elif player2var == 28:
            player2var = 84
        elif player2var == 51:
            player2var = 67
        elif player2var == 72:
            player2var = 91
        elif player2var == 80:
            player2var = 99
        ##### EELS #####
        elif player2var == 17:
            player2var = 7
        elif player2var == 54:
            player2var = 34
        elif player2var == 62:
            player2var = 19
        elif player2var == 64:
            player2var = 60
        elif player2var == 87:
            player2var = 36
        elif player2var == 93:
            player2var = 73
        elif player2var == 95:
            player2var = 75
        elif player2var == 98:
            player2var = 79


        ###test drawPlayers()###
        self.w.player1  = PhotoImage(file="1player.png")
        self.w.player2  = PhotoImage(file="2player.png")

        #iterates through all the tiles
        for x in range(100):
            if board.Board().board[int(x/10)][x%10] == player1var: #player1
                Player1 = self.w.create_image((x%10)*self.square_size+2, int(x/10)*self.square_size+2, anchor="nw", image=self.w.player1)
            elif board.Board().board[int(x/10)][x%10] == player2var: #player2
                Player1 = self.w.create_image((x%10)*self.square_size+2, int(x/10)*self.square_size+2, anchor="nw", image=self.w.player2)

        #when someone reaches 100
        if player1var >= 100:
            player1var = 100
            self.w.create_text(290, 920, anchor="nw", font=("Arial", 20, "bold"), text="PLAYER 1 WINS!")
        elif player2var >= 100:
            player2var = 100
            self.w.create_text(290, 920, anchor="nw", font=("Arial", 20, "bold"), text="PLAYER 2 WINS!")


    #this function is used to draw the player pieces on the board
    #def drawPlayers(self):

    #    self.w.player1  = PhotoImage(file="1player.png")
    #    self.w.player2  = PhotoImage(file="2player.png")

        #iterates through all the tiles
#        for x in range(100):
#            if board.Board().board[int(x/10)][x%10] == player1var: #player1
#                Player1 = self.w.create_image((x%10)*self.square_size+2, int(x/10)*self.square_size+2, anchor="nw", image=self.w.player1)
#            elif board.Board().board[int(x/10)][x%10] == player2var: #player2
#                Player1 = self.w.create_image((x%10)*self.square_size+2, int(x/10)*self.square_size+2, anchor="nw", image=self.w.player2)


#calls the class
BoardGUI()
