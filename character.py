import pygame

class Character():
    def __init__(self,game,x,y):
        self.game = game
        self.image = pygame.image.load("images/Player1.png").convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = 10

        self.jumpImage = pygame.image.load("images/Player2.png").convert_alpha()
        self.jumpScale = 1
        #self.jumpImage = pygame.transform.scale(self.jumpImage,(self.rect.width*2,self.rect.height*2))

        self.runCycle = [pygame.image.load("images/Player2.png").convert_alpha(),
                         pygame.image.load("images/Player3.png").convert_alpha(),
                         pygame.image.load("images/Player4.png").convert_alpha(),
                         pygame.image.load("images/Player5.png").convert_alpha()]#images to animate running
        self.runFrame = 0 # running image
        self.animCounter = 0 
        self.imgCount = 1 #cycle of images-repetition
        self.jumping = False
        self.jumpCounter = 0 #skipping frames

        
    def move(self,keys):
        if keys[pygame.K_LEFT] and self.rect.x >= 500 : # "LEFT" key pressed
            self.rect.move_ip(-9,0)
        if keys[pygame.K_RIGHT] and self.rect.x <= 710: # "RIGHT" key pressed
            self.rect.move_ip(9,0)
        if keys[pygame.K_UP]:
            self.jumping = True
        if keys[pygame.K_SPACE] and self.game.turnTime:
            self.game.progress = 0
            self.game.generateObjects()
            self.game.turnRect.bottom = 0
            self.game.turnTime = False
            
            
        
    def animate(self):
        self.animCounter += 1
        if self.animCounter == 3: #speed of changing frame
            self.runFrame += self.imgCount
            self.animCounter = 0
            if self.runFrame == 3 or self.runFrame == 0:
                self.imgCount =-self.imgCount # imagecount cycle started again from negative
                 

    def collide(self):
        for gem in self.game.gems:
            if self.rect.colliderect(gem.rect):
                self.game.gems.remove(gem)
                self.game.score += 10

        for spike in self.game.spikes:
            if self.rect.colliderect(spike.rect):
                self.game.spikes.remove(spike)
                self.game.score -= 5
                self.game.health -= 1

        for bridge in self.game.bridges:
            if self.jumping == False:
                if self.rect.colliderect(bridge.rect):
                    self.game.bridges.remove(bridge)
                    self.game.health -= 1

    
    def draw(self):
        if self.jumping == True:
            if self.jumpCounter < 15:
                self.jumpScale += 0.025
            else:
                self.jumpScale -= 0.025
            self.image = pygame.transform.scale(self.jumpImage,(self.rect.width*self.jumpScale,self.rect.height*self.jumpScale))
            
            self.jumpCounter += 1
            if self.jumpCounter == 30: #this means it wil skip the frames for 0.5 sec; not animating
                self.jumpCounter = 0
                self.jumpScale = 1
                self.jumping = False #stops jumping after 0.5 sec
        else:
            self.image = self.runCycle[self.runFrame]
        self.game.screen.blit(self.image,self.rect)

    def update(self,keys):
        #self.image = pygame.transform.scaleimage(10,56)
        self.collide()
        self.animate()
        self.draw()
        self.move(keys)
