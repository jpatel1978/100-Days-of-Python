
welcome = """
░██╗░░░░░░░██╗███████╗██╗░░░░░░█████╗░░█████╗░███╗░░░███╗███████╗  ████████╗░█████╗░
░██║░░██╗░░██║██╔════╝██║░░░░░██╔══██╗██╔══██╗████╗░████║██╔════╝  ╚══██╔══╝██╔══██╗
░╚██╗████╗██╔╝█████╗░░██║░░░░░██║░░╚═╝██║░░██║██╔████╔██║█████╗░░  ░░░██║░░░██║░░██║
░░████╔═████║░██╔══╝░░██║░░░░░██║░░██╗██║░░██║██║╚██╔╝██║██╔══╝░░  ░░░██║░░░██║░░██║
░░╚██╔╝░╚██╔╝░███████╗███████╗╚█████╔╝╚█████╔╝██║░╚═╝░██║███████╗  ░░░██║░░░╚█████╔╝
░░░╚═╝░░░╚═╝░░╚══════╝╚══════╝░╚════╝░░╚════╝░╚═╝░░░░░╚═╝╚══════╝  ░░░╚═╝░░░░╚════╝░
"""

logo = """
    __                       _   __                    
   / / _   _    /7  _   _   / \,' / _   _    /7  _   _ 
n_/ /,'o| / \/7/_7,'o| //7 / \,' /,'o| / \/7/_7,'o| //7
\_,' |_,7/_n_///  |_,7//  /_/ /_/ |_,7/_n_///  |_,7//  
                                                       
                                                                                                                                             
"""

print(welcome)
print(logo)
print("Your mission is to find the way out of Jantar Mantar")
choice1 = input('You\'re at a cross road. Where do you want to go? Type "left" or "right" \n').lower()
if choice1 == "left":
  choice2 = input('You\'ve come to a sea. There is an island in the middle of the sea. Type "wait boat" to wait for a boat. Type "wait ship" to wait for a ship. \n').lower()
  if choice2 == "wait boat":
    choice3 = input("You arrive at the island unharmed. There is a house with 4 doors. One red, one yellow and one blue, one black. Which colour do you choose? \n").lower()
    if choice3 == "red":
      print("It's a room full of fire. Game Over.")
    elif choice3 == "yellow":
      print("You found the treasure! You Win!")
    elif choice3 == "blue":
      print("You enter a room of beasts. Game Over.")
    elif choice3 == "black":
      print("You enter a room of ghosts. Game Over.")
    else:
      print("You chose a door that doesn't exist. Game Over.")
  else:
    print("There's a ship coming with 50 passengers with a waiting in this port of 2 minutes.")
    choice4 = input("Do you want to go onto that ship? \n").lower()
    if choice4 == "yes":
      print("You have reached the island safely, There are 4 houses. One Named YelYol, One Named BlanBol, One Named ReRed, One Named BluBlu")
      choice5 = input("Which door do you want to go?").lower()
      if choice5 == "rered":
        print("You entered a room full or fire. Game Over")
      elif choice5 == "blanbol":
        print("You have entered a room of Ghosts. Game Over")
      elif choice5 == "yelyol":
        print("You have found the treasure! Great")
      elif choice5 == "blublu":
        print("You have entered a room of Beasts. Game Over")
      else:
        print("You choosed a house that doesn't exist. Game Over")
    else:
      print("A Kidnapper kidnapped you. Game Over")
