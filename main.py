"""
PLEASE DO NOT EDIT THIS
Final project
text adventure game
...
author : mr Truong
p1 basic scenes
p2 fight
p3 add new scene
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
  adventure = input("\nHello " + name +" Do you want to go on an adventure? \nEnter 1 for yes or 2 for No. > ")

  if adventure == "1":#remember input is in string format
    goAdventure()#calls the next scene in the game
  else:
      print("\n" + name.upper() + "!!! You\'re lame and live out your life in boredom!!")#ends the game with a lame message
        
def goAdventure():
  global name
  
  choice = input("\n" + name + """ Do you want to go to the forest or the mountain?\n
Options - enter the number you want to go to:
      1. go to the forest
      2. go to the mountain
      Choice: > """)
      
      #check user input to find out what function to call next
  if(choice == "1"):
    goToForest()
  elif(choice == "2"):
    goToMountain()

def goToForest():
  print("\nYou head to the dark...")
  choice = input("""\nDo you take the LONG route or the SHORT route\n
  Options - Enter the number of your choice
  1. Take the Short route
  2. Take the Long round
  Choice: > """)
  
  if choice == "1":
    getLost()
  elif choice == "2":
    goToMountain()
  else:
    goToForest()

        
def goToMountain():
  global monster1HP #allows the use of global variables
  global playerHP
  global inventory
  global gold
  
  print("\nYou have reach the mountain of the Blah Blahs ")
    
  
  if(monster1HP > 0):
    print("you see a giant heading your way and he wants to crush you!")
    choice = input("""
    What do you do?
    options:
    1. Run 
    2. Check you Inventory
    3. Hit giant with sword
    Choice: > """)
    
    if (choice == "1"):
      getLost()
    elif (choice == "2"):
      print("\nInventory: ")
      print(inventory)
      goToMountain()
    elif (choice == "3"):
      #you attack giant
      dmg = randint(11,12)
      print("\nYou attack with your sword and do " + str(dmg) + " damage to the giant!!")
      monster1HP = monster1HP - dmg
      print("\nGiant has " + str(monster1HP) + " remaining")
      
      #giant attacks You
      dmg = randint(1,10);
      print("\nGiant attacks you with a club and does " + str(dmg) + " damage to you!!")
      playerHP = playerHP - dmg
      print("\nYou Have " + str(playerHP) + " remaining")
      goToMountain()
    else:
      goToMountain()
  
  elif(playerHP <= 0 ):
    print("\nthe giant killed you. start the game again")
    startGame()
  else:
      choice = input("""
      You defeated the giant and lies lifeless at your feet
    What do you do?
    options:
    1. search the giant for loot
    2. continue down the trail
    3. turn back to the forest
    Choice: > """)

      if (choice == "1"):#be careful of looping bug here
        print("\nYou find 10 gold pieces and a shiny sword")
        gold = gold + 10
        inventory.append("Shiny Sword")
        inventory.remove("cheap sword")
        print("You now have " + str(gold) + " gold pieces and In your inventory:")
        print(inventory)
        goToMountain()
      elif (choice == "2"):
        winGame()#you wouldn't actually win the game here as it is too early but this is just an example so it's ending here. you would put your next function here for the next scene
      else:
        goToForest()#loops back to different part of game

def getLost():#end of game
    print("\nYou got lost... and die! Sorry")

def winGame():#end of game
  print("\nYou win!! game over")

# Create more functions to complete the game

# Don't forget to call the startGame function!  
startGame()
