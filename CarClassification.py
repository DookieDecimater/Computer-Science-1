#Car Classes
#Jackson Bauer

class car(object):
    condition = 'new'
    print(condition)

    def __init__(self, model, color, mpg):
        self.model = model
        self.color = color
        self.mpg = mpg
        
    def display_car(self):
        print('This is a '+ self.color +' '+ self.model + ' with ' + self.mpg + ' MPG.')
        
    def drive_car(self):
        self.condition = 'After driving the Delorean is used'
        print(self.condition)
        
my_car = car('Delorean', 'Silver', '88')
my_car.display_car()
my_car.drive_car()

print()

class ecar(car):
  
    condition = 'Brand new'
    print(condition)
    def __init__(self, model, color, battery_type):
        self.model = model
        self.color = color
        self.battery_type = battery_type
        
    def display_car(self):
        print('This is a ' + self.color + ' ' + self.model + ' with a ' + self.battery_type + ' battery.')
        
    def drive_car(self):
        self.condition = 'After driving the Telsa is still like new'
        print(self.condition)
        
        
my_e_car = ecar('Tesla', 'Red', 'Molten Salt')
my_e_car.display_car()
my_e_car.drive_car()