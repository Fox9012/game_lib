#создай игру "Лабиринт"!
from pygame import *
def start_maze():
    mixer.init()
    font.init()
    mw = display.set_mode((900, 700))
    display.set_caption('Maze')
    BG = transform.scale(image.load('background.jpg'), (900, 700))
    clock = time.Clock()
    mixer.music.load('jungles.ogg')
    mixer.music.play()
    lose_txt = font.Font(None, 50).render('YOU LOSE!',True,(205, 134, 44))
    lose_fx = mixer.Sound('kick.ogg')
    win_txt = font.Font(None, 50).render('YOU WIN!',True,(154, 210, 0))
    win_fx = mixer.Sound('money.ogg')
    class GameSprite(sprite.Sprite):
        def __init__(self,x , y, w, h, filename, speed=0):
            super().__init__()
            self.image = transform.scale(image.load(filename), (w, h))
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
            self.speed = speed
        def reset(self):
            mw.blit(self.image, (self.rect.x, self.rect.y))
    class Player(GameSprite):
        def update(self):
            key_pressed = key.get_pressed()
            if key_pressed[K_w] and self.rect.top > 0:
                self.rect.y -= self.speed
            if key_pressed[K_s] and self.rect.bottom < 700:
                self.rect.y += self.speed
            if key_pressed[K_d] and self.rect.right < 900:
                self.rect.x += self.speed
            if key_pressed[K_a] and self.rect.left > 0:
                self.rect.x -= self.speed
    class Enemy(GameSprite):
        def __init__(self ,x ,y ,w ,h , filename, speed=0):
            super().__init__(x, y, w, h, filename, speed)
            self.direction = 'left'
        def update_h(self):
            if self.rect.x > 800:
                self.direction = 'left'
            elif self.rect.x < 630:
                self.direction = 'right'
            if self.direction == 'left':
                self.rect.x -= self.speed
            else:
                self.rect.x += self.speed
        def update_v(self):
            if self.rect.y > 500:
                self.direction = 'down'
            elif self.rect.y < 150:
                self.direction = 'up'
            if self.direction == 'down':
                self.rect.y -= self.speed
            else:
                self.rect.y += self.speed
    class Wall(sprite.Sprite):
        def __init__(self, x, y, w, h, color):
            super().__init__()
            self.color = color
            self.image = Surface((w , h))
            self.image.fill(self.color)
            self.rect = self.image.get_rect()
            self.rect.x = x
            self.rect.y = y
        def reset(self):
            mw.blit(self.image, (self.rect.x, self.rect.y))
    player = Player(25, 550, 70, 70, 'hero.png',5)
    enemy1 = Enemy(300, 400, 70, 70, 'cyborg.png',5)
    enemy2 = Enemy(750, 400, 70, 70, 'cyborg.png',5)
    goal = GameSprite(750, 550, 70, 70, 'treasure.png')
    wall1 = Wall(0, 0, 20, 900,(143, 225, 30))
    wall2 = Wall(0, 0, 1000, 20,(143, 225, 30))
    wall3 = Wall(100, 125, 20, 900,(143, 225, 30))
    wall4 = Wall(0,650, 100, 900,(143, 225, 30))
    wall5 = Wall(100, 110, 150, 20,(143, 225, 30))
    wall6 = Wall(250,110, 20, 150,(143, 225, 30))
    wall7 = Wall(250,350, 20, 500,(143, 225, 30))
    wall8 = Wall(400, 0, 20, 260,(143, 225, 30))
    wall9 = Wall(400,355, 20, 230,(143, 225, 30))
    wall10 = Wall(0, 680, 1000, 20,(143, 225, 30))
    wall11 = Wall(500,240, 20, 135,(143, 225, 30))
    wall12 = Wall(400,355, 100, 20,(143, 225, 30))
    wall13 = Wall(400,240, 100, 20,(143, 225, 30))
    wall14 = Wall(600,0, 20, 150,(143, 225, 30))
    wall15 = Wall(600,250, 20, 500,(143, 225, 30))
    run = True
    finish = False
    while run:
        for e in event.get():
            if e.type == QUIT:
                run = False
        if not finish:
            mw.blit(BG, (0 ,0))
            player.reset()
            player.update()
            enemy1.reset()
            enemy1.update_v()
            enemy2.reset()
            enemy2.update_h()
            goal.reset()
            wall1.reset()
            wall2.reset()
            wall3.reset()
            wall4.reset()
            wall5.reset()
            wall6.reset()
            wall7.reset()
            wall8.reset()
            wall9.reset()
            wall10.reset()
            wall11.reset()
            wall12.reset()
            wall13.reset()
            wall14.reset()
            wall15.reset()
            if sprite.collide_rect(player,wall1):
                lose_fx.play()
                mw.blit(lose_txt,(300, 300))
                finish = True
            if sprite.collide_rect(player,wall2):
                lose_fx.play()
                mw.blit(lose_txt,(300, 300))
                finish = True
            if sprite.collide_rect(player,wall3):
                lose_fx.play()
                mw.blit(lose_txt,(300, 300))
                finish = True
            if sprite.collide_rect(player,wall4):
                lose_fx.play()
                mw.blit(lose_txt,(300, 300))
                finish = True
            if sprite.collide_rect(player,wall5):
                lose_fx.play()
                mw.blit(lose_txt,(300, 300))
                finish = True
            if sprite.collide_rect(player,wall6):
                lose_fx.play()
                mw.blit(lose_txt,(300, 300))
                finish = True
            if sprite.collide_rect(player,wall7):
                lose_fx.play()
                mw.blit(lose_txt,(300, 300))
                finish = True
            if sprite.collide_rect(player,wall8):
                lose_fx.play()
                mw.blit(lose_txt,(300, 300))
                finish = True
            if sprite.collide_rect(player,wall9):
                lose_fx.play()
                mw.blit(lose_txt,(300, 300))
                finish = True
            if sprite.collide_rect(player,wall10):
                lose_fx.play()
                mw.blit(lose_txt,(300, 300))
                finish = True
            if sprite.collide_rect(player,wall11):
                lose_fx.play()
                mw.blit(lose_txt,(300, 300))
                finish = True
            if sprite.collide_rect(player,wall12):
                lose_fx.play()
                mw.blit(lose_txt,(300, 300))
                finish = True
            if sprite.collide_rect(player,wall13):
                lose_fx.play()
                mw.blit(lose_txt,(300, 300))
                finish = True
            if sprite.collide_rect(player,wall14):
                lose_fx.play()
                mw.blit(lose_txt,(300, 300))
                finish = True
            if sprite.collide_rect(player,wall15):
                lose_fx.play()
                mw.blit(lose_txt,(300, 300))
                finish = True
            if sprite.collide_rect(player,enemy2):
                lose_fx.play()
                mw.blit(lose_txt,(300, 300))
                finish = True
            if sprite.collide_rect(player,enemy1):
                lose_fx.play()
                mw.blit(lose_txt,(300, 300))
                finish = True
            if sprite.collide_rect(player,goal):
                win_fx.play()
                mw.blit(win_txt,(300, 300))
                finish = True  
        clock.tick(60)
        display.update()