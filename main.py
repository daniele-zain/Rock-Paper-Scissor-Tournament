import pygame
import random

pygame.init()

screen = pygame.display.set_mode((800,600))

RockImg = pygame.image.load('png\\rock.png')
PaperImg = pygame.image.load('png\scroll.png')
ScissorImg = pygame.image.load('png\scissors.png')


object_width = 15
object_height = 15

class Rock:
    def __init__(self, RockImg, RockX, RockY, velocityX, velocityY):
        self.RockImg = RockImg
        self.RockX = RockX
        self.RockY = RockY
        self.velocityX = velocityX
        self.velocityY = velocityY
        self.rect = pygame.Rect(self.RockX, self.RockY, object_width, object_height)
    
    def move(self):
        self.RockX += self.velocityX
        self.RockY += self.velocityY
        if self.RockX <= 0 or self.RockX >= 785: 
            self.velocityX = -self.velocityX
        if self.RockY <= 0 or self.RockY >= 585: 
            self.velocityY = -self.velocityY
        self.rect.topleft = (self.RockX, self.RockY)


class Paper:
    def __init__(self, PaperImg, PaperX, PaperY, velocityX, velocityY):
        self.PaperImg = PaperImg
        self.PaperX = PaperX
        self.PaperY = PaperY
        self.velocityX = velocityX
        self.velocityY = velocityY
        self.rect = pygame.Rect(self.PaperX, self.PaperY, object_width, object_height)

    def move(self):
        self.PaperX += self.velocityX
        self.PaperY += self.velocityY
        if self.PaperX <= 0 or self.PaperX >= 785:
            self.velocityX = -self.velocityX
        if self.PaperY <= 0 or self.PaperY >= 585:
            self.velocityY = -self.velocityY
        self.rect.topleft = (self.PaperX, self.PaperY)



class Scissor:
    def __init__(self, ScissorImg, ScissorX, ScissorY, velocityX, velocityY):
        self.ScissorImg = ScissorImg
        self.ScissorX = ScissorX
        self.ScissorY = ScissorY
        self.velocityX = velocityX
        self.velocityY = velocityY
        self.rect = pygame.Rect(self.ScissorX, self.ScissorY, object_width, object_height)

    def move(self):
        self.ScissorX += self.velocityX
        self.ScissorY += self.velocityY
        if self.ScissorX <= 0 or self.ScissorX >= 785:
            self.velocityX = -self.velocityX
        if self.ScissorY <= 0 or self.ScissorY >= 585:
            self.velocityY = -self.velocityY
        self.rect.topleft = (self.ScissorX, self.ScissorY)




rocks = []
papers = []
scissors = []
num = 30

for x in range(num):
    RockX = random.randrange(0,250)
    RockY = random.randrange(250,350)

    PaperX = random.randrange(250,500)
    PaperY = random.randrange(250,350)

    ScissorX = random.randrange(500,750)
    ScissorY = random.randrange(250,350)

    rock_velocityX = random.choice([-1, 1]) * random.uniform(0.01, 0.2)
    rock_velocityY = random.choice([-1, 1]) * random.uniform(0.01, 0.2)
    paper_velocityX = random.choice([-1, 1]) * random.uniform(0.01, 0.2)
    paper_velocityY = random.choice([-1, 1]) * random.uniform(0.01, 0.2)
    scissor_velocityX = random.choice([-1, 1]) * random.uniform(0.01, 0.2)
    scissor_velocityY = random.choice([-1, 1]) * random.uniform(0.01, 0.2)

    rocks.append(Rock(RockImg, RockX, RockY, rock_velocityX, rock_velocityY))
    papers.append(Paper(PaperImg, PaperX, PaperY, paper_velocityX, paper_velocityY))
    scissors.append(Scissor(ScissorImg, ScissorX, ScissorY, scissor_velocityX, scissor_velocityY))


running = True
fullscreen = False
while running:

    screen.fill((100, 100, 100))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_F11:  # Toggle fullscreen with F11 key
                fullscreen = not fullscreen
                if fullscreen:
                    screen = pygame.display.set_mode((800, 600), pygame.FULLSCREEN)
                else:
                    screen = pygame.display.set_mode((800, 600), pygame.RESIZABLE)

    for rock in rocks:
        rock.move()
        screen.blit(rock.RockImg, (rock.RockX, rock.RockY))

    for paper in papers:
        paper.move()
        screen.blit(paper.PaperImg, (paper.PaperX, paper.PaperY))
    
    for scissor in scissors:
        scissor.move()
        screen.blit(scissor.ScissorImg, (scissor.ScissorX, scissor.ScissorY))

    for rock in rocks:
        for scissor in scissors:
            if rock.rect.colliderect(scissor.rect):
                scissors.remove(scissor)
                rocks.append(Rock(RockImg, scissor.ScissorX, scissor.ScissorY, scissor.velocityX, scissor.velocityY))

    for paper in papers:
        for rock in rocks:
            if paper.rect.colliderect(rock.rect):
                rocks.remove(rock)
                papers.append(Paper(PaperImg, rock.RockX, rock.RockY, rock.velocityX, rock.velocityY))

    for scissor in scissors:
        for paper in papers:
            if scissor.rect.colliderect(paper.rect):
                papers.remove(paper)
                scissors.append(Scissor(ScissorImg, paper.PaperX, paper.PaperY, paper.velocityX, paper.velocityY))


    pygame.display.update()
