
import sys
import pygame
import pygame.font
import pygame.freetype
import random

from pygame.locals import *
from gmsequences import gm_seq_init
from settings import Settings
from os.path import exists


#----------------------------------------------------------------- 
# Overall class to manage game assets and behavior
class SequenceManager:


  #--------------------------------------------------------------- 
  # Initialize the game, and create game resources
  def __init__(self):

    pygame.init()
    self.settings = Settings()

    # Initiate games sequences
    self.cid = 's001' 
    self.ret = {} 
    self.list = [] 
    gm_seq_init(self.list)
    self.check_list(self.list)

    # Display init 
    self.screen = pygame.display.set_mode( 
              (self.settings.screen_width, self.settings.screen_height))
    pygame.display.set_caption(self.settings.set_caption)
    self.font = pygame.freetype.SysFont("comicsansms", 0) 

    self.imagectrl = Images(self)
    self.buttonm = Button(self,"m","",0)
    self.buttonr = Button(self,"r","",1)
    self.buttonl = Button(self,"l","",-1)


  #--------------------------------------------------------------- 
  # Breaks a long string into smaller strings
  def chunkstring (self, string, length):
    return (string[0+i:length+i] for i in range(0, len(string), length))


  #--------------------------------------------------------------- 
  # Draws text at the bottom of the screen. Basic implementation.
  def draw_text (self, text, text_size, color):

    text_rect = self.font.get_rect(text,size=text_size)
    text_rect.bottom = self.screen.get_rect().bottom
    self.font.render_to(self.screen,text_rect,text,color,size=text_size)  


  #--------------------------------------------------------------- 
  # Draws text at the bottom of the screen, breaking down long text 
  # message into smaller strings. This version might break up 
  # individual words.
  def draw_text2 (self, text, text_size, color):

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


  #--------------------------------------------------------------- 
  # Draws text at the bottom of the screen, breaking down long text 
  # message into smaller test strings. This version won't break up 
  # words.

  def draw_text3 (self, text, text_size, color):

    MAXLEN = 150
    mylist1 = text.split(' ') 
    mylist2 = [] 
    str = ''

    # Captures strings of MAXLEN size into mylist2
    for tinystr in mylist1:
      if (len(tinystr) > MAXLEN):
        sys.exit()
      elif (len(str) + len(tinystr) < MAXLEN):
        if (str ==''):
          str = tinystr
        else:
          str = f"{str} {tinystr}"
      else:
        mylist2.append(str)
        str = tinystr 

    # Pushes final string into mylist2 
    if (len(str) > 0):
      mylist2.append(str)

    # Displays message at the bottom of the screen 
    max = len(mylist2)
    num = 0
    while (num < max):
      text2 = mylist2[num]
      text_rect2 = self.font.get_rect(text2, size=text_size)
      text_rect2.bottom = self.screen.get_rect().bottom - 20*(max-num) 
      text_rect2.left = 10
      self.font.render_to(self.screen, text_rect2, text2, color, size=text_size)  
      num += 1


  #--------------------------------------------------------------- 
  # Check validity of the elements in the sequence list
  def check_list (self, list):

    for seq in list:

      if (len(seq.next) != 1 and len(seq.next) != 2 and len(seq.next) != 3): 
        print(f"check_list: invalid entries in dictionary for seq {seq.id}, exiting")
        sys.exit()

      if (not exists(seq.img)): 
        print(f"check_list: warning, {seq.img} not found for seq {seq.id}")

      if (seq.method == ''): 
        print(f"check_list: error, method not defined for seq {seq.id}, exiting")
        sys.exit()

      if (seq.rmax < 2): 
        print(f"check_list: error, incorrect rmax value for seq {seq.id}, exiting")
        sys.exit()


  #--------------------------------------------------------------- 
  # Routine to start the main game 
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
            print(f"Error: sequence \'{self.cid}\' not found, exiting") 
            sys.exit()

          # Redraw the screen during each pass through the loop.
          self.screen.fill(self.settings.bg_color)
          self.draw_text3(seq.msg,16,(0,0,0))  

          if (exists(seq.img)):
            print("Loading image:",seq.img)
            self.imagectrl.load(self,seq.img)
            self.imagectrl.blitme()

          print(seq.msg)

          # Retrieve information from next structure 
          options = []
          next = []
          for var in seq.next:
            options.append(var)
            next.append(seq.next[var])
          print("User choices",options)
          print("Next sequence",next)

          # Determine what to display in the boxes 
          if (len(options) == 1):
            self.buttonm.prep_msg(options[0])
            self.buttonm.draw_button()
            next_m = next[0]
          elif (len(options) == 2):
            self.buttonl.prep_msg(options[0])
            self.buttonl.draw_button()
            next_l = next[0]
            self.buttonr.prep_msg(options[1])
            self.buttonr.draw_button()
            next_r = next[1]
          elif (len(options) == 3):
            self.buttonl.prep_msg(options[0])
            self.buttonl.draw_button()
            next_l = next[0]
            self.buttonr.prep_msg(options[2])
            self.buttonr.draw_button()
            next_r = next[2]
            self.buttonm.prep_msg(options[1])
            self.buttonm.draw_button()
            next_m = next[1]

          pygame.display.flip()

          # Work out where to go next 
          if (seq.method == 'rand'):
            if (len(seq.next) != 2): 
              print("Error, invalid sequence data,exiting")
              sys.exit()
            rval = random.randint(1,seq.rmax)
            print(f"rval is {rval} / rmax is {seq.rmax}")
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
                  print("Mouse click detected",mouse)
                  if (len(seq.rscreen) != 0 and len(self.ret) != 0):
                    if seq.rscreen in self.ret.keys():
                      rid = self.ret[seq.rscreen]
                      print("run_game: return id from return screen identified",rid)
                      self.cid = rid 
                      found = True
                  elif (self.buttonl.check_match(mouse) and len(options) != 1): 
                    self.cid = next_l
                    found = True
                  elif (self.buttonr.check_match(mouse) and len(options) != 1): 
                    self.cid = next_r
                    found = True
                  elif (self.buttonm.check_match(mouse) and len(options) != 2): 
                    self.cid = next_m
                    found = True

          # Manage return state 
          self.ret = {} 
          if (len(seq.ret) != 0):
            print(f"Copying return stack from {self.cid}:",seq.ret)
            self.ret = seq.ret


#-----------------------------------------------------------------
# A class to manage images
class Images():
 
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
# A class to manage displaying buttons 
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
        self.prep_msg(msg)


    def prep_msg(self, msg):
        """Turn msg into a rendered image and center text on the button."""
        self.msg_image = self.font.render(msg, True, self.text_color, self.button_color)
        self.msg_image_rect = self.msg_image.get_rect()
        self.msg_image_rect.center = self.rect.center


    def draw_button(self):
        # Draw blank button and then draw message.
        self.screen.fill(self.button_color, self.rect)
        self.screen.blit(self.msg_image, self.msg_image_rect)


    def check_match(self, mouse):

        if (self.rect.left <= mouse[0] <= self.rect.right
            and self.rect.top <= mouse[1] <= self.rect.bottom):
          ret = True
        else:
          ret = False 

        if (ret):
          print(f"Check_match button {self.id}, MATCH at {mouse}")
        return (ret)


#----------------------------------------------------------------- 
# Function to manage user input
def gm_user_choice (question_str, next):

  for var in next:
    print(f"Option offered {var}: {next[var]}")

  found = False
  while(not found):
    user_input = input(question_str).lower()
    for var in next:
      if (var == user_input):
        found = True
        nout = next[var]

  return(nout)

