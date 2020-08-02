color_KYKY = color(random(0,255),random(0,255),random(0,255))
 
def setup():
    size(1000,1000)
    noLoop()

def draw():
 translate(500,500)

 strokeWeight(15)
 stroke(50,200,0)
 line(0,0,0,500)

#Центр цветка
 fill(0)
 stroke(0)
 ellipse(0,0,250,250)

 strokeWeight(5)
 fill(255,255,0)
 stroke(150,150,0)

#Лепестки
 for i in range(1,16,1):
    color_KYKY = color(random(0,255),random(0,255),random(0,255))
    fill(color_KYKY)    
    rotate(radians(24))
    ellipse(0,-200,100,250) 
    
#Цифры
 for i in range(1,16,1): 
    fill(random(0,255),random(0,255),random(0,255))     
    rotate(radians(24))
    textSize(i+30)
    text(i,-20,-200) 
    
def mouseClicked():
    global color_KYKY
    color_KYKY = color(random(0,255),random(0,255),random(0,255))
    redraw()

    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
    
