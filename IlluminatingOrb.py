# import essentials
from vpython import *
import time

# define parameters
red=1
green=1
blue=0
deltar=0.01
deltag=-0.01
deltab=0.01
redapply=0
greenapply=0
blueapply=0
xshift=1
orb_radius=2
width=0.5

# vpython canvas
canvas(width=1320,height=680)

# create bars
rod1=box(
    size=vector(width,red,width),
    pos=vector(-3*xshift,0,0),
    color=color.red
)
rod2=box(
    size=vector(width,green,width),
    pos=vector(-2*xshift,0,0),
    color=color.green
)
rod3=box(
    size=vector(width,blue,width),
    pos=vector(-xshift,0,0),
    color=color.blue
)

attach_light(rod1)
attach_light(rod2)
attach_light(rod3)

# create orb object
orb=sphere(radius=orb_radius,pos=vector(orb_radius,0,0))
attach_light(orb)

redlabel=label(
    pos=vector(-3*xshift,-xshift,0),
    color=color.red,
    text='Red\n'+str(int(redapply*255)),
    font='serif',
    border=10
)
greenlabel=label(
    pos=vector(-2*xshift,-xshift,0),
    color=color.green,
    text='Green\n'+str(int(greenapply*255)),
    font='serif',
    border=10
)
bluelabel=label(
    pos=vector(-xshift,-xshift,0),
    color=color.blue,
    text='Blue\n'+str(int(blueapply*255)),
    font='serif',
    border=10
)
whitelabel=label(
    pos=vector(2*xshift,2*xshift,0),
    color=color.white,
    text='R+G+B: '+str(int(redapply+greenapply+blueapply)*255),
    font='sans',
    border=15,
    xoffset=-60,
    yoffset=50,
    height=16
)

# program loop
while True:
    rate(50)

    red+=deltar
    blue+=deltab
    green+=deltag

    if red>=1:
        redapply=1
    else:
        redapply=red
    if green>=1:
        greenapply=1
    else:
        greenapply=green
    if blue>=1:
        blueapply=1
    else:
        blueapply=blue

    orb.color=vector(redapply,greenapply,blueapply)

    if red>=1.5 or red<=0:
        deltar=-deltar
    if blue>=1.5 or blue<=0:
        deltab=-deltab
    if green>=1.5 or green<=0:
        deltag=-deltag
    
    rod1.size=vector(width,2*redapply,width)
    rod2.size=vector(width,2*greenapply,width)
    rod3.size=vector(width,2*blueapply,width)

    redlabel.text='Red\n'+str(int(redapply*255))
    bluelabel.text='Blue\n'+str(int(blueapply*255))
    greenlabel.text='Green\n'+str(int(greenapply*255))
    whitelabel.text='R+G+B: '+str(int(redapply+greenapply+blueapply)*255)