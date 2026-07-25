import pgzrun
import os
import random

WIDTH=800
HEIGHT=600
os.environ["SDL_VIDEO_CENTERED"]="1"
actors=["batteryimg", "bottleimg", "chipsimg", "plasticbag"]
level=1
game_over=False
animations=[]
speed=10
paperbag=Actor("paperimg")
myactors=["paperimg"]
Actors=[]

def actorsmaking(level):
    global myactors, Actors
    myactors=["paperimg"]
    for i in range(level):
        choice=random.choice(actors)
        myactors.append(choice)
    Actors=[]
    for i in range(len(myactors)):
        Actors.append(Actor(myactors[i]))
    gaps=WIDTH//(len(Actors)+1)
    random.shuffle(Actors)
    index=1
    for i in Actors:
        i.x=gaps*index
        index+=1

def ActorAnimate():
    global animations
    duration=speed-level
    for i in Actors:
        i.anchor=("center", "bottom")
        animation=animate(i,duration=duration,on_finished=game_end,y=600)
        animations.append(animation)

def stop_animations():
    for i in animations:
        if i.running:
            i.stop()

def on_mouse_down(pos):
    for i in Actors:
        if i.collidepoint(pos):
            if "paperimg" in i.image:
                level_end()
            else:
                game_end()

def game_end():
    global game_over
    game_over=True

def level_end():
    global level
    global Actors
    global animations
    global myactors
    
    if level==5:
        pass
    else:
        level +=1
        #print(level)
        Actors=[]
        animations=[]
        myactors=[]
        stop_animations()
        




def update():
    if len(Actors)==0:
        print(len(myactors))
        actorsmaking(level)
        ActorAnimate()




def draw():
    global myactors
    if game_over==False:
        screen.blit("background",(0,0))
        for i in Actors:
            i.draw()
    else:
        screen.blit("background",(0,0))
        screen.draw.text("Game over!", color="white", center=(400,300))

    


pgzrun.go()

