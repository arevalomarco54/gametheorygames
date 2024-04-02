import pygame
import random
import framework as fr

class MPScreen(fr.Screen):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # Fonts
        self.font = pygame.font.Font(None, 55)
        self.small_font = pygame.font.Font(None, 35)

        #Create Heads Image
        heads = fr.ImageButton(self.load_penny_image("heads"), "headsImg",(150,150))
        heads.setPos((fr.GRID_WIDTH-heads.size[0]*2-50*1)/2, fr.GRID_HEIGHT/5)

        #create computer image
        computer_img = fr.Image(pygame.image.load('images/both.png'),"computerImg",(300,150))
        computer_img.setPos((fr.GRID_WIDTH-computer_img.size[0])/2,fr.GRID_HEIGHT/5*3)

        #Create Tails Image
        tails = fr.ImageButton(self.load_penny_image("tails"), "tailsImg",(150,150))
        tails.setPos((heads.x + heads.size[0]+50), fr.GRID_HEIGHT/5)

        #Create Text
        text= fr.Text("Ready! Choose an Image", self.small_font, "mainText")
        text.setPos(((fr.GRID_WIDTH - text.size[0])/2,(fr.GRID_HEIGHT - text.size[1])))

        #Create Even Score Count
        evenScore= fr.Text("Even Score: 0", self.small_font, "evenText")
        evenScore.setPos((0,(fr.GRID_HEIGHT - evenScore.size[1])))

        #create Odd Score Count
        oddScore= fr.Text("Odd Score: 0" , self.small_font, "oddText")
        oddScore.setPos(((fr.GRID_WIDTH-oddScore.size[0]),(fr.GRID_HEIGHT - oddScore.size[1])))

        #add buttons and objects to screen
        self.addButtons([heads, tails])
        self.addObjects([text, computer_img, evenScore, oddScore])
    # Function to load image based on side (Heads or Tails)
    def load_penny_image(self, side):
        if side == "heads":
            return pygame.image.load("images/heads.png")
        else:
            return pygame.image.load("images/tails.png")



    # Function to determine winner based on choices
    def get_winner(self, player_choice, computer_choice):
        if player_choice == computer_choice:
            return "Even"
        else:
            return "Odd"
        

    #game loop
    def play(self):
        even_score = 0 
        odd_score = 0 
        player_choice = None
        computer_choice = None
        game_over = False
        result = None
        computer_img = self.getObject("computerImg")
        text = self.getObject("mainText")
        even = self.getObject("evenText")
        odd = self.getObject("oddText")
        while not game_over:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                # Detect mouse clicks on buttons (replace with your button logic)
                elif event.type == pygame.MOUSEBUTTONDOWN:
                    x,y = pygame.mouse.get_pos()
                    for button in self.buttons:
                        if button.checkClicked(x,y):
                            if type(button) is fr.NavButton:
                                game_over = True
                                return
                            else:
                                player_choice=button.title[0:-3]
            if player_choice:
                    computer_choice = random.choice(["heads", "tails"])
                    computer_img.image = self.load_penny_image(computer_choice)
                    computer_img.size = (150,150)
                    result = self.get_winner(player_choice, computer_choice)
                    player_choice = None
                    computer_choice = None

            if result:
                if result == "Even":
                    text.updateMessage("Even Wins!")
                    even_score+=1
                    even.updateMessage("Even Score: " + str(even_score))

                    text.color = fr.RED
                elif result == "Odd":
                    text.updateMessage("Odd Win!")
                    odd_score +=1
                    odd.updateMessage("Odd Score: " + str(odd_score))
                    odd.setPos(((fr.GRID_WIDTH-odd.size[0]),(fr.GRID_HEIGHT - odd.size[1])))
                    text.color = fr.GREEN
                result = None
                text.setPos(((fr.GRID_WIDTH - text.size[0])/2,(fr.GRID_HEIGHT - text.size[1])))

            # Update screen
            self.screenUpdate()




if __name__ == "__main__":
    #make screen
    pygame.init()
    pygame.font.init()
    screen = MPScreen("Matching Pennies", fr.WHITE)
    screen.makeCurrentScreen()
    screen.play()
    pygame.quit()