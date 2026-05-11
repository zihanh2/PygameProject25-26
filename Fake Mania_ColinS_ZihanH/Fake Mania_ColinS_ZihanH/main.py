from gamelib import*

def him_update():
    him.draw()
    him.visible=True
    dpsbar.moveTo(him.x-50 , him.y +50)
    hpbar.moveTo(him.x-50 , him.y +50)
    hpbar.width = him.health
    if him.health > 100 :
        him.health = 100
    #move left
    if keys.Pressed[K_a] or keys.Pressed[K_LEFT]:
        him.x -= 7
        himl.draw()
        game.scrollBackground("right",0)
        dpsbar.moveTo(him.x-50 , him.y +50)
        hpbar.moveTo(him.x-50 , him.y +50)
        himl.moveTo(him.x,him.y)

    #move right 
    if keys.Pressed[K_d] or keys.Pressed[K_RIGHT]:
        him.x += 7
        himr.draw()
        game.scrollBackground("left",0)
        dpsbar.moveTo(him.x-50 , him.y +50)
        hpbar.moveTo(him.x-50 , him.y +50)
        himr.moveTo(him.x,him.y)

    #move forward 
    if keys.Pressed[K_w] or keys.Pressed[K_UP]:
        him.y -= 7
        himf.draw()
        game.scrollBackground("down",15)
        dpsbar.moveTo(him.x-50 , him.y +50)
        hpbar.moveTo(him.x-50 , him.y +50)
        himf.moveTo(him.x,him.y)

    #move backward
    if keys.Pressed[K_s] or keys.Pressed[K_DOWN]:
        him.y += 7
        himb.draw()
        game.scrollBackground("up",15)
        dpsbar.moveTo(him.x-50 , him.y +50)
        hpbar.moveTo(him.x-50 , him.y +50)
        himb.moveTo(him.x,him.y)

  
    if him.isOffScreen("right"):
        him.x -=7
    if him.isOffScreen("left"):
        him.x +=7
    if him.isOffScreen("top"):
        him.y +=7
    if him.isOffScreen("bottom"):
        him.y -=7
    if him.isOffScreen("all"):
        game.drawText("RETURN NOW", game.width/3,game.height-500,sf)
        
def positionObjects_enemy(objects):
    for i in range(len(objects)):
        x = randint(-6000,6000)
        y = randint(-6000,6000)
        objects[i].moveTo(x,-y)
        s = randint(4,8)
        objects[i].moveTowards(him,s)
        objects[i].visible = True

def positionObjects_item(objects):
    for i in range(len(objects)):
        x = randint(100,900)
        y = randint(100,7000)
        objects[i].moveTo(x,-y)
        s = randint(4,8)
        objects[i].setSpeed(s , 180)
        objects[i].visible = True

        
def power_update():

    for i in range(len(pill)):
        pill[i].move()
        if him.collidedWith(pill[i]):
            him.health += 5
            pill[i].visible = False
            game.score +=1
            hu.play( True )
       
game = Game(1000,800,"The Player")

bk = Animation( "./images/white.png" , 1 , game , 223 , 148 )
bk.resizeTo(game.width,game.height)
game.setBackground(bk)
bk.draw()


f=Font(black,48,black,"Times New Roman") 
sf=Font(red,20,black,"Times New Roman")
#IMAGES 

#You Lose/ You Win

you_lose = Image( "images//youlose.png" , game )
you_lose.y = 190

you_win = Image( "images//youwin.png" , game ) 
you_win.y = 190 

end = Image("images//endscreen.png" , game) 
end.resizeTo(1000,700) 

#Intro / Start 

title = Image("images//title.png",game)
title.resizeBy(25)
title.y = 190

intro = Image( "images//intro.png" , game )
intro.resizeBy(-25)
intro.y = 100

story = Image("images/story.png", game)
story.resizeBy(-25)
story.y = 650
story1 = Image("images/story.png", game)
story1.resizeBy(-25)
story2 = Image("images/story2.png", game)
story2.resizeBy(-15)

storyscreen = Image("images/storyscreen2.png", game)
storyscreen.resizeTo(900, 700)
storyscreen.visible = False

start = Image( "images//gamestart.png" ,game)
start.resizeBy(-25)
start.y = 500
start1 = Image( "images//gamestart.png" ,game)
start1.resizeBy(-25)
start2 = Image("images/gamestart2.png", game)
start2.resizeBy(-15)

howto = Image("images/howto.png", game)
howto.resizeBy(-43)
howto.y = 575
howto1 = Image("images/howto.png", game)
howto1.resizeBy(-43)
howto2 = Image("images/howto2.png", game)
howto2.resizeBy(-15)

tutorial = Image("images/tutorial3.png", game)
tutorial.resizeTo(1000, 800)
tutorial.visible = False

rb = Image("images//back.png", game)
rb.resizeBy(-50)
rb.moveTo(925,685)
rb.visible = False

rb1 = Image("images//back.png", game)
rb1.resizeBy(-50)
rb1.visible = False

