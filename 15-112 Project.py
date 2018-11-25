import pygame

def blit_text(surface, text, pos, font, color=pygame.Color('white')):

    words = [word.split(' ') for word in text.splitlines()]
    space = font.size(' ')[0]
    max_width, max_height = surface.get_size()
    x, y = pos
    for line in words:
        for word in line:
            word_surface = font.render(word, 0, color)
            word_width, word_height = word_surface.get_size()
            if x + word_width >= max_width:
                x = pos[0]
                y += word_height
            surface.blit(word_surface, (x, y))
            x += word_width + space
        x = pos[0]
        y += word_height

class mainScreen():

    def __init__(self):

        self.running = True
        self.clock = pygame.time.Clock()
        self.screen = pygame.display.set_mode((900, 540))
        self.background = pygame.image.load("Main Menu Picture.png")
        self.background = pygame.transform.scale(self.background, (900, 540))

        while self.running==True:

            self.screen.blit(self.background, [0, 0])
            pygame.display.set_caption("Main Menu")

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            self.startFont = pygame.font.SysFont("Comic Sans MS", 30)
            pygame.draw.rect(self.screen, (255, 255, 255), (507, 377, 106, 56))
            pygame.draw.rect(self.screen, (143, 11, 15), (510, 380, 100, 50))
            self.textsurface = self.startFont.render("Start", True,(255, 255, 255))
            self.screen.blit(self.textsurface, (520, 382))

            self.instructionsFont = pygame.font.SysFont("Comic Sans MS", 30)
            pygame.draw.rect(self.screen, (255, 255, 255), (677, 377, 186, 56))
            pygame.draw.rect(self.screen, (143, 11, 15), (680, 380, 180, 50))
            self.textsurface = self.instructionsFont.render("Instructions",True,(255, 255, 255))
            self.screen.blit(self.textsurface, (684, 382))

            pygame.draw.rect(self.screen, (255, 255, 255), (677, 0, 56, 56))
            pygame.draw.rect(self.screen, (143, 11, 15), (680, 3, 50, 50))
            self.settings=pygame.image.load("settings-icon.png")
            self.settings=pygame.transform.scale(self.settings,[40,40])
            self.screen.blit(self.settings,(684,8))

            if 507 <= pygame.mouse.get_pos()[0] <= 613 and 377 <= pygame.mouse.get_pos()[1] <= 433 and pygame.MOUSEBUTTONDOWN:

                pygame.draw.rect(self.screen, (255, 255, 255),(507, 377, 106, 56))
                pygame.draw.rect(self.screen, (72, 11, 15),(510, 380, 100, 50))
                self.textsurface = self.startFont.render("Start", True,(255, 255, 255))
                self.screen.blit(self.textsurface,(520, 382))

            elif 677 <= pygame.mouse.get_pos()[0] <= 863 and 377 <= pygame.mouse.get_pos()[1] <= 433 and pygame.MOUSEBUTTONDOWN:

                pygame.draw.rect(self.screen, (255, 255, 255),(677, 377, 186, 56))
                pygame.draw.rect(self.screen, (72, 11, 15),(680, 380, 180, 50))
                self.textsurface = self.instructionsFont.render("Instructions",True,(255, 255, 255))
                self.screen.blit(self.textsurface, (684, 382))

            elif 677 <= pygame.mouse.get_pos()[0] <= 733 and 0 <= pygame.mouse.get_pos()[1] <= 56 and pygame.MOUSEBUTTONDOWN:

                pygame.draw.rect(self.screen, (255, 255, 255),(677, 0, 56, 56))
                pygame.draw.rect(self.screen, (72, 11, 15), (680, 3, 50, 50))
                self.settings = pygame.transform.scale(self.settings, [40, 40])
                self.screen.blit(self.settings, (684, 8))

            if 507 <= pygame.mouse.get_pos()[0] <= 613 and 377 <= pygame.mouse.get_pos()[1] <= 433 and pygame.mouse.get_pressed()[0]:

                pygame.mixer.Sound.play(sound)
                Start()

            elif 677<=pygame.mouse.get_pos()[0]<=863 and 377<=pygame.mouse.get_pos()[1]<=433 and pygame.mouse.get_pressed()[0]:

                pygame.mixer.Sound.play(sound)
                Instructions()

            elif 677 <= pygame.mouse.get_pos()[0] <= 733 and 0 <=pygame.mouse.get_pos()[1] <= 56 and pygame.mouse.get_pressed()[0]:

                pygame.mixer.Sound.play(sound)
                Settings()

            pygame.display.flip()
            self.clock.tick(30)

