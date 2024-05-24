def setup():

    size(1000,1000)


    background(255)
def draw():

    global bg

    if mousePressed==True:
       line (mouseX,mouseY,pmouseX,pmouseY) 
    fill(255)
    # левый верхний угол 250 150, размеры 100 на 50
    rect(250,30,100,50) # x от 250 до 250+100, y от 150 до 150 + 50  
    fill(255,0,0)
    rect(350,30,100,50)
    fill(0)
    rect(430,30,100,50)#black
    fill(12,7,216)
    rect(530,30,100,50)

    fill(155,0,0)
    textSize(20)

    rect(630,30,100,50)
    fill(200,0,0)
    rect(730,30,100,50)
    fill(0)
    text(u"больше",600+100/2,30+50/2)
    text(u"меньше",700+100/2,30+50/2)
    text(u"стирает",210+100/2,30+50/2)
    text(u"красн",310+100/2,30+50/2)
    fill(255)
    text(u"чёрный",400+100/2,30+50/2)
   
    text(u"синий",500+100/2,30+50/2)
    fill(150)
    rect(250,82,100,50)
    
    
    fill(100)
    rect(830,30,100,50)
    
    fill(0)
    text(u"круг",800+100/2,30+50/2)
    fill(52)
    rect(930,30,100,50)
    fill(255)
    text(u"квад",900+100/2,30+50/2)

def mouseClicked():
    
    global bg

    # если прямоугольная кнопка нажата
    if mouseX > 250 and mouseX < 350 and mouseY > 30 and mouseY < 90:
        background(255)
    if mouseX > 350 and mouseX < 390 and mouseY > 40 and mouseY < 100:   
        stroke(255,0,0)
    if mouseX > 400 and mouseX < 490 and mouseY > 30 and mouseY < 120:   
        stroke(0) 
    if mouseX > 490 and mouseX < 610 and mouseY > 30 and mouseY < 130:  
        stroke(0,0,255)

    if mouseX > 560 and mouseX < 710 and mouseY > 30 and mouseY < 150:  
        strokeWeight(5)

    if mouseX > 720 and mouseX < 870 and mouseY > 30 and mouseY < 170:  
        strokeWeight(1)
    if mouseX > 830 and mouseX < 930 and mouseY > 30 and mouseY < 90:  
        ellipse(500,500, 250, 250)
    if mouseX > 930 and mouseX < 1030 and mouseY > 30 and mouseY < 90:  
        rect(500,500, 250, 250)
    if mouseX > 250 and mouseX < 350 and mouseY > 82 and mouseY < 132:  
       triangle(500, 500, 450, 700, 550, 700)
