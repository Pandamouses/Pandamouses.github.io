import random
import operator
import matplotlib.pyplot
import agentframework
import csv
import matplotlib.animation 
import tkinter
import matplotlib
matplotlib.use('TkAgg')
import requests
import bs4
import agentwolf



# drag the table from the website 
r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})  


#test whether the table is successfully dragged
#print(content)      


#resize and draw event Fig
fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])




# Just showing menu elements
root = tkinter.Tk()
root.geometry('1000x1000')
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)
root.title("Hunting_model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)

#TEST THE  POP UP MENU
#canvas.draw()   


environment=[]
f = open('in1.txt', newline ='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist=[]
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)


#Test whether environment background can successfully show
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()



# Initialisation        
random.seed() # THIS SETS THE RANDOM SEED FOR REPRODUCIBILITY
num_of_agents = 40 #set 40 agents which represent sheep
no_of_wolf = 3 #set 3 wolves
num_of_iterations = 150 #iteration 150 times
neighbourhood = 20 #define a share distance
agents = [] #create sheep list
# Initialise a list to contain wolf
wolf=[] #create wolf list
color=[] #color of sheep
color1=[] #color of wolf

color.append('white') #add sheep color
color1.append('Blue') #add wolf color
color1.append('Black') #add wolf color
color1.append('Green') #add wolf color




# Make the sheep and wolf.
# 0 -40
# sheep
for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(i,environment, y, x, agents,color))
    

# wolf
for i in range(no_of_wolf):
    y1 = int(td_ys[i + num_of_agents].text)
    x1 = int(td_xs[i + num_of_agents].text)
    wolf.append(agentwolf.Wolf(x1,y1,color1[random.randint(0, len(color1)-1)],wolf))

  
    

d = 3  
v = 50

# wolf kills sheep within 30 unit
def caught(agents, wolf):
    """
   if distance between agents and wolves <30
   then the sheep will die and becomes red

    Parameters
    ----------
    agents : TYPE
        DESCRIPTION.
    wolf : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    if ((((agents.x - wolf.x1)**2) +
            ((agents.y - wolf.y1)**2)) ** 0.5) <30:
         agents.alive=False
         agents.color='Red'
        
    #Test how many sheep got killed
         print("Got kill")
#doctest.testmod()    


# repeatly calling function update
#Move the agents.   eat the agents.  perform catch sheep.
carry_on = True	
def update(frame_number):
    """
    function to be called repeatly in FuncAnimation, conducting sheep and wolves'
    movement, eat, share information and caught 

    Parameters
    ----------
    frame_number : TYPE
        DESCRIPTION.

    Returns
    -------
    None.

    """
    fig.clear()   
    global carry_on
    
    for i in range(num_of_agents): 
        agents[i].move(d)
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)  
        
        #TEST WHETHER SHEEP IS updating SUCCESSFULLY
        print(agents[i])
    
    for i in range(no_of_wolf):  
        wolf[i].move(v)
        
        #TEST WHETHER WOLF IS updating SUCCESSFULLY
        #print(wolf[i])
      
        caught(agents[i],wolf[i])

        #doctest.testmod()
       
 # Set stop condition stop the loop       
    if random.random() < 0.01:
       """
       if random number < 0.01, then stop carry_on and print stop condition
       """
       carry_on = False
       
       print("stopping condition") 
       
     

        
        
# plot the ENVIRONMENT.
    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.imshow(environment)
    
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y,color=agents[i].color)
    #plot wolf    
    for i in range(no_of_wolf):
        matplotlib.pyplot.scatter(wolf[i].x1, wolf[i].y1, color=wolf[i].cor)
    #matplotlib.pyplot.show()







# frames waiting to be called
def gen_function(b = [0]):
    """
    set the times to update the animation

    Parameters
    ----------
    b : TYPE, optional
        DESCRIPTION. The default is [0].

    Yields
    ------
    TYPE
        DESCRIPTION.

    """
    a = 0
    global carry_on 
    while (a < 50) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
#animation created        
def run():
    """
    run the animation

    Returns
    -------
    None.

    """
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
  
    canvas.draw()




#RUN the model  
model_menu.add_command(label="Run model", command=run)   
root.mainloop()        
