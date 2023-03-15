import pygame, math
from numpy import interp
class darkJump:
    #The game is implemented poorly
    #Probably a lot of spelling errors
    #I hope you get to the end. It's my favourite part
    #If you get stuck try to find an arrow
    
    class vector:
    #Vectors are useful way of dealing with movement and positions
    #Lets make our own
        def __init__(self, x: int, y: int):
            self.x = x                                                                                                                                                           
            self.y = y
        
        def __add__(self, another):
            return darkJump.vector(self.x + another.x, self.y + another.y)
        
        def __sub__(self, another):
            return darkJump.vector(self.x - another.x, self.y - another.y)
        
        def __mul__(self, value: int):
            return darkJump.vector(self.x * value, self.y * value)   
        
        def lenght(self):
            return math.sqrt(self.x**2+self.y**2)
            
        def set_len(self, value: int):
            l = self.lenght()
            self.x = self.x/l * value
            self.y = self.y/l  * value
            
        @property
        def get(self):
            return(self.x, self.y)
        
        def __str__(self):
            return f"{self.x}, {self.y}"

    def __init__(self):
        pygame.init()
        #Window size DON'T CHANGE
        self.X = 1000
        self.Y = 1000
        
        self.window = pygame.display.set_mode((self.X, self.Y))
        self.clock = pygame.time.Clock()
        self.my_font = pygame.font.SysFont('calibri', 40)
        self.my_font2 = pygame.font.SysFont('calibri', 20)
        self.my_font3 = pygame.font.SysFont('couriernew', 40)
        #Platforms = (XX, YY, width)
        self.platforms =[(400, 850, 100),   (0, 950, 1000),   (350, 780, 70),   (200, 750, 70)
                        ,(100, 675, 100),   (250, 640, 90),   (400, 590, 100),  (700, 780, 60)
                        ,(100, 450, 50),    (50, 350, 50),    (150, 260, 60),   (225, 190, 100)
                        ,(200, 510, 100),   (75, 130, 75),    (450, 170, 80),   (680, 190, 80)
                        ,(870, 470, 80)]
        
        self.coins     =[(730, 750), (111, 90), (910, 440)]
        self.coinSprite = pygame.image.load("coin.png")
        self.coins_collected = 0
        
        self.end_timer = 0
        
        self.create_player()
        self.loop()
        
    def create_player(self):
        self.img = pygame.image.load("monster.png")
        self.max_speed = 6
        self.speed = 1
        
        self.pos = self.vector(self.X / 2, self.Y - self.img.get_width()/2 - 100) 
        self.vel = self.vector(0, 0)
        self.acc = self.vector(0, 0)
         
    def on_floor(self):
        for platform in self.platforms:
            if platform[0] - 20 < self.pos.x and platform[0] + platform[2] + 20 > self.pos.x:
                if (self.acc + self.pos + self.vel).y >= platform[1] and self.pos.y <= platform[1]: 
                    self.floor = platform[1]
                    return True
        
    def move(self):
            def move_right(self):
                self.acc += self.vector(self.speed, 0)

            def move_left(self):
                self.acc -= self.vector(self.speed, 0)
                
            def jump(self):
                if self.on_floor(): self.acc -= self.vector(0, 15)
                
            def friction(self):
                if self.vel.x < 0: self.acc += self.vector(2, 0)
                if self.vel.x > 0: self.acc -= self.vector(2, 0)
            
            def calc_vectors(self):
                self.vel += self.acc
                #Limit the x speed to x max speed
                if abs(self.vel.x) > self.max_speed: 
                    if self.vel.x > 0: self.vel.x = self.max_speed
                    if self.vel.x < 0: self.vel.x =-self.max_speed
                #Make the edges of the screen "bouncy"
                if self.pos.x + self.vel.x <= 0 or self.pos.x + self.vel.x + self.img.get_width()/2 >= self.X: self.vel.x = self.vel.x * -1
                #add the calculated velocity to position
                self.pos += self.vel
                #set acceleration to 0 as it has been "used"
                self.acc = self.vector(0, 0)
                
            keys = pygame.key.get_pressed()
            if keys[pygame.K_LEFT]: move_left(self)
            if keys[pygame.K_RIGHT]: move_right(self)
            if keys[pygame.K_UP]:jump(self)
            self.vel += self.vector(0, 1)
            if self.on_floor() and self.vel.y > 0: 
                self.vel.y = 0
                self.pos.y = self.floor
                if not (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]): friction(self)
            calc_vectors(self)

    def draw(self):
        def draw_ligh(self):
            #drawing the lights seperatly so that they overlap nicely
            smooth = 100
            player_cordinates = self.pos - self.vector(0, self.img.get_width() / 2 + 10)
            for i in range(smooth):
                c = interp(i, [0, smooth], [1, 20])
                y = interp(i, [0, smooth], [1, 30])
                ccc= (y, y, c)
                for coin in self.coins:
                    coin_cordinates = (coin[0], coin[1])
                    pygame.draw.circle(self.window, ccc, coin_cordinates, interp(i, [0, smooth], [130, 0]))
                pygame.draw.circle(self.window, ccc, player_cordinates.get, interp(i, [0, smooth], [190, 0]))
                '''
            for coin in self.coins:
                coin_cordinates = (coin[0], coin[1])
                pygame.draw.circle(self.window, (5, 5, 5), coin_cordinates, 90)
            if self.end_timer < 3000: pygame.draw.circle(self.window, (5, 5, 5), player_cordinates.get, 130)
            for coin in self.coins:
                coin_cordinates = (coin[0], coin[1])
                pygame.draw.circle(self.window, (7, 7, 7), coin_cordinates, 75)
            if self.end_timer < 6000: pygame.draw.circle(self.window, (7, 7, 7), player_cordinates.get, 100)
            for coin in self.coins:
                coin_cordinates = (coin[0], coin[1])
                pygame.draw.circle(self.window, (11, 11, 10), coin_cordinates, 60)
            if self.end_timer < 9000: pygame.draw.circle(self.window, (11, 11, 10), player_cordinates.get, 75)
            for coin in self.coins:
                coin_cordinates = (coin[0], coin[1])
                pygame.draw.circle(self.window, (13, 13, 10), coin_cordinates, 40)
            if self.end_timer < 10000: pygame.draw.circle(self.window, (13, 13, 10), player_cordinates.get, 60)
            for coin in self.coins:
                coin_cordinates = (coin[0], coin[1])
                pygame.draw.circle(self.window, (17, 15, 10), coin_cordinates, 25)
            if self.end_timer < 12000: pygame.draw.circle(self.window, (17, 15, 10), player_cordinates.get, 40)        
            '''
        def draw_player(self):
            draw_cordinates = self.pos - self.vector(0, self.img.get_width() / 2 + 10)
            self.window.blit(self.img, (draw_cordinates.x - self.img.get_width() / 2, draw_cordinates.y - self.img.get_height() / 2))

        def draw_platforms(self):
            for platform in self.platforms:
                platformX = platform[0]
                platformY = platform[1]
                platformW = platform[2]
                
                pygame.draw.circle(self.window, (0, 0, 0), (platformX, platformY), 8)
                pygame.draw.circle(self.window, (0, 0, 0), (platformX + platformW, platformY), 8)
                pygame.draw.rect(self.window, (0, 0, 0), (platformX , platformY -8, platformW, 16), )
        
        def draw_coins(self):
            for coin in self.coins:
                draw_cordinates = (coin[0], coin[1])
                self.window.blit(self.coinSprite, (draw_cordinates[0] - self.coinSprite.get_width() / 2, draw_cordinates[1] - self.coinSprite.get_height() / 2))

        def write_centered(self,cord: tuple, s: str, i: int):
            if i == 0: text_surface = self.my_font.render(s, True, (0, 0, 0))
            if i == 1: text_surface = self.my_font2.render(s, True, (60, 60, 60))
            if i == 2: text_surface = self.my_font3.render(s, False, (40, 40, 20))
            self.window.blit(text_surface, (cord[0] - text_surface.get_width()/2, cord[1]))
    
        self.window.fill((0, 0, 0))
        draw_ligh(self)
        write_centered(self, (275, 190), "--->", 0)
        draw_player(self)
        draw_coins(self)
        draw_platforms(self)
        if pygame.time.get_ticks() < 4500: write_centered(self, (self.pos - self.vector(0, 120)).get, "Somebody threw these coins into my cosy well...", 1)
        if pygame.time.get_ticks() > 4500 and pygame.time.get_ticks() < 9000: write_centered(self, (self.pos - self.vector(0, 120)).get, "The shine hurts my eyes.", 1)
        if pygame.time.get_ticks() > 9000 and pygame.time.get_ticks() < 13500: write_centered(self, (self.pos - self.vector(0, 120)).get, "I need to cover them as fast as possible.", 1)
        if self.coins_collected < 1: write_centered(self, (930, 950), "I", 2)
        if self.coins_collected < 2: write_centered(self, (950, 950), "I", 2)
        if self.coins_collected < 3: write_centered(self, (970, 950), "I", 2)
        if self.coins_collected == 3:
            self.coins_collected = 4
            self.t = pygame.time.get_ticks()
        if self.coins_collected == 4:
            self.end_timer = pygame.time.get_ticks() - self.t
        if self.end_timer < 12000 and self.coins_collected == 4: write_centered(self, (self.pos - self.vector(0, 120)).get, "Finally... Darkness", 1)
        if self.end_timer > 12000 and self.coins_collected == 4: write_centered(self, (500, 500), "The monster is happy, and the game has ended.", 1)
        pygame.display.flip()
      
    def  collect_coin(self):
        playerd_dimensionDiv2 = (self.img.get_width()/2, self.img.get_height()/2)
        #Hitbox = (object: xMin, xMax, yMin, yMax)
        #Player hitbox
        ph                = (self.pos.x - playerd_dimensionDiv2[0], self.pos.x + playerd_dimensionDiv2[0],
                             self.pos.y - playerd_dimensionDiv2[1], self.pos.y + playerd_dimensionDiv2[1])
        for coin in self.coins:
            coin_dimensionDiv2 = (self.coinSprite.get_width()/2, self.coinSprite.get_height()/2)
            #Coin hitbox
            ch          =   (coin[0] - coin_dimensionDiv2[0], coin[0] + coin_dimensionDiv2[0],
                             coin[1] - coin_dimensionDiv2[1], coin[1] + coin_dimensionDiv2[1])
            if ((ph[1] >= ch[0] and ph[0] <= ch[0]) or (ph[0] <= ch[1] and ph[1] >= ch[1])) and ((ph[3] >= ch[2] and ph[2] <= ch[2]) or (ph[2] <= ch[3] and ph[3] >= ch[3])):
                self.coins_collected += 1
                self.coins.remove(coin)
                
    def loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit()
            self.move()
            self.draw()
            self.collect_coin()
            self.clock.tick(60)

if __name__ == "__main__":
    darkJump()