#!/usr/bin/env python3

"""
Temple hunt - this programs parses an input command file to generate an executable
"""

import re
import getopt 
import sys 

#----------------------------------------------------------------- 
# print_header: print the python file header 
def print_header():

  print("#!/usr/bin/env python3",file=fout)
  print("import re",file=fout)
  print("import random",file=fout)

  return()

#----------------------------------------------------------------- 
# print_functions: print functions used in the program 
def print_functions():

  print("""

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
  """,
  file=fout)

#----------------------------------------------------------------- 
# print_start: prints the initial code
def print_start():

  print( """
##################################################################
# Main
##################################################################

valid_states = ['st000','st001']
state = 'st001';

# Program loop 
while True:

  # Check current state is valid
  if state not in valid_states:
    print(\"ERROR, not a valid state\",state)
    quit()

  # Exit the game
  if state == 'st000':
     tr_end_game(\"ending the game\")
  """,file=fout)

  return()


##################################################################
# Main
##################################################################

linenb = 0
verbose = 0

# Command line arguments
 
opts,args = getopt.getopt(sys.argv[1:],"hvi:")
for opt, arg in opts:
  if opt in ['-h']:
    print("temple-run-gen.py [-h][-v][-i ifile]")
    exit()
  elif opt in ['-v']:
    verbose = 1
  elif opt in ['-i']:
    fnamein = arg
    print("temple-run-gen.py: processing file",fnamein)

# Proces file 

fin = open(fnamein,"r")
fout= open("temple-run-play.py","w")

print_header()
print_functions()
print_start()


for line in fin:

  linenb = linenb + 1

  if (verbose):
    print("** new line",line)

  # First isolate comments
  mcomm = re.findall("(\s*#.*)",line)
  if len(mcomm) == 1:
    print("  "+mcomm[0],file=fout)

  # Process all non-comments 
  else:

    # Processing state field 
    mstate = re.findall("^\s*(st[0-9]+)\s*:\s*$",line)
    if (verbose):
      print(mstate)
    if len(mstate) == 1:
      print("  if state == \'" + mstate[0] + "\':",file=fout)
    elif len(mstate) > 1:
      print("ERROR: state field syntax error on line",linenb) 
      quit

    # Processing print field 
    mprint = re.findall("\s+print\s*:\s*(\".*\")\s*",line)
    if (verbose):
      print(mprint)
    if len(mprint) == 1:
      print("    print(",mprint[0],")",file=fout)
    elif len(mprint) > 1:
      print("ERROR: print field syntax error on line",linenb) 
      quit

    # Processing next field - rand choice 
    mrand = re.findall("^\s+next\s*:\s*rand\(([0-9]):([0-9])\)\s+goto\s+(\w+)\s+(\w+)\s*",line)
    if (verbose):
      print(mrand)
    if len(mrand) == 1:
      print("    chance =random.randint("+mrand[0][0]+","+mrand[0][1]+")",file=fout)
      print("    if ( chance == "+mrand[0][0]+" ):",file=fout)
      print("      tr_new_state(\'"+mrand[0][2]+"\')",file=fout)
      print("      state = \'"+mrand[0][2]+"\'",file=fout)
      print("      continue",file=fout)
      print("    else:",file=fout)
      print("      tr_new_state(\'"+mrand[0][3]+"\')",file=fout)
      print("      state = \'"+mrand[0][3]+"\'",file=fout) 
      print("      continue",file=fout)
      print("",file=fout)
    elif len(mprint) > 1:
      print("ERROR: print field syntax error on line",linenb) 
      quit

    # Processing next field - if statement 
    mnext = re.findall('if\s+(\w+)\s+goto\s+(\w+)',line)
    mnextchk = re.findall('^\s+next\s*:',line)
    if (verbose):
      print(mnext,len(mnext))
    if len(mnext) == 2 and len(mnextchk) == 1:
      print("    tr_new_state(\'"+mnext[0][1]+"\')",file=fout)
      print("    tr_new_state(\'"+mnext[1][1]+"\')",file=fout)
      print("    state = tr_user_choice_x2(\">>\",\'"+mnext[0][0]+"\',\'"+mnext[0][1]+"\',\'"+mnext[1][0]+"\',\'"+mnext[1][1]+"\')",file=fout)
      print("    continue",file=fout)
      print("",file=fout)
    elif len(mnext) == 3 and len(mnextchk) == 1:
      print("    tr_new_state(\'"+mnext[0][1]+"\')",file=fout)
      print("    tr_new_state(\'"+mnext[1][1]+"\')",file=fout)
      print("    tr_new_state(\'"+mnext[2][1]+"\')",file=fout)
      print("    state = tr_user_choice_x3(\">>\",\'"+mnext[0][0]+"\',\'"+mnext[0][1]+"\',\'"+mnext[1][0]+"\',\'"+mnext[1][1]+"\',\'"+mnext[2][0]+"\',\'"+mnext[2][1]+"\')",file=fout)
      print("    continue",file=fout)
      print("",file=fout)
    elif len(mnext) > 1:
      print("ERROR: next field syntax error one line",linenb) 
      quit

fin.close()
fout.close()






