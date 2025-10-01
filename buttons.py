import pygame
###import button
##
### Create a surface for the button
##SCREEN_HEIGHT = 500
##SCREEN_WIDTH = 800
##
##screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
##pygame.display.set_caption("Button start")



class Button():
    def __init__(self,game,x,y,text):
        self.game = game
        self.text = text
        self.image = pygame.image.load("images/button"+text+".png").convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.topleft = (x,y)
        if self.text in ["Easy","Medium","Hard"]:
            self.selected = False

    def draw(self,screen):
        if self.text in ["Easy","Medium","Hard"]:
            if self.selected:
                self.image = pygame.image.load("images/button"+self.text+"2.png").convert_alpha()
                screen.blit(self.image, (self.rect.x, self.rect.y))
            else:
                self.image = pygame.image.load("images/button"+self.text+".png").convert_alpha()
                screen.blit(self.image, (self.rect.x, self.rect.y))
        else:
            self.image = pygame.image.load("images/button"+self.text+".png").convert_alpha()
            screen.blit(self.image, (self.rect.x, self.rect.y))

    def click(self):
        if self.text == "Easy":
            self.game.difficulty = 2
            for button in self.game.buttons:
                if button.text in ["Medium","Hard"]:
                    button.selected = False
            self.selected = True           
                    

        elif self.text == "Medium":
            self.game.difficulty = 3
            for button in self.game.buttons:
                if button.text in ["Easy","Hard"]:
                    button.selected = False
            self.selected = True    
        elif self.text == "Hard":
            self.game.difficulty = 4
            for button in self.game.buttons:
                if button.text in ["Easy","Medium"]:
                    button.selected = False
            self.selected = True    

        elif self.text == "Start3": 
            self.game.playing = True
            self.game.buttons = self.game.gameplayButtons
            self.game.resetGame()
            self.game.generateObjects()

        elif self.text == "Pause":
            if self.game.paused == False:
                self.game.paused = True
                self.game.buttons = self.game.pauseButtons
            else:
                self.game.paused = False
                self.game.buttons = self.game.gameplayButtons

        elif self.text == "Resume":
            self.game.paused = False
            self.game.buttons = self.game.gameplayButtons

        elif self.text == "StartAgain":
            self.game.playing = True
            self.game.buttons = self.game.gameplayButtons
            self.game.resetGame()
            self.game.generateObjects()
            self.game.paused = False

        elif self.text == "MainMenu":
            self.game.playing = False
            self.game.paused = False
            self.game.buttons = self.game.menuButtons
            self.game.resetGame()
            self.game.generateObjects()


        
            
                
        
            











##startButton = Button(100,100,"Start")
##startButton = Button(100,100,"Exit")       
##
##run = True
##while run:
##
##    for event in pygame.event.get():
##        if event.type == pygame.QUIT:
##            run = False
##
##    screen.fill((255,255,255))
##    
##    startButton.draw(screen)
##
##    pygame.display.update()
##
##pygame.quit()