def Start():

    clock = pygame.time.Clock()
    running=True
    screen2 = pygame.display.set_mode((900, 540))

    while running == True:

        pygame.display.set_caption("Tarneeb")
        background = pygame.image.load("Game Picture.jpg")
        background = pygame.transform.scale(background, (900, 540))
        screen2.blit(background, [0, 0])

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        instructionsFont = pygame.font.SysFont("Comic Sans MS", 30)
        pygame.draw.rect(screen2, (255, 255, 255), (0,0, 186, 56))
        pygame.draw.rect(screen2, (143, 11, 15), (3,3, 180, 50))
        textsurface = instructionsFont.render("Instructions", True,(255, 255, 255))
        screen2.blit(textsurface, (7, 5))

        settingsFont = pygame.font.SysFont("Comic Sans MS", 30)
        pygame.draw.rect(screen2, (255, 255, 255), (407,0, 136, 56))
        pygame.draw.rect(screen2, (143, 11, 15), (410,3, 130, 50))
        textsurface = settingsFont.render("Settings", True,(255, 255, 255))
        screen2.blit(textsurface, (414, 5))

        quitFont = pygame.font.SysFont("Comic Sans MS", 30)
        pygame.draw.rect(screen2, (255, 255, 255), (822, 0, 78, 56))
        pygame.draw.rect(screen2, (143, 11, 15), (825, 3, 72, 50))
        textsurface = quitFont.render("Quit", True, (255, 255, 255))
        screen2.blit(textsurface, (829, 5))

        if 0 <= pygame.mouse.get_pos()[0] <= 186 and 0 <= pygame.mouse.get_pos()[1] <= 56 and pygame.MOUSEBUTTONDOWN:

            pygame.draw.rect(screen2, (255, 255, 255), (0, 0, 186, 56))
            pygame.draw.rect(screen2, (72, 11, 15), (3, 3, 180, 50))
            textsurface = instructionsFont.render("Instructions", True, (255, 255, 255))
            screen2.blit(textsurface, (7, 5))

        elif 407 <= pygame.mouse.get_pos()[0] <= 543 and 0 <= pygame.mouse.get_pos()[1] <= 56 and pygame.MOUSEBUTTONDOWN:

            pygame.draw.rect(screen2, (255, 255, 255), (407, 0, 136, 56))
            pygame.draw.rect(screen2, (72, 11, 15), (410, 3, 130, 50))
            textsurface = settingsFont.render("Settings", True,(255, 255, 255))
            screen2.blit(textsurface, (414, 5))

        elif 822 <= pygame.mouse.get_pos()[0] <= 900 and 0 <= pygame.mouse.get_pos()[1] <= 56 and pygame.MOUSEBUTTONDOWN:

            pygame.draw.rect(screen2, (255, 255, 255), (822, 0, 78, 56))
            pygame.draw.rect(screen2, (72, 11, 15), (825, 3, 72, 50))
            textsurface = quitFont.render("Quit", True, (255, 255, 255))
            screen2.blit(textsurface, (829, 5))

        if 0 <= pygame.mouse.get_pos()[0] <= 186 and 0 <= pygame.mouse.get_pos()[1] <= 56 and pygame.mouse.get_pressed()[0]:

            pygame.mixer.Sound.play(sound)
            Instructions()

        elif 407 <= pygame.mouse.get_pos()[0] <= 543 and 0 <= pygame.mouse.get_pos()[1] <= 56 and pygame.mouse.get_pressed()[0]:

            pygame.mixer.Sound.play(sound)
            Settings()

        elif 822 <= pygame.mouse.get_pos()[0] <= 900 and 0 <=pygame.mouse.get_pos()[1] <= 56 and pygame.mouse.get_pressed()[0]:

            pygame.mixer.Sound.play(sound)
            running=False


        pygame.display.flip()
        clock.tick(6)

def Instructions():

    running=True
    clock=pygame.time.Clock()

    while running == True:

        pygame.display.set_caption("Instructions")
        screen3 = pygame.display.set_mode((900, 540))
        background = pygame.image.load("Instructions Background.jpg")
        background = pygame.transform.scale(background, (900, 540))
        backFont = pygame.font.SysFont("Comic Sans MS", 30)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen3.blit(background, [0, 0])
        textsurface = backFont.render("Back", True, (255, 255, 255))
        screen3.blit(textsurface,(753,452))

        f = open("Instructions.txt", "r")
        f = f.read()
        blit_text(screen3,f,(350,30),pygame.font.SysFont("Times New Roman",19))

        if pygame.MOUSEBUTTONDOWN and 730<=pygame.mouse.get_pos()[0]<=842 and 440<=pygame.mouse.get_pos()[1]<=502:

            textsurface = backFont.render("Back", True, (177, 62, 75))
            screen3.blit(textsurface, (753, 452))

        if 730<=pygame.mouse.get_pos()[0]<=842 and 440<=pygame.mouse.get_pos()[1]<=502 and pygame.mouse.get_pressed()[0]:

            pygame.mixer.Sound.play(sound)
            running=False

        pygame.display.flip()
        clock.tick(6)

