import pgzrun
import pygame
import os
import random
WIDTH=800
HEIGHT=600
y=random.randint(0,600)
speed=1
shark=Actor("shark")
seahorse=Actor("seahorse")
octopus=Actor("octopus")
fish=Actor("fishnotplayer")
fish.pos=800,y
jellyfish=Actor("jellyfish")
seaturtle=Actor("seaturtle")
dolphin=Actor("dolphin")
#starfish=Actor("starfish")
speedlist=[1,0.5,0.5,2,2,1,2]
actorpos=[]
levelactors=[fish,jellyfish,seaturtle,seahorse,octopus,shark,dolphin]
scorelist=[5,7,10,14,20,50,35]

def scale_player():
    global player
    player._surf = pygame.transform.scale(player._surf, (playersizeL,playersizeH))



playersizeL=40
playersizeH=40
game_over=False
playerpointingright=0
x=0

score=6
os.environ["SDL_VIDEO_CENTERED"]="1"


player=Actor("playerfish")

player.pos=400,100
scale_player()

def create_actors():
    global actorpos
    for i in range(4):
        y=random.randint(20,580)
        if i==0:
            actorpos.append(y)
            levelactors[i].pos=0,y
        #while y-actorpos[i-1]<75:
        y=random.randint(20,580)

        actorpos.append(y)
        levelactors[i].pos=0,y
            
        
           


create_actors()



def draw():
    global score,levelactors
    screen.blit("bg",(0,0))
    player.draw()
    if score<21 and game_over==False:
        for i in range(4):    
            levelactors[i].draw()
            screen.draw.text(str(scorelist[i]), (levelactors[i].x,levelactors[i].y),color="black")
    else:
        for i in range(len(levelactors)):
            levelactors[i].draw()
            screen.draw.text(str(scorelist[i]), (levelactors[i].x,levelactors[i].y),color="black")


    if game_over==True:
        screen.draw.text("GAME OVER", (400,300), color="black")
        levelactors=[]
    
  

    screen.draw.text(str(score),(player.x,player.y),color="black")
    

        




def update():
    global playersizeL,playersizeH,levelactors,playerpointingright,score,game_over,speedlist
    if keyboard.up:
        player.y -=2
    if keyboard.down:
        player.y+=2
    if keyboard.left:
        player.x-=2
        if playerpointingright==1:
            player._surf=pygame.transform.flip(player._surf,1,0)
            playerpointingright=0

    if keyboard.right:
        player.x+=2
        if playerpointingright==0:
            player._surf=pygame.transform.flip(player._surf,1,0)
            playerpointingright=1

    if keyboard.space:
        scale_player()
    
    for i in range(len(levelactors)):
        levelactors[i].right +=speedlist[i]
    

    for i in range(len(levelactors)):
        if player.colliderect(levelactors[i]):
            if int(scorelist[i])<score:
                if levelactors[i]==fish:
                    score+=2
                elif levelactors[i]==jellyfish:
                    score+=3
                elif levelactors[i] ==seaturtle:
                    score+=4
                elif levelactors[i]==dolphin:
                    score+=5
                elif levelactors[i]==seahorse:
                    score+=6
                elif levelactors[i]==octopus:
                    score+=7
                elif levelactors[i]==shark:
                    score+=8
                #elif levelactors[i]==starfish:
                #    score+=6
                scorelist.remove(scorelist[i])
                levelactors.remove(levelactors[i])
                speedlist.remove(speedlist[i])
                playersizeL+=10
                playersizeH+=10
                
        
                scale_player()
                break
            elif score<int(scorelist[i]):
                print ('Game over is true')
                game_over=True
                
        if levelactors[i].x>800:
            levelactors[i].x=0
            y=random.randint(20,580)
            levelactors[i].pos=0,y

           
            

           
    










    #Actor._surf = pygame.transform.scale(Actor._surf, (width, height))



pgzrun.go()

    