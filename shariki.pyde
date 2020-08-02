x = 100
fon = 0
cvet = color(random(0,255),random(0,255),random(0,255))
ggvp = 10

def setup():
    size(1000,1000)

def draw():
    global  fon
    global  ggvp
    
    global x
    strokeWeight(ggvp)
    fill(random(0,255),random(0,255),random(0,255))
    stroke(random(0,255),random(0,255),random(0,255))
    ellipse(x * 1.1,200,50,50)
    strokeWeight(ggvp)
    stroke(random(0,255),random(0,255),random(0,255))
    ellipse(x,100,50,50)
    strokeWeight(ggvp)
    stroke(random(0,255),random(0,255),random(0,255))
    ellipse(x * 1.2,300,50,50)
    strokeWeight(ggvp)
    stroke(random(0,255),random(0,255),random(0,255))
    ellipse(x * 1.3,400,50,50)
    strokeWeight(ggvp)
    stroke(random(0,255),random(0,255),random(0,255))
    ellipse(x * 1.4,500,50,50)
    strokeWeight(ggvp)
    stroke(random(0,255),random(0,255),random(0,255))
    ellipse(x * 1.5,600,50,50)
    strokeWeight(ggvp)
    stroke(random(0,255),random(0,255),random(0,255))
    ellipse(x * 1.6,700,50,50)
    strokeWeight(ggvp)
    stroke(random(0,255),random(0,255),random(0,255))
    ellipse(x * 1.7,800,50,50)
    strokeWeight(ggvp)
    stroke(random(0,255),random(0,255),random(0,255))
    ellipse(x * 1.8,900,50,50)
    x = x + 1
    fon = fon + 1
    ggvp = ggvp + 0.1
    if (fon == 256):
        fon = 0
