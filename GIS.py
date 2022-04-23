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
#import agentwolf


r = requests.get('http://www.geog.leeds.ac.uk/courses/computing/practicals/python/agent-framework/part9/data.html')
content = r.text
soup = bs4.BeautifulSoup(content, 'html.parser')
td_ys = soup.find_all(attrs={"class" : "y"})
td_xs = soup.find_all(attrs={"class" : "x"})  
        



fig = matplotlib.pyplot.figure(figsize=(7, 7))
ax = fig.add_axes([0, 0, 1, 1])



# Just showing menu elements
root = tkinter.Tk()
root.geometry('1000x1000')
menu_bar = tkinter.Menu(root)
root.config(menu=menu_bar)
model_menu = tkinter.Menu(menu_bar)
menu_bar.add_cascade(label="Model", menu=model_menu)

root.title("Agent_Model")
canvas = matplotlib.backends.backend_tkagg.FigureCanvasTkAgg(fig, master=root)
canvas._tkcanvas.pack(side=tkinter.TOP, fill=tkinter.BOTH, expand=1)
    
#def distance_between(agents_row_a, agents_row_b):
    #return (((agents_row_a.x - agents_row_b.x)**2) +
            #((agents_row_a.y - agents_row_b.y)**2)) ** 0.5

environment=[]
f = open('in1.txt', newline ='')
reader = csv.reader(f, quoting=csv.QUOTE_NONNUMERIC)
for row in reader:
    rowlist=[]
    for value in row:
        rowlist.append(value)
    environment.append(rowlist)
#         print(value)
#matplotlib.pyplot.imshow(environment)
#matplotlib.pyplot.show()
        
random.seed(1)
num_of_agents = 20
num_of_iterations = 100
neighbourhood = 20
agents = []
#wolf=[]
color=['w']
      

# Make the agents.
# 0 - 10 
       

for i in range(num_of_agents):
    y = int(td_ys[i].text)
    x = int(td_xs[i].text)
    agents.append(agentframework.Agent(i,environment, y, x, agents))
    #agents.append(agentframework.Agent(i,agents,environment))
   
#Make a wolf
#for i in range(1):
    #wolf.append(agentwolf.Wolf(i,environment, wolf))

    
#v = 6
d = 3
# Move the agents.eat the agent.
carry_on = True	
def update(frame_number):
    
    fig.clear()   
    global carry_on
    #for j in range(num_of_iterations):
        #print(agents[0])
    for i in range(num_of_agents): 
        print(agents[i])
        agents[i].move(d)
        agents[i].eat()
        agents[i].share_with_neighbours(neighbourhood)
       # wolf[i].move(d)
        
        
        
    if random.random() < 0.1:
        carry_on = False
        print("stopping condition") 

        
        
        

    matplotlib.pyplot.ylim(0, 99)
    matplotlib.pyplot.xlim(0, 99)
    matplotlib.pyplot.imshow(environment)
    for i in range(num_of_agents):
        matplotlib.pyplot.scatter(agents[i].x,agents[i].y)
    #matplotlib.pyplot.show()

def gen_function(b = [0]):
    a = 0
    global carry_on #Not actually needed as we're not assigning, but clearer
    while (a < 10) & (carry_on) :
        yield a			# Returns control and waits next call.
        a = a + 1
def run():
    animation = matplotlib.animation.FuncAnimation(fig, update, frames=gen_function, repeat=False)
  
    canvas.draw()



#for agents_row_a in agents:
    #for agents_row_b in agents:
        #distance = distance_between(agents_row_a,agents_row_b)
  
model_menu.add_command(label="Run model", command=run)   
root.mainloop()        
