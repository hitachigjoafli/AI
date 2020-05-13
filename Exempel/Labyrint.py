import util

rows = 'ABCDEFGHIJ'
# Labyrint=[
#     [97,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,98,0],
# ]
# Labyrint=[
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,9,9,9,9,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
# ]
# Labyrint=[
#     [0,0,0,0,0,0,9,9,0,0],
#     [0,9,9,9,9,9,0,0,0,0],
#     [0,9,0,0,0,9,0,9,0,0],
#     [0,0,0,9,0,0,0,9,0,0],
# ]

Labyrint=[
    [0,0,0,0,0,8,0,0,0,0],
    [0,3,3,4,3,2,0,0,0,0],
    [3,0,0,0,0,0,0,1,2,0],
    [0,0,0,0,0,0,0,0,0,0],
]

# Labyrint=[
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
#     [0,0,0,0,0,0,0,0,0,0],
# ]
def FindAction(place,Labyrint,rows,maxrow,maxcol):
    actions=[]
    if place[0]>=0 and place[0]<=maxrow:
        if place[1]>=0 and place[1]<=maxcol:
            value=Labyrint[place[0]][place[1]]
            if value!=9:
                # return  rows[place[0]]+str(place[1]+1)
                return [rows[place[0]]+str(place[1]+1),value+1]
    return 0

def PlaceOnBoard(Labyrint):
    #Skapar rutnät och lägger in . på varje plats
    LabyrintDict={}
    for idx, row in enumerate(Labyrint):
        for idx2,col in enumerate(row):
            # print(rows[idx])
            state=col
            place=rows[idx]+str(idx2+1)
            actions=[]
            for neighbour in [[idx,idx2-1],[idx,idx2+1],[idx-1,idx2],[idx+1,idx2]]:
                Action=FindAction(neighbour,Labyrint,rows,len(Labyrint)-1,len(row)-1)
                if Action!=0:
                    actions.append(Action)
            LabyrintDict[place] = {"state":col,"actions":actions}
    return LabyrintDict

LabDict=    PlaceOnBoard(Labyrint)

# print(LabDict['B2'])
# print(LabDict)



# def depthFirstSearch(node,graph,goal): #Söker djupet först
#     #Skapar en lista enligt LIFO (Last in first out) principen. håller värdena state och actions.
#     frontier = util.Stack()
#     #Redan tidigare utforskade noder, en array med states.
#     exploredNodes = []
#     #Skapar startNoden, innehåller en tom start statet och en tom array då vi inte har några actions
#     startNode = (node, [])
#     #Lägger in startnoden i frontier
#     frontier.push(startNode)
    
#     while not frontier.isEmpty(): #sålänge frontier inte är tom så kör
#         #Ta den node som sist blev inlagd i frontier arrayen. Delar upp den i state och actions
#         currentState, actions = frontier.pop()
#         #Om Nuvarande noden inte är utforskad så lägg den i utforskad
#         if currentState not in exploredNodes:
#             exploredNodes.append(currentState)
#             #Om denna noden är målet så printa ut vägen och returna actions (väg från början till mål)
#             if goal==currentState:
#                 print(node,"to", goal, actions)
#                 return actions
#             else:
#                 #Ta fram alla möjliga vägar att gå vidare genom att titta i graph vilka barn som finns till noden.
#                 successors = graph[currentState]
#                 #Lägg till varje Successor i frontier efter att ha räknat ut deras action.
#                 # print(currentState,successors)
#                 for succState in successors['actions']:
#                     newAction = actions + [succState]
#                     newNode = (succState, newAction)
#                     frontier.push(newNode)

#     return actions

def depthFirstSearch(node,graph,goal): #Söker djupet först
    #Skapar en lista enligt LIFO (Last in first out) principen. håller värdena state och actions.
    frontier = util.Stack()
    #Redan tidigare utforskade noder, en array med states.
    exploredNodes = []
    #Skapar startNoden, innehåller en tom start statet och en tom array då vi inte har några actions
    startNode = (node, [],0)
    #Lägger in startnoden i frontier
    frontier.push(startNode)
    
    while not frontier.isEmpty(): #sålänge frontier inte är tom så kör
        #Ta den node som sist blev inlagd i frontier arrayen. Delar upp den i state och actions
        currentState, actions, currentCost = frontier.pop()
        #Om Nuvarande noden inte är utforskad så lägg den i utforskad
        if currentState not in exploredNodes:
            exploredNodes.append(currentState)
            #Om denna noden är målet så printa ut vägen och returna actions (väg från början till mål)
            if goal==currentState:
                print(node,"to", goal, actions,"Cost:",currentCost)
                return actions
            else:
                #Ta fram alla möjliga vägar att gå vidare genom att titta i graph vilka barn som finns till noden.
                successors = graph[currentState]
                #Lägg till varje Successor i frontier efter att ha räknat ut deras action.
                # print(currentState,successors)
                for succState, succCost in successors['actions']:
                    newAction = actions + [succState]
                    newCost= currentCost+succCost
                    newNode = (succState, newAction,newCost)
                    frontier.push(newNode)

    return actions

