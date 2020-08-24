import tkinter
import BlackjackSetup
import GameFunctionality
import GameEvents

# Sets the main menu
class Application(tkinter.Frame):
    def __init__(self, master = None):
        super().__init__(master)
        self.master = master
        self.pack()
        self.create_widgets()


    # Sets a value for each button when button pressed
    def create_widgets(self):
        # Hit Button
        self.Hit = tkinter.Button(self, text = "Hit", fg = "black", command = lambda:self.main_game(0)) # The value for the Hit Button is 0
        self.Hit["state"] == "normal"
        self.Hit.pack(side = tkinter.TOP)

        # Fold Button
        self.Fold = tkinter.Button(self, text = "Fold (Stand)", fg = "black", command = lambda:self.main_game(1))
        self.Hit["state"] == "normal"
        self.Fold.pack(side = tkinter.BOTTOM)
       

        # Quit Button
        self.Quit = tkinter.Button(self, text = "Quit", fg = "red", command = self.master.destroy)
        self.Quit.pack(side = tkinter.BOTTOM)


    def main_game(self, Button_value):
        if Button_value == 0 and self.Hit["state"] == "normal":
            BlackjackSetup.show_cards()
            GameFunctionality.hit(BlackjackSetup.player)
        elif Button_value == 1 and self.Fold["state"] == "normal":
            self.Hit["state"] = "disabled"
            self.Fold["state"] = "disabled"
            GameEvents.dealer_AI()
            

