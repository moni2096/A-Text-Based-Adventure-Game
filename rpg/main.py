from room import Room
from item import Item
from character import Enemy,Friend


kitchen = Room("Kitchen")
kitchen.set_description("A dank and dirty room buzzing with flies.")

dining_hall = Room("Dining Hall")
dining_hall.set_description("A place to eat and enjoy with family.")

ballroom = Room("Ballroom")
ballroom.set_description("A place to meet and greet.")

kitchen.link_room(dining_hall, "south")
dining_hall.link_room(kitchen, "north")
dining_hall.link_room(ballroom, "west")
ballroom.link_room(dining_hall, "east")

dave = Enemy("Dave", "A smelly zombie")
dave.set_conversation("What's up world!! How is it going??")
dave.set_weakness("cheese")

catrina = Friend("Catrina", "A friendly skeleton")
catrina.set_conversation("Hello!!! I am your new friend")
catrina.set_weakness("sword")

tabitha = Enemy("Tabitha", "An enormous spider with countless eyes and furry legs.")
tabitha.set_conversation("Sssss....I'm so bored...")
tabitha.set_weakness("book")
ballroom.set_character(tabitha)

book = Item("book")
book.set_description("A really good book entitled 'Knitting for dummies'")
dining_hall.set_item(book)

cheese = Item("cheese")
cheese.set_description("A big block of smelly chesse")
ballroom.set_item(cheese)



ballroom.set_character(catrina)

dining_hall.set_character(dave)

current_room = kitchen

backpack = []

dead = False
 
while dead == False:		
  print("\n")         
  current_room.get_details()

  inhabitant = current_room.get_character()
  if inhabitant is not None:
    inhabitant.describe()
  
  item = current_room.get_item()
  if item is not None:
    item.describe()
      
  command = input("> ")    
  if command in ["north", "south", "east", "west"]:
    current_room = current_room.move(command)
    
  elif command == "talk":
    if inhabitant is not None:
      inhabitant.talk()
      
  elif command == "fight":
    if inhabitant is not None:

      print("What do you choose to fight with?")
      # choose what you want to fight with
      fight_with = input()
      
      if fight_with in backpack:
        if inhabitant.fight(fight_with) == True:
          print("Congratzz!! You won the fight!!")
          current_room.character = None
          if inhabitant.get_defeated() == 2:
            print("Congratulations, you have vanquished the enemy horde!")
            dead = True
          else:
            print("Oops!! You lost the fight!!")
            print("Your game is over!!")
            dead = True
      else:
        print("You dont have a " + fight_with)
    else:
      print("There is no one here to fight with")
        
  elif command == "hug":
    if inhabitant == None:
      print("There is no one to give a hug")
    else:
      if isinstance(inhabitant,Enemy):
        print("I would never hug my enemy!")
      else:
        inhabitant.hug()
        
  elif command == "steal":
    if inhabitant == None:
      print("There is no one you can steal from")
    elif isinstance(inhabitant,Friend):
      print("Do you really want to steal from your friend??")
    else:
      print("You need to fight to steal object. Choose an object to fight with:")
      fight_with = input()
      if inhabitant.fight(fight_with) == True:
        print("You stole an item!!")
      else:
        print("Oops!! You lost the fight!!")
        print("Your game is over!!")
        dead = True
        
  elif command == "take":
    if current_room.get_item() != None:
      print("You put the " + item.get_name() + " in your backpack")
      backpack.append(current_room.get_item())
      current_room.set_item(None)
    else:
      print("There's nothing here to take!")
      
  else:
    print("I don't know how to " + command)
      
  
  
  
      
      
        
  
  
        