def breadthFirstSearch(node,graph,goal): #Letar på bredden först
    #Skapar en lista enligt FIFO (First in first out) principen. håller värdena state och actions och en kostnad.
    frontier = util.Queue()
    #Redan tidigare utforskade noder, en array med states.
    exploredNodes = []
    #Lägger in startnoden i frontier (state, tom actionlista och 0 kostnad.)
    startNode = (node, [],0)
    frontier.push(startNode)
    
    while not frontier.isEmpty():
        #börja med att ta den första noden i listan.
        currentState, actions,currentCost = frontier.pop()
        
        #Om Nuvarande noden inte är utforskad så lägg den i utforskad
        if currentState not in exploredNodes:
            exploredNodes.append(currentState)
 #Om denna noden är målet så printa ut vägen och returna actions (väg från början till mål) samt kostanden
            if goal==currentState:
                print(node,"to", goal, actions,"Cost:",currentCost)
                return actions
            else:
 #Ta fram alla möjliga vägar att gå vidare genom att titta i graph vilka barn som finns till noden.
                successors = graph[currentState]
                #Lägg till varje Successor i frontier efter att ha räknat ut deras action.
                for succState, succCost in successors['actions']:
                    newAction = actions + [succState]
                    newCost= currentCost+succCost
                    newNode = (succState, newAction,newCost)
                    frontier.push(newNode)

    return actions        

def uniformCostSearch(node,graph,goal):
     #Skapar en lista enligt  Prioriterings(Oftast och i detta fall lägst värde först) principen. håller värdena state och actions värde.
    frontier = util.PriorityQueue()
    #Redan tidigare utforskade noder, en dictionary med states som parameter namn och  kostnaden som värde.
    exploredNodes = {} 
       #Skapar startNoden, innehåller en tom start statet och en tom array då vi inte har några action
    startNode = (node, [],0)   
     #Lägger in startnoden i frontier
    frontier.push(startNode,0)
    while not frontier.isEmpty(): #sålänge frontier inte är tom så kör
        #börja med att ta den första noden i listan, det vill säga den med lägst kostnadsvärde.
        currentState, actions,currentCost = frontier.pop()
        #Om Nuvarande noden inte är utforskad så lägg den i utforskad eller om denna vägen är billigare än den tidigare utforskade vägen så lägg till.
        if currentState not in exploredNodes or  currentCost< exploredNodes[currentState]:
            exploredNodes[currentState]=currentCost 
            #Om denna noden är målet så printa ut vägen och returna actions (väg från början till mål)
            if goal==currentState:
                print(node,"to", goal, actions,"Cost:",currentCost)
                return actions
            else:    
                #Ta fram alla möjliga vägar att gå vidare genom att titta i graph vilka barn som finns till noden.
                successors = graph[currentState]
                #Lägg till varje Successor i frontier samt uppdatera den efter att ha räknat ut deras action.
                for succState, succCost in successors['actions']:
                    newAction = actions + [succState]
                    newCost= currentCost+succCost
                    newNode = (succState, newAction,newCost)
                    frontier.update(newNode,newCost)
    return actions  


def nullHeuristic(state):
    #En heuristic som räknar ut kostnaden från nuvarande state till målet. 
    return 0

def aStarSearch(node,graph,goal, heuristic=nullHeuristic):
    #A-star letar efter den billigaste sammanlagda vägen och med heurustiken. 
   #Skapar en lista enligt  Prioriterings(Oftast och i detta fall lägst värde först) principen. håller värdena state och actions värde.
    frontier = util.PriorityQueue()
    #Redan tidigare utforskade noder, en array med states.
    exploredNodes = []
    #Skapar startNoden, innehåller en tom start statet och en tom array då vi inte har några actions
    startNode = (node, [],0)

    frontier.push(startNode,0)#0 an är för att visa att första kostnaden är 0 detta ersätts senare i frontier.update
    
    while not frontier.isEmpty(): #sålänge frontier inte är tom så kör
        #börja med att ta den första noden i listan, det vill säga den med lägst kostnadsvärde.
        currentState, actions,currentCost = frontier.pop() #Tar ut värdet som har lägst kostnad
        exploredNodes.append((currentState, currentCost))   
        #Om denna noden är målet så printa ut vägen och returna actions (väg från början till mål)
        if goal==currentState:
            # print(exploredNodes)
            print(node,"to", goal, actions,"Cost:",currentCost)
            return actions
        else:  
            #Ta fram alla möjliga vägar att gå vidare genom att titta i graph vilka barn som finns till noden.
            successors = graph[currentState] 
             #Lägg till varje Successor i frontier samt uppdatera den efter att ha räknat ut deras action.
            for succState, succCost in successors['actions']:
                newAction = actions + [succState]
                newCost= currentCost+succCost
                newNode = (succState, newAction,newCost)
                
                A_explored=False

                for explored in exploredNodes:#titta om den är utforskad, är den utforskad och den nya kostnaden är högre än den gamla så ska vi inte utforska den
                    exploredState,exploredCost= explored
                    if succState==exploredState  and newCost>= exploredCost:
                        A_explored=True
                    
                if not A_explored: #Annars lägger vi till den i frontier och i explored
                    frontier.push(newNode,newCost+heuristic(succState))
                    exploredNodes.append((succState,newCost))

    return actions  