def Settings():

    clock=pygame.time.Clock()
    screen4 = pygame.display.set_mode((900, 540))
    background = pygame.image.load("Settings Background.jpg")
    background = pygame.transform.scale(background, (900, 540))
    MusicFont=pygame.font.SysFont("Comic Sans MS", 30)
    soundEffectsFont=pygame.font.SysFont("Comic Sans MS", 30)
    backFont = pygame.font.SysFont("Comic Sans MS", 30)
    creditsFont=pygame.font.SysFont("Comic Sans Ms",30)
    running=True
    Tick = pygame.image.load("Tick.jpg")
    Tick = pygame.transform.scale(Tick, [40, 40])

    while running==True:

        pygame.display.set_caption("Settings")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen4.blit(background, [0, 0])

        textsurface = MusicFont.render("Music", True, (255, 255, 255))
        screen4.blit(textsurface,(100,153))

        pygame.draw.rect(screen4, (143, 11, 15) , (350, 150, 56, 56))
        pygame.draw.rect(screen4, (255, 255, 255), (353, 153, 50, 50))

        if 350 <= pygame.mouse.get_pos()[0] <= 406 and 150 <= pygame.mouse.get_pos()[1] <= 206 and pygame.mouse.get_pressed()[0]:

            if pygame.mixer.music.get_volume()==0.0:
                pygame.mixer.music.set_volume(0.296875)

            else:
                pygame.mixer.music.set_volume(0.0)
                pygame.draw.rect(screen4, (255, 255, 255), (353, 153, 50, 50))

        if pygame.mixer.music.get_volume()==0.296875:
            screen4.blit(Tick,(358,158))

        textsurface = soundEffectsFont.render("Sound Effects", True, (255, 255, 255))
        screen4.blit(textsurface,(100,228))
        pygame.draw.rect(screen4, (143, 11, 15), (350, 225, 56, 56))
        pygame.draw.rect(screen4, (255, 255, 255), (353, 228, 50, 50))

        if 350 <= pygame.mouse.get_pos()[0] <= 406 and 225 <= pygame.mouse.get_pos()[1] <= 281 and pygame.mouse.get_pressed()[0]:

            if sound.get_volume()==0.0:
                sound.set_volume(1.0)

            else:
                sound.set_volume(0.0)
                pygame.draw.rect(screen4, (255, 255, 255), (353, 228, 50, 50))

        if sound.get_volume()==1.0:
            screen4.blit(Tick, (358, 233))

        textsurface = backFont.render("Back", True, (255, 255, 255))
        screen4.blit(textsurface,(753,452))

        textsurface = creditsFont.render("Credits",True, (255,255,255))
        screen4.blit(textsurface,(147,452))

        if pygame.MOUSEBUTTONDOWN and 730<=pygame.mouse.get_pos()[0]<=842 and 440<=pygame.mouse.get_pos()[1]<=502:

            textsurface = backFont.render("Back", True, (100, 100, 120))
            screen4.blit(textsurface, (753, 452))

        elif pygame.MOUSEBUTTONDOWN and 124<=pygame.mouse.get_pos()[0]<=236 and 440<=pygame.mouse.get_pos()[1]<=502:

            textsurface = backFont.render("Credits", True, (100, 100, 120))
            screen4.blit(textsurface, (147, 452))

        if 730<=pygame.mouse.get_pos()[0]<=842 and 440<=pygame.mouse.get_pos()[1]<=502 and pygame.mouse.get_pressed()[0]:

            pygame.mixer.Sound.play(sound)
            running=False

        elif 124<=pygame.mouse.get_pos()[0]<=236 and 440<=pygame.mouse.get_pos()[1]<=502 and pygame.mouse.get_pressed()[0]:

            pygame.mixer.Sound.play(sound)
            Credits()

        pygame.display.flip()
        clock.tick(6)

def Credits():

    clock=pygame.time.Clock()
    screen5= pygame.display.set_mode((900,540))
    background=pygame.image.load("Credits Background.jpg")
    background=pygame.transform.scale(background,(900,540))
    backFont = pygame.font.SysFont("Comic Sans MS", 30)
    running=True

    while running==True:

        pygame.display.set_caption("Credits")

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen5.blit(background,[0,0])

        f=open("Credits.txt","r")
        f=f.read()

        blit_text(screen5,f,(50,50),pygame.font.SysFont("Times New Roman",19))

        textsurface = backFont.render("Back", True, (255, 255, 255))
        screen5.blit(textsurface, (50, 452))

        if pygame.MOUSEBUTTONDOWN and 27 <= pygame.mouse.get_pos()[0] <= 139 and 440 <= pygame.mouse.get_pos()[1] <= 502:

            textsurface = backFont.render("Back", True, (81, 56, 36))
            screen5.blit(textsurface, (50, 452))

        if 27<=pygame.mouse.get_pos()[0]<=236 and 139 <= pygame.mouse.get_pos()[1] <= 502 and pygame.mouse.get_pressed()[0]:

            pygame.mixer.Sound.play(sound)
            running = False

        pygame.display.flip()
        clock.tick(6)

def playMusic():

    pygame.mixer.init()
    pygame.mixer.music.set_volume(0.3)
    if pygame.mixer.music.get_busy()==False:
        pygame.mixer.music.load("Background Music.mp3")
        pygame.mixer.music.play(-1,0.0)
        playMusic()

def implement():

    pygame.init()
    Icon = pygame.image.load("Icon.png")
    global sound
    sound = pygame.mixer.Sound("Button Sound.wav")
    sound.set_volume(1.0)
    pygame.display.set_icon(Icon)
    mainScreen()

playMusic()
implement()
