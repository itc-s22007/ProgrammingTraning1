import random
import math
class Ball:
    def __init__(self, canvas, color,paddle):
        self.canvas = canvas
        self.paddle = paddle
        self.id = self.canvas.create_oval(10, 10, 25, 25, fill=color)
        self.canvas_height = self.canvas.winfo_height()
        self.canvas_width = self.canvas.winfo_width()
        self.init_x = self.canvas_width / 2 - 7.5
        self.init_y = self.canvas_height / 2 - 7.5
        self.speed = 0
        self.x = 0
        self.y = 0
    def start(self, evt):
        if self.speed != 0:
            return
        self.canvas.moveto(self.id, self.init_x, self.init_y)
        self.speed = 3
        angle = math.radians(random.choice(list(range(20, 65, 5))))
        direction = random.choice([1, -1])
        self.x = math.cos(angle) * self.speed * direction
        self.y = math.sin(angle) * self.speed
    def draw(self):
        self.canvas.move(self.id, self.x, self.y)
        pos = self.canvas.coords(self.id)
        if pos[0] <= 0:
            self.fix(pos[0] - 0, 0)
        if pos[1] <= 0:
            self.fix(0, pos[1])
        if pos[2] >= self.canvas_width:
            self.fix(pos[2] - self.canvas_width, 0)
        if pos[3] >= self.canvas_height:
            self.fix(0, pos[3] - self.canvas_height)
            self.failed()
        paddle_pos = self.canvas.coords(self.paddle.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2]\
           and paddle_pos[1] <= pos[3] <= paddle_pos[3]:
            self.fix(0, pos[3] - paddle_pos[1])
    def Break(self):
        bblock_pos = self.canvas.coords(self.block.id)
        if pos[2] >= paddle_pos[0] and pos[0] <= paddle_pos[2] \
           and paddle_pos[1] <= pos[3] <= paddle_pos[3]:
            self.fix(0, pos[3] - paddle_pos[1])
    def fix(self, diff_x, diff_y):
        self.canvas.move(self.id, -(diff_x * 2), -(diff_y * 2))
        if diff_x != 0:
            self.x = -self.x
        if diff_y != 0:
            self.y = -self.y
    def delete(self, target):
        figure = self.figs.pop(self.x, self.y)
        self.canvas.delete(figure)
    def collision(self):
        for ball in self.Block:
            collided_block = None
            max_area = 0  
            for block in self.Block:
                collision_rect = ball.getCollisionCoords(block)
                if collision_rect is not None:
                    x1, y1, x2, y2 = collision_rect
                    area = (x2 - x1) * (y2 - y1)
                    if area > max_area:
                        max_area = area
                        collided_block = block
            if collided_block is not None:
                ball.reflect(collided_block)
                self.delete(collided_block)
            for another_ball in self.Ball:
                if another_ball is ball:
                    continue
                if ball.getCollisionCoords(another_ball) is not None:
                    ball.reflect(another_ball)
            if ball.getCollisionCoords(self.paddle) is not None:
                ball.reflect(self.paddle)
    def failed(self):
        self.x = 0
        self.y = 0
        self.speed = 0
