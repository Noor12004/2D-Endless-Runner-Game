import pygame, random

class Bridge():
    def __init__(self,game,lane,y): #lane not x
        self.game = game
        self.image = pygame.image.load("images/br1.png").convert_alpha()
        self.rect = self.image.get_rect()
        if lane == 1:
            self.rect.x = 480 # x-positions where the bridge obstacle can be placed
        elif lane == 2:
            self.rect.x = 580
        else:
            self.rect.x = 680 
        self.rect.y = y
        self.checkPlacement()
        
    def checkPlacement(self):

        for obstacle in self.game.gems + self.game.spikes + self.game.bridges:
            if self.rect.colliderect(obstacle.rect):
                self.relocate()
                print("Bridge relocation - collision")
                return
            if self.rect.x == 580 and ((obstacle.rect.x == 480 or obstacle.rect.x == 680) and self.rect.y == obstacle.rect.y):
                self.relocate()
                print("Bridge relocation - other obstacle too close")
                return
        

    def relocate(self):
        lane = random.randint(1,3)
        y = random.randrange(self.game.distance, 0, self.game.space)
        if lane == 1:
            self.rect.x = 480
        elif lane == 2:
            self.rect.x = 580
        else:
            self.rect.x = 680 
        self.rect.y = y
        self.checkPlacement()
    def draw(self):
        self.game.screen.blit(self.image,self.rect)

    def move(self):
        self.rect.y += self.game.scrollSpeed 


    def update(self):
        self.draw()
        self.move()

class Spike():
    def __init__(self,game,lane,y):
        self.game = game
        self.image = pygame.image.load("images/sp1.png").convert_alpha()
        self.rect = self.image.get_rect()
        if lane == 1:
            self.rect.x = 480
        elif lane == 2:
            self.rect.x = 580
        else:
            self.rect.x = 680 

        self.rect.y = y
        self.checkPlacement()

    def checkPlacement(self):
        
        for obstacle in self.game.gems + self.game.spikes + self.game.bridges:
            if self.rect.colliderect(obstacle.rect):
                self.relocate()
                print("Spike relocation - collision")
                return
            if self.rect.x == 580 and ((obstacle.rect.x == 480 or obstacle.rect.x == 680) and self.rect.y == obstacle.rect.y):
                self.relocate()
                print("Spike relocation - other obstacle too close")
                return
            
    def relocate(self):
        lane = random.randint(1,3)
        y = random.randrange(self.game.distance, 0, self.game.space)
        if lane == 1:
            self.rect.x = 480
        elif lane == 2:
            self.rect.x = 580
        else:
            self.rect.x = 680 
        self.rect.y = y
        self.checkPlacement()

    def draw(self):
        self.game.screen.blit(self.image,self.rect)

    def move(self):
        self.rect.y += self.game.scrollSpeed

    def update(self):
        self.draw()
        self.move()


class Gem(pygame.sprite.Sprite):
    def __init__(self,game,lane,y):
        self.game = game
        self.image = pygame.image.load("images/gem1.png").convert_alpha()
        self.rect = self.image.get_rect()
        if lane == 1:
            self.rect.x = 480
        elif lane == 2:
            self.rect.x = 580
        else:
            self.rect.x = 680 
        self.rect.y = y
        self.checkPlacement()

    def checkPlacement(self):
            
        for obstacle in self.game.gems + self.game.spikes + self.game.bridges:
            if self.rect.colliderect(obstacle.rect):
                self.relocate()
                print("Gem relocation - collision")
                return
            if self.rect.x == 580 and ((obstacle.rect.x == 480 or obstacle.rect.x == 680) and self.rect.y == obstacle.rect.y):
                self.relocate()
                print("Gem relocation - other obstacle too close")
                return

    def relocate(self):
        lane = random.randint(1,3)
        y = random.randrange(self.game.distance, 0, self.game.space)
        if lane == 1:
            self.rect.x = 480
        elif lane == 2:
            self.rect.x = 580
        else:
            self.rect.x = 680 
        self.rect.y = y
        self.checkPlacement()
        
            
       
    def draw(self):
        self.game.screen.blit(self.image,self.rect)

    def move(self):
        self.rect.y += self.game.scrollSpeed

    def update(self):
        self.draw()
        self.move()


class Health():
    def __init__(self,game,x,y):
        self.game = game
        self.image = pygame.image.load("images/h1.png").convert_alpha()
        self.image2 = pygame.image.load("images/h1.png").convert_alpha()
        self.image3 = pygame.image.load("images/h1.png").convert_alpha()
        
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y

        self.rect2 = self.image2.get_rect()
        self.rect2.x = x + 50
        self.rect2.y = y

        self.rect3 = self.image3.get_rect()
        self.rect3.x = x + 100
        self.rect3.y = y
        
    def draw(self):
        if self.game.health >= 1:
            self.game.screen.blit(self.image,self.rect)
        if self.game.health >= 2:
            self.game.screen.blit(self.image2,self.rect2)
        if self.game.health >= 3:
            self.game.screen.blit(self.image3,self.rect3)

    def update(self):
        self.draw()
