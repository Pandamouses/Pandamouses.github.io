# THIS FILE CREATES CLASS SHEEP, FUNCTION OF MOVE
import random



class Wolf:
    

    
    def __init__(self,x1,y1,cor,c):
        self.x1=x1
        self.y1=y1
        #self.color1=cor
        self.cor=cor
        #self.x1=random.randint(0,99)
        #self.y1=random.randint(0,99)   
        #self.store = 0 # We'll come to this in a second.
        self.wolf =c
        
    
    #def __str__(self):
        #return "id="+ str(self.id)+",x="+str(self._x)+",y="+str(self._y)+",sharing="+str(self.store)
    
    def move(self,v):
        self.x1=self.move_coordinate(self.x1,v)
        self.y1=self.move_coordinate(self.y1,v)
        #if random.random() < 0.5:
            #self.x1 = (self.x1 + 1) % 100
        #else:
           # self.x1 = (self.x1 - 1) % 100

        #if random.random() < 0.5:
            #self.y1 = (self.y1 + 1) % 100
       # else:
            #self.y1 = (self.y1 - 1) % 100
    
    def move_coordinate(self,a,v):
        if random.random()<0.33:
            return a
        elif random.random()<0.5:
            a=(a+random.randint(4,v))%100
        else:
            a=(a-random.randint(4,v))%100
        return a

    #def distance_between(self, agent):
     #return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
        
   
    #def eat(self): # can you make it eat what is left?
       #if self.environment[self._y][self._x] > 10:
          #self.environment[self._y][self._x] -= 10
         # self.store += 10
    

    #def distance_between(self, agent):
     #return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
        
    