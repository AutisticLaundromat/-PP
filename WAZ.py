#global variables for free use więc nie musisz pisać liczbowo tylko piszesz słówka
x = 200
y = 200
speed = 5

#setup gry całego ekranu mam nadzieje że wiecie o co chodzi to takie intro nie wiem jak to wytłumaczyć
def setup():
    size(400, 400)
    
def draw():
    global x, y

    background(220)
    
#tu ruch
    if keyPressed:
        if keyCode == LEFT:
            x -= speed
        if keyCode == RIGHT:
            x += speed
        if keyCode == UP:
            y -= speed
        if keyCode == DOWN:
            y += speed

    rect(x, y, 50, 50)