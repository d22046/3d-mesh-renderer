import pygame
import math
pygame.init()

#colors:
black = [0,0,0]
green = [120, 255, 0]
red = [255, 0, 0]
blue = [0,0, 255]
yellow = [255, 255, 0]

screen_width = 1000
screen_height = 600
dis = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("3D")
clock = pygame.time.Clock()

scaler = 400    #determines how big you want the objects to look
middle_x = screen_width/2
middle_y = screen_height/2

pi = 3.141592653589793
def radian(number):
    return number / (360 / (2 * pi))

x_rotation = radian(0.8)
y_rotation = radian(0.8)

#clockwise (p) and counter_clockwise (n)
pSin_x = math.sin(x_rotation)
nSin_x = math.sin(2 * pi - x_rotation)
pCos_x = math.cos(x_rotation)
nCos_x = math.cos(2 * pi - x_rotation)

pSin_y = math.sin(y_rotation)
nSin_y = math.sin(2 * math.pi - y_rotation)
pCos_y = math.cos(y_rotation)
nCos_y = math.cos(2 * math.pi - y_rotation)

class Vertex():
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.flat_x = 0
        self.flat_y = 0
