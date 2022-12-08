#!/usr/bin/env python3

import random

valid_states = [0,1]
die_states = []
state = 1;

#---------------------------------------------------------------
# function tr_user_choice_x2 
def tr_user_choice_x2 (question_str,choice_a,state_a,choice_b,state_b):

  user_input = input(question_str).lower()
  while (user_input != choice_a and user_input != choice_b):
    user_input = input(question_str).lower()
  if user_input == choice_a:
    mystate = state_a
  elif user_input == choice_b:
    mystate = state_b

  return(mystate)

#---------------------------------------------------------------
# function tr_user_choice_x3 
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

#---------------------------------------------------------------
# function tr_end_game
def tr_end_game (text_print):

    print(text_print)
    quit()

#---------------------------------------------------------------
# function tr_new_state 
def tr_new_state (mystate):

    valid_states.append(mystate)
    return()

#---------------------------------------------------------------
# function die_state 
def die_state (mystate):

    die_states.append(mystate)
    return()



################################################################ 
# main program 

while True :

  # Check current state is valid
  if state not in valid_states:
      print("ERROR, not a valid state",state)
      quit()

  # Check for dying state 
  if state in die_states:
    tr_end_game("You entered a die state")

  # [STATE 0] exit game 
  if state == 0:
     tr_end_game("ending the game")

  # [STATE 1] starting the game 
  #   yes -> 2
  #   no -> 0 (leave) 
  if state == 1:
    print("You are an intrepid explorer. Your goal is to reach the lost treasure that lies within the sacred temple. But it will not be easy.")
    tr_new_state(2)
    str = "Do you wish to begin? (y/n)"
    state = tr_user_choice_x2(str,"y",2,"n",0)
    continue

  # [STATE 2] three options provided to the user 
  #   left -> 100 
  #   right -> 200 
  #   straight -> 300
  if state == 2:
    tr_new_state(100)
    tr_new_state(200)
    tr_new_state(300)
    str = "You enter the temple and reach a dark hallway. You follow it until you reach a crossroads. Do you wish to go left, right or straight? l/r/s."
    state = tr_user_choice_x3(str,"l",100,"r",200,"s",300)
    continue

  #-------------------------------------------------------------
  # States 1xx:  
  #-------------------------------------------------------------

  # [STATE 100] enter the room, there are two doors 
  #   l -> 101
  #   r -> 120: you will die
  if state == 100:
    tr_new_state(101)
    tr_new_state(120)
    str = "You go left and enter a room. There are two doors. Which one will you take? l/r."
    state = tr_user_choice_x2(str,"l",101,"r",120)
    continue

  # [STATE 101] you took the left door
  #   y -> 103
  #   n -> 150 
  if state == 101:
    tr_new_state(103)
    tr_new_state(150)
    print("You take the left door and walk down a long hallway. As you walk, you notice a small room breaking off from the hallway.")
    str = "It appears to contain a chest. It could be a trap. Do you wish to enter the room and open the chest? y/n."
    state = tr_user_choice_x2(str,"y",103,"n",150)
    continue

  # [STTE 103] you entered the room, 50% chance of surviving
  #   die -> 0 
  #   survive -> 104 or 105 
  if state == 103:
    chance = random.choice(["chance0","chance1"])
    if chance == "chance1":
       print("You enter the room and open the chest. A trap triggers and sends an arrow hurtling into your chest. You are dead.")
       str = "Do you wish to play again? (y/n)"
       state = tr_user_choice_x2(str,"y",1,"n",0)
       continue
    else:
      tr_new_state(105)
      tr_new_state(106)
      print("You enter the room and open the chest. It contains a sword. You now have the means to defend yourself.")
      print("You exit the room and continue down the corridor. You reach a room. Inside is a fierce demon.")
      str = "Do you wish to fight the demon or do you wish to run and escape the temple empty-handed? f/r."
      state = tr_user_choice_x2(str,"r",105,"f",106)
      continue

  # [STATE 105] run and escape, but you'll die 
  #   y -> 1: restart the game
  #   n -> 0: leave
  if state == 105:
     print("You run and escape the temple empty-handed.")
     str = "Do you wish to play again? (y/n)"
     state = tr_user_choice_x2(str,"y",1,"n",0)
     continue

  # [STATE 106] you fight with the weapon and win 
  #   y -> 1: restart the game
  #   n -> 0: leave
  if state == 106:
     print("You are armed with a sword, so you easily defeat the demon. It was guarding a chest. Inside the chest is the lost treasure.")
     str = "Do you wish to play again? (y/n)"
     state = tr_user_choice_x2(str,"y",1,"n",0)
     continue

  # [STATE 120] you will die 
  #   yes -> 1: restart 
  #   no -> 0: exit game 
  if state == 120:
     print("You take the right door and enter a small room. The doors closes behind you. You are trapped. You hear a noise from the ceiling and look up.")
     str = "The ceiling is lined with massive spikes and is slowly descending towards you. You are dead. Game over. Do you wish to restart? y/n."
     state = tr_user_choice_x2(str,"y",1,"n",0)
     continue

  # [STATE 150] you did not enter room, continue forward where the monster is
  #   f -> 151: you die because you don't have a weapon 
  #   r -> 152: you loose 
  if state == 150:
    tr_new_state(151)
    tr_new_state(152)
    print("You do not enter the room and continue down the corridor. You reach a room. Inside is a fierce demon.")
    str = "Do you wish to fight the demon or do you wish to run and escape the temple empty-handed? f/r."
    state = tr_user_choice_x2(str,"f",151,"r",152)
    continue

  # [STATE 151] you fight but die because you don't have a weapon 
  if state == 151:
     str= "You are unarmed so the demon easily defeats you. You are dead. Do you wish to restart? y/n."
     state = tr_user_choice_x2(str,"y",1,"n",0)
     continue

  # [STATE 152] runaway and loose 
  if state == 152:
     tr_end_game("You run away and loose")
     continue


  #-------------------------------------------------------------
  # States 2xx:  
  #-------------------------------------------------------------

  # [STATE 200] you turn right at the first branch 
  #   f -> 201: fight 
  #   r -> 202: run
  if state == 200:
    tr_new_state(201)
    tr_new_state(202)
    print("You go right, down a long corridor. As you walk, you hear a series of load, ferocious screeches from behind you.")
    str = "You turn around to discover that a horde of flesh eating baboons are pursuing you. Do you want to run or fight? r/f."
    state = tr_user_choice_x2(str,"f",201,"r",202)
    continue

  # [STATE 201] you fight the baboons and die 
  if state == 201:
     str = "You attempt to fight the horde but you are no match for the baboons. They easily defeat you. You are dead. Do you wish to restart? y/n."
     state = tr_user_choice_x2(str,"y",1,"n",0)
     continue

  # [STATE 202] you run to avoid the baboons 
  #   r -> 203 
  #   l -> 220
  if state == 202:
    tr_new_state(203)
    tr_new_state(220)
    print("You run from the horde of baboons until you reach a crossroads. You do not have a lot of time to make a decision.")
    str = "Do you want to go left or right? l/r."
    state = tr_user_choice_x2(str,"r",203,"l",220)
    continue

  # [STATE 203] you have have a turn right escaping the baboons 
  #   n -> 204:you don't trust
  #   y -> 205. you trust 
  if state == 203:
    tr_new_state(204)
    tr_new_state(205)
    print("You run from the horde of baboons until you reach a crossroads. You do not have a lot of time to make a decision.")
    print("You go right and run down a hallway until you reach a room. The baboons are still in pursuit. Within the room, stands a cloaked figure, wielding a sword.")
    str = "It defeats the horde of baboons and turns to you. It is beckoning you. Do you trust it? It may kill you. y/n."
    state = tr_user_choice_x2(str,"n",204,"y",205)
    continue

  # [STATE 204] you don't trust the cloaked figure and die 
  if state == 204:
    print("You do not approach the dark figure. Angered, it transforms into a massive serpent and devours you.")
    str = "You are dead. Do you wish to restart? y/n."
    state = tr_user_choice_x2(str,"y",1,"n",0)
    continue

  # [STATE 205] you trust the cloaked figure 
  #   n -> 206: refuse help
  #   y -> 207. accept help 
  if state == 205:
    tr_new_state(206)
    tr_new_state(207)
    str = "You approach the dark figure. It is offering you help. Do you accept? y/n."
    state = tr_user_choice_x2(str,"n",206,"y",207)
    continue

  # [STATE 206] die because you denied help 
  if state == 206:
    print("You deny it's help and continue down a hallway, until you reach an uncrossable gulch.")
    str = "Suddenly, a swarm of poisonous hornets fly from the gulch and kill you. You are dead. Do you wish to restart? y/n."
    state = tr_user_choice_x2(str,"y",1,"n",0)
    continue

  # [STATE 207] accept help and get rich 
  if state == 207:
    print("You accept the dark figure's proposal and continue on down a hallway.")
    print("You reach the gulch and use the rope to reach the other side. There, you find the lost treasure.")
    str = "You won but at the cost of a cut of the treasure. Do you wish to play again? y/n."
    state = tr_user_choice_x2(str,"y",1,"n",0)
    continue

  # [STATE 220] you went left to avoid the baboons 
  if state == 220:
    print("You go left and enter a room. The door closes behind you. You are trapped but you are safe from the horde of baboons.")
    print("In the center of the room is an altar. Atop the altar are 3 buttons. You do not know what they do. The only thing to do is to push a button.")
    input("Which button do you push? The left button, the right button or the middle button? l/r/m.")
    number=random.randint(1, 3)
    if number == 1:
      print("You pressed the wrong button. The floor collapses beneath you and you fall into a pit of snakes. They eat you alive.")
      str = "You are dead. Do you wish to restart? y/n."
      state = tr_user_choice_x2(str,"y",1,"n",0)
      continue
    elif number == 2:
      print("You press the button and the door reopens behind you. You are no longer trapped but you let the baboons into the room.")
      str = "The horde of baboons enter the room and kill you. You are dead. Do you wish to restart? y/n."
      state = tr_user_choice_x2(str,"y",1,"n",0)
      continue
    else:
      print("You pressed the right button. A door on the other side of the room opens, revealing a chest. Inside is the lost treasure.")
      str = "You won. Do you wish to play again? y/n."
      state = tr_user_choice_x2(str,"y",1,"n",0)
      continue

  #-------------------------------------------------------------
  # States 3xx:  
  #-------------------------------------------------------------

  # [STATE 300] after going straight you find a sword 
  #   y -> 301: take the sword 
  #   n -> 350: don't take the sword
  if state == 300:
    tr_new_state(301) 
    tr_new_state(350) 
    str = "You go straight and reach a room containing an altar. On the altar is a sword. Do you want to take the sword? It could be a trap. y/n."
    state = tr_user_choice_x2(str,"y",301,"n",350)
    continue

  # [STATE 301] you take the sword 
  if state == 301:
    number=random.randint(1,2)
    if number == 1:
      print("You try to take the sword but it is a trap. The trap triggers and sends a poison dart flying into your neck.")
      str = "You are dead. Do you wish to restart? y/n."
      state = tr_user_choice_x2(str,"y",1,"n",0)
      continue
    elif number == 2:
      tr_new_state(302) 
      tr_new_state(303) 
      print("You take the sword from the altar but hear a growl behind you. You turn to face a massive ravenous jaguar.")
      str = "Do you want to fight the jaguar or do you want to run and escape the temple empty-handed? f/r."
      state = tr_user_choice_x2(str,"r",302,"f",303)
      continue

  # [STATE 302] you run from the jaguar and escape empty handed.
  if state == 302:
     str= "You run and escape the temple empty-handed. Do you wish to play again? y/n."
     state = tr_user_choice_x2(str,"y",1,"n",0)
     continue

  # [STATE 303] you fight the jaguar 
  if state == 303:
    print("You turn to face the jaguar and raise your sword.")
    number = random.randint(1,2)
    if number == 1:
      str = "Despite wielding a sword, you are defeated and devoured by the jaguar. You are dead. Do you wish to play again? y/n."
      state = tr_user_choice_x2(str,"y",1,"n",0)
      continue
    else:
       print("You defeat the jaguar and notice a key strapped to one of it's legs. You take the key and notice a chest sitting in the corner of the room.")
       str = "You open the chest and claim the lost treasure. You won. Do you wish to play again? y/n."
       state = tr_user_choice_x2(str,"y",1,"n",0)
       continue

  # [STATE 350] you don't take the sword 
  if state == 350:
    tr_new_state(351) 
    tr_new_state(352) 
    print ("You do not take the sword and hear a growl behind you. You turn to face a massive ravenous jaguar.")
    str = "Do you want to fight the jaguar, despite having no weapons, or do you want to run and escape the temple empty-handed? f/r."
    state = tr_user_choice_x2(str,"r",351,"f",352)
    continue

  # [STATE 351] you run from the jaguar without the sword 
  if state == 351:
    str = "You run and escape the temple empty-handed. Do you wish to play again? y/n."
    state = tr_user_choice_x2(str,"y",1,"n",0)
    continue

  # [STATE 352] you fight with the juaguar without the sword 
  if state == 352:
    number = random.randint(1, 10)
    if number == 7:
      print("Despite the odds, you defeated the jaguar without a weapon and notice a key strapped to one of it's legs.")
      print("You take the key and notice a chest sitting in the corner of the room. You open the chest and claim the lost treasure.")
      str = "You won. Do you want to play again? y/n."
      state = tr_user_choice_x2(str,"y",1,"n",0)
      continue
    else: 
      str = "As you do not have a weapon, the jaguar easily defeats you. You are dead. Do you wish to play again? y/n."
      state = tr_user_choice_x2(str,"y",1,"n",0)
      continue
