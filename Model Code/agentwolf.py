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
        self.wolf =c
        
    def __str__(self): # print content
        return "x="+str(self.x1)+",y="+str(self.y1)
    def move(self,v):
        self.x1=self.move_coordinate(self.x1,v)
        self.y1=self.move_coordinate(self.y1,v)
       
    
    def move_coordinate(self,a,v):
        if random.random()<0.33:
            return a
        elif random.random()<0.5:
            a=(a+random.randint(4,v))%100
        else:
            a=(a-random.randint(4,v))%100
        return a

    
    
        
    