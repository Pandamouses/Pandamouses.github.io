import random



class Wolf:
    

    
    def __init__(self,o,environment,c):
        self.id=o
        self.environment = environment
        self._x=random.randint(0,99)
        self._y=random.randint(0,99)   
        self.store = 0 # We'll come to this in a second.
        self.wolf =c
        
    
    #def __str__(self):
        #return "id="+ str(self.id)+",x="+str(self._x)+",y="+str(self._y)+",sharing="+str(self.store)
    
    def move(self,v):
        self._x=self.move_coordinate(self._x,v)
        self._y=self.move_coordinate(self._y,v)
       # if random.random() < 0.5:
           # self.x = (self.x + 1) % 100
       # else:
            #self.x = (self.x - 1) % 100

       # if random.random() < 0.5:
           # self.y = (self.y + 1) % 100
        #else:
            #self.y = (self.y - 1) % 100
    
    def move_coordinate(self,a,v):
        if random.random()<0.33:
            return a
        elif random.random()<0.5:
            a=(a+random.randint(1,v))%100
        else:
            a=(a-random.randint(1,v))%100
        return a

    #def eat(self): # can you make it eat what is left?
       #if self.environment[self._y][self._x] > 10:
          #self.environment[self._y][self._x] -= 10
         # self.store += 10
    

    #def distance_between(self, agent):
     #return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
        
    