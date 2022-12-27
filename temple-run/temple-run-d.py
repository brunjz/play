#!/usr/bin/env python3
#Game Name: Temple Hunt. (254 lines of code).

#Random is imported:
import random

#Loop is set to false until game is initiated:
loop = False

#Function to capture user input (2 parameters):
def user_input_x2(question_str,arg1,arg2):
    arg = ""
    while(arg != arg1 and arg != arg2):
        arg = input(question_str).lower()
    return (arg)
    
#Function to capture user input (3 parameters):
def user_input_x3(question_str,arg1,arg2,arg3):
    arg = ""
    while(arg != arg1 and arg != arg2 and arg != arg3):
        arg = input(question_str).lower()
    return (arg)

#This is the introduction:
print("You are an intrepid explorer. Your goal is to reach the lost treasure that lies within the sacred temple. But it will not be easy.")

#While True loop is initiated:
while True:
    begin = user_input_x2("Do you wish to begin? y/n.","y","n")
    
    if begin == "y":
        #Loop variable is set to true:
        loop = True
    #while loop is created:
    while loop:        

        if begin == "y":
            #This is where the player chooses which of the 3 branches to take:
            choice1=user_input_x3("You enter the temple and reach a dark hallway. You follow it until you reach a crossroads. Do you wish to go left, right or straight? l/r/s.","l","r","s")

            #Branch 1 (l):
            if choice1=="l":
                leftchoice1 = user_input_x2("You go left and enter a room. There are two doors. Which one will you take? l/r.","l","r")
                if leftchoice1 == "l":
                    print("You take the left door and walk down a long hallway. As you walk, you notice a small room breaking off from the hallway.")
                    leftchoice2=user_input_x2("It appears to contain a chest. It could be a trap. Do you wish to enter the room and open the chest? y/n.","y","n")
                    if leftchoice2=="y":
                        number=random.randint(1, 2) 
                        if number == 2:
                            print ("You enter the room and open the chest. It contains a sword. You now have the means to defend yourself.")
                            print("You exit the room and continue down the corridor. You reach a room. Inside is a fierce demon.")
                            left3=user_input_x2("Do you wish to fight the demon or do you wish to run and escape the temple empty-handed? f/r.","f","r")
                            if left3 == "f":
                                print("You are armed with a sword, so you easily defeat the demon. It was guarding a chest. Inside the chest is the lost treasure.")
                                restart=user_input_x2("You the won the game. Do you wish to play again? y/n.","y","n")
                                if restart == "y":
                                    loop = False
                                elif restart == "n": 
                                    print("Exiting game.")
                                    quit()
                            elif left3 == "r":
                                restart=user_input_x2("You run and escape the temple empty-handed. Do you wish to play again? y/n.","y","n")
                                if restart == "y":
                                    loop = False
                                elif restart == "n":
                                    print("Exiting game.")
                                    quit()                                                           
                        elif number == 1:
                            print("You enter the room and open the chest. A trap triggers and sends an arrow hurtling into your chest. You are dead.")
                            restart=user_input_x2("Do you wish to restart? y/n.","y","n")
                            if restart == "y":
                                loop = False
                            elif restart == "n":
                                print("Exiting game.")
                                quit()
                    elif leftchoice2 == "n":
                        print("You do not enter the room and continue down the corridor. You reach a room. Inside is a fierce demon.")
                        left3=user_input_x2("Do you wish to fight the demon or do you wish to run and escape the temple empty-handed? f/r.","f","r")
                        if left3 == "f":
                            restart=user_input_x2("You are unarmed so the demon easily defeats you. You are dead. Do you wish to restart? y/n.","y","n")
                            if restart == "y":
                                loop = False
                            elif restart == "n":
                                print("Exiting game.")
                                quit()
                        elif left3 == "r":
                            restart=user_input_x2("You run and escape the temple empty-handed. Do you wish to play again? y/n.","y","n")
                            if restart == "y":
                                loop = False
                            elif restart == "n":
                                print("Exiting game.")
                                quit()
                            
                #Branch 2 (r):    
                elif leftchoice1 == "r":
                    print("You take the right door and enter a small room. The doors closes behind you. You are trapped. You hear a noise from the ceiling and look up.")
                    restart=user_input_x2("The ceiling is lined with massive spikes and is slowly descending towards you. You are dead. Game over. Do you wish to restart? y/n.","y","n")
                    if restart == "y":
                        loop = False
                    elif restart == "n":
                        print("Exiting game.")
                        quit()
            elif choice1 == "r":
                print("You go right, down a long corridor. As you walk, you hear a series of load, ferocious screeches from behind you.")
                rightchoice1=user_input_x2("You turn around to discover that a horde of flesh eating baboons are pursuing you. Do you want to run or fight? r/f.","r","f")
                if rightchoice1 == "f":
                    restart=user_input_x2("You attempt to fight the horde but you are no match for the baboons. They easily defeat you. You are dead. Do you wish to restart? y/n.","y","n")
                    if restart == "y":
                        loop = False
                    elif restart == "n":
                        print("Exiting game.")
                        quit()
                elif rightchoice1 == "r":
                    print("You run from the horde of baboons until you reach a crossroads. You do not have a lot of time to make a decision.")
                    rightchoice2=user_input_x2("Do you want to go left or right? l/r.","l","r")
                    if rightchoice2 == "r":
                        print("You go right and run down a hallway until you reach a room. The baboons are still in pursuit. Within the room, stands a cloaked figure, wielding a sword.")
                        approach=user_input_x2("It defeats the horde of baboons and turns to you. It is beckoning you. Do you trust it? It may kill you. y/n.","y","n")
                        if approach == "n":
                            print("You do not approach the dark figure. Angered, it transforms into a massive serpent and devours you.")
                            restart=user_input_x2("You are dead. Do you wish to restart? y/n.","y","n")
                            if restart == "y":
                                loop = False
                            elif restart == "n":
                                print("Exiting game.")
                                quit()
                        elif approach == "y":
                            gethelp=user_input_x2("You approach the dark figure. It is offering you help. Do you accept? y/n.","y","n")
                            if gethelp == "y":
                                print ("The dark figure hands you a rope. Then, in a low, croaky voice, it speaks. 'Ahead lies a gulch. With this rope, you can cross it'.")
                                print("'Beyond the gulch lies the lost treasure. As a payment for my assistance, I want an 80% cut of the gold.'")
                                accept=user_input_x2("Do you accept the dark figure's proposal? y/n.","y","n")
                                if accept == "n":
                                    restart=user_input_x2("Angered, it brandishes it's sword and cuts you down. You are dead. Do you wish to restart? y/n.","y","n")
                                    if restart == "y":
                                        loop = False
                                    elif restart == "n":
                                        print("Exiting game.")
                                        quit()
                                elif accept == "y":
                                    print("You accept the dark figure's proposal and continue on down a hallway.")
                                    print("You reach the gulch and use the rope to reach the other side. There, you find the lost treasure.")
                                    restart=user_input_x2("You won but at the cost of a cut of the treasure. Do you wish to play again? y/n.","y","n")
                                    if restart == "y":
                                        loop = False
                                    elif restart == "n":
                                        print("Exiting game.")
                                        quit()              
                            elif gethelp == "n":
                                print("You deny it's help and continue down a hallway, until you reach an uncrossable gulch.")
                                restart=user_input_x2("Suddenly, a swarm of poisonous hornets fly from the gulch and kill you. You are dead. Do you wish to restart? y/n.","y","n")
                                if restart == "y":
                                    loop = False
                                elif restart == "n":
                                    print("Exiting game.")
                                    quit()
                    elif rightchoice2 == "l":
                        print("You go left and enter a room. The door closes behind you. You are trapped but you are safe from the horde of baboons.")
                        print("In the center of the room is an altar. Atop the altar are 3 buttons. You do not know what they do. The only thing to do is to push a button.")
                        number=random.randint(1, 3)
                        button=user_input_x3("Which button do you push? The left button, the right button or the middle button? l/r/m.","l","r","m")
                        if button == "l" or "r" or "m":
                            if number == 1:
                                print("You pressed the wrong button. The floor collapses beneath you and you fall into a pit of snakes. They eat you alive.")
                                restart=user_input_x2("You are dead. Do you wish to restart? y/n.","y","n")
                                if restart == "y":
                                    loop = False
                                elif restart == "n":
                                    print("Exiting game.")
                                    quit()
                            elif number == 2:
                                print("You press the button and the door reopens behind you. You are no longer trapped but you let the baboons into the room.")
                                restart=user_input_x2("The horde of baboons enter the room and kill you. You are dead. Do you wish to restart? y/n.","y","n")
                                if restart == "y":
                                    loop = False
                                elif restart == "n":
                                    print("Exiting game.")
                                    quit()
                            elif number == 3:
                                print("You pressed the right button. A door on the other side of the room opens, revealing a chest. Inside is the lost treasure.")
                                restart=user_input_x2("You won. Do you wish to play again? y/n.","y","n")
                                if restart == "y":
                                    loop = False
                                elif restart == "n":
                                    print("Exiting game.")
                                    quit()
            #Branch 3 (s):                        
            elif choice1 == "s":
                sword=user_input_x2("You go straight and reach a room containing an altar. On the altar is a sword. Do you want to take the sword? It could be a trap. y/n.","y","n")
                if sword == "y":
                    number=random.randint(1, 2)
                    if number == 1:
                        print("You try to take the sword but it is a trap. The trap triggers and sends a poison dart flying into your neck.")
                        restart=user_input_x2("You are dead. Do you wish to restart? y/n.","y","n")
                        if restart == "y":
                            loop = False
                        elif restart == "n":
                            print("Exiting game.")
                            quit()
                    elif number == 2:
                        print("You take the sword from the altar but hear a growl behind you. You turn to face a massive ravenous jaguar.")
                        run=user_input_x2("Do you want to fight the jaguar or do you want to run and escape the temple empty-handed? f/r.","f","r")
                        if run == "r":
                            restart=user_input_x2("You run and escape the temple empty-handed. Do you wish to play again? y/n.","y","n")
                            if restart == "y":
                                loop = False
                            elif restart == "n":
                                print("Exiting game.")
                                quit()
                        elif run == "f":
                            print("You turn to face the jaguar and raise your sword.")
                            number2=random.randint(1,2)
                            if number2 == 1:
                                restart=user_input_x2("Despite wielding a sword, you are defeated and devoured by the jaguar. You are dead. Do you wish to play again? y/n.","y","n")
                                if restart == "y":
                                    loop = False
                                elif restart == "n":
                                    print ("Exiting game.")
                                    quit()
                            elif number2 == 2:
                                print("You defeat the jaguar and notice a key strapped to one of it's legs. You take the key and notice a chest sitting in the corner of the room.")
                                restart=user_input_x2("You open the chest and claim the lost treasure. You won. Do you wish to play again? y/n.","y","n")
                                if restart == "y":
                                    loop = False
                                elif restart == "n":
                                    print("Exiting game.")
                                    quit()
                elif sword == "n":
                    print ("You do not take the sword and hear a growl behind you. You turn to face a massive ravenous jaguar.")
                    run2=user_input_x2("Do you want to fight the jaguar, despite having no weapons, or do you want to run and escape the temple empty-handed? f/r.","f","r")
                    if run2 == "r":
                        restart=user_input_x2("You run and escape the temple empty-handed. Do you wish to play again? y/n.","y","n")
                        if restart == "y":
                            loop = False
                        elif restart == "n":
                            print("Exiting game.")
                            quit()
                    elif run2 == "f":
                        number3=random.randint(1, 10)
                        if number3 == 7:
                            print("Despite the odds, you defeated the jaguar without a weapon and notice a key strapped to one of it's legs.")
                            print("You take the key and notice a chest sitting in the corner of the room. You open the chest and claim the lost treasure.")
                            restart=user_input_x2("You won. Do you want to play again? y/n.","y","n")
                            if restart == "y":
                                loop = False
                            elif restart == "n":
                                print("Exiting game.")
                                quit()
                        elif number3 != 7:
                            restart=user_input_x2("As you do not have a weapon, the jaguar easily defeats you. You are dead. Do you wish to play again? y/n.","y","n")
                            if restart == "y":
                                loop = False
                            elif restart == "n":
                                print("Exiting game.")
                                quit()
                            
                                

                
                
                        
    
        
    
                                    
                            
                            
                                
                            
                        
                        
                                        
                                                
                                                
                                            
                                            
                                
                                
                        
                        
                
        
            
            
                
                
                
                
        
    

