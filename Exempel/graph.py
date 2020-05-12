
graph = {
    'A' : ['B','C'],
    'B' : ['D', 'E'],
    'C' : ['F'],
    'D' : [],
    'E' : ['F'],
    'F' : []
}
# cities = {
#     'Stockholm' : ['Strängnäs','Västerås'],
#     'Västerås' : ['Stockholm', 'Köping', 'Eskilstuna'],
#     'Eskilstuna' : ['Strängnäs', 'Västerås', 'Kungsör'],
#     'Kungsör' : ['Köping', 'Eskilstuna'],
#     'Köping' : ['Kungsör', 'Västerås'],
#     'Strängnäs' : ['Stockholm', 'Eskilstuna'],
# }
cities = {
    'Stockholm' : [['Strängnäs',9],['Västerås',10]],
    'Västerås' : [['Stockholm',10],['Köping',4],['Eskilstuna',7]],
    'Strängnäs' :[['Stockholm',9],['Eskilstuna',5]],
    'Kungsör' : [['Köping',3],['Eskilstuna',5]],
    'Köping' : [['Kungsör',3],['Västerås',4]],
    'Eskilstuna' : [['Kungsör',5],['Västerås',5],['Strängnäs',5]],
}
cities3 = {
    'Stockholm' : [['Strängnäs',9],['Västerås',10]],
    'Västerås' : [['Stockholm',10],['Köping',4],['Eskilstuna',7]],
    'Strängnäs' :[['Stockholm',9],['Eskilstuna',5]],
    'Kungsör' : [['Köping',3],['Eskilstuna',5],['Katrineholm',5]],
    'Köping' : [['Kungsör',3],['Västerås',4]],
    'Katrineholm' : [['Kungsör',5]],
    'Eskilstuna' : [['Kungsör',5],['Västerås',5],['Strängnäs',5]],
}


import util

def dfs(visited, graph, node):
    if node not in visited:
        print (node)
        visited.add(node)
        for neighbour in graph[node]:
            dfs(visited, graph, neighbour)

def bfs(visited, graph, node):
    if len(visited)==0:
        print (node)
        visited.add(node)
    for neighbour in graph[node]:
        if neighbour not in visited:
            print (neighbour)
            visited.add(neighbour)
    for neighbour in graph[node]:
        bfs(visited, graph, neighbour)



def depthFirstSearch(node,graph,goal): #Söker djupet först
    #Skapar en lista enligt LIFO (Last in first out) principen. håller värdena state och actions.
    frontier = util.Stack()
    #Redan tidigare utforskade noder, en array med states.
    exploredNodes = []
    #Skapar startNoden, innehåller en tom start statet och en tom array då vi inte har några actions
    startNode = (node, [])
    #Lägger in startnoden i frontier
    frontier.push(startNode)
    
    while not frontier.isEmpty(): #sålänge frontier inte är tom så kör
        #Ta den node som sist blev inlagd i frontier arrayen. Delar upp den i state och actions
        currentState, actions = frontier.pop()
        #Om Nuvarande noden inte är utforskad så lägg den i utforskad
        if currentState not in exploredNodes:
            exploredNodes.append(currentState)
            #Om denna noden är målet så printa ut vägen och returna actions (väg från början till mål)
            if goal==currentState:
                print(node,"to", goal, actions)
                return actions
            else:
                #Ta fram alla möjliga vägar att gå vidare genom att titta i graph vilka barn som finns till noden.
                successors = graph[currentState]
                #Lägg till varje Successor i frontier efter att ha räknat ut deras action.
                # print(currentState,successors)
                for succState, succCost in successors:
                    newAction = actions + [succState]
                    newNode = (succState, newAction)
                    frontier.push(newNode)

    return actions  

#Okommneterad
# def depthFirstSearch(node,graph,goal):
#     frontier = util.Stack()
#     exploredNodes = []
#     startState = node
#     startNode = (startState, [])
#     frontier.push(startNode)
#     while not frontier.isEmpty():
#         currentState, actions = frontier.pop()
#         if currentState not in exploredNodes:
#             exploredNodes.append(currentState)

#             if goal==currentState:
#                 print(startState,"to", goal, actions)
#                 return actions
#             else:
#                 successors = graph[currentState]
#                 for succState, SuccCost in successors:
#                     newAction = actions + [succState]
#                     newNode = (succState, newAction)
#                     frontier.push(newNode)
#     return actions  

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
                for succState, succCost in successors:
                    newAction = actions + [succState]
                    newCost= currentCost+succCost
                    newNode = (succState, newAction,newCost)
                    frontier.push(newNode)

    return actions  


# def breadthFirstSearch(node,graph,goal):
#     frontier = util.Queue()
#     exploredNodes = []
#     startState = node
#     startNode = (startState, [],0)
#     frontier.push(startNode)
#     while not frontier.isEmpty():
#         currentState, actions,currentCost = frontier.pop()
#         if currentState not in exploredNodes:
#             exploredNodes.append(currentState)
#             if goal==currentState:
#                 print(startState,"to", goal, actions,"Cost:",currentCost)
#                 return actions
#             else:
#                 successors = graph[currentState]
#                 for succState, succCost in successors:
#                     newAction = actions + [succState]
#                     newCost= currentCost+succCost
#                     newNode = (succState, newAction,newCost)
#                     frontier.push(newNode)

#     return actions  

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
                for succState, succCost in successors:
                    newAction = actions + [succState]
                    newCost= currentCost+succCost
                    newNode = (succState, newAction,newCost)
                    frontier.update(newNode,newCost)
    return actions  



#     return actions  

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
            print(exploredNodes)
            print(node,"to", goal, actions,"Cost:",currentCost)
            return actions
        else:  
            #Ta fram alla möjliga vägar att gå vidare genom att titta i graph vilka barn som finns till noden.
            successors = graph[currentState] 
             #Lägg till varje Successor i frontier samt uppdatera den efter att ha räknat ut deras action.
            for succState, succCost in successors:
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
            print(exploredNodes)
            print(node,"to", goal, actions,"Cost:",currentCost)
            return actions
        else:
            successors = graph[currentState]
            for succState, succCost in successors:
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







# Driver Code

# visited = set() # Skapar och sätter en array som ska ha koll på besökta noder
# print("Breadth first Search")
# bfs(visited, graph, 'A')
# print("Depth first Search")
# visited = set() # Set to keep track of visited nodes.
# dfs(visited, graph, 'A')


# print("depthFirstSearch")
# test= depthFirstSearch("Stockholm",cities,"Kungsör")
# print(test)

# print("breadthFirstSearch")
# test= breadthFirstSearch("Stockholm",cities,"Kungsör")
# print(test)

# print("uniformCostSearch")
# test= uniformCostSearch("Stockholm",cities,"Kungsör")
# print(test)

# print("aStarSearch")
# test= aStarSearch("Stockholm",cities,"Kungsör")
# print(test)

# print("greedyBestFindSearch")
# test= greedyBestFindSearch("Stockholm",cities,"Kungsör")
# print(test)
print("depthFirstSearch")
test= depthFirstSearch("Stockholm",cities3,"Katrineholm")
print(test)

print("breadthFirstSearch")
test= breadthFirstSearch("Stockholm",cities3,"Katrineholm")
print(test)

print("uniformCostSearch")
test= uniformCostSearch("Stockholm",cities3,"Katrineholm")
print(test)

print("aStarSearch")
test= aStarSearch("Stockholm",cities3,"Katrineholm")
print(test)

print("greedyBestFindSearch")
test= greedyBestFindSearch("Stockholm",cities3,"Katrineholm")
print(test)

