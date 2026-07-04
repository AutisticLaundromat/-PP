gracz = None
obiekty_do_zbierania = []
obiekty_do_unikania = []
klawisze = {LEFT: False, RIGHT: False}

punkty = 0
zycia = 3

class Gracz:
    def __init__(self):
        self.szer = 30
        self.wys = 50
        self.x = 200 - self.szer / 2
        self.y = 350
        self.speed = 5
        
    def ruch(self):
        if klawisze[LEFT]:
            self.x -= self.speed
        if klawisze[RIGHT]:
            self.x += self.speed
            
        self.x = constrain(self.x, 0, width - self.szer)

    def pokaz(self):
        fill(0, 255, 0)
        rect(self.x, self.y, self.szer, self.wys)
        
    def sprawdz_kolizje(self, obiekt):
        promien = obiekt.rozmiar / 2
        test_x = obiekt.x
        test_y = obiekt.y

        if obiekt.x < self.x:
            test_x = self.x
        elif obiekt.x > self.x + self.szer:
            test_x = self.x + self.szer

        if obiekt.y < self.y:
            test_y = self.y
        elif obiekt.y > self.y + self.wys:
            test_y = self.y + self.wys

        dystans_x = obiekt.x - test_x
        dystans_y = obiekt.y - test_y
        dystans = sqrt((dystans_x ** 2) + (dystans_y ** 2))

        return dystans <= promien

class ObiektDoZbierania:
    def __init__(self):
        self.rozmiar = 20
        self.resetuj()

    def resetuj(self):
        self.x = random(self.rozmiar, width - self.rozmiar)
        self.y = random(-400, -50)
        self.speed = random(2, 5)

    def aktualizuj(self):
        self.y += self.speed
        if self.y > height + self.rozmiar:
            self.resetuj()

    def pokaz(self):
        fill(255, 255, 0) # Żółty dla obiektów do zbierania
        ellipse(self.x, self.y, self.rozmiar, self.rozmiar)

class ObiektDoUnikania(ObiektDoZbierania):
    def pokaz(self):
        # Nadpisanie metody pokaz() dla zmiany wyglądu obiektu
        fill(255, 0, 0) # Czerwony dla przeszkód
        ellipse(self.x, self.y, self.rozmiar, self.rozmiar)

def setup():
    global gracz
    size(400, 400)
    gracz = Gracz()

    for i in range(7):
        obiekty_do_zbierania.append(ObiektDoZbierania())
        
    for i in range(5):
        obiekty_do_unikania.append(ObiektDoUnikania())

def draw():
    global punkty, zycia
    background(0, 218, 255)

    # Rysowanie interfejsu (HUD)
    fill(0)
    textSize(16)
    text("Punkty: " + str(punkty), 10, 20)
    text(u"Życia: " + str(zycia), 10, 40)

    if zycia <= 0:
        textAlign(CENTER)
        textSize(32)
        text("KONIEC GRY", width/2, height/2)
        return # Zatrzymanie logiki gry

    gracz.ruch()
    gracz.pokaz()

    # Logika obiektów do zbierania
    for oz in obiekty_do_zbierania:
        oz.aktualizuj()
        oz.pokaz()
        if gracz.sprawdz_kolizje(oz):
            punkty += 1
            oz.resetuj()

    # Logika obiektów do unikania
    for ou in obiekty_do_unikania:
        ou.aktualizuj()
        ou.pokaz()
        if gracz.sprawdz_kolizje(ou):
            zycia -= 1
            ou.resetuj()

def keyPressed():
    if keyCode in klawisze:
        klawisze[keyCode] = True

def keyReleased():
    if keyCode in klawisze:
        klawisze[keyCode] = False
