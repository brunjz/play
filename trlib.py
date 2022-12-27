
import pygame
import pygame.font

#----------------------------------------------------------------- 
# function tr_user_choice: using dict as an input 
def tr_user_choice (question_str,next):

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

