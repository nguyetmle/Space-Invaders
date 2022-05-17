from graphics import *
from random import *
import math
from time import sleep
from bullet import Bullet

class Invaders:
    """Attributes of Invaders class are as follows:
        INSTANCE VARIABLES:
        self.xPos: starting x-coordinator of invader
        self.yPos: starting y-coordinator of invader
        self.col: number of columns of invaders
        self.row: number of rows of invaders
        self.total: a list of invaders"""
    def __init__(self,win,xPos, yPos):
        """creates a list of invaders of different colors"""
        self.win = win
        self.xPos = xPos
        self.yPos = yPos
        self.total = []
        imagelist = []
        i = 0 
        for i in range(10):
            image = "img/invader"+str(i)+".png"
            imagelist.append(image)
            i = i + 1
        self.imagelist = imagelist
        self.gameOver = False

    def create(self,col,row,imageindex):
        """draws a matrix of invaders"""
        self.col = col
        self.row = row
        image = self.imagelist[imageindex]
        initY = self.yPos
        for i in range(self.row):
            initX = self.xPos
            for j in range(self.col):
                invader = Image(Point(initX, initY),image)
                invader.draw(self.win)
                self.total.append(invader) 
                initX += 40
            initY -= 40
            
    def move(self,speed):
        """moves invaders downward"""
        for invader in self.total:
            invader.move(0,speed) #inputs speed

    def isCollision(self,pt1,pt2):   
        x1 = pt1.getX()
        x2 = pt2.getX()
        y1 = pt1.getY()
        y2 = pt2.getY()
        distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
        if distance <= 15:
            return True
        else:
            return False

    def isKilled(self,bulletPos):
        """checks for collision between invader and bullet
            if True, undraws invader"""
        for invader in self.total:
            x = invader.getAnchor().getX()
            y = invader.getAnchor().getY()
            invaderPos = Point(x,y)
            if self.isCollision(bulletPos,invaderPos):
                invader.undraw()
                self.total.remove(invader)
                return True

    def attack(self,pt):
        """checks if invader hits screen bottom
            checks if invader hits player
            if yes, turns gameOver boolean to True"""
        playerPos = pt
        for invader in self.total:
            invader_x = invader.getAnchor().getX()
            invader_y = invader.getAnchor().getY()
            invaderPos = Point(invader_x,invader_y)
            if invader_y >= 580:  #screen 1000x600
                self.gameOver = True
            elif self.isCollision(playerPos,invaderPos):
                self.gameOver = True
        

def main():
    win = GraphWin("test invaders",1000,600)
    invaders = Invaders(win,200,200)
    invaders.create(15,9,9)
    while True:
        invaders.move(4)
##        invaders.isKilled(Point(250,100))
##
    

if __name__ == "__main__":
    main()
