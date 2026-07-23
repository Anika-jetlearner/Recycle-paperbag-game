import pgzrun
import os
import random

WIDTH=800
HEIGHT=600
os.environ["SDL_VIDEO_CENTERED"]="1"
actors=["batteryimg", "bottleimg", "chipsimg", "plasticbag"]
level=3
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

    animate


def update():
    actorsmaking(level)




def draw():
    global myactors
    screen.blit("background",(0,0))
    for i in Actors:
        i.draw()


pgzrun.go()

