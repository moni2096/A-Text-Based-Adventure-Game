class Character:

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True
        
class Enemy(Character):
  
  enemies_defeated = 0
  
  def __init__(self, char_name, char_description):
    super().__init__(char_name, char_description)
    self.weakness = None
 
 # Getters and setters for weakness   
  def set_weakness(self,weakness):
    self.weakness = weakness

  def get_weakness(self):
    return self.weakness
    
  def fight(self, combat_item):
    if combat_item == self.weakness:
        print("You fend " + self.name + " off with the " + combat_item )
        Enemy.enemies_defeated += 1
        return True
    else:
        print(self.name + " crushes you, puny adventurer")
        return False
  
  # Getters and setters for enemies defeated
  def get_defeated(self):
    return Enemy.enemies_defeated
  
  def set_defeated(self, number_defeated):
    Enemy.enemies_defeated = number_defeated
        
  def steal(self):
    print("You steal from " + self.name)
    
  def bribe(self):
    print("You bribed " + self.name)
    
  def send_to_sleep(self):
    print("You sent" + self.name + "to sleep")
    
class Friend(Enemy):
  def __init__(self, char_name, char_description):
    super().__init__(char_name, char_description)
    self.feeling = None
  
  def hug(self):
    print(self.name + " hugs you back!")

