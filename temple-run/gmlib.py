
import sys
import pygame
import pygame.font
import pygame.freetype
import random

from pygame.locals import *
from gmsequences import gm_seq_init
from settings import Settings


#----------------------------------------------------------------- 
class SequenceManager:
  """Overall class to manage game assets and behavior."""

  def __init__(self):
    """Initialize the game, and create game resources."""
    pygame.init()

    self.cid = 's001' 

    # Initiate games sequences
    self.list = [] 
    gm_seq_init(self.list)

    # Display init 
    self.settings = Settings()
    self.screen = pygame.display.set_mode( 
              (self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption(self.settings.set_caption)
    self.imagectrl = Images(self)
    self.buttonm = Button(self,"m","b0",0)
    self.buttonr = Button(self,"r","b+1",1)
    self.buttonl = Button(self,"l","b-1",-1)
    self.font = pygame.freetype.SysFont("comicsansms", 0) 


  def chunkstring(self, string, length):
    """ Breaks a long string into smaller strings. """
    return (string[0+i:length+i] for i in range(0, len(string), length))


  def draw_text(self, text, text_size, color):
    """Draw text in the middle of the screen."""

    text_rect = self.font.get_rect(text,size=text_size)
    text_rect.bottom = self.screen.get_rect().bottom
    self.font.render_to(self.screen,text_rect,text,color,size=text_size)  


  def draw_text_lg(self, text, text_size, color):
    """Draw text in the middle of the screen."""

    mylist = []
    mylist = list(self.chunkstring(text,155))

    max = len(mylist)
    num = 0
    while (num < max):
      text2 = mylist[num]
      text_rect2 = self.font.get_rect(text2, size=text_size)
      text_rect2.bottom = self.screen.get_rect().bottom - 20*(max-num) 
      text_rect2.left = 10
      self.font.render_to(self.screen, text_rect2, text2, color, size=text_size)  
      num += 1


  def run_game(self):
      """Start the main loop for the game."""

      while True:

          # Detect exit code 
          if (self.cid == 's000'):
            print("Leaving the game")
            sys.exit() 

          # Identify current sequence
          found = False
          num = 0
          while (not found and num < len(self.list)):
            seq = self.list[num]
            num = num + 1
            if (seq.id == self.cid):
              found = True 
              print(f"Entering sequence {seq.id}")

          if (not found):
            print(f"Error: sequence {self.cid} not found, exiting") 
            sys.exit()

          # Redraw the screen during each pass through the loop.
          print("Loading image:",seq.img)
          print(seq.msg)
          self.screen.fill(self.settings.bg_color)
          self.imagectrl.load(self,seq.img)
          self.imagectrl.blitme()
          self.draw_text_lg(seq.msg,16,(0,0,0))  

          # Get choice information 
          choice = []
          next = []
          for var in seq.next:
            choice.append(var)
            next.append(seq.next[var])
          print("Choice",choice)
          print("Next",next)

          # Choice to display in box 
          if (len(choice) == 2):
            self.buttonl._prep_msg(choice[0])
            self.buttonl.draw_button()
            next_l = next[0]
            self.buttonr._prep_msg(choice[1])
            self.buttonr.draw_button()
            next_r = next[1]
          elif (len(choice) == 3):
            self.buttonl._prep_msg(choice[0])
            self.buttonl.draw_button()
            next_l = next[0]
            self.buttonr._prep_msg(choice[2])
            self.buttonr.draw_button()
            next_r = next[2]
            self.buttonm._prep_msg(choice[1])
            self.buttonm.draw_button()
            next_m = next[1]

          pygame.display.flip()

          # Work out where to go next 
          if (seq.method == 'rand'):
            if (len(seq.next) != 2): 
              print("Error, invalid sequence data,exiting")
              sys.exit()
            rval = random.randint(1,seq.rmax)
            print("rval is",rval)
            if (rval == 1):
              self.cid = next[0]
            else:
              self.cid = next[1]

          # Watch for keyboard and mouse events.
          else:
            found = False
            while (not found):
              mouse = pygame.mouse.get_pos()
              for event in pygame.event.get():
                if event.type == pygame.QUIT:
                  sys.exit()
                elif event.type == pygame.MOUSEBUTTONDOWN:
                  print("mouse click detected",mouse)
                  if (self.buttonl.check_match(mouse)): 
                    found = True
                    self.cid = next_l
                  elif (self.buttonr.check_match(mouse)): 
                    found = True
                    self.cid = next_r
                  elif (self.buttonm.check_match(mouse) and len(choice) == 3): 
                    found = True
                    self.cid = next_m

          print("Next sequence is",self.cid)




#----------------------------------------------------------------- 
# function gm_user_choice: using dict as an input 
def gm_user_choice (question_str,next):

  for var in next:
    print(f"Choice offered {var}: {next[var]}")

  found = False
  while(not found):
    user_input = input(question_str).lower()
    for var in next:
      if (var == user_input):
        found = True
        nout = next[var]

  return(nout)

#-----------------------------------------------------------------
class Images():
    """A class to manage images."""
 
    def __init__(self,instance):
        """Initialize settings. """
        super().__init__()
        self.screen = instance.screen
        self.settings = instance.settings
        self.screen_rect = instance.screen.get_rect()


    def load(self,instance,myimage):
        """Load an image at its starting position."""
        super().__init__()
        self.screen = instance.screen
        self.settings = instance.settings
        self.screen_rect = instance.screen.get_rect()

        # Load the ship image and get its rect.
        self.image = pygame.image.load(myimage)
        self.rect = self.image.get_rect()

        # Start each new ship at the bottom center of the screen.
        self.rect.midtop = self.screen_rect.midtop

    def blitme(self):
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)
 
#----------------------------------------------------------------- 
class Button:
 
    def __init__(self, instance, id, msg, offset):
        """Initialize button attributes."""
        self.screen = instance.screen
        self.screen_rect = self.screen.get_rect()
        self.id = id 
        self.msg = msg 
        
        # Set the dimensions and properties of the button.
        self.width, self.height = 130, 50
        self.button_color = (0, 255, 0)
        self.text_color = (255, 255, 255)
        self.font = pygame.font.SysFont(None, 40)
        
        # Build the button's rect object and center it.
        self.rect = pygame.Rect(0, 0, self.width, self.height)
        self.rect.center = self.screen_rect.center
        self.rect.centerx += offset*150 
        
        # The button message needs to be prepped only once.
        self._prep_msg(msg)

    def _prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center

    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)

    def check_match(self, mouse):

        print(f"check_match {self.id}, mouse is {mouse}")
        print(f"check_match {self.id}, l {self.rect.left} r {self.rect.right} b {self.rect.bottom} t {self.rect.top}") 
        if (self.rect.left <= mouse[0] <= self.rect.right
            and self.rect.top <= mouse[1] <= self.rect.bottom):
          ret = True
        else:
          ret = False 

        if (ret):
          print(f"check_match {self.id}, MATCH at {mouse}")
        return (ret)

