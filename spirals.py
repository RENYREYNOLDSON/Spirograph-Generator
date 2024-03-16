import pygame,sys,random,math
from pygame.locals import*
pygame.init()
screen=pygame.display.set_mode((1600,900))
clock=pygame.time.Clock()

bgColour=(255,255,255)
colour=(0,0,0)
numberDots=500
addAngle=5
thickness=4
increase=0
size=400
speed=60


class Dot:
    def __init__(self,x,y):
        self.x=x
        self.y=y
        self.dist=y-450
        self.angle=0
    def draw(self,number):
        if number>0:
            pygame.draw.line(screen,colour,(self.x,self.y),(dots[number-1].x,dots[number-1].y),thickness)
    def move(self):
        self.angle+=self.dist/addAngle
        self.x=800+math.cos(math.radians(self.angle))*self.dist
        self.y=450+math.sin(math.radians(self.angle))*self.dist
        self.dist+=increase
dots=[]    
for i in range(numberDots):
    dots.append(Dot(450,450+i*size/numberDots))
def drawDots():
    number=0
    for point in dots:
        point.draw(number)
        point.move()
        number+=1
while True:

    screen.fill(bgColour)

    drawDots()
    for event in pygame.event.get():
        if event.type==QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(speed)
