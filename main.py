from tkinter import *
from ball import Ball
from paddle import Paddle
from block import Block
class Game:
    def __init__(self):
        self.tk = Tk()
        self.tk.title("Game")
        self.tk.resizable(False, False)
        self.tk.wm_attributes("-topmost", True)
        self.canvas = Canvas(self.tk, width=500, height=400, bd=False, highlightthickness=False)
        self.canvas.pack()
        self.tk.update()
        self.paddle = Paddle(self.canvas, "blue")
        self.ball = Ball(self.canvas, "red",self.paddle)
        self.block = Block(self.canvas, "red")
        self.canvas.bind_all("<KeyPress-Left>", self.paddle.turn_left)
        self.canvas.bind_all("<KeyPress-Right>", self.paddle.turn_right)
        self.canvas.bind_all("<KeyPress-space>", self.ball.start)
    def main(self):
        self.update()
        self.tk.mainloop()
    def update(self):
        self.ball.draw()
        self.paddle.draw()
        self.canvas.after(1000 // 60, self.update)
game = Game()
game.main()
