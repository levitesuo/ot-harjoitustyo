# Complete your game here
import pygame
import random
 
pygame.init()
 
class BOT:
    def __init__(self, image, height, speed):
        self.speed = speed
        self.image = image
        self.pos = image.get_rect().move(0, 480 - height)
        self.score = 0
 
    def move(self,left=False, right=False):
        if right:
            self.pos.right += self.speed
        if left:
            self.pos.right -= self.speed
        if self.pos.right > 640:
            self.pos.left = 0
        if self.pos.right < 50:
             self.pos.right = 640
 
    def collides(self, other):
        left_bound = self.pos[0]
        right_bound = left_bound + self.image.get_width()
        upper_bound = self.pos[1]
        lower_bound = upper_bound + self.image.get_height()
 
        o_left_bound = other.x
        o_right_bound = o_left_bound + other.image.get_width()
        o_upper_bound = other.y
        o_lower_bound = o_upper_bound + other.image.get_height()
 
        collides_x =  (left_bound <= o_right_bound and left_bound >= o_left_bound) or (right_bound >= o_left_bound and right_bound <= o_right_bound)
        collides_y = (upper_bound <= o_lower_bound and upper_bound >= o_upper_bound) or (lower_bound >= o_upper_bound and lower_bound <= o_lower_bound)
        return collides_x and collides_y
 
class Coin:
    def __init__(self, image):
        self.x = random.randint(0, 640)
        self.y = -image.get_height()
        self.image = image
        self.speed = random.randint(1,3)
 
    def fall(self):
        self.y += self.speed
 
    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        pygame.display.flip()
 
class Enemy:
    def __init__(self, image):
        self.x = random.randint(0, 640)
        self.y = -image.get_height()
        self.image = image
        self.speed = random.randint(1,3)
 
    def fall(self):
        self.y += self.speed
 
    def draw(self, window):
        window.blit(self.image, (self.x, self.y))
        pygame.display.flip()
                 
 
win = pygame.display.set_mode((640, 480))
clock = pygame.time.Clock()          
rob = pygame.image.load('robot.png')
cimage = pygame.image.load('coin.png')
eimage = pygame.image.load('monster.png')
robot = BOT(rob, rob.get_height(), 3)
 
enemies = []
coins = []
font = pygame.font.SysFont("Arrial", 24)
 
while True:
    win.fill((100, 100, 100))
   
   
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
 
 
    keys = pygame.key.get_pressed()
 
    if keys[pygame.K_LEFT]:
        robot.move(left=True)
    if keys[pygame.K_RIGHT]:
        robot.move(right=True)
 
    if random.randint(0, 100) > 99:
        coins.append(Coin(cimage))
    for c in coins:
        
        c.fall()
        c.draw(win)
        if robot.collides(c):
            coins.remove(c)
            robot.score += 1
        if c.y > 480 + c.image.get_height():
            coins.remove(c)
 
    if random.randint(0, 1000) > 995:
        enemies.append(Enemy(eimage))
    for e in enemies:
        
        e.fall()
        e.draw(win)
        if robot.collides(e):
            enemies = []
            coins = []
            robot = BOT(rob, rob.get_height(), 3)
 
        if e.y > 480 + e.image.get_height():
            enemies.remove(e)
    
    score_text = font.render(f"Score: {robot.score}", True, (0,0, 255))
    win.blit(score_text, (5,5))
    win.blit(robot.image, robot.pos)
    pygame.display.flip()
    clock.tick(30)