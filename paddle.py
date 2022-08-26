class Paddle:
    def __init__(self, canvas, color):
        self.canvas = canvas
        self.id = self.canvas.create_rectangle(0, 0, 450, 10, fill=color)
        self.canvas_width = self.canvas.winfo_width()
        self.x = 0
        self.canvas.moveto(self.id, self.canvas_width / 2 - 50, 370)
    def draw(self):
        self.canvas.move(self.id, self.x, 0)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.x = 0
            self.canvas.move(self.id, -pos[0], 0)
        if pos[2] >= self.canvas_width:
            self.x = 0
            self.canvas.move(self.id, -(pos[2] - self.canvas_width), 0)
    def turn_left(self, evt):
        self.x = -3
    def turn_right(self, evt):
        self.x = 3
