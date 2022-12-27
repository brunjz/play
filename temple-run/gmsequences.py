
#-----------------------------------------------------------------
# class Sequence
class Sequence():

    def __init__(self,id):
        self.id = id
        self.msg = ''
        self.method = 'uinput'
        self.rmax = 2 
        self.next = {}
        self.img = 'images/default.jpg' 

    def identify():
        print(f"Sequence {self.name}: {self.msg}")

#-----------------------------------------------------------------
# def seq_init 
def gm_seq_init(mylist):

  myseq = Sequence('s001')
  myseq.img = 'images/start.jpg'
  myseq.msg += "You are an intrepid explorer. Your goal is to discover the lost treasure that lies within the sacred temple. But it will not be easy. "
  myseq.msg += "Do you wish to begin? "
  myseq.next = {'yes':'s002','no':'s000'} 
  mylist.append(myseq)

  myseq = Sequence('s002')
  myseq.img = 'images/junction.jpg'
  myseq.msg += "You enter the temple and reach a dark hallway. You follow it until you reach a crossroads. " 
  myseq.msg += "Do you wish to go left, straight or right? "
  myseq.next = {'left':'s100','straight':'s300','right':'s200'} 
  mylist.append(myseq)

  # Enter the room, there are two doors
  myseq = Sequence('s100')
  myseq.img = 'images/leftandright.jpg'
  myseq.msg += "You go left and enter a room. There are two doors. Which one will you take? "
  myseq.next = {'left':'s101','right':'s120'} 
  mylist.append(myseq)

  # You took the left door
  myseq = Sequence('s101')
  myseq.img = 'images/findchest.jpg'
  myseq.msg += "You take the left door and walk down a long hallway. As you walk, you notice a small room breaking off from the hallway. "
  myseq.msg += "It appears to contain a chest. It could be a trap. Do you wish to enter the room and open the chest? "
  myseq.next = {'yes':'s102','no':'s150'} 
  mylist.append(myseq)

  # You entered the room and open the chest, you have 50% chance of surviving
  myseq = Sequence('s102')
  myseq.method = 'rand'
  myseq.rmax = 2 
  myseq.msg += "** processing random function"
  myseq.next = {'x':'s103','y':'s104'} 
  mylist.append(myseq)

  # You open the chest and die
  myseq = Sequence('s103')
  myseq.img = 'images/arrowkill.jpg'
  myseq.msg += "You enter the room and open the chest. A trap triggers and sends an arrow hurtling into your chest. You are dead. "
  myseq.msg += "Do you wish to play again? "
  myseq.next = {'yes':'s001','no':'s000'} 
  mylist.append(myseq)

  # You open the cheat and survive
  myseq = Sequence('s104')
  myseq.img = 'images/fightdemon.jpg'
  myseq.msg += "You enter the room and open the chest. It contains a sword. You now have the means to defend yourself. "
  myseq.msg += "You exit the room and continue down the corridor. You reach a room. Inside is a fierce demon. "
  myseq.msg += "Do you wish to fight the demon or do you wish to run and escape the temple empty-handed? "
  myseq.next = {'run':'s105','fight':'s106'} 
  mylist.append(myseq)

  # Run and escape
  myseq = Sequence('s105')
  myseq.img = 'images/runaway.jpg'
  myseq.msg += "You run and escape the temple empty-handed. "
  myseq.msg += "Do you wish to play again? "
  myseq.next = {'yes':'s001','no':'s000'} 
  mylist.append(myseq)

  # You fight with the weapon and win
  myseq = Sequence('s106')
  myseq.img = 'images/treasure.jpg'
  myseq.msg += "You are armed with a sword, so you easily defeat the demon. It was guarding a chest. Inside the chest is the lost treasure. "
  myseq.msg += "Do you wish to play again? "
  myseq.next = {'yes':'s001','no':'s000'} 
  mylist.append(myseq)

  # You will die after taking the right door
  myseq = Sequence('s120')
  myseq.img = 'images/dead.jpg'
  myseq.msg += "You take the right door and enter a small room. The doors closes behind you. You are trapped. "
  myseq.msg += "You hear a noise from the ceiling and look up. "
  myseq.msg += "The ceiling is lined with massive spikes and is slowly descending towards you. You are dead. Game over. Do you wish to restart? "
  myseq.next = {'yes':'s001','no':'s000'} 
  mylist.append(myseq)

  # You did not enter room, continue forward where the monster is
  myseq = Sequence('s150')
  myseq.msg += "You do not enter the room and continue down the corridor. You reach a room. Inside is a fierce demon. "
  myseq.msg += "Do you wish to fight the demon or do you wish to run and escape the temple empty-handed? "
  myseq.next = {'fight':'s151','run':'s152'} 
  mylist.append(myseq)

  # You fight but die because you don't have a weapon
  myseq = Sequence('s151')
  myseq.img = 'images/killedbydemon.jpg'
  myseq.msg += "You are unarmed so the demon easily defeats you. You are dead. Do you wish to restart? "
  myseq.next = {'yes':'s001','no':'s000'} 
  mylist.append(myseq)

  # Runaway and lose
  myseq = Sequence('s152')
  myseq.img = 'images/runaway.jpg'
  myseq.msg += "You run away and lose. Do you wish to restart? "
  myseq.next = {'yes':'s001','no':'s000'} 
  mylist.append(myseq)


