"""
PLEASE DO NOT EDIT THIS
Final project
text adventure game
...
author : mr Truong
"""
from random import randint
name = ""#variable for character name
monster1HP = randint(10,20)
playerHP = 100
inventory = ["cheap sword"]
gold = 0


def startGame():#first scene of the adventure
  global name #allows the use of the name variable in line 7 so it doesn't overwrite with a local variable
  name = input("You are a Py-ian, a villager of Codeia. What is your name? ")
  adventure = input("\nHello " + name +" Do you want to go on an adventure? Type in yes or no.")

  if adventure == "yes":#be careful with the case of the input consider error checking here
    goAdventure()#calls the next scene in the game
  else:
	  print("\n" + name.upper() + "!!! You\'re lame and live out your life in boredom!!")#ends the game with a lame message
		
def goAdventure():
  global name
  
  choice = int(input("\n" + name + """ Do you want to go to the forest or the mountain?\n
Options - selecet the number you want to do:
	  1. go to the forest
	  2. go to the mountain
	  Choice: """))
	  
	  #check user input to find out what function to call next
  if(choice == 1):
    goToForest()
  elif(choice == 2):
    goToMountain()

def goToForest():
	print("\nYou head to the dark ...")
	#BE CAREFUL WITH CASE WHEN TAKING IN STRING INPUT
	choice = input("\nDo you take the long route or the short route?")
	
	#a type of error check - forces user to goToMountain if incorrect string is entered
	if choice == "short":
		getLost()
	else:  
		goToMountain()
		
def goToMountain():
  global monster1HP #allows the use of global variables
  global playerHP
  global inventory
  global gold
  
  print("\nYou have reach the mountain of the BlahBas ")
    
  
  if(monster1HP > 0):
    print("you see a giant heading your way and he wants to crush you!")
    choice = int(input("""
    What do you do?
    options:
    1. Run 
    2. Check you Inventory
    3. Hit giant with sword"""))
    
    if (choice == 1):
      getLost()
    elif (choice == 2):
      print("\nInventory: ")
      print(inventory)
      goToMountain()
    elif (choice == 3):
      #you attack giant
      dmg =100 #randint(1,10);
      print("\nYou attack with your sword and do " + str(dmg) + " to the giant!!")
      monster1HP = monster1HP - dmg
      print("\nGiant has " + str(monster1HP) + " remaining")
      
      #giant attacks You
      dmg = randint(1,10);
      print("\nGiant attacks you with a club and does " + str(dmg) + " to you!!")
      playerHP = playerHP - dmg
      print("\nYou Have " + str(playerHP) + " remaining")
      goToMountain()
  
  elif(playerHP <= 0 ):
    print("\nthe giant killed you. start the game again")
    startGame()
  else:
	  choice = int(input("""
	  You defeated the giant and lies lifeless at your feet
    What do you do?
    options:
    1. search the giant for loot
    2. continue down the trail
    3. turn back to the forest
    Choice: 
    """))
	  if (choice == 1):#be careful of looping bug here
	    print("\nYou find 10 gold pieces")
	    gold = gold + 10
	    goToMountain()
	  elif (choice == 2):
	    winGame()#you wouldn't actually win the game here as it is too early but this is just an example so it's ending here.
	  else:
	    goToForest()#loops back to different part of game

def getLost():#end of game
	print("\nYou got lost... and die! sorry")

def winGame():#end of game
  print("\nYou win!! game over")

# Create more functions to complete the game

# Don't forget to call the startGame function!  
startGame()
