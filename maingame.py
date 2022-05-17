#Michelle Le, Samuel Crockford
#COM 110
#Final Project
#This program allows user to play Space Invaders game (with a twist!)

import pygame
from pygame import mixer
from time import sleep
from graphics import *
from random import randrange

from buttonClass import Button
from invader import Invaders
from player import Player
from bullet import Bullet
from coin import Coin

def byValue(pair):  #helper function to sort the tuples
    return pair[1]

def updateScore(name,score):  #helper function to update score
    file = open("leaderboard.txt","r")
    data = file.readlines()
    file.close()

    infile = open("leaderboard.txt","w")
    global scoreList
    scoreList = []
    scoreList.append((name,int(score)))
    
    for line in data:
        pName, pScore = line.split() 
        scoreList.append((pName,int(pScore)))#add name and score to a list of tuples

    scoreList.sort(key = byValue,reverse = True)#sort the list based on scores
    
    for i in range(len(scoreList)):
        infile.write(scoreList[i][0]+" " +str(scoreList[i][1])+"\n")#rewrites the sorted tuple to the file
    
    infile.close()
    
def intro():  #intro window
    #background
    win = GraphWin("Welcome to Space Invader",1000,600)
    bg = Image(Point(500,300),"img/introbackground.gif")
    bg.draw(win)

    #title
    title = Text(Point(500,150),"SPACE INVADER")
    title.setSize(50)
    title.setFace("arial")
    title.setTextColor("yellow")
    title.setStyle("bold")
    title.draw(win)

    #button
    playButton = Button(win,Point(300,500),100,50,"Play")
    ruleButton = Button(win,Point(500,500),100,50,"Rule")
    quitButton = Button(win,Point(700,500),100,50,"Quit")

    return win,playButton,ruleButton,quitButton

def leaderboard(): #window to show highscores
    #background
    win = GraphWin("Leaderboard",600,600)
    win.setBackground("black")

    #title
    title = Text(Point(300,100), "LEADERBOARD")
    title.setSize(30)
    title.setFace("arial")
    title.setTextColor("yellow")
    title.setStyle("bold")
    title.draw(win)

    #heading
    nameCol = Text(Point(200,200),"Player")
    nameCol.setSize(18)
    nameCol.setFace("arial")
    nameCol.setTextColor("lemon chiffon")
    nameCol.setStyle("bold")
    nameCol.draw(win)
    
    scoreCol = Text(Point(400,200),"Score")
    scoreCol.setSize(18)
    scoreCol.setFace("arial")
    scoreCol.setTextColor("lemon chiffon")
    scoreCol.setStyle("bold")
    scoreCol.draw(win)

    #display scores and names
    space = 0
    for topScores in scoreList[:10]:
        name, score = topScores[0], topScores[1]
        
        showName = Text(Point(200,250 + space), name) 
        showName.setSize(12)
        showName.setFace('arial')
        showName.setFill('white smoke')
        showName.draw(win)
        
        showScore = Text(Point(400,250 + space), str(score))
        showScore.setSize(12)
        showScore.setFace('arial')
        showScore.setFill('white smoke')
        showScore.draw(win)

        space += 30
    
def rule():  #window to show rules
    #background
    win = GraphWin("Rule",600,600)
    bg = Image(Point(300,300),"img/rulebackground.gif")
    bg.draw(win)

    #title
    title = Text(Point(300,50),"MISSION")
    title.setSize(20)
    title.setStyle("bold")
    title.setFace('courier')
    title.setFill('yellow')
    title.draw(win)
    
    #rule
    rule = Text(Point(300,120),"Kill all invaders and collect coins\
\nAfter each round, new invader is unlocked \nand the number of invaders increases")
    rule.setSize(12)
    rule.setStyle("bold italic")
    rule.setFace('courier')
    rule.setFill('yellow')
    rule.draw(win)

    #spacebar
    Image(Point(100,250),"img/spacebar.png").draw(win)
    spacebar = Text(Point(200,250),"Shoot")
    spacebar.setSize(12)
    spacebar.setStyle("bold")
    spacebar.setFace('courier')
    spacebar.setFill('yellow')
    spacebar.draw(win)

    #arrow
    Image(Point(350,250),"img/arrow.png").draw(win)
    move = Text(Point(450,250),"Move")
    move.setSize(12)
    move.setStyle("bold")
    move.setFace('courier')
    move.setFill('yellow')
    move.draw(win)

    #invader point
    Image(Point(100,350),"img/invader3.png").draw(win)
    invaderPts = Text(Point(200,350),"+10pts")
    invaderPts.setSize(12)
    invaderPts.setStyle("bold")
    invaderPts.setFace('courier')
    invaderPts.setFill('yellow')
    invaderPts.draw(win)

    #coin point
    Image(Point(350,350),"img/coin.png").draw(win)
    coinPts = Text(Point(450,350),"+20pts")
    coinPts.setSize(12)
    coinPts.setStyle("bold")
    coinPts.setFace('courier')
    coinPts.setFill('yellow')
    coinPts.draw(win)  


