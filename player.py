from graphics import *
from time import sleep
from bullet import Bullet
from invader import Invaders

class Player:
    """Attributes of Player class are as follows:
        INSTANCE VARIABLES:
        self.pt: position of player
        self.player: player image
        self.currentBullets: list of bullets that player shoot"""
    def __init__(self,win,pt):
        """create player on graphical window"""
        self.win = win
        self.px = pt.getX()
        self.py = pt.getY()
        self.player = Image(Point(self.px,self.py),"img/spaceship.gif")
        self.player.draw(win)
        self.currentBullets = []

        #key binding
        self.win.bind("<Up>",self.moveUp)
        self.win.bind("<Down>",self.moveDown)
        self.win.bind("<Left>",self.moveLeft)
        self.win.bind("<Right>",self.moveRight)
        self.win.bind("<space>",self.shoot)
        self.win.pack()
        self.win.focus_set()

    def moveUp(self, event):
        """moves player up"""
        if self.py - 20 >= 30:
            self.player.move(0,-20)
            self.py -= 20
            
    def moveDown(self, event):
        """moves player down"""
        if self.py + 20 <= 550:
            self.player.move(0,20)
            self.py += 20

    def moveRight(self, event):
        """moves player to the right"""
        if self.px + 20 <= 980:
            self.player.move(20,0)
            self.px += 20

    def moveLeft(self, event):
        """moves player to the left"""
        if self.px - 20 >= 20:
            self.player.move(-20,0)
            self.px -= 20

    def shoot(self, event):
        """draws bullet from player position
            adds each bullet drawn to the list of bullets"""
        img = "img/bulletUp.png"
        bullet = Bullet(self.win,self.px,self.py - 30,img)
        self.currentBullets.append(bullet)

    def moveBullets(self):
        """moves bullet upward
            if bullet hits upper screen, undraws bullet and removes from bullet list"""
        for bullet in self.currentBullets:
            if bullet.getY() > 0:
                bullet.move(20)
            else:
                bullet.remove()
                self.currentBullets.remove(bullet)

    
    
def main():
    win = GraphWin("test player",1000,600)
    win.setBackground("black")

    player = Player(win,Point(500,550))

    while True:
        player.moveBullets()
        
    win.close()

if __name__ == "__main__":
    main()
    
    
            
            
