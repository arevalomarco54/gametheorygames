import pygame
GRID_WIDTH = 700
GRID_HEIGHT = 500
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (34,171,36)
PURPLE = (109,59,191)
YELLOW = (190, 163, 9)
MAGENTA = (205,14,102)
BLUE = (15, 130, 242)
PINK = (230,135,179)
ORANGE = (253,140,0)
RED = (196, 30, 58)
GREY = (189,189,189)
pygame.font.init()
gamefont = pygame.font.SysFont('Times New Roman', 25)

class Screen():
    def __init__(self, title, color):
        self.title = title
        self.color = color
        self.current = False
        self.buttons = []
        self.objects = []
        self.screen =None
    def makeCurrentScreen(self):
        self.current=True
        pygame.display.set_caption(self.title)
        self.screen = pygame.display.set_mode((GRID_WIDTH, GRID_HEIGHT))
    
    def endCurrentScreen(self):
        self.current = False
    def getObject(self, title):
        for o in self.objects:
            if o.title == title:
                return o
        return None
    def screenUpdate(self):
        if self.current:
            self.screen.fill(self.color)
            for object in self.objects:
                object.draw(self.screen)
        pygame.display.update()

    def returnScreen(self):
        return self.screen
    
    def addObject(self,o):
        self.objects.append(o)
        
    def addObjects(self, o):
        for obj in o:
            self.addObject(obj)

    def addButton(self,b):
        self.objects.append(b)
        self.buttons.append(b)

    def addButtons(self,b):
        for button in b:
            self.addButton(button)
    
    

class Image():
    def __init__(self, image, name, size, pos = (0,0)):
        self.image = image
        self.size = size
        self.x,self.y = pos
        self.title = name
    def draw(self,screen):
        screen.blit(pygame.transform.scale(self.image,self.size), (self.x,self.y))
    def setPos(self, x,y):
        self.x = x
        self.y = y

        
class Text():
    def __init__(self, message, font, title, pos = (0,0), color = BLACK):
        self.pos = pos
        self.font = font
        self.message = message
        self.title = title
        self.size = pygame.font.Font.size(self.font, self.message)
        self.color = color
    def draw(self, screen):
        text = self.font.render(self.message, True, self.color)
        screen.blit(text, self.pos)
    def updateMessage(self, new_message):
        self.message = new_message
        self.size = pygame.font.Font.size(self.font, self.message)
    def setPos(self, pos):
        self.pos = pos


class Button():
    def __init__(self, size, color, title, pos=(0,0)):
        self.width,self.length = size
        self.x,self.y = pos
        self.color = color
        self.clicked = False
        self.title = title
        self.rect = pygame.Rect(self.x, self.y, self.width, self.length)
    def checkClicked(self, x,y):
        if(self.x <=x and (self.x+self.width)>=x and self.y <=y and (self.y+self.length)>=y):
            self.clicked = True
        else: 
            self.clicked = False
        return self.clicked
    def draw(self,screen):
        pygame.draw.rect(screen,self.color, self.rect)
        pygame.draw.line(screen, BLACK, (self.x, self.y), (self.x+self.width, self.y ), 1)
        pygame.draw.line(screen, BLACK, (self.x, self.y), (self.x, self.y+self.length ), 1)
        pygame.draw.line(screen, BLACK, (self.x+self.width, self.y), (self.x+self.width, self.y+self.length), 1)
        pygame.draw.line(screen, BLACK, (self.x, self.y+self.length), (self.x+self.width, self.y+self.length), 1)
       
    
class NavButton(Button):
    def __init__(self, size, text, color, screen, title, pos=(0, 0)):
        super().__init__(size, color, title, pos)
        self.screen = screen
        self.text =text
        self.buttonText = gamefont.render(self.text, False, BLACK)
    def changeScreen(self, currentScreen):
        currentScreen.endCurrentScreen()
        self.screen.makeCurrentScreen()
        return self.screen
    def draw(self, screen):
        super().draw(screen)
        screen.blit(self.buttonText, (self.x+self.width/10,self.y+self.length/3))

class ImageButton(Image):
    def __init__(self,image,name, size, pos = (0,0)):
        super().__init__(image, name, size, pos )

    def checkClicked(self, x,y):
        if(self.x <=x and (self.x+self.size[0])>=x and self.y <=y and (self.y+self.size[1])>=y):
            self.clicked = True
        else: 
            self.clicked = False
        return self.clicked
      