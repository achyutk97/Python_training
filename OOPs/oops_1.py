# 1
class Things():
    pass
    
example = Things()
print(Things())
print(example)


# 2

class Things2():
    latters = "abc"
    
print(Things2.latters)

# 3
class Things3():
    def __init__(self, input):
        self.letters = input

print(Things3("xyz").letters)

# 4
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

example = Element('Hydrogen', 'H', 1)
print(example.name, example.symbol, example.number)

# 5
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

dict_data = {"name": "Hydrogen", "symbol": "H", "number": 1}
hydrogen = Element(**dict_data)
print(example.name, example.symbol, example.number)

# 6
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def dump(self):
        print(self.name, self.symbol, self.number)
        
        
dict_data = {"name": "Hydrogen", "symbol": "H", "number": 1}
hydrogen = Element(**dict_data)
hydrogen.dump()
print(hydrogen)

# 7
class Element():
    def __init__(self, name, symbol, number):
        self.name = name
        self.symbol = symbol
        self.number = number

    def __str__(self):
        return f"{self.name}, {self.symbol}, {self.number}"
        
dict_data = {"name": "Hydrogen", "symbol": "H", "number": 1}
hydrogen = Element(**dict_data)
print(hydrogen)

# 8
class Element():
    def __init__(self, name, symbol, number):
        self.__name = name
        self.__symbol = symbol
        self.__number = number

    @property
    def name(self):
        return self.__name
    
    @property
    def name(self):
        return self.__symbol
    
    @property
    def name(self):
        return self.__number
        
dict_data = {"name": "Hydrogen", "symbol": "H", "number": 1}
hydrogen = Element(**dict_data)
print(example.name, example.symbol, example.number)

# 9 

class Bear():
    def eats(self):
        return 'berries'

class Rabbit():
    def eats(self):
        return 'clover'
    
class Octothorpe():
    def eats(self):
        return 'campers'

bear = Bear()
print(bear.eats())

rabbit = Rabbit()
print(rabbit.eats())

octothorpe = Octothorpe()
print(octothorpe.eats())

# 10 

class Laser():
    def does(self):
        return 'disintegrate'
    
class Claw():
    def does(self):
        return 'crush'
    
class SmartPhone():
    def does(self):
        return 'ring'
    
class Robot():
    def __init__(self, laser, claw, smartPhone):
        self.laser = laser
        self.claw = claw
        self.smartPhone = smartPhone
        
    def does(self):
        print(self.laser.does(), self.claw.does(), self.smartPhone.does())
        
laser = Laser()
claw = Claw()
smartPhone = SmartPhone()

robot = Robot(laser, claw, smartPhone)
robot.does()