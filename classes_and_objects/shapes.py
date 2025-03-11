import pygame
from colors import *

# AMONG US MAKER
def draw_amongus(window, color, x, y, scale=1, flip= False):

        if flip:
            amogus_body = Ellipse(window,color, x * scale, y * scale,300 *scale,400 * scale)
            amogus_legs1 = Rectangle(window, color, (x+ 50)* scale, (y+ 300)* scale,50* scale,150* scale)
            amogus_legs2 = Rectangle(window, color, (x+ 200)* scale, (y + 300)* scale,50* scale,150* scale)
            amogus_backpack = Rectangle(window, color, (x + 275)* scale, (y + 50)* scale,75* scale,300* scale)
            glass = Ellipse(window, CC_BLUE, (x-50)* scale, (y+50)* scale ,300* scale,50* scale)
        else:
            amogus_body = Ellipse(window,color, x* scale , y* scale,300* scale,400* scale)
            amogus_legs1 = Rectangle(window, color, (x+ 50)* scale, (y+ 300)* scale,50* scale,150* scale)
            amogus_legs2 = Rectangle(window, color, (x+ 200)* scale, (y + 300)* scale,50* scale,150* scale)
            amogus_backpack = Rectangle(window, color, (x - 50)* scale, (y + 50)* scale,75* scale,300* scale)
            glass = Ellipse(window, CC_BLUE, (x+50)* scale, (y+50)* scale ,300* scale,50* scale)

        amongus = [amogus_body,amogus_backpack,amogus_legs1,amogus_legs2,glass]

        return amongus

# SHAPE CLASSES

class Shape():

    def __init__(self, window, color, width=0):
        self.window = window
        self.color = color
        self.width = width

    def change_color(self, new_color):
        if not new_color is tuple:
            raise ValueError("Needs a tuple with 3 int values (0-255, 0-255, 0-255)")
        
        self.color = new_color

    def change_width(self, new_width):
        self.width = new_width

class Line(Shape):

    def __init__(self,window, color, start_coord, end_coord, width):
        super().__init__(window, color, width)
        self.color = color
        self.start = start_coord
        self.end = end_coord
        self.width = width

    def draw(self):
        pygame.draw.line(self.window,self.color, self.start, self.end, self.width)

class Rectangle(Shape):

    def __init__(self, window, color, x, y ,side_width=1, side_length=1, line_width=0):
        super().__init__(window,color, line_width)
        self.rect = pygame.Rect(x,y,side_width,side_length)

    def draw(self):
        pygame.draw.rect(self.window, self.color, self.rect, self.width)

class Square(Rectangle):

    def __init__(self, window, color, x, y, side_length = 1, line_width = 0):
        super().__init__(window, color, x, y, side_length, side_length, line_width)

class Circ(Shape):
    
    def __init__(self, window, color, center_coords, radius, width=0):
        super().__init__(window,color, width)
        self.center = center_coords
        self.r = radius


    def draw(self):
        pygame.draw.circle(self.window, self.color, self.center, self.r, self.width)

class Ellipse(Rectangle):

    def __init__(self, window, color, x, y, side_width=1, side_length=1, line_width = 0):
        super().__init__(window, color, x, y, side_width, side_length, line_width)

    def draw(self):
        pygame.draw.ellipse(self.window, self.color, self.rect, self.width)

class Polygon(Shape):

    def __init__(self,window, color, points, width=0):
        super().__init__(window,color,width)
        self.points = points


    def draw(self):
        pygame.draw.polygon(self.window,self.color,self.points,self.width)