def game():  #window to play game
    #background
    win = GraphWin("Space Invader",1000,600)
    bg = Image(Point(500,300),"img/gamebackground.gif")
    bg.draw(win)

    #music start
    pygame.init()
    mixer.init()
    music = pygame.mixer.music.load("music.wav")
    pygame.mixer.music.play(-1)
    boom = pygame.mixer.Sound("explosion.wav")
    begin = pygame.mixer.Sound("begin.wav")
    end = pygame.mixer.Sound("end.wav")
    coinsound = pygame.mixer.Sound("coin.wav")

    #input user's name
    namePrompt = Text(Point(350,300),"Enter your name: ")
    namePrompt.setSize(18)
    namePrompt.setFace("courier")
    namePrompt.setTextColor("white")
    namePrompt.setStyle("bold")
    namePrompt.draw(win)

    userInput = Entry(Point(650,300),30)
    userInput.setText("Anonymous")
    userInput.draw(win)
        
    #click play
    play = Button(win,Point(500,400),100,40,"Play!")
    pt = win.getMouse()
    while not play.isClicked(pt):
        pt = win.getMouse()
    pygame.mixer.Sound.play(begin)
    namePrompt.undraw()
    userInput.undraw()
    play.undraw()

    pName = userInput.getText()
    if pName == "":
        pName = "Anonymous" #set default name to Player if user doesn't type name

    #name holder
    showName = Text(Point(180,50),"Player: " + str(pName))
    showName.setSize(18)
    showName.setFace("arial")
    showName.setTextColor("yellow")
    showName.setStyle("bold")
    showName.draw(win)
    
    #score holder
    score = 0
    showScore = Text(Point(800,50),"Score: " + str(score))
    showScore.setSize(18)
    showScore.setFace("arial")
    showScore.setTextColor("yellow")
    showScore.setStyle("bold")
    showScore.draw(win)

    #round
    roundNum = 1
    showRound = Text(Point(500,300),"ROUND " + str(roundNum))
    showRound.setSize(30)
    showRound.setFace("arial")
    showRound.setTextColor("yellow")
    showRound.setStyle("bold")
    showRound.draw(win)

    sleep(1.5)
    showRound.undraw()

    #create Player object
    player = Player(win,Point(500,550))
    
    #create Invaders object
    speed = 0.5 #starting speed
    row = 3  #starting row
    invaders = Invaders(win,200,100)
    invadimg = 1
    invaders.create(15,row,invadimg) #fix number of columns to 15
    invadersCount = len(invaders.total)

    #create Coin object
    coin = Coin(win)
    coinNum = 7
    coin.create(coinNum)
    coinCount = len(coin.total)

    #start game
    while not invaders.gameOver:
        invaders.move(speed)
        player.moveBullets()

        #if bullet hits invader
        for bullet in player.currentBullets:
            x = bullet.getX()
            y = bullet.getY()
            if invaders.isKilled(Point(x,y)):
                pygame.mixer.Sound.play(boom)
                invadersCount = len(invaders.total)
                bullet.remove()
                player.currentBullets.remove(bullet)
                score = score + 10  #add score for player
                showScore.setText("Score: " + str(score))

        #if player collects coin successfully
        if coin.collect(Point(player.px,player.py)):
            pygame.mixer.Sound.play(coinsound)
            coinCount = len(coin.total)
            score = score + 20  #add score for player
            showScore.setText("Score: " + str(score))
            

        #if number of coins on screen is smaller than half the total coin
        if coinCount <= coinNum//2:
            coin.create(coinNum - coinCount) #create more coins
            coinCount = len(coin.total)
            
        #when player kills all invaders on screen
        if invadersCount == 0: 
            #start new round
            roundNum += 1
            showRound.setText("ROUND " +str(roundNum))
            showRound.draw(win)
            sleep(1.5)
            showRound.undraw()

            #increase the number of row and change icons
            row += 1
            invadimg += 1
            if invadimg > 9:
                invadimg = randrange(1,9)
            invaders.create(15,row,invadimg)  
            invadersCount = len(invaders.total)

            #increase speed
            speed += 0.1
            if speed > 3: #set maximum speed as 3
                speed = 3
            
        invaders.attack(Point(player.px,player.py)) #check gameOver conditions
        sleep(0.02)
        
    #when game is over
    pygame.mixer.Sound.play(end)
    pygame.mixer.music.stop()

    player.player.undraw()
    explosion = Image(Point(player.px,player.py),"img/explosion.png")
    explosion.draw(win)
    sleep(2)
    explosion.undraw()
    gameOver = Image(Point(500,300),"img/game over.png")
    gameOver.draw(win)

    #update score 
    updateScore(pName,score)

    #choice: replay, see board, exit game
    restart = Button(win, Point(300, 450), 100, 40, 'Restart')
    viewBoard = Button(win, Point(500, 450), 100, 40, 'Leaderboard')
    Exit = Button(win, Point(700, 450), 100, 40, 'Exit')

    pt = win.getMouse()
    while not Exit.isClicked(pt):
        if viewBoard.isClicked(pt):
            leaderboard() 
        elif restart.isClicked(pt):
            win.close()
            game()
            break  #break out of while loop when window is closed
        pt = win.getMouse()
    pygame.mixer.music.stop()
    win.close()

def main():
    win,playButton,ruleButton,quitButton = intro() 

    pt = win.getMouse()
    while not quitButton.isClicked(pt): #while quit button is not clicked
        if playButton.isClicked(pt): #if play button is clicked
            win.close()
            game() #play game
            break  #break out of while loop when window is closed
        elif ruleButton.isClicked(pt): #if rule button is clicked
            rule() #show rule           
        pt = win.getMouse()
    win.close()
main()
