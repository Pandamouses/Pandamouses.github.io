import random



class Agent:
    

    
    def __init__(self,o,environment,y,x,b):
        self.id=o
        self.environment = environment
        #self.x=random.randint(0,99)
        #self.y=random.randint(0,99)
        self.y=y
        self.x=x
        
        self.store = 0 # We'll come to this in a second.
        self.agents =b
        if (x == None):
          self._x = random.randint(0,100)
        else:
           self._x = x
        if (y == None):
          self._y = random.randint(0,100)
        else:
           self._y = y
    
    def __str__(self):
        return "id="+ str(self.id)+",x="+str(self.x)+",y="+str(self.y)+",sharing="+str(self.store)
    
    def move(self,d):
        self.x=self.move_coordinate(self.x,d)
        self.y=self.move_coordinate(self.y,d)
       # if random.random() < 0.5:
           # self.x = (self.x + 1) % 100
       # else:
            #self.x = (self.x - 1) % 100

       # if random.random() < 0.5:
           # self.y = (self.y + 1) % 100
        #else:
            #self.y = (self.y - 1) % 100
    
    def move_coordinate(self,a,d):
        if random.random()<0.33:
            return a
        elif random.random()<0.5:
            a=(a+random.randint(1,d))%100
        else:
            a=(a-random.randint(1,d))%100
        return a

    def eat(self): # can you make it eat what is left?
       if self.environment[self.y][self.x] > 10:
          self.environment[self.y][self.x] -= 10
          self.store += 10
    

    def distance_between(self, agent):
     return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
        
    def share_with_neighbours(self, neighbourhood):
       for agent in self.agents:
          if (self.id != agent.id):
          
              dist = self.distance_between(agent)
              if dist <= neighbourhood:
                sum = self.store + agent.store
                ave = sum /2
                self.store = ave
                agent.store = ave
                
               # print("sharing " + str(dist) + " " + str(ave))
            
  
 
        
        
        
        
        
        
        
         