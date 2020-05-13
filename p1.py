
from random import randint
name = "" #variable for character name

def startGame():#first scene of the adventure
  global name #allows the use of the name variable in line 7 so it doesn't overwrite with a local variable
  name = input("You are a Py-ian, a villager of Codeia. What is your name? ")
  adventure = input("\nHello " + name +" Do you want to go on an adventure? \nEnter 1 for yes or 2 for No. > ")

  if adventure == "1":#remember input is in string format
    goAdventure()#calls the next scene in the game
  else:
      print("\n" + name.upper() + "!!! You're lame and live out your life in boredom!!")#ends the game with a lame message
        
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
  
  print("\nYou have reach the mountain of the Blah Blahs ")
  
  choice = input("""
      You defeated the giant and lies lifeless at your feet
    What do you do?
    options:
    1. continue down the trail
    2. turn back to the forest
    Choice: > """)


  if (choice == "1"):
    winGame()#you wouldn't actually win the game here as it is too early but this is just an example so it's ending here. you would put your next function here for the next scene
  else:
    goToForest()#loops back to different part of game

def getLost():#end of game
    print("\nYou got lost... and die! Sorry")

def winGame():#end of game
  print("\nThat was easy, You win!! Game Over")

# Create more functions to make the game more interesting

# Don't forget to call the startGame function!  
startGame()