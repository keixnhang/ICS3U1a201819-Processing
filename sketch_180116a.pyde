class Enemy:
    def __init__(self):
        self.pos = PVector(random(0,width),-40)
        self.type = int(random(2))
        self.speed1 = PVector(0,random(3,6.5))
        self.speed2 = PVector(0,random(1,5))
        self.energy = PVector(5, 50)
        self.height = 50
        self.width = 30
        if self.type == 1:
            self.width = 30
            self.height = 30
            self.energy.x = 5
        else:
            self.width = 50
            self.height = 50
            self.energy.y = 50
        
        
    def draw(self):
        stroke(0)
        fill(125,0,0)
        ellipse(self.pos.x,self.pos.y,self.width,self.height)
    
    def update(self):
        self.pos.add(self.speed2)
        
enemies = []        
                    
    




x=350
score=0
energy=40



value=0



y2=610

y=690


speed=PVector(5,5)
speed1=PVector((random(1,5)),(random(3,6.5)))
speed2=PVector((random(1,5)),(random(1,5)))
plane = PVector(x-15,y-40)

y3=plane.y-40
y4=plane.y-120
y5=plane.y-200
y6=plane.y-280
y7=plane.y-360
y8=plane.y-440
y9=plane.y-520
y10=plane.y-600

x2=x3=x4=x5=x6=x7=x8=x9=x10=plane.x+20.5

p=0
img=0
img2=0
img3=0
p2=-700
screen = 'menu'
def setup():
    global img2
    global img
    global img3
    size(700,700)
    img = loadImage('background2.jpg')
    img.resize(700,700)
    
    img2 = loadImage('background1.jpg')
    img2.resize(700,700)
    
    img3 = loadImage('zhengban.png')
    img3.resize(50,50)
    
    for _ in range(10):
        enemies.append(Enemy())
            

