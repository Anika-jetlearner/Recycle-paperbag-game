import pgzrun
import os
import random
WIDTH=800
HEIGHT=600
x=400
game_over=False
winner=False
score=0

os.environ["SDL_VIDEO_CENTERED"]="1"
bulletcreated=False
alienmoveleft=[True,True,True,True,True,True,True]

player=Actor("spacecraft")
alien=Actor("alienspacecraft")
alien1=Actor("alienspacecraft1")
alien2=Actor("alienspacecraft2")
alien3=Actor("alienspacecraft3")
alien4=Actor("alienspacecraft4")
alien5=Actor("alienspacecraft5")
alien6=Actor("alienspacecraft6")
alien.pos=x,50
alien1.pos=490,50
alien2.pos=580,50
alien3.pos=670,50
alien4.pos=310,50
alien5.pos=220,50
alien6.pos=130,50
alienships=[]

#Actor("alienspacecraft")
     #alienships.append(Actor("alienspacecraft"))
alienships=[alien,alien1,alien2,alien3,alien4,alien5,alien6]

player.pos=400,540
bullet=Actor("bullet")
bullet.pos=player.x,player.y-70
def draw():
    global bulletcreated,winner,game_over,alienships
    screen.fill("dark blue")
    player.draw()
    for i in alienships:
        i.draw()
    
    if bulletcreated==True:
        bullet.draw()
        bullet.top-=15
    if game_over==True:
        screen.draw.text("GAME OVER", (350,300), color="black")
        screen.draw.text("Your score was {}".format(score),(340,400),color="black")
        alienships=[]
    if winner==True:
        
        screen.draw.text("YOU WON", (350,300), color="black")
        screen.draw.text("Your score was {}".format(score),(340,400),color="black")
         
   

def update():
    global bulletcreated,game_over,score,alienmoveleft,winner,alienships
    
    if keyboard.right:
        player.x+=2.5
    if keyboard.left:
        player.x-=2.5
    
    if keyboard.space:
        bulletcreated=True

    if len(alienships)==0 and score>1:
        winner=True
                                 
                                                    
    
        
    
    if bullet.y<0:
        bulletcreated=False
        bullet.pos=player.x,player.y-70

    for i in range(len(alienships)):
        if alienmoveleft[i]==True:
            alienships[i].x-=5
        if alienmoveleft[i]==False:
             alienships[i].x+=5
        if alienships[i].x<0:
            alienships[i].y+=150
            alienmoveleft[i]=False
        if alienships[i].y>500:
                game_over=True
                
                break
              
        if alienships[i].x>800:
                alienships[i].x-=5
                alienships[i].y+=150
                alienmoveleft[i]=True
        
        
        if bullet.colliderect(alienships[i]):
                alienships.remove(alienships[i])
                alienmoveleft.remove(alienmoveleft[i])
                score+=1
                break
                
                print(len(alienships))
                
        
                
                  
                   
   
pgzrun.go()