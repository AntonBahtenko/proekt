import pygame 
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('jungles.ogg')
pygame.mixer.music.play()

window = pygame.display.set_mode((700,500))
fps = pygame.time.Clock()

fon = pygame.image.load("background.jpg")
fon = pygame.transform.scale(fon,(700,500))

class GameObject(pygame.sprite.Sprite):
    def __init__(self, image, visota, shirina,x, y,speed):
        super().__init__()
        self.img_sprite = pygame.image.load(image)
        self.img_sprite = pygame.transform.scale(self.img_sprite,(visota,shirina))

        self.hitbox = self.img_sprite.get_rect()
        self.hitbox.x = x
        self.hitbox.y = y
        
        self.speed = speed
        self.move = ''
    def show(self):
        window.blit(self.img_sprite,self.hitbox)

class GamePlayer(GameObject):
    keys = pygame.key.get_pressed()
       if ypravlenenie(self):
       if keys[pygame.K_w] and self.hitbox.y > 0:
            self.hitbox.y -= self.speed

        if keys[pygame.K_s] and self.hitbox.y < 450:
            self.hitbox.y += self.speed 

        if keys[pygame.K_d] and self.hitbox.x < 650:
            self.hitbox.x += self.speed 

        if keys[pygame.K_a] and self.hitbox.x >0:
            self.hitbox.x -= self.speed 

class Wall(pygame.sprite.Sprite):
    def __init__(self, wall_x, wall_y,wall_shirina, wall_visota, wall_r, wall_g, wall_b):
        super().__init__()
        self.wall_shirina = wall_shirina
        self.wall_visota = wall_visota
        self.wall_r = wall_r
        self.wall_g = wall_g
        self.wall_b = wall_b

        self.wall_image = pygame.Surface((self.wall_shirina, self.wall_visota))
        self.wall_image.fill((self.wall_r,self.wall_g,self.wall_b))

        self.wall_hitbox = self.wall_image.get_rect()
        self.wall_hitbox.x = wall_x
        self.wall_hitbox.y = wall_y

    def show(self):
        window.blit(self.wall_image,self.wall_hitbox)


player = GamePlayer("hero.png",50,50, 10, 430, 5)

zoloto = GameObject("treasure.png",60,60, 600,420,0)

run = True
w1 = Wall(80,150,10,280,123,123,123)
w2 = Wall(80,140,90,10,123,123,123)
w3 = Wall(170,140,10,280,123,123,123)
w4 = Wall(170,420,200,10,123,123,123)
w5 = Wall(360,80,10,340,123,123,123)
w6 = Wall(450,140,10,400,123,123,123)
w7 = Wall(360,70,180,10,123,123,123)
w8 = Wall(540,70,10,310,123,123,123)
w9 = Wall(540,380,300,10,123,123,123)

class Enemy(GameObject):
    def forward(self):
        if self.hitbox.y < 440:
            self.move = "pravo"
        if self.hitbox.y > 100:
            self.move = "levo"
            

        if self.move == 'levo':
            self.hitbox.y -= self.speed
        else:
            self.hitbox.y +=self.speed
vrag = Enemy("cyborg.png",50,50, 100, 420, 3)

while run:
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            run = False

    window.blit(fon,(0,0))
    player.show()
    player.ypravlenenie()
    vrag.show()
    zoloto.show()
    w1.show()
    w2.show()
    w3.show()
    w4.show()
    w5.show()
    w6.show()
    w7.show()
    w8.show()
    w9.show()
    vrag.forward()
    if player.hitbox.colliderect(w1.wall_hitbox) or player.hitbox.colliderect(w2.wall_hitbox) or player.hitbox.colliderect(w2.wall_hitbox) or player.hitbox.colliderect(w3.wall_hitbox) or player.hitbox.colliderect(w4.wall_hitbox) or player.hitbox.colliderect(w5.wall_hitbox) or player.hitbox.colliderect(w6.wall_hitbox) or player.hitbox.colliderect(w7.wall_hitbox) or player.hitbox.colliderect(w8.wall_hitbox) or player.hitbox.colliderect(w9.wall_hitbox):
        player.hitbox.x = 20
        player.hitbox.y = 400
        

    

    pygame.display.update()
    fps.tick(60)

