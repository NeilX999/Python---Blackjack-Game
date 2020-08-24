#!/usr/bin/python

# Python BlackJack

import GameFramework


# Window Setup
root = GameFramework.tkinter.Tk()
Game = GameFramework.Application(master = root)
window_width, window_height = 250, 150
Game.master.minsize(window_width, window_height)
Game.master.maxsize(window_width, window_height)
Game.master.title("Python Blackjack")
Game.mainloop()