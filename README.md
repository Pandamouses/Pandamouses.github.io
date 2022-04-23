# Agent Base Model

## Content list
This model is created to monitor wolves hunt sheep event. It simulates wolves chase the sheep, catch it and eat it.This model contains four files: GIS.py, agentframework.py agentwolf.py, and in1.txt.

- GIS.py contains code of creating sheep and wolf lists, fetching table from website which used to generize sheep and wolves location, creating a model background use data from in1.txt, wolves catching sheep function,  and creating a canvas and a menu which animates the wolves hunt sheep event.

- agentframework.py contains code of class `Agent` which represents sheep. It includes move, eat amd share information with neighborhood functions, and code`self.alive=True` which is used to simulates whether sheep is hunted or not. If sheep is alive, then sheep can move: ```if(self.alive):
           self.x=self.move_coordinate(self.x,d)
           self.y=self.move_coordinate(self.y,d)```, if the sheep is hunted, then the sheep is dead, and stop moving with color red: ` agents.alive=False
         agents.color='Red'`.

- agentwolf.py contains code of class `Wolf` which represents wolves. It only includes move function, but the wolves can move faster than sheep. Because in sheep:
    
   ` def move_coordinate(self,a,d):`
     
          if random.random()<0.33:
              return a
          elif random.random()<0.5:
              a=(a+random.randint(1,d))%100
          else:
              a=(a-random.randint(1,d))%100
          return a `

   the value of d is `d = 3 `, while in wolf:``` def move_coordinate(self,a,v):```
       
        `if random.random()<0.33:
             return a
         elif random.random()<0.5:
             a=(a+random.randint(4,v))%100
         else:
             a=(a-random.randint(4,v))%100
         return a`

   the value if v is `v = 6`, so wolves has a high possibility to move faster than sheep.

- in1.txt contains raster data, each value represtents a pixel, so all the data can form a environment background.

## How to run
This model runs in python, after clicking `run file`, it will pop up a menu. And click `Model` in the menu bar, click `Run model` the model will start to run. Sheep will move randomly and wolves will move faster. There will be 3 wolves with random color **black, green** and **blue**, and all the sheep(40) are **white**. Wolves and sheep are set to move only 10 times. If sheep is within 20 unit range of wolf, the sheep would be caught and die. This is a [screen shot](hunting.png)of the model showing 3 dead sheep. If the model keeps running, then all the sheep is suppose to die.
## Issues

