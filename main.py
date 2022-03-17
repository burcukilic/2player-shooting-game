import pygame
pygame.init()
font = pygame.font.Font("freesansbold.ttf",128)
win = pygame.display.set_mode((1400,700))
run = True
clock = pygame.time.Clock()
bg = pygame.image.load('sky.jpg')
bg = pygame.transform.scale(bg,(1400,700))
lb = pygame.image.load('longblock.png')
lb = pygame.transform.scale(lb,(757,70))
sb = pygame.image.load('block2.png')
sb = pygame.transform.scale(sb,(160,80))
bi = pygame.transform.scale(pygame.image.load('bullllet.png'),(10,10))
chars = [pygame.transform.scale(pygame.image.load('c'+str(i+1)+'.png'),(57,76)) for i in range(3)]
chars.append(pygame.transform.scale(pygame.image.load('c4.png'),(84,76)))
puimglist = [pygame.transform.scale(pygame.image.load(["heart","fire","shield"][i]+".png"),(35,35)) for i in range(3)]
puimglist[1] = pygame.transform.scale(puimglist[1],(85,85))
lw = 757
lh = 70
sw = 160
sh = 80
bullets0 = []
bullets1 = []
fire0 = False
fire1 = False
gameover = False

pygame.mixer.music.load('backgroundmusic.mp3')

class Char:

    def __init__(self,x,y,state,xmomentum,ymomentum,a,facing,jump,color,hp,armor):
        self.x=x
        self.y=y
        self.state=state
        self.xmomentum=xmomentum
        self.ymomentum=ymomentum
        self.a=a
        self.facing=facing
        self.k = 0
        self.jump=jump
        self.color = color
        self.hp = hp
        self.armor = armor

    def draw(self,win):
        self.x += self.xmomentum
        self.y += self.ymomentum

        if self.state==0:
            ci = win.blit([pygame.transform.flip(chars[0],True,False),chars[0]][self.facing],(self.x,self.y))
        elif self.state==1:
            ci = win.blit(chars[1+round(self.a)%2],(self.x,self.y))
            self.a+=1/15
        elif self.state==2:
            ci = win.blit(pygame.transform.flip(chars[1+round(self.a)%2],True,False),(self.x,self.y))
            self.a+=1/15
        elif self.state==3:
            ci = win.blit([pygame.transform.flip(chars[3],True,False),chars[3]][self.facing],(self.x,self.y))
            self.k += 1
            if self.k ==10:
                self.state=0

        if b1.colliderect(ci):
            if (self.y+76-10 <= 590):
                if self.ymomentum >= 0:
                    self.y = 590-76
                    self.ymomentum = 0
                    self.jump = False
            if (self.y >= 590 + lh):
                self.y = 590+lh
                self.ymomentum = 0
            if (self.x+57<=340+5):
                self.x = 340-57

            if (self.x>=340+lw-5):
                self.x = 340+lw


        elif b2.colliderect(ci):
            if (self.y + 76 - 10 <= 240):
                if self.ymomentum >= 0:
                    self.y = 240 - 76
                    self.ymomentum = 0
                    self.jump = False
            if (self.y >= 240 + lh-15):
                self.y = 240+lh
                self.ymomentum = 0
            if (self.x+57<=340+5):
                self.x = 340-57-5

            if (self.x>=340+lw-5):
                self.x = 340+lw+5


        elif b3.colliderect(ci):
            if (self.y + 76 - 10 <= 410):
                if self.ymomentum >= 0:
                    self.y = 410 - 76
                    self.ymomentum = 0
                    self.jump = False
            if (self.y >= 410 + sh-10):
                self.y = 410+sh
                self.ymomentum = 0
            if (self.x+57<=100+5):
                self.x = 100-57

            if (self.x>=100+sw-5):
                self.x = 100+sw


        elif b4.colliderect(ci):
            if (self.y + 76 - 10 <= 410):
                if self.ymomentum >= 0:
                    self.y = 410 - 76
                    self.ymomentum = 0
                    self.jump = False
            if (self.y >= 410 + sh-10):
                self.y = 410+sh
                self.ymomentum = 0
            if (self.x+57<=1190+5):
                self.x = 1190-57
            if (self.x>=1190+sw-5):
                self.x = 1190+sw



        for bullet in [bullets1,bullets0][self.color]:
            if bullet.b.colliderect(ci)&(self.armor==False):
                [bullets1,bullets0][self.color].remove(bullet)
                self.hp -= 10
        global putype, pu
        if pu:
            if puimg.colliderect(ci):
                if putype == 0:
                    self.hp += 30
                    if self.hp>100:
                        self.hp = 100
                if putype == 1:
                    if self.armor is False:
                        self.hp -= 30
                if putype ==2:
                    if self.armor is False:
                        self.armor = True
                        global f
                        f = [0 for i in range(2)]
                        f[self.color] = 180

                pu = False
        if self.armor==True:
            pygame.draw.rect(win,(240,240,160),(self.x+32-25+(self.facing-1)*8, self.y-25,50*f[self.color]/180,5))
            f[self.color] -= 1
            if f[self.color] == 0 :
                self.armor= False



        if self.y>=700:
            self.hp = 0
        if self.hp <=0:
            global losecolor
            losecolor = [(0,0,255),(255,0,0)][self.color]
            global gameover
            gameover = True




        pygame.draw.rect(win,[(255,0,0),(0,0,255)][self.color],(self.x+64/2-50/2+(self.facing-1)*(8),self.y-15,self.hp/2,5))


    def fire(self):
        self.k = 0
        [bullets0,bullets1][self.color].append(Bullet((self.x-2,self.x+84)[self.facing],self.y+20,self.facing))





