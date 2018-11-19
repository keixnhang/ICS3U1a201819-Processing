x = 0
y = 20
p = 600
q = 600

text_size = 40

rotation = 0

rotation_speed = 2

text_size_speed = 1

animate = False


def setup():
    global sat_img
    global back_img
    size(1400,932)
    back_img = loadImage("beach.jpg")
    sat_img = loadImage("1.png")
    
def draw():
    global x
    global p
    global q
    global text_size
    global rotation
    global rotation_speed
    global text_size_speed
    
    x +=3
    if x >=1200:
        x = 0
    background(back_img)
    
    noStroke()
    
    triangle(p,2*p, 300, 400, 600, 600)
    if keyPressed:
        if key == 'a':
            p += 20
        if p>=600:
            p = 0
    rect(y,30,160,160,80,80,40,40)
    
    quad(19, 30, 29, 56, 62, 70, 30, 60)
    
    
    
    
    if animate:
        rotation_speed += 0.01
        text_size_speed += 0.3
        text_size += text_size_speed
        rotation += rotation_speed
        
    textAlign(CENTER, CENTER)
    
    translate(width/2, height/2)
    
    rotate(rotation)
    
    textSize(text_size)
    
    fill(200, 50, 225, 225-text_size/2)
    
    text("STICH!!!", 0, 0)
    '''
    def mouseClicked():
        global y 
        y += 100
        if y >= 1200:
            y = 0
    '''
    image(sat_img, 0, 0, 243, 227)
    
    noStroke()
    fill(255, 102, 178)
    ellipse(q, height/2, 50, 50)
    ellipse(q+30, height/2, 50, 50)
    ellipse(q+10, height/2-20, 50, 50)
    
    if animate:
        rotation_speed += 0.01
        text_size_speed +=0.3
        text_size += text_size_speed
        rotation += rotation_speed
def mouseClicked():
    global q
    q += 20
    if q > 640:
        q = 0
        
        rect(y, 20, 150, 150, 80, 80, 20, 20)
