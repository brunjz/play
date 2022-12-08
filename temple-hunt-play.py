#!/usr/bin/env python3
import re
import random


#----------------------------------------------------------------- 
# function tr_user_choice_x2: user input with 2 choices 
def tr_user_choice_x2 (question_str,choice_a,state_a,choice_b,state_b):

  user_input = input(question_str).lower()
  while (user_input != choice_a and user_input != choice_b):
    user_input = input(question_str).lower()
  if user_input == choice_a:
    mystate = state_a
  elif user_input == choice_b:
    mystate = state_b

  return(mystate)

#----------------------------------------------------------------- 
# function tr_user_choice_x3: user input with 3 choices 
def tr_user_choice_x3 (question_str,choice_a,state_a,choice_b,state_b,choice_c,state_c):

  user_input = input(question_str).lower()
  while (user_input != choice_a and user_input != choice_b and user_input != choice_c):
    user_input = input(question_str).lower()
  if user_input == choice_a:
    mystate = state_a
  elif user_input == choice_b:
    mystate = state_b
  elif user_input == choice_c:
    mystate = state_c

  return(mystate)

#----------------------------------------------------------------- 
# function tr_end_game: ends the game
def tr_end_game (text_print):

    print(text_print)
    quit()

#----------------------------------------------------------------- 
# function tr_new_state: create a new valid state
def tr_new_state (mystate):

    valid_states.append(mystate)
    return()
  

##################################################################
# Main
##################################################################

valid_states = ['st000','st001']
state = 'st001';

