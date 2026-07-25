import pgzrun
import os
import random

WIDTH=800
HEIGHT=600
score=0
x=400
#y=50
basket=Actor("basket")
basket.pos=400,500
apple=Actor("apple")
apple.pos=x,50
os.environ["SDL_VIDEO_CENTERED"]="1"




def draw():
    screen.fill("light blue")
    basket.draw()
    apple.draw()
    screen.draw.text("Score: " + str(score), color="black", topleft=(10,10))

def update():
    global x
    global score
    if keyboard.left:
        basket.x -=2.7
    if keyboard.right:
        basket.x +=2.7
    apple.y+=3

    if apple.y ==602:
        x=random.randint(50,750)
        apple.pos=x,50
        
    if apple.colliderect(basket):
        score+=1
        x=random.randint(50,750)
        apple.pos=x,50


  



pgzrun.go()
