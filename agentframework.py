# THIS FILE CREATES CLASS SHEEP, FUNCTIONS OF MOVE, EAT, AND SHARE WITH NEIGHBOURS


import random



class Agent:
    

    
    def __init__(self,o,environment,y,x,b,color):
        self.id=o
        self.environment = environment
        self.alive=True
        #self.x=random.randint(0,99)
        #self.y=random.randint(0,99)
        self.y=y
        self.x=x
        self.color=color
        self.store = 0 
        self.agents =b
        if (x == None):
          self._x = random.randint(0,100)
        else:
           self._x = x
        if (y == None):
          self._y = random.randint(0,100)
        else:
           self._y = y
    
    def __str__(self): # print content
        return "id="+ str(self.id)+",x="+str(self.x)+",y="+str(self.y)+",sharing="+str(self.store)
    
    def move(self,d): #move the sheep
        
        if(self.alive): #move the sheep if sheep alives
           self.x=self.move_coordinate(self.x,d)
           self.y=self.move_coordinate(self.y,d)
      
    
    def move_coordinate(self,a,d):
        if self.color != 'Red':
          if random.random()<0.33:
              return a
          elif random.random()<0.5:
              a=(a+random.randint(1,d))%100
          else:
              a=(a-random.randint(1,d))%100
          return a

    def eat(self): 
       if self.environment[self.y][self.x] > 10:
          self.environment[self.y][self.x] -= 10
         # if (isinstance(self.environment[self.y][self.x], float)):
             # print(self.environment[self.y][self.x])
          self.store += 10
    
                       
    def distance_between(self, agent): #distance between current location and last location
     return (((self.x - agent.x)**2) + ((self.y - agent.y)**2))**0.5
    
     #if distance between current location and last location < 20, then share the information   
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
            
  
 
        
        
        
        
        
        
        
         