# Program loop 
while True:

  # Check current state is valid
  if state not in valid_states:
    print("ERROR, not a valid state",state)
    quit()

  # Exit the game
  if state == 'st000':
     tr_end_game("ending the game")
  
  #-------------------------------------------------------------
  # Temple hunt: game file 
  #-------------------------------------------------------------
  # Starting the game 
  if state == 'st001':
    print( "You are an intrepid explorer. Your goal is to reach the lost treasure that lies within the sacred temple. But it will not be easy." )
    print( "Do you wish to begin? y/n" )
    tr_new_state('st002')
    tr_new_state('st000')
    state = tr_user_choice_x2(">>",'y','st002','n','st000')
    continue

  # Three first choices offered to the player 
  if state == 'st002':
    print( "You enter the temple and reach a dark hallway. You follow it until you reach a crossroads. Do you wish to go left, right or straight? l/r/s." )
    tr_new_state('st100')
    tr_new_state('st200')
    tr_new_state('st300')
    state = tr_user_choice_x3(">>",'l','st100','r','st200','s','st300')
    continue

  #-------------------------------------------------------------
  # States 1xx:  
  #-------------------------------------------------------------
  # Enter the room, there are two doors 
  if state == 'st100':
    print( "You go left and enter a room. There are two doors. Which one will you take? l/r." )
    tr_new_state('st101')
    tr_new_state('st120')
    state = tr_user_choice_x2(">>",'l','st101','r','st120')
    continue

  # You took the left door
  if state == 'st101':
    print( "You take the left door and walk down a long hallway. As you walk, you notice a small room breaking off from the hallway." )
    print( "It appears to contain a chest. It could be a trap. Do you wish to enter the room and open the chest? y/n." )
    tr_new_state('st102')
    tr_new_state('st150')
    state = tr_user_choice_x2(">>",'y','st102','n','st150')
    continue

  # You entered the room and open the chest, you have 50% chance of surviving
  if state == 'st102':
    chance =random.randint(1,2)
    if ( chance == 1 ):
      tr_new_state('st103')
      state = 'st103'
      continue
    else:
      tr_new_state('st104')
      state = 'st104'
      continue

  # You open the chest and die 
  if state == 'st103':
    print( "You enter the room and open the chest. A trap triggers and sends an arrow hurtling into your chest. You are dead." )
    print( "Do you wish to play again? (y/n)" )
    tr_new_state('st001')
    tr_new_state('st000')
    state = tr_user_choice_x2(">>",'y','st001','n','st000')
    continue

  # You open the cheat and survive 
  if state == 'st104':
    print( "You enter the room and open the chest. It contains a sword. You now have the means to defend yourself." )
    print( "You exit the room and continue down the corridor. You reach a room. Inside is a fierce demon." )
    print( "Do you wish to fight the demon or do you wish to run and escape the temple empty-handed? f/r." )
    tr_new_state('st105')
    tr_new_state('st106')
    state = tr_user_choice_x2(">>",'r','st105','f','st106')
    continue

  # Run and escape
  if state == 'st105':
    print( "You run and escape the temple empty-handed." )
    print( "Do you wish to play again? (y/n)" )
    tr_new_state('st001')
    tr_new_state('st000')
    state = tr_user_choice_x2(">>",'y','st001','n','st000')
    continue

  # You fight with the weapon and win 
  if state == 'st106':
    print( "You are armed with a sword, so you easily defeat the demon. It was guarding a chest. Inside the chest is the lost treasure." )
    print( "Do you wish to play again? (y/n)" )
    tr_new_state('st001')
    tr_new_state('st000')
    state = tr_user_choice_x2(">>",'y','st001','n','st000')
    continue

  # You will die after taking the right door 
  if state == 'st120':
    print( "You take the right door and enter a small room. The doors closes behind you. You are trapped. You hear a noise from the ceiling and look up." )
    print( "The ceiling is lined with massive spikes and is slowly descending towards you. You are dead. Game over. Do you wish to restart? y/n." )
    tr_new_state('st001')
    tr_new_state('st000')
    state = tr_user_choice_x2(">>",'y','st001','n','st000')
    continue

  # You did not enter room, continue forward where the monster is
  if state == 'st150':
    print( "You do not enter the room and continue down the corridor. You reach a room. Inside is a fierce demon." )
    print( "Do you wish to fight the demon or do you wish to run and escape the temple empty-handed? f/r." )
    tr_new_state('st151')
    tr_new_state('st152')
    state = tr_user_choice_x2(">>",'f','st151','r','st152')
    continue

  # You fight but die because you don't have a weapon 
  if state == 'st151':
    print( "You are unarmed so the demon easily defeats you. You are dead. Do you wish to restart? y/n." )
    tr_new_state('st001')
    tr_new_state('st000')
    state = tr_user_choice_x2(">>",'y','st001','n','st000')
    continue

  # Runaway and lose 
  if state == 'st152':
    print( "You run away and lose. Do you wish to restart? y/n." )
    tr_new_state('st001')
    tr_new_state('st000')
    state = tr_user_choice_x2(">>",'y','st001','n','st000')
    continue

  #-------------------------------------------------------------
  # States 2xx:  
  #-------------------------------------------------------------
  # You turn right at the first branch 
  if state == 'st200':
    print( "You go right, down a long corridor. As you walk, you hear a series of load, ferocious screeches from behind you." )
    print( "You turn around to discover that a horde of flesh eating baboons are pursuing you. Do you want to run or fight? r/f." )
    tr_new_state('st201')
    tr_new_state('st202')
    state = tr_user_choice_x2(">>",'f','st201','r','st202')
    continue

  # You fight the baboons and die 
  if state == 'st201':
    print( "You attempt to fight the horde but you are no match for the baboons. They easily defeat you. You are dead. Do you wish to restart? y/n." )
    tr_new_state('st001')
    tr_new_state('st000')
    state = tr_user_choice_x2(">>",'y','st001','n','st000')
    continue

  # You run to avoid the baboons 
  if state == 'st202':
    print( "You run from the horde of baboons until you reach a crossroads. You do not have a lot of time to make a decision." )
    print( "Do you want to go left or right? l/r." )
    tr_new_state('st203')
    tr_new_state('st220')
    state = tr_user_choice_x2(">>",'r','st203','l','st220')
    continue

  # You made a turn right escaping the baboons, and come across a cloaked figure 
  if state == 'st203':
    print( "You run from the horde of baboons until you reach a crossroads. You do not have a lot of time to make a decision." )
    print( "You go right and run down a hallway until you reach a room. The baboons are still in pursuit. Within the room, stands a cloaked figure, wielding a sword." )
    print( "It defeats the horde of baboons and turns to you. It is beckoning you. Do you trust it? It may kill you. y/n." )
    tr_new_state('st204')
    tr_new_state('st205')
    state = tr_user_choice_x2(">>",'n','st204','y','st205')
    continue

  # You don't trust the cloaked figure and die 
  if state == 'st204':
    print( "You do not approach the dark figure. Angered, it transforms into a massive serpent and devours you." )
    print( "You are dead. Do you wish to restart? y/n." )
    tr_new_state('st001')
    tr_new_state('st000')
    state = tr_user_choice_x2(">>",'y','st001','n','st000')
    continue

  # You trust the cloaked figure 
  if state == 'st205':
    print( "You approach the dark figure. It is offering you help. Do you accept? y/n." )
    tr_new_state('st206')
    tr_new_state('st207')
    state = tr_user_choice_x2(">>",'n','st206','y','st207')
    continue

  # You die after you denied help 
  if state == 'st206':
    print( "You deny help and continue down a hallway, until you reach an uncrossable gulch." )
    print( "Suddenly, a swarm of poisonous hornets fly from the gulch and kill you. You are dead. Do you wish to restart? y/n." )
    tr_new_state('st001')
    tr_new_state('st000')
    state = tr_user_choice_x2(">>",'y','st001','n','st000')
    continue

  # You accept help and get rich 
  if state == 'st207':
    print( "You accept the dark figure's proposal and continue on down a hallway." )
    print( "You reach the gulch and use the rope to reach the other side. There, you find the lost treasure." )
    print( "You won but at the cost of a cut of the treasure. Do you wish to play again? y/n." )
    tr_new_state('st001')
    tr_new_state('st000')
    state = tr_user_choice_x2(">>",'y','st001','n','st000')
    continue

  # You went left to avoid the baboons
  if state == 'st220':
    print( "You go left and enter a room. The door closes behind you. You are trapped but safe from the horde of baboons." )
    print( "In the center of the room is an altar. Atop the altar are 3 buttons. You do not know what they do. The only thing to do is to push a button." )
    print( "Which button do you push? The left button, the right button or the middle button? l/r/m." )
    tr_new_state('st221')
    tr_new_state('st221')
    tr_new_state('st221')
    state = tr_user_choice_x3(">>",'l','st221','r','st221','m','st221')
    continue

  # First twist of the coin
  if state == 'st221':
    chance =random.randint(1,3)
    if ( chance == 1 ):
      tr_new_state('st223')
      state = 'st223'
      continue
    else:
      tr_new_state('st222')
      state = 'st222'
      continue

  # Second twist of the coin 
  if state == 'st222':
    chance =random.randint(1,2)
    if ( chance == 1 ):
      tr_new_state('st224')
      state = 'st224'
      continue
    else:
      tr_new_state('st225')
      state = 'st225'
      continue

  # First outcome 
  if state == 'st223':
    print( "You pressed the wrong button. The floor collapses beneath you and you fall into a pit of snakes. They eat you alive." )
    print( "You are dead. Do you wish to restart? y/n." )
    tr_new_state('st001')
    tr_new_state('st000')
    state = tr_user_choice_x2(">>",'y','st001','n','st000')
    continue

  # Second outcome 
  if state == 'st224':
    print( "You press the button and the door reopens behind you. You are no longer trapped but you let the baboons into the room." )
    print( "The horde of baboons enter the room and kill you. You are dead. Do you wish to restart? y/n." )
    tr_new_state('st001')
    tr_new_state('st000')
    state = tr_user_choice_x2(">>",'y','st001','n','st000')
    continue

  # Third outcome 
  if state == 'st225':
    print( "You pressed the right button. A door on the other side of the room opens, revealing a chest. Inside is the lost treasure." )
    print( "You won. Do you wish to play again? y/n." )
    tr_new_state('st001')
    tr_new_state('st000')
    state = tr_user_choice_x2(">>",'y','st001','n','st000')
    continue

  #-------------------------------------------------------------
  # States 3xx:  
  #-------------------------------------------------------------
  # After going straight you find a sword 
  if state == 'st300':
    print( "You go straight and reach a room containing an altar. On the altar is a sword. Do you want to take the sword? It could be a trap. y/n." )
    tr_new_state('st301')
    tr_new_state('st350')
    state = tr_user_choice_x2(">>",'y','st301','n','st350')
    continue

  # You take the sword 
  if state == 'st301':
    chance =random.randint(1,2)
    if ( chance == 1 ):
      tr_new_state('st302')
      state = 'st302'
      continue
    else:
      tr_new_state('st303')
      state = 'st303'
      continue

  # You take the sword, but it's a trap. You die
  if state == 'st302':
    print( "You try to take the sword but it is a trap. The trap triggers and sends a poison dart flying into your neck." )
    print( "You are dead. Do you wish to restart? y/n." )
    tr_new_state('st001')
    tr_new_state('st000')
    state = tr_user_choice_x2(">>",'y','st001','n','st000')
    continue

  # You take the sword and carry on
  if state == 'st303':
    print( "You take the sword from the altar but hear a growl behind you. You turn to face a massive ravenous jaguar." )
    print( "Do you want to fight the jaguar or do you want to run and escape the temple empty-handed? f/r." )
    tr_new_state('st304')
    tr_new_state('st305')
    state = tr_user_choice_x2(">>",'r','st304','f','st305')
    continue

  # You run from the jaguar and escape empty handed.
  if state == 'st304':
    print( "You run and escape the temple empty-handed. Do you wish to play again? y/n." )
    tr_new_state('st001')
    tr_new_state('st000')
    state = tr_user_choice_x2(">>",'y','st001','n','st000')
    continue

  # You fight the jaguar 
  if state == 'st305':
    print( "You turn to face the jaguar and raise your sword." )
    chance =random.randint(1,2)
    if ( chance == 1 ):
      tr_new_state('st306')
      state = 'st306'
      continue
    else:
      tr_new_state('st307')
      state = 'st307'
      continue

  # You fight the jaguar and die 
  if state == 'st306':
    print( "Despite wielding a sword, you are defeated and devoured by the jaguar. You are dead. Do you wish to play again? y/n." )
    tr_new_state('st001')
    tr_new_state('st000')
    state = tr_user_choice_x2(">>",'y','st001','n','st000')
    continue

  # You fight the jaguar and win 
  if state == 'st307':
    print( "You defeat the jaguar and notice a key strapped to one of it's legs. You take the key and notice a chest sitting in the corner of the room." )
    print( "You open the chest and claim the lost treasure. You won. Do you wish to play again? y/n." )
    tr_new_state('st001')
    tr_new_state('st000')
    state = tr_user_choice_x2(">>",'y','st001','n','st000')
    continue

  # You don't take the sword 
  if state == 'st350':
    print( "You do not take the sword and hear a growl behind you. You turn to face a massive ravenous jaguar." )
    print( "Do you want to fight the jaguar, despite having no weapons, or do you want to run and escape the temple empty-handed? f/r." )
    tr_new_state('st351')
    tr_new_state('st352')
    state = tr_user_choice_x2(">>",'r','st351','f','st352')
    continue

  # You run away from the jaguar without the sword 
  if state == 'st351':
    print( "You run and escape the temple empty-handed. Do you wish to play again? y/n." )
    tr_new_state('st001')
    tr_new_state('st000')
    state = tr_user_choice_x2(">>",'y','st001','n','st000')
    continue

  # You fight with the juaguar without the sword 
  if state == 'st352':
    chance =random.randint(1,9)
    if ( chance == 1 ):
      tr_new_state('st353')
      state = 'st353'
      continue
    else:
      tr_new_state('st354')
      state = 'st354'
      continue

  # You fight and win 
  if state == 'st353':
    print( "Despite the odds, you defeated the jaguar without a weapon and notice a key strapped to one of it's legs." )
    print( "You take the key and notice a chest sitting in the corner of the room. You open the chest and claim the lost treasure." )
    print( "You won. Do you want to play again? y/n." )
    tr_new_state('st001')
    tr_new_state('st000')
    state = tr_user_choice_x2(">>",'y','st001','n','st000')
    continue

  # You fight and die 
  if state == 'st354':
    print( "As you do not have a weapon, the jaguar easily defeats you. You are dead. Do you wish to play again? y/n." )
    tr_new_state('st001')
    tr_new_state('st000')
    state = tr_user_choice_x2(">>",'y','st001','n','st000')
    continue