def greedyBestFindSearch(node,graph,goal, heuristic=nullHeuristic):
    #greedy best försöker alltid hitta den snabbaste/billigaste vägen till målet och kommer då gå på vad den tror är kortast väg genom att titta på nästa steg. 
   #Skapar en lista enligt  Prioriterings(Oftast och i detta fall lägst värde först) principen. håller värdena state och actions värde.
    frontier = util.PriorityQueue() 
     #Redan tidigare utforskade noder, en dictionary med states som parameter namn och  kostnaden som värde.
    exploredNodes = []
    startNode = (node, [],0)

    frontier.push(startNode,0)#0 an är för att visa att första kostnaden är 0 detta ersätts senare i frontier.update
    
    while not frontier.isEmpty():
        #begin exploring first (lowest-cost) node on frontier
        currentState, actions,currentCost = frontier.pop() #Tar ut värdet som har lägst kostnad
        exploredNodes.append((currentState, currentCost))
        if goal==currentState:
            # print(exploredNodes)
            print(node,"to", goal, actions,"Cost:",currentCost)
            return actions
        else:
            successors = graph[currentState]
            for succState, succCost in successors['actions']:
                newAction = actions + [succState]
                newCost= currentCost+succCost
                newNode = (succState, newAction,newCost)
                
                A_explored=False

                for explored in exploredNodes:#titta om den är utforskad, är den utforskad så ska vi inte utforska den igen
                    exploredState,exploredCost= explored

                    if succState==exploredState:
                        A_explored=True
                    
                if not A_explored: #Annars lägger vi till den i frontier och i explored
                    frontier.push(newNode,newCost+heuristic(succState))
                    exploredNodes.append((succState,newCost))

    return actions  

Paths=[]
print("depthFirstSearch")
test= depthFirstSearch("A1",LabDict,"D10")
test.insert(0,"A1")
Paths.append(["depthFirstSearch",test])
print("breadthFirstSearch")
test= breadthFirstSearch("A1",LabDict,"D10")
test.insert(0,"A1")
Paths.append(["breadthFirstSearch",test])

print("uniformCostSearch")
test= uniformCostSearch("A1",LabDict,"D10")
test.insert(0,"A1")
Paths.append(["uniformCostSearch",test])

print("aStarSearch")
test= aStarSearch("A1",LabDict,"D10")
test.insert(0,"A1")
Paths.append(["aStarSearch",test])

print("greedyBestFindSearch")
Path= greedyBestFindSearch("A1",LabDict,"D10")
Path.insert(0,"A1")
Paths.append(["greedyBestFindSearch",Path])
# print(test)


##Grafiskt
from tkinter import *
import time
master = Tk()
from random import randint

def getCord(cordinate):
    letter=cordinate[0]
    y = rows.index(letter)
    x=int(cordinate[1:])-1
    # print(x,"X  Y",y)
    sizevalue=50
    x= x*sizevalue
    y=  y*sizevalue
    return x, y,x +sizevalue, y+sizevalue


#Skapa spelplan
C = Canvas(master, bg="green", height=600, width=600)
C.pack()
distanceY=0
distanceX=0
colors=['SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
    'LightSkyBlue3', 'LightSkyBlue4', 'SlateGray1', 'SlateGray2', 'SlateGray3',
    'SlateGray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
    'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
    'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2']#Färger för att ha färgskala
sizevalue=50
for row in range(len(Labyrint)): 
    for col in range(len(Labyrint[0])):
       coord = distanceX, distanceY, distanceX+sizevalue, distanceY+sizevalue
       distanceX+=sizevalue
       C.create_rectangle(coord, fill=colors[Labyrint[row][col]])
    distanceY+=sizevalue
    distanceX=0

text = Text(master, height=2, width=30)
text.pack()

for Name,Path in Paths:
    print(Path)
    #Skapa start
    FormerX, FormerY, StartWidth,StartHeight= getCord(Path.pop(0))
    C.create_rectangle(FormerX,FormerY,StartWidth,StartHeight, fill="yellow")
    #Skapa mål
    Goal= getCord(Path[-1])
    C.create_rectangle(Goal[0],Goal[1],Goal[2],Goal[3], fill="gold")
    # Skapa Musen
    Mouse=C.create_rectangle(FormerX,FormerY,StartWidth,StartHeight, fill="brown")
    speed=0.8 #Hastighet
    while len(Path)>0:
        time.sleep(speed)
        
        text.delete("insert linestart", "insert lineend")
        text.insert(END, Name)
        X, Y, X2, Y2 = getCord(Path.pop(0))
        MovementX= X-FormerX #Mät aavståndet för förflyttning
        MovementY= Y-FormerY
        # print("Step",MovementX,MovementY)
        C.move(Mouse, MovementX, MovementY)
        C.update()
        FormerX=X
        FormerY=Y
    time.sleep(5)



mainloop()