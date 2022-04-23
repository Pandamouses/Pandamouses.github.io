# Agent Base Model

## Content list
This model is created to monitor wolves hunt sheep event. It simulates wolves chase the sheep, catch it and eat it.This model contains four files: GIS.py, agentframework.py agentwolf.py, and in1.txt.

- GIS.py contains code of creating sheep and wolf lists, fetching table from website which used to generize sheep and wolves location, creating a model background use data from in1.txt, wolves catching sheep function,  and creating a canvas and a menu which animates the wolves hunt sheep event.
- agentframework.py contains code of class `Agent` which represents sheep. It includes move, eat amd share information with neighborhood functions, and code`self.alive=True` which is used to simulates whether sheep is hunted or not. If sheep is alive, then sheep can move: ```if(self.alive):
           self.x=self.move_coordinate(self.x,d)
           self.y=self.move_coordinate(self.y,d)```, if the sheep is hunted, then the sheep is dead, and stop moving with color red: ` agents.alive=False
         agents.color='Red'`.
- agentwolf.py contains code of class `Wolf` which represents wolves. It only includes move function,
