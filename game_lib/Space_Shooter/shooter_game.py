#Создай собственный Шутер!

from pygame import *
from random import*
import time as tm
font.init()
mixer.init()
window = display.set_mode((700, 500))
display.set_caption('Space Shooter')
BG = transform.scale(image.load('galaxy.jpg'),(700,500))
clock = time.Clock()
mixer.music.load('space.ogg')
mixer.music.play()
shoot = mixer.Sound('fire.ogg')
lose_txt = font.Font('gnyrwn971.ttf', 50).render('YOU LOSE!',True,(205, 134, 44))
win_txt = font.Font('gnyrwn971.ttf', 50).render('YOU WIN!',True,(205, 134, 44))
pass_check = 0
kill_check = 0
time_shoot = 0
life = 3
rel_time = False
num_fire = 0

class GameSprite(sprite.Sprite):
    def __init__(self,x , y, w, h, filename, speed=0):
        super().__init__()
        self.image = transform.scale(image.load(filename), (w, h))
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.speed = speed
    def reset(self):
        window.blit(self.image, (self.rect.x, self.rect.y))
class Player(GameSprite):
    def update(self):
        keys = key.get_pressed()
        if keys[K_d] and self.rect.x < 650:
            self.rect.x += self.speed
        if keys[K_a] and self.rect.x > 0:
            self.rect.x -= self.speed
    def fire(self):
        bullets.add(Bullet(self.rect.centerx,self.rect.top,5,10,'bullet.png',10))
class Enemy(GameSprite):
    def update(self):
        global pass_check
        if self.rect.y > 450:
            self.rect.y = 0
            self.rect.x = randint(10, 650)
            pass_check += 1
            self.speed = randint(2,4)
            
        else:
            self.rect.y += self.speed
class Bullet(GameSprite):
    def update(self):
        self.rect.y -= self.speed
        if self.rect.y < 0:
            self.kill()
class Asteroids(GameSprite):
    def update(self):
        self.rect.y += self.speed
        if self.rect.y > 450:
            self.rect.y = 0
            self.rect.x = randint(10, 650)
            self.speed = 2
player = Player(300, 400, 50, 100, 'rocket.png',5)
asteroid = Asteroids(20,0,50,50,'asteroid.png',2)
enemies = sprite.Group()
bullets = sprite.Group()
for i in range(5):
    enemies.add(Enemy(randint(10, 650), 0, 80, 50, 'ufo.png',randint(2,4)))

def start_shooter(run):
    finish = False
    run = run
    while run:
        for e in event.get():
            if e.type == QUIT:
                run = False
            if e.type == KEYDOWN:
                if e.key == K_SPACE:
                    if num_fire < 5:
                        num_fire += 1
                        player.fire()
                        shoot.play()
                    if num_fire >= 5 and rel_time == False:
                        rel_time = True
                        last_time = tm.time()
        if not finish:
            window.blit(BG, (0, 0))
            player.reset()
            player.update()
            asteroid.reset()
            asteroid.update()
            enemies.draw(window)
            enemies.update()
            enemy_pass = font.Font('gnyrwn971.ttf', 30).render('lost: ' + str(pass_check),True,(205, 134, 44))
            kills = font.Font('gnyrwn971.ttf', 30).render('kills: ' + str(kill_check),True,(205, 134, 44))
            lifes = font.Font('gnyrwn971.ttf', 30).render('lifes: ' + str(life),True,(205, 134, 44))
            window.blit(lifes,(20,70))
            window.blit(enemy_pass,(20,10))
            window.blit(kills,(20,40))
            if pass_check >= 10:
                finish = True
                window.blit(lose_txt,(250,200))
            if sprite.spritecollide(player,enemies,False):
                finish = True
                window.blit(lose_txt,(250,200))
            bullets.draw(window)
            bullets.update()
            if sprite.groupcollide(enemies,bullets,True,True):
                enemies.add(Enemy(randint(10, 650), 0, 80, 50, 'ufo.png',randint(2,4)))
                kill_check += 1
            if kill_check >= 10:
                finish = True
                window.blit(win_txt,(270,200))
            if sprite.collide_rect(player,asteroid):
                life -= 1
                asteroid.rect.y = 0
                asteroid.rect.x = randint(10, 650)
            sprite.spritecollide(asteroid,bullets,True)
            if life <= 0:
                finish = True
                window.blit(lose_txt,(250,200))
            if rel_time == True:
                now_time = tm.time()
                if now_time - last_time < 3:
                    wait_reload = font.Font('gnyrwn971.ttf', 30).render('wait reload',True,(255, 0, 0))
                    window.blit(wait_reload,(250,470))
                else:
                    num_fire = 0
                    rel_time = False
        display.update()
        clock.tick(60)
    