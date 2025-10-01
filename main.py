import pygame, random, sys
import tkinter as tk
from tkinter import messagebox
from character import *
from objects import *
from buttons import *

pygame.init()
clock = pygame.time.Clock()
pygame.display.set_caption("Endless Runner")

class Game():
    def __init__(self):
        self.menuBg = pygame.image.load("images/main menu 3.jpg")
        self.pauseBg = pygame.image.load("images/pause menu4.jpg")
        self.gameoverBg = pygame.image.load("images/Game over.jpg")


        self.health = 3
        self.scroll = 0
        self.SCREEN_SIZE = 1280,720
        self.screen = pygame.display.set_mode(self.SCREEN_SIZE)
        self.bg = pygame.image.load("images/bg3.jpg").convert()
        self.bg2 = pygame.image.load("images/bg3.jpg").convert()
        self.turnImage = pygame.image.load("images/turn.jpg").convert()

        self.turnRect = self.turnImage.get_rect()
        self.turnRect.bottom = 0
        self.difficulty = 3
        self.scrollSpeed = self.difficulty * 4

        self.playing = False
        self.paused = False
        self.menuButtons = [Button(self,400,530,"Start3"),
                            Button(self,200,430,"Easy"),
                            Button(self,500,430,"Medium"),
                            Button(self,800,430,"Hard")]

        self.gameplayButtons = [Button(self,20,20,"Pause")]

        self.pauseButtons = [Button(self,20,20,"Pause"),
                             Button(self,500,300,"Resume"),
                             Button(self,500,400,"StartAgain"),
                             Button(self,500,500,"MainMenu")]
        
        self.gameoverButtons = [Button(self,500,500,"StartAgain"),
                                Button(self,500,600,"MainMenu")]
        

        self.buttons = self.menuButtons

        for button in self.buttons:
            if button.text == "Medium":
                button.selected = True

        self.spikes = []
        self.bridges = []
        self.gems = []

        self.distance = -4000
        self.space = 250 #50 + (self.difficulty*20)

        self.font = pygame.font.SysFont("Verdana",30,True)
        self.fontcolour = (255,255,255)
        self.level = 0
        self.score = 0
        self.progress = 0 # how much distance we have covered
        self.turnTime = False

    def startTurn(self):
        if self.progress <= self.distance: 
            self.turnRect.y += self.scrollSpeed ## when the above condition is hit, turn is brought down on the screen by the scroll speed
            self.screen.blit(self.turnImage,self.turnRect)
            self.turnTime = True
        else:
            self.turnTime = False

    def checkMissedTurn(self):
        if self.turnTime:
            if self.turnRect.bottom >= 900:
                self.updateLeaderboard()
                self.drawGameOver()
                self.playing = False
                self.paused = False
                self.buttons = self.gameoverButtons
     

    def checkHealth(self):
        if self.health == 0:
            self.updateLeaderboard()
            self.drawGameOver()
            self.playing = False
            self.paused = False
            self.buttons = self.gameoverButtons

    def updateScore(self):
        if self.score < 0:
            self.score = 0
        
        self.scoreText = "SCORE:"+str(self.score)
        self.scoreFont = self.font.render(self.scoreText,True,self.fontcolour) 
        self.scoreRect = self.scoreFont.get_rect()
        self.scoreRect.x = 1090
        self.scoreRect.y = 80

        self.screen.blit(self.scoreFont,self.scoreRect)

    def updateLeaderboard(self):
        file = open("leaderboard.txt","r")
        data = file.read()
        leaderboard = []
        for line in data.split("\n"):
            line = line.split(",")
            if len(line)==2:
                leaderboard.append([line[0],int(line[1])])
        
        file = open("leaderboard.txt","w")
        newName = False
        for player in leaderboard:
            if player[0] == name:
                newName = True
                if player[1] > self.score:
                    file.write(player[0]+","+str(player[1])+"\n")
                else:
                    file.write(player[0]+","+str(self.score)+"\n")
            else:
                file.write(player[0]+","+str(player[1])+"\n")
        if newName == False:
            file.write(name+","+str(self.score)+"\n")
        
        file.close() 

    def resetGame(self):
        self.health = 3
        self.scroll = 0
        self.level = 0
        self.score = 0
        self.progress = 0
        self.turnRect.bottom = 0
        self.turnTime = False

    def generateObjects(self):
        self.spikes = []
        self.bridges = []
        self.gems = []
        self.scrollSpeed = self.difficulty * 4
        for i in range(self.difficulty+1):
            self.spikes.append(Spike(game,random.randint(1,3),random.randrange(self.distance, 0,self.space)))
        for i in range(self.difficulty+1):
            self.bridges.append(Bridge(game,random.randint(1,3),random.randrange(self.distance, 0,self.space)))
        for i in range(self.difficulty+3):
            self.gems.append(Gem(game,random.randint(1,3),random.randrange(self.distance, 0,self.space)))
            

    def draw(self):
        if self.playing:
            self.screen.blit(self.bg,(0,self.scroll))
            self.screen.blit(self.bg2,(0,-720+self.scroll))
            if self.paused == False:

                self.scroll += self.scrollSpeed
                if self.scroll >= 720:
                    self.scroll = 0
            else:
                self.drawPauseMenu()
        else: #menu
            self.drawMenu()

        if self.health == 0:
            self.drawGameOver()

        if self.turnTime:
            if self.turnRect.bottom >= 900:
                self.drawGameOver()
        

        for button in self.buttons:
            button.draw(self.screen)

    def drawMenu(self):
        #self.screen.fill((255,255,0))
        self.screen.blit(self.menuBg,(0,0))

    def drawPauseMenu(self):
        self.screen.blit(self.pauseBg,(0,0))

    def drawGameOver(self):
        self.screen.blit(self.gameoverBg,(0,0))
        
        self.currentScore = self.font.render(str(self.score),True,self.fontcolour)
        self.currentRect = self.currentScore.get_rect()
        self.currentRect.x = 510
        self.currentRect.y = 280

        self.screen.blit(self.currentScore,self.currentRect)

        file = open("leaderboard.txt","r")
        data = file.read()
        leaderboard = []
        newName = False
        for line in data.split("\n"):
            line = line.split(",")
            if line[0] == name:
                newName = True
                if int(line[1]) > self.score:
                    highScore = line[1]
                else:
                    highScore = self.score
        if newName == False:
            highScore = self.score
                    
        
        self.highScore = self.font.render(str(highScore),True,self.fontcolour)
        self.highRect = self.highScore.get_rect()
        self.highRect.x = 620
        self.highRect.y = 335

        self.screen.blit(self.highScore,self.highRect)        


        
        
            
    def update(self):
        self.draw()
        if self.playing and self.paused == False:
            self.progress -= self.scrollSpeed #tracks your progress as you go down the track
            self.checkMissedTurn()
            
            self.startTurn() #updates the function where the turn is supposed to start a turn
            self.updateScore()
            self.checkHealth()