class Bullet:
    def __init__(self,x,y,facing):
        self.x=x
        self.y=y
        self.facing=facing
        self.b = 0
    def drawbullet(self,win):
        self.x+=(self.facing*2-1)*10
        self.b = win.blit(bi,(self.x,self.y))







c = Char(500,160,0,0,0,0,1,0,0,100,False)
c2 = Char(700,500,0,0,0,0,1,0,1,100,False)
h = 0
n = 0
bgx = 0

import random

global pu
pu = False
global newvar
newvar=480
def game():
    global coordinates
    global pu,newvar
    if pu==False:
        pur = random.randint(1,4000)
        if pur <30:
            newvar = 480
            global putype
            putype = random.randint(0,2)
            puloc = random.randint(0,3)
            pu = True
            coordinates = [(random.randint(340,340+lw-35-50*(putype==1)),590-43-40*(putype==1)),
                           (random.randint(340,340+lw-35-50*(putype==1)),240-43-40*(putype==1)),
                           (random.randint(100,100+sw-35-50*(putype==1)),410-43-40*(putype==1)),
                           (random.randint(1190,1190+sw-35-50*(putype==1)),410-43-40*(putype==1))][puloc]
    if pu:
        newvar -= 1
        if newvar == 0:
            pu = False
        global puimg
        puimg = win.blit(puimglist[putype],(coordinates))


    global fire0
    if fire0 is True:
        global h
        h += 1
        if h == 10:
            h = 0
            fire0 = False
    global fire1
    if fire1 is True:
        global n
        n += 1
        if n == 10:
            n = 0
            fire1 = False

    global b1,b2,b3,b4

    b1 = win.blit(lb, (340, 590))
    b2 = win.blit(lb, (340, 240))
    b3 = win.blit(sb, (100, 410))
    b4 = win.blit(sb, (1190, 410))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            global run
            run = False

        if event.type == pygame.KEYDOWN:
            # FOR RIGHT PLAYER
            if event.key == pygame.K_RIGHT:
                c.state = 1
                c.facing = 1
                c.xmomentum = 5
            if event.key == pygame.K_LEFT:
                c.state = 2
                c.facing = 0
                c.xmomentum = -5
            if event.key == pygame.K_RETURN:
                if not fire0:
                    fire0 = True
                    c.state = 3
                    c.fire()
            if event.key == pygame.K_UP:
                if c.jump is False:
                    c.jump = True
                    c.ymomentum = -15
            # FOR WASD PLAYER
            if event.key == pygame.K_d:
                c2.state = 1
                c2.facing = 1
                c2.xmomentum = 5
            if event.key == pygame.K_a:
                c2.state = 2
                c2.facing = 0
                c2.xmomentum = -5
            if event.key == pygame.K_SPACE:
                if not fire1:
                    fire1 = True
                    c2.state = 3
                    c2.fire()
            if event.key == pygame.K_w:
                if c2.jump is False:
                    c2.jump = True
                    c2.ymomentum = -15
        if event.type == pygame.KEYUP:
            # FOR RIGHT
            if event.key == pygame.K_RIGHT:
                if c.xmomentum > 0:
                    c.xmomentum = 0
                    c.state = 0

            if event.key == pygame.K_LEFT:
                if c.xmomentum < 0:
                    c.xmomentum = 0
                    c.state = 0
            # FOR WASD
            if event.key == pygame.K_d:
                if c2.xmomentum > 0:
                    c2.xmomentum = 0
                    c2.state = 0
            if event.key == pygame.K_a:
                if c2.xmomentum < 0:
                    c2.xmomentum = 0
                    c2.state = 0

    if c.ymomentum <= 5:
        c.ymomentum += 1
    if c2.ymomentum <= 5:
        c2.ymomentum += 1
    if c.jump & (c.ymomentum <= 0):
        c.ymomentum += -0.5
    if c2.jump & (c2.ymomentum <= 0):
        c2.ymomentum += -0.5

    for bullet in bullets0:
        bullet.drawbullet(win)
    for bullet in bullets1:
        bullet.drawbullet(win)

    # ENDING STUFF
    c.draw(win)
    c2.draw(win)

def gameoverfunc():
    retrytext = font.render("RETRY?", True, losecolor)
    txt = win.blit(retrytext, (400, 300))
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            global run
            run = False
        if event.type==pygame.MOUSEBUTTONDOWN:
            if txt.collidepoint(event.pos[0],event.pos[1]):
                global gameover,c,c2,h,n,bgx,bullets0,bullets1,fire0,fire1
                gameover = False
                c = Char(500, 160, 0, 0, 0, 0, 1, 0, 0, 100,False)
                c2 = Char(700, 500, 0, 0, 0, 0, 1, 0, 1, 100,False)
                h = 0
                n = 0
                bgx = 0
                bullets0 = []
                bullets1 = []
                fire0 = False
                fire1 = False

pygame.mixer.music.play(-1)
while run:
    win.blit(bg, (bgx, 0))
    win.blit(bg, (bgx + 1400, 0))
    bgx -= 2
    if bgx <= -1400:
        bgx = 0

    if gameover == False:
        game()
    else:
        gameoverfunc()

    clock.tick(60)
    pygame.display.update()


pygame.quit()

