from time import sleep
import math
from random import randrange
from graphics import *

class Coin:
    """Attributes of Coin class are as follows:
        INSTANCE VARIABLES:
        self.total: a list of coins created"""
    def __init__(self,win):
        self.win = win
        self.ptList = []
        self.total = []

    def create(self,num):
        """draws coins on graphical window
            appends each coin drawn to a list of coins"""
        self.num = num
        for i in range(self.num):
            x = randrange(100,900,40)
            y = randrange(200,600,40)
            pt = Point(x,y)

            while pt in self.ptList:
                x = randrange(100,900,40)
                y = randrange(250,600,40)
                pt = Point(x,y)

            self.ptList.append(pt)
            coin = Image(pt,"img/coin.png")
            coin.draw(self.win)
            self.total.append(coin)

    def isCollision(self,pt1,pt2):
        """checks for collision between 2 objects"""
        x1 = pt1.getX()
        x2 = pt2.getX()
        y1 = pt1.getY()
        y2 = pt2.getY()
        distance = math.sqrt((math.pow(x1 - x2, 2)) + (math.pow(y1 - y2, 2)))
        if distance <= 10:
            return True
        else:
            return False

    def collect(self,playerPos):
        """checks for collision between player and coin
            if true, undraws coin and removes from coin list"""
        for coin in self.total:
            coin_x = coin.getAnchor().getX()
            coin_y = coin.getAnchor().getY()
            coinPos = Point(coin_x,coin_y)
            if self.isCollision(playerPos,coinPos):
                coin.undraw()
                self.total.remove(coin)
                return True

    
            
            
            
