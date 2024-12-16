import pgzrun

#settijng output window's width and height of screen

WIDTH=500
HEIGHT=600

#title of the window
TITLE= 'First shape project'

#adding or putting the things on the screen
def draw():
    corner1 = (0,0)
    corner2 = (30,30)
    rectangle = rect(corner1,corner2)
    #adding the created rectangle on screen
    screen.draw.filled_rect(rectangle,(0,255,0))#0,255,0 is rgb value of green color
    #drawing a line
    #start point and 