def getName():
    game.name = e1.get()
    if len(game.name) >= 4 and len(game.name) <=20:
        print(game.name)
        master.destroy()
    else:
        tk.messagebox.showerror("showerror", "ERROR - Name must be between 4 and 20 characters.") 
    
        
#------------------


##while len(name) < 4 or len(name) > 20:
##    name = input("Name must be between 4-20 characters: ")

game = Game() #---instantiation


#------Name entry window -------
master = tk.Tk()
tk.Label(master, text="Enter your Name").grid(row=0)

e1 = tk.Entry(master)

e1.grid(row=0, column=1)

tk.Button(master,text="Start Game",command = getName).grid(row=1,column=0)

master.mainloop()

#-------------------------------

name = game.name

player = Character(game,500,600)

health = Health (game,1120,20)

while True: #---game loop
    
    for event in pygame.event.get(): #---event listener
        if event.type == pygame.QUIT:
            sys.exit()
            quit()
        if event.type == pygame.MOUSEBUTTONUP:            
            for button in game.buttons:
                if button.rect.collidepoint(event.pos):
                    button.click()
                 
    keys = pygame.key.get_pressed()
    game.update()
    if game.playing and game.paused == False:
        for bridge in game.bridges:
            bridge.update()
        player.update(keys)
        for spike in game.spikes:
            spike.update()
        for gem in game.gems:
            gem.update()
            
        health.update()
    clock.tick(60)
    pygame.display.flip() #---prepares and draws the frame
