from graphics import *
from time import sleep

class Bullet:
    """Attributes of Bullet class are as follows:
        INSTANCE VARIABLES:
        self.x: x-coordinator of bullet
        self.y: y-coordinator of bullet
        self.bullet: bullet image"""
    def __init__(self,win,x,y,img):
        """draws bullet on graphical window"""
        self.win = win
        self.bullet = Image(Point(x,y),img)
        self.bullet.draw(win)
        self.yPos = y
        self.xPos = x

    def getY(self):
        """gets y-coordinator of bullet"""
        return self.yPos

    def getX(self):
        """gets x-coordinator of bullet"""
        return self.xPos

    def move(self, increment):
        """moves bullet upward"""
        self.bullet.move(0 , -increment)
        self.yPos -= increment

    def remove(self):
        """undraws bullet"""
        self.bullet.undraw()

            
def main():
    win = GraphWin("test", 400, 400)
    bullet = Bullet(win, 100, 300)
        
if __name__ == "__main__":
    main()


 
