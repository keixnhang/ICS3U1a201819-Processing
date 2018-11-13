# Need to load image file into 
# the sketch's data folder.
# Top menu: Sketch -> Add File

def setup():
    global sat_img
    global back_img

    size(2144, 1424)
    sat_img = loadImage("e.png")
    back_img = loadImage("b.jpg")


def draw():
    background(back_img)
    image(sat_img, 0, 50, 50, 50)
