# Multiple inheritance. and multi level -
#
# Create a class - Animal
#
# Create a child class - Land Animal (Animal)
# Create a child class - WaterAnimal (Animal)
#
# Create a child class Amphibian (LandAnimal,WaterAnimal)


class Animal:
    # Constructor
    def __init__(self, kind, color):
        self.kind = kind
        self.color = color

    # Method
    def display(self):
        print("\n\nAnimal kind : ", self.kind, "and color is : ", self.color)


class LandAnimal(Animal):
    # Constructor
    def __init__(self,kind, color, legs):
        self.kind = kind
        self.color = color
        self.legs = legs
        # Method

    def display_land_animal(self):
        print("\n\n Water Animal Name: ", self.landanimalname)

# class waterAnimal(animal):
#         # Constructor
#         def __init__(self):
#             self.wateranimalname = input("Enter water animal name ")
#             animal.__init__(self)
#
#     # Method
#     def displaywateranimal(self):
#         print("\n\n Water Animal Name: ", self.wateranimalname)
#
#
# class ampibian(landAnimal, waterAnimal)
#     # Constructor
#     def __init__(self):
#         self.ampibianname= input("\n\n ampibian Animal Name : ")
#         landAnimal.__init__(self)
#         waterAnimal.__init__(self)
#
#
#     # Method
#     def displayampibiananimal(self):
#         print("ampibian Animal Name: ", self.ampibianname)
#         landAnimal.displaylandanimal()
#         waterAnimal.displaywateranimal()
#
#
#
# # Objects of class 'student'
# ampibian1 =ampibian()
# ampibian2 = ampibian()
#
# # Call method of class 'student'
# ampibian1.displayampibiananimal()
# ampibian2.displayampibiananimal()