#-------------------------------------------------------------
# States 2xx:  
#-------------------------------------------------------------

  # You turn right at the first branch 
  myseq = Sequence('s200')
  myseq.img = 'images/baboons.jpg' 
  myseq.msg += "You go right, down a long corridor. As you walk, you hear a series of load, ferocious screeches from behind you. "
  myseq.msg += "You turn around to discover that a horde of flesh eating baboons are pursuing you. Do you want to run or fight? "
  myseq.next = {'fight':'s201','run':'s202'} 
  mylist.append(myseq)

  # You fight the baboons and die 
  myseq = Sequence('s201')
  myseq.img = 'images/baboonskill.jpg' 
  myseq.msg += "You attempt to fight the horde but you are no match for the baboons. They easily defeat you. You are dead. Do you wish to restart? "
  myseq.next = {'yes':'s001','no':'s000'} 
  mylist.append(myseq)

  # You run to avoid the baboons 
  myseq = Sequence('s202')
  myseq.msg += "You run from the horde of baboons until you reach a crossroads. You do not have a lot of time to make a decision. "
  myseq.msg += "Do you want to go left or right? "
  myseq.next = {'right':'s203','left':'s220'} 
  mylist.append(myseq)

  # You made a turn right escaping the baboons, and come across a cloaked figure 
  myseq = Sequence('s203')
  myseq.img = 'images/clokedfigure.jpg' 
  myseq.msg += "You run from the horde of baboons until you reach a crossroads. You do not have a lot of time to make a decision. "
  myseq.msg += "You go right and run down a hallway until you reach a room. The baboons are still in pursuit. "
  myseq.msg += "Within the room, stands a cloaked figure, wielding a sword. "
  myseq.msg += "It defeats the horde of baboons and turns to you. It is beckoning you. Do you trust it? It may kill you. "
  myseq.next = {'no':'s204','yes':'s205'} 
  mylist.append(myseq)

  # You don't trust the cloaked figure and die 
  myseq = Sequence('s204')
  myseq.img = 'images/bigsnake.jpg' 
  myseq.msg += "You do not approach the dark figure. Angered, it transforms into a massive serpent and devours you. "
  myseq.msg += "You are dead. Do you wish to restart? "
  myseq.next = {'yes':'s001','no':'s000'} 
  mylist.append(myseq)

  # You trust the cloaked figure 
  myseq = Sequence('s205')
  myseq.img = 'images/offerhelp.jpg' 
  myseq.msg += "You approach the dark figure. It is offering you help. Do you accept? "
  myseq.next = {'no':'s206','yes':'s207'} 
  mylist.append(myseq)

  # You die after you denied help 
  myseq = Sequence('s206')
  myseq.img = 'images/hornetskill.jpg' 
  myseq.msg += "You deny help and continue down a hallway, until you reach an uncrossable gulch. "
  myseq.msg += "Suddenly, a swarm of poisonous hornets fly from the gulch and kill you. You are dead. Do you wish to restart? "
  myseq.next = {'yes':'s001','no':'s000'} 
  mylist.append(myseq)

  # You accept help and get rich 
  myseq = Sequence('s207')
  myseq.img = 'images/treasure.jpg' 
  myseq.msg += "You accept the dark figure's proposal and continue on down a hallway. "
  myseq.msg += "You reach the gulch and use the rope to reach the other side. There, you find the lost treasure. "
  myseq.msg += "You won but at the cost of a cut of the treasure. Do you wish to play again? "
  myseq.next = {'yes':'s001','no':'s000'} 
  mylist.append(myseq)

  # You went left to avoid the baboons
  myseq = Sequence('s220')
  myseq.img = 'images/threebuttons.jpg' 
  myseq.msg += "You go left and enter a room. The door closes behind you. You are trapped but safe from the horde of baboons. "
  myseq.msg += "In the center of the room is an altar. Atop the altar are 3 buttons. You do not know what they do. "
  myseq.msg += "The only thing to do is to push a button. "
  myseq.msg += "Which button do you push? The left button, the right button or the middle button? "
  myseq.next = {'left':'s221','middle':'s221','right':'s221'} 
  mylist.append(myseq)

  # First flip of the coin
  myseq = Sequence('s221')
  myseq.method = 'rand' 
  myseq.rmax = 3 
  myseq.msg += "** calling random function"
  myseq.next = {'x':'s223','y':'s222'} 
  mylist.append(myseq)

  # Second flip of the coin 
  myseq = Sequence('s222')
  myseq.method = 'rand' 
  myseq.rmax = 2 
  myseq.msg += "** calling random function"
  myseq.next = {'x':'s224','y':'s225'} 
  mylist.append(myseq)

  # First outcome 
  myseq = Sequence('s223')
  myseq.img = 'images/pitsnakes.jpg' 
  myseq.msg += "You pressed the wrong button. The floor collapses beneath you and you fall into a pit of snakes. They eat you alive. "
  myseq.msg += "You are dead. Do you wish to restart? "
  myseq.next = {'yes':'s001','no':'s000'} 
  mylist.append(myseq)

  # Second outcome 
  myseq = Sequence('s224')
  myseq.img = 'images/baboonskill.jpg' 
  myseq.msg += "You press the button and the door reopens behind you. You are no longer trapped but you let the baboons into the room. "
  myseq.msg += "The horde of baboons enter the room and kill you. You are dead. Do you wish to restart? "
  myseq.next = {'yes':'s001','no':'s000'} 
  mylist.append(myseq)

  # Third outcome 
  myseq = Sequence('s225')
  myseq.img = 'images/treasure.jpg' 
  myseq.msg += "You pressed the right button. A door on the other side of the room opens, revealing a chest. Inside is the lost treasure. "
  myseq.msg += "You won. Do you wish to play again? "
  myseq.next = {'yes':'s001','no':'s000'} 
  mylist.append(myseq)


