class Animal:
    def __init__(self):
        self.no_eyes = 2
        print("We all are Animal.........")
    def breathe(self):
        print("Inhaling.....")
        
class Fish(Animal):
    def __init__(self):
        super().__init__()
        print("I am Fish")
    
    
    def breathe(self):
       super().breathe()
       print("We are doing this under water......")
    
    
    
    
    
    def swim(self):
        print("Moving.....in water")
        
kinny = Fish()
kinny.swim()
kinny.breathe()
print(kinny.no_eyes)
