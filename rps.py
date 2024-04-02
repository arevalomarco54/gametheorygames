import pygame
import random
import framework as fr
class RPSScreen(fr.Screen):
  def __init__(self, title, color):
    super().__init__(title, color)
    self.choices = ["rock", "paper", "scissors"]
    self.font = pygame.font.Font(None, 55)
    self.small_font = pygame.font.Font(None, 35)
    # Game objects

    rock = fr.ImageButton(self.get_game_object("rock"), "rockImg",(100,100))
    rock.setPos((fr.GRID_WIDTH-rock.size[0]*3-50*2)/2, fr.GRID_HEIGHT/5)

    paper = fr.ImageButton(self.get_game_object("paper"), "paperImg",(100,100))
    paper.setPos(rock.x + rock.size[0]+50, fr.GRID_HEIGHT/5)

    scissors = fr.ImageButton(self.get_game_object("scissors"), "scissorsImg", (100,100))
    scissors.setPos(paper.x + paper.size[0]+50, fr.GRID_HEIGHT/5)

    computer_img = fr.Image(self.get_game_object(None),"computerImg",(150,150))
    computer_img.setPos((fr.GRID_WIDTH-computer_img.size[0])/2,fr.GRID_HEIGHT/5*3)

    title = fr.Text("Rock Paper Scissors",self.font, "mainText")
    title.setPos(((fr.GRID_WIDTH - title.size[0])/2,(fr.GRID_HEIGHT - title.size[1])/2))

    text= fr.Text("Ready! Choose an image to play!", self.small_font, "bottomText")
    text.setPos(((fr.GRID_WIDTH - text.size[0])/2,(fr.GRID_HEIGHT - text.size[1])))

    self.addObjects([title,text,computer_img])
    self.addButtons([rock,paper,scissors])


  def get_game_object(self,choice):
    """Loads an image based on the game object."""
    if choice == "rock":
      return pygame.image.load("images/rock.png")
    elif choice == "paper":
      return pygame.image.load("images/paper.png")
    elif choice == "scissors":
      return pygame.image.load("images/scissors.png")
    else:
      return pygame.image.load("images/rps.png")




  def get_winner(self, player, computer):
    """Determines the winner based on player and computer choices."""
    # Tie
    if player == computer:
      return "tie"

    # Player wins
    if player == "rock" and computer == "scissors":
      return "player"
    elif player == "paper" and computer == "rock":
      return "player"
    elif player == "scissors" and computer == "paper":
      return "player"

    # Computer wins
    return "computer"


  def play(self):
      player_choice = None
      computer_choice = None
      game_over = False
      result = None
      computer_img = self.getObject("computerImg")
      text = self.getObject("bottomText")
  # Main loop
      while not game_over:
          for event in pygame.event.get():
              if event.type == pygame.QUIT:
                  game_over = True
              # Detect mouse clicks on buttons (replace with your button logic)
              elif event.type == pygame.MOUSEBUTTONDOWN:
                  x,y = pygame.mouse.get_pos()
                  for button in self.buttons:
                      if button.checkClicked(x,y):
                          player_choice=button.title[0:-3]
              # Game logic based on player input
          if player_choice:
                  computer_choice = random.choice(self.choices)
                  computer_img.image = self.get_game_object(computer_choice)
                  result = self.get_winner(player_choice, computer_choice)
                  player_choice = None
                  computer_choice = None

      # Display Text

          if result:
              if result == "tie":
                  text.updateMessage("It's a Tie!")
                  text.color = fr.YELLOW
              elif result == "player":
                  text.updateMessage("You Win!")
                  text.color = fr.GREEN
              else:
                  text.updateMessage("You Lose!")
                  text.color = fr.RED
              text.setPos(((fr.GRID_WIDTH - text.size[0])/2,(fr.GRID_HEIGHT - text.size[1])))
          self.screenUpdate()


if __name__ == "__main__":
    #make screen
    pygame.init()
    pygame.font.init()
    screen = RPSScreen("RPS", fr.GREY)
    screen.makeCurrentScreen()
    screen.play()
    pygame.quit()