#-------------------------------------------------------------
# States 3xx:  
#-------------------------------------------------------------

  # After going straight you find a sword 
  myseq = Sequence('s300')
  myseq.img = 'images/findsword.jpg' 
  myseq.msg += "You go straight and reach a room containing an altar. On the altar is a sword. Do you want to take the sword? It could be a trap. "
  myseq.next = {'yes':'s301','no':'s350'} 
  mylist.append(myseq)

  # You take the sword 
  myseq = Sequence('s301')
  myseq.method = 'rand' 
  myseq.rmax = 2 
  myseq.msg += "** calling random function"
  myseq.next = {'x':'s302','y':'s303'} 
  mylist.append(myseq)

  # You take the sword, but it's a trap. You die
  myseq = Sequence('s302')
  myseq.img = 'images/arrowkill.jpg'
  myseq.msg += "You try to take the sword but it is a trap. The trap triggers and sends a poison dart flying into your neck. "
  myseq.msg += "You are dead. Do you wish to restart? "
  myseq.next = {'yes':'s001','no':'s000'} 
  mylist.append(myseq)

  # You take the sword and carry on
  myseq = Sequence('s303')
  myseq.msg += "You take the sword from the altar but hear a growl behind you. You turn to face a massive ravenous jaguar. "
  myseq.msg += "Do you want to fight the jaguar or do you want to run and escape the temple empty-handed? "
  myseq.next = {'run':'s304','fight':'s305'} 
  mylist.append(myseq)

  # You run from the jaguar and escape empty handed.
  myseq = Sequence('s304')
  myseq.img = 'images/runaway.jpg'
  myseq.msg += "You run and escape the temple empty-handed. Do you wish to play again? "
  myseq.next = {'yes':'s001','no':'s000'} 
  mylist.append(myseq)

  # You fight the jaguar 
  myseq = Sequence('s305')
  myseq.method = 'rand' 
  myseq.rmax = 2 
  myseq.msg += "** calling random function"
  myseq.next = {'x':'s306','y':'s307'} 
  mylist.append(myseq)

  # You fight the jaguar and die 
  myseq = Sequence('s306')
  myseq.img = 'images/dead.jpg' 
  myseq.msg += "Despite wielding a sword, you are defeated and devoured by the jaguar. You are dead. Do you wish to play again? "
  myseq.next = {'yes':'s001','no':'s000'} 
  mylist.append(myseq)

  # You fight the jaguar and win 
  myseq = Sequence('s307')
  myseq.img = 'images/treasure.jpg' 
  myseq.msg += "You defeat the jaguar and notice a key strapped to one of it's legs. "
  myseq.msg += "You take the key and notice a chest sitting in the corner of the room. "
  myseq.msg += "You open the chest and claim the lost treasure. You won. Do you wish to play again? "
  myseq.next = {'yes':'s001','no':'s000'} 
  mylist.append(myseq)

  # You don't take the sword 
  myseq = Sequence('s350')
  myseq.msg += "You do not take the sword and hear a growl behind you. You turn to face a massive ravenous jaguar. "
  myseq.msg += "Do you want to fight the jaguar, despite having no weapons, or do you want to run and escape the temple empty-handed? "
  myseq.next = {'run':'s351','fight':'s352'} 
  mylist.append(myseq)

  # You run away from the jaguar without the sword 
  myseq = Sequence('s351')
  myseq.img = 'images/runaway.jpg' 
  myseq.msg += "You run and escape the temple empty-handed. Do you wish to play again? "
  myseq.next = {'yes':'s001','no':'s000'} 
  mylist.append(myseq)

  # You fight with the juaguar without the sword 
  myseq = Sequence('s352')
  myseq.method = 'rand' 
  myseq.rmax = 9 
  myseq.msg += "** calling random function"
  myseq.next = {'x':'s353','y':'s354'} 
  mylist.append(myseq)

  # You fight and win 
  myseq = Sequence('s353')
  myseq.img = 'images/treasure.jpg' 
  myseq.msg += "Despite the odds, you defeated the jaguar without a weapon and notice a key strapped to one of it's legs."
  myseq.msg += "You take the key and notice a chest sitting in the corner of the room. You open the chest and claim the lost treasure."
  myseq.msg += "You won. Do you want to play again? "
  myseq.next = {'yes':'s001','no':'s000'} 
  mylist.append(myseq)

  # You fight and die 
  myseq = Sequence('s354')
  myseq.img = 'images/dead.jpg' 
  myseq.msg += "As you do not have a weapon, the jaguar easily defeats you. You are dead. Do you wish to play again? "
  myseq.next = {'yes':'s001','no':'s000'} 
  mylist.append(myseq)