def draw():
    global screen
    if screen == 'menu':
        
        background(255)
        fill(0)
        textAlign(CENTER)
        textSize(50)
        text("play",100,300)
        textSize(20)
        textAlign(CENTER)
        text('Press [p] for play',130,340)
        textSize(50) 
        textAlign(CENTER)
        text("instruction",175,500)
        textSize(20)
        textAlign(CENTER)
        text('Press [i] for instruction',155,540)
        
        textSize(100)
        textAlign(CENTER)
        text('Plane Wars',width/2, 150)
        if keyPressed:
            if key == 'p':
                screen = 'play'
        if keyPressed:
            if key == 'i':
                screen = "instruction"
    elif screen == "play":
        global img
        global p
        global p2
        global img2
        image(img,0,p)
        image(img2,0,p2)
        p+=1
        p2+=1
        if p >= 700:
            p=0
       
        if p2 >= 0:
            p2=-700
            
        for enemy in enemies:
            enemy.update()
            enemy.draw()
        
            a=x2-enemy.pos.x
            a2=x3-enemy.pos.x
            a3=x4-enemy.pos.x
            a4=x5-enemy.pos.x
            a5=x6-enemy.pos.x
            a6=x7-enemy.pos.x
            a7=x8-enemy.pos.x
            a8=x9-enemy.pos.x
            a9=x10-enemy.pos.x
            b=y2-enemy.pos.y
            b2=y3-enemy.pos.y
            b3=y4-enemy.pos.y
            b4=y5-enemy.pos.y
            b5=y6-enemy.pos.y
            b6=y7-enemy.pos.y
            b7=y8-enemy.pos.y
            b8=y9-enemy.pos.y
            b9=y10-enemy.pos.y
            distance9= sqrt(a**2 + b**2)
            distance1= sqrt(a2**2 + b2**2)
            distance2= sqrt(a3**2 + b3**2)
            distance3= sqrt(a4**2 + b4**2)
            distance4= sqrt(a5**2 + b5**2)
            distance5= sqrt(a6**2 + b6**2)
            distance6= sqrt(a7**2 + b7**2)
            distance7= sqrt(a8**2 + b8**2)
            distance8= sqrt(a9**2 + b9**2)
            
            if keyPressed is True and keyCode==16:
                score=0
                enemy.pos.y = -40
                enemy.pos.x = random(0,width)
                speed.y=5
           
            
            if enemy.pos.y > 740:
                enemies.remove(enemy)
                enemies.append(Enemy())
                
            plane2 = PVector(plane.x+25,plane.y-25)
            
            distance = PVector.sub(enemy.pos,plane2)    
        
            if enemy.type == 1:
                textSize(10)
                text(enemy.energy.x,enemy.pos.x - 10,enemy.pos.y + 30)
                if distance.mag() <= 10 + 15:
                    fill(70)
                    textSize(60)
                    text("You lose!",width/2-100,height/2)
                    speed1.y=0
                    speed.y=0
                    speed1.x=0
                    enemy.speed1.y = 0
                    enemy.speed2.y = 0
                
                if distance9 <= 15:
                    enemy.energy.x -= 1
                    if enemy.energy.x == 0:
                        enemies.append(Enemy())
                        enemies.remove(enemy)
                        score +=1
                if distance2 <= 15:
                    enemy.energy.x -= 1
                    if enemy.energy.x == 0:
                        enemies.append(Enemy())
                        enemies.remove(enemy)
                        score +=1
                if distance3 <= 15:
                    enemy.energy.x -= 1
                    if enemy.energy.x == 0:
                        enemies.append(Enemy())
                        enemies.remove(enemy)
                        score +=1
                if distance4 <= 15:
                    enemy.energy.x -= 1
                    if enemy.energy.x == 0:
                        enemies.append(Enemy())
                        enemies.remove(enemy)
                        score +=1
                if distance5 <= 15:
                    enemy.energy.x -= 1
                    if enemy.energy.x == 0:
                        enemies.append(Enemy())
                        enemies.remove(enemy)
                        score +=1
                if distance6 <= 15:
                    enemy.energy.x -= 1
                    if enemy.energy.x == 0:
                        enemies.append(Enemy())
                        enemies.remove(enemy)
                        score +=1
                if distance7 <= 15:
                    enemy.energy.x -= 1
                    if enemy.energy.x == 0:
                        enemies.append(Enemy())
                        enemies.remove(enemy)
                        score +=1
                if distance8 <= 15:
                    enemy.energy.x -= 1
                    if enemy.energy.x == 0:
                        enemies.append(Enemy())
                        enemies.remove(enemy)
                        score +=1
               
                    
            else:
                textSize(10)
                text(enemy.energy.y,enemy.pos.x - 15,enemy.pos.y + 40)
                if distance.mag() <= 10 + 25:
                    fill(70)
                    textSize(60)
                    text("You lose!",width/2-100,height/2)
                    speed1.y=0
                    speed.y=0
                    speed1.x=0
                    enemy.speed1.y = 0
                    enemy.speed2.y = 0
                
                if distance9 <= 25:
                    enemy.energy.y -= 1
                    if enemy.energy.y == 0:
                        enemies.append(Enemy())
                        enemies.remove(enemy)
                        score +=3
                if distance2 <= 25:
                    enemy.energy.y -= 1
                    if enemy.energy.y == 0:
                        enemies.append(Enemy())
                        enemies.remove(enemy)
                        score +=3
                if distance3 <= 25:
                    enemy.energy.y -= 1
                    if enemy.energy.y == 0:
                        enemies.append(Enemy())
                        enemies.remove(enemy)
                        score +=3
                if distance4 <= 25:
                    enemy.energy.y -= 1
                    if enemy.energy.y == 0:
                        enemies.append(Enemy())
                        enemies.remove(enemy)
                        score +=3
                if distance5 <= 25:
                    enemy.energy.y -= 1
                    if enemy.energy.y == 0:
                        enemies.append(Enemy())
                        enemies.remove(enemy)
                        score +=3
                if distance6 <= 25:
                    enemy.energy.y -= 1
                    if enemy.energy.y == 0:
                        enemies.append(Enemy())
                        enemies.remove(enemy)
                        score +=3
                if distance7 <= 25:
                    enemy.energy.y -= 1
                    if enemy.energy.y == 0:
                        enemies.append(Enemy())
                        enemies.remove(enemy)
                        score +=3
                if distance8 <= 25:
                    enemy.energy.y -= 1
                    if enemy.energy.y == 0:
                        enemies.append(Enemy())
                        enemies.remove(enemy)
                        score +=3
                    
        global value
        global x
        global x2
        global x3
        global x4
        global x5
        global x6
        global x7
        global x8
        global x9
        global x10

        global y
        global y2
        global y3
        global y4
        global y5
        global y6
        global y7
        global y8
        global y9
        global y10
        global speed
        global speed1
        global ball
        global score
        global energy
        fill(value)
    
        image(img3,plane.x,plane.y)
        print keyCode
    
        #draw the bullets
        y2-=speed.y
        fill(255)
        rect(x2,y2,3,35) 
   
    
        y3-=speed.y
        rect(x3,y3,3,35) 
    
    
        y4-=speed.y
        rect(x4,y4,3,35) 

        y5-=speed.y
        rect(x5,y5,3,35) 

        y6-=speed.y
        rect(x6,y6,3,35) 
        
        y7-=speed.y
        rect(x7,y7,3,35) 
    
        y8-=speed.y
        rect(x8,y8,3,35) 
    
        y9-=speed.y
        rect(x9,y9,3,35) 
    
        y10-=speed.y
        rect(x10,y10,3,35) 

        #the rule of bullets, if they get out of the screen, it will disappear and go back to the original point.
        if y2<= 0:
            y2=plane.y-40  
            x2=plane.x+20.5
        if y3 <= 0:
            y3=plane.y-40  
            x3=plane.x+20.5
        if y4 <= 0:
            y4=plane.y-40  
            x4=plane.x+20.5
        if y5 <= 0:
            y5=plane.y-40  
            x5=plane.x+20.5
        if y6 <= 0:
            y6=plane.y-40  
            x6=plane.x+20.5
        if y7 <= 0:
            y7=plane.y-40  
            x7=plane.x+20.5
        if y8 <= 0:
            y8=plane.y-40   
            x8=plane.x+20.5
        if y9 <= 0:
            y9=plane.y-40  
            x9=plane.x+20.5
        if y10 <= 0:
            y10=plane.y-40  
            x10=plane.x+20.5
        
   
        #your plane's movement.
        if keyPressed is True and keyCode == 37:
            plane.x-=3
        
        if keyPressed is True and keyCode == 39:
            plane.x+=3


  
        
            
        
        # score 
        fill(255)   
        textSize(40)
        text(score,50,70)    
        
        
    elif screen == 'instruction':
        
        if keyPressed:
            if key == 'm':
                screen = "menu"
        background(255)
        fill(0)
        textSize(70)
        text('instruction', width/4, 150)
        textAlign(LEFT)
        textSize(20)
        text('''   
                Welcome to Plane War.
                In the game, use keyboard tocontrol your plane to move.
                Your plane will launches guided missile to destroy
                enemoy planes.
                Once you destroied a enemoy plane, you get one score. 
                In this game,
                there is no win, try to elude the enemoy plane,
                if they touch you once, the game is over.
                Try to surpass your score.
                Have fun!''', width/50,200) 
        
        textSize(15)
        text('Press [m] for menu',width/2.5, 600)
        
            