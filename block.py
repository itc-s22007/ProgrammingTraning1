class Block:
    x = 63
    y = 40
    def __init__(self, canvas, color):
        self.cnavas = canvas
        self.id = [canvas.create_rectangle(i*self.x, m*self.y, (i+1)*self.x, (m+1)*self.y, fill = color) for i in range(12) for m in range(3)]
