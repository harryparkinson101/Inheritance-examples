# inheritance 
# we do not need to assign user variables so there is no need for an __init__ constructor method
''' users
  - Wizards
  - Archers
  - Ogres
'''
class User:
    def sign_in(self):
        print('Logged in')
# we use inheritance to acess the parent class
class Wizard(User):
    def __init__(self, name, power):
        self.name = name
        self.power = power

    def attack(self):
        print(f'Attacking with power of {self.power}')

class Archer(User):
    def __init__(self, name, num_arrows):
        self.name = name
        self.num_arrows = num_arrows

    def attack(self):
        print(f'Attacking with arrows: arrows left- {self.num_arrows}')

wizard2 = Wizard('Harry', 50 )
archer1 = Archer('Robin', 200)

wizard2.attack()
archer1.attack()        

# we can use isinstance to check if x is an instance of y class

archer2 = Archer('Charles', 7)
# this will print True because archer2 is an instance of Archer
#print(isinstance(archer2, Archer))

# This will also print True because archer2 is a subclass of User
#print(isinstance(archer2, User))

# This will print True because User and Archer are both object type
#print(isinstance(archer2, object))

# we can instanciate a new User using inheritance
#wizard1 = Wizard()
# we can inherit fuctions from parents 

#print(wizard2.sign_in())

