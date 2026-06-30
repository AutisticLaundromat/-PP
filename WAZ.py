gracz = None
obiekty = [] #Lista, w której będą przechowywane spadające obiekty

class Gracz:
    def __init__(self):
        self.x = 200
        self.y = 350
        self.szer = 30
        self.wys = 50
        self.speed = 5
        
    def ruch(self):
        if keyPressed:
            if keyCode == LEFT:
                self.x -= self.speed
            elif keyCode == RIGHT:
                self.x += self.speed

    def pokaz(self):
        fill(0, 255, 0)
        rect(self.x, self.y, self.szer, self.wys)
        
class SpadajacyObiekt:
    def __init__(self):
        # Losowe miejsce pojawienia się nad ekranem
        self.x = random(width)
        self.y = random(-400, 0)
        self.speed = random(2, 5)

    def aktualizuj(self):
        # Przesunięcie obiektu w dół
        self.y += self.speed

        # Jeśli obiekt spadnie poza ekran, wraca na górę w losowym miejscu
        if self.y > height:
            self.y = random(-100, 0)
            self.x = random(width)

    def pokaz(self):
        fill(255, 0, 0)
        ellipse(self.x, self.y, 20, 20)
def setup():
    global gracz

    size(400, 400)

    gracz = Gracz()

    # Tworzy 10 spadających obiektów
    for i in range(10):
        obiekty.append(SpadajacyObiekt())


def draw():
    background(220)

    gracz.ruch()
    gracz.pokaz()

    for o in obiekty:
        o.aktualizuj()
        o.pokaz()