rb2 = Image("images//back.png", game)
rb2.resizeBy(-45)
rb2.visible = False

#Hit Effect

hit = Image( "images//hit.png" , game ) 
hit.resizeBy(-40)

slash = Animation ( "images//slash.png" , 9 , game , 141/3 , 192/3 , -25 )
slash.resizeBy(200)

'''
punchl = Animation ("images//punchl.png" , 2 , game , 198 , 255/2 , -10)
punchr = Animation ("images//punchr.png" , 2 , game , 198 , 255/2 , -10)
punchu = Animation ("images//punchu.png" , 2 , game , 255/2 , 198 , -10)
punchd = Animation ("images//punchd.png" , 2 , game , 255/2 , 198 , -10)
'''
#ENTITIES 

#DR.INSANITY
boss = Image("images//boss.png" , game)
boss.y=-500

bossdps = Image("images//boss.png" , game)
bossbar = Shape("bar" , game , boss.health , 10 , blue)
boss.health = 100
bossdpsbar = Shape("bar" , game , bossdps.health , 10 , red)
bossdps.health = 100

#Ghost
ghost = []
for i in range(50):
    '''
    g = Image ( "images//ghost.png" , game )
    '''
    g = Animation ( "images//ghost3.png" , 6 , game , 283/6 , 46 , -12 )
    g.resizeBy(175)
    ghost.append(g)
    #ghost[i].collisionBorder = "circle"

#Slime
slime = []
for i in range(50):
    '''
    s = Image ( "images//slime.png" , game )
    '''
    s = Animation ( "images//slime2.png" , 4 , game , 515/4 , 78 , -10 )
    s.resizeBy(10)
    slime.append(s)
    #slime[i].collisionBorder = "rectangle"

#Pill
pill = []
for i in range(50): 
    p = Image("images//pill.png" , game)
    p.resizeBy(-40)
    pill.append(p)
    #pill[i].collisionBorder = "circle"

potion = []
for i in range(10): 
    b = Image("images//potion.png" , game)
    potion.append(b)


ppotion = Image("images/ppotion.png", game)
ppotion.y = -1500

acid = Image("images/acid.png", game)
acid.resizeBy(-25)
acid.y = 2000

effect = Animation("images/effect.png", 25, game, 960/5, 960/5, 2)
effect.resizeBy(50)
effect.visible = False

antidote = Image("images/antidote.png", game)

#HIM
himf = Animation( "./images/dudefoward.png" ,3 , game, 209/3 , 74 , - 7)
himb = Animation( "./images/dudeback.png" , 3 , game, 209/3 , 74 , - 7)
himl = Animation( "./images/dudeleft.png" , 3 , game, 209/3 , 75 , - 7)
himr = Animation( "./images/duderight.png", 3 , game , 209/3 , 75 , - 7)
him = Image("images//dudeidle.png",game)

dpsbar = Shape("bar" , game , himf.health , 10 , red)
himf.health = 100

hpbar = Shape("bar" , game , him.health , 10 , green)
him.health = 100

#MISC
progressbar = Shape("bar",game,200,20,magenta)
progressbar.moveTo(10,70)

progressbar2 = Shape("bar",game,200,20,magenta)
progressbar2.moveTo(10,70)


idlecursor = Image("images/idlecursor.png", game)
idlecursor.resizeBy(-95)

#SOUNDS 

gamemusic = Sound("./sounds/gamemusic.wav",0)
gamestart = Sound("./sounds/Gamestart.wav",1)
lose = Sound("./sounds/lose.wav",2)
win = Sound("./sounds/win.wav",3)

ga = Sound("./sounds/ghostattack.wav",4)
sa = Sound("./sounds/slimeattack.wav",5)
ed = Sound("./sounds/mobdeath.wav",6)

ss = Sound("./sounds/slash.wav",9)
sh = Sound("./sounds/slashhit.wav",8)
hu = Sound("./sounds/heal.wav",7) 

select = Sound("./sounds/select.wav",10)


#Story/Info

mouse.visible = False
while not game.over:
    game.processInput()
    idlecursor.draw()
    game.scrollBackground("up",0)
    him.draw()
    title.draw()
    start.draw()
    intro.draw()
    story.draw()
    howto.draw()
    tutorial.draw()
    storyscreen.draw()
    rb.draw()
    
    idlecursor.moveTo(mouse.x, mouse.y)

    if idlecursor.collidedWith(story, "rectangle"):
        story.setImage(story2.image)
        
    else:
        story.setImage(story1.image)
        

    
    if idlecursor.collidedWith(howto, "rectangle"): 
        howto.setImage(howto2.image)
        
    else:
        howto.setImage(howto1.image)
        

    if idlecursor.collidedWith(start, "rectangle"): 
        start.setImage(start2.image)
        
    else:
        start.setImage(start1.image)
        

    if idlecursor.collidedWith(rb , "rectangle"): 
        rb.setImage(rb2.image)
    else:
        rb.setImage(rb1.image)
        
        
    

    if idlecursor.collidedWith(story, "rectangle") and mouse.LeftClick:
        storyscreen.visible = True
        rb.visible = True
    
    if idlecursor.collidedWith(rb, "rectangle") and mouse.LeftClick:
        storyscreen.visible = False
        tutorial.visible = False
        rb.visible = False
            
    if idlecursor.collidedWith(howto, "rectangle") and mouse.LeftClick:
        tutorial.visible = True
        rb.visible = True

    '''    
    if keys.Pressed[K_SPACE]: 
        storyscreen.visible = False
        tutorial.visible = False
    '''
    if idlecursor.collidedWith(start, "rectangle") and mouse.LeftClick: #Starting the game
        game.over = True
        idlecursor.visible = False
        mouse.visible = True
    game.update(30)

#MAIN S1
game.over = False 
positionObjects_enemy(slime)
positionObjects_item(pill)
game.score = 0
while not game.over:
    game.scrollBackground("up",0)
    game.processInput()
    
    him.draw()
    him_update()
    power_update()
    gamemusic.play()
    
    progressbar.draw()
    progressbar.width = 200 - game.score * 4
    
    if keys.Pressed[K_SPACE] or keys.Pressed[K_f] or mouse.LeftClick:
        slash.draw("Once")
        slash.moveTo(him.x,him.y)
        
    for i in range(len(slime)):
        slime[i].move()
        
        if him.collidedWith(slime[i]):
            him.health -= 10
            game.score += 1
            slime[i].visible = False
            sa.play()
            hit.moveTo(him.x,him.y)
            hit.draw()

        if pill[i].y > game.height + 100 and pill[i].visible:
            game.score +=1
            pill[i].visible = False 


    if him.health < 0 or game.score == 50:
        game.over = True
    game.drawText("First Stage", 10, 10, sf)
    game.update(30)

#MAIN S2
game.over = False 
positionObjects_enemy(ghost)
positionObjects_item(pill)
game.score = 0

while not game.over:
    game.scrollBackground("up",0)
    game.processInput()
    
    him.draw()
    him_update()
    power_update()
    gamemusic.play()

    progressbar2.draw() 
    progressbar2.width = 200 - game.score * 4
    
    for i in range(len(ghost)):
        ghost[i].move()
        
        if him.collidedWith(ghost[i]):
            him.health -= 10
            game.score += 1 
            ghost[i].visible = False
            ga.play()
        if pill[i].y > game.height + 100 and pill[i].visible:
            game.score += 1
            pill[i].visible = False 

    if him.health < 0 or game.score == 50:
        game.over = True
    game.drawText("Second Stage", 10, 10, sf)        
    game.update(30)


#BOSS S3 
game.over = False

game.score = 0
positionObjects_item(pill)
positionObjects_item(potion)
positionObjects_enemy(slime)
positionObjects_enemy(ghost)
while not game.over:
    game.scrollBackground("up",0)
    game.processInput()
    him_update()
    power_update()
    
    acid.draw()
    ppotion.moveTowards(him, 4)
    effect.draw(False)
    boss.moveTowards(him, 3)
    #bossdpsbar.moveTo(boss.x - 55, boss.y + 70)
    #bossbar.moveTo(boss.x - 55, boss.y + 70)
    #bossbar.width = boss.health

    progressbar2.draw() 
    progressbar2.width = 200 - game.score * 4
    
    for i in range(len(slime)):
        slime[i].move()
        ghost[i].move()

        if him.collidedWith(slime[i]):
            him.health -= 5
            slime[i].visible = False
            hit.moveTo(him.x,him.y)
            hit.draw()
            sa.play()

        if him.collidedWith(ghost[i]):
            him.health -= 10
            ghost[i].visible = False
            ga.play()

                
        if pill[i].y > game.height + 100 and pill[i].visible:
            game.score += 1
            pill[i].visible = False
            
    for i in range(len(potion)):
        potion[i].move()
        
        if potion[i].collidedWith(him):
            effect.visibe = True
            effect.moveTo(potion[i].x, potion[i].y + 20)
            potion[i].visible = False
            him.health -= 20





    if ppotion.collidedWith(him):
        acid.moveTo(ppotion.x, ppotion.y)
        ppotion.visible = False
    if him.collidedWith(acid, "rectangle"):
        him.health -= 1
    if boss.collidedWith(him):
        him.health = 0
    if boss.health <= 0 or him.health <= 0:
        game.over = True
    if him.health < 0 or game.score == 50:
        game.over = True
    
    game.drawText("Final Stage", 10, 10, sf)
    game.update(30)
  

#END SCREENS
game.over = False


if him.health > 0:
    game.setMusic("sounds//win.wav")
else:
    game.setMusic("sounds//lose.wav")
game.playMusic()

while not game.over:
    game.processInput()
    end.draw()
    game.drawText("PRESS [Q] TO QUIT", game.width/3.5,game.height-100,f)
    if him.health > 0:
        you_win.draw()
        
    else:
        you_lose.draw()
        

    if keys.Pressed[K_q]:
        game.over = True
        game.quit()

    game.update(30)









