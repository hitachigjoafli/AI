from random import randint
#TestQueens
Queens= "24748552" #24
# Queens= "82417536" #28 = vinst
# Queens= "...3333." #22
# Queens= "...543." #25
# Queens= "...345." #25
# Queens= "55555555" #0
rows = 'ABCDEFGH'
cols = '12345678'


#Placerar ut på ett bärde, skickar in antalet damer, rader och kolumner.
def PlaceOnBoard(Queens,rows,cols):
    #Skapar rutnät och lägger in . på varje plats
    Board = [r + c for r in rows for c in cols] 
    BoardDict = { i : "." for i in Board }
    counter=0
    Boardplaces=[]
    #För varje dam lägg ut ett Q på den platsen i Boarden. Lägg även in den platsen i Boardplaces
    for Queen in Queens:
        if Queen!=".":
            BoardDict[rows[counter]+Queen]="Q"
            Boardplaces.append(rows[counter]+Queen)
        counter+=1
    return BoardDict,Boardplaces

#Fitfunctionen, skicka in Boarddictionarien, Damernas placering och om det ska loggas eller inte
#Det som händer är att man tittar på alla möjliga sitationer en dam kan kollidera med en annan. Alltså samma rad, samma kolumn eller på någon av diagonalerna.
def fitfunction(BoardDict,Boardplaces,Logger):
    #Tips
    # print(BoardDict['A2'])
    # letter="B"
    # print(BoardDict[letter+'3'])
    AllQueenInteractions=0
    #För varje dam så dela upp placeringen i rad och kolumn
    for QueenPlace in Boardplaces:
        if Logger:
            print("Queenplace:",QueenPlace)
        Queennumber=int(QueenPlace[1])
        Queenletter= QueenPlace[0]
        counter=1
        #Rows
        for letter in rows:
            if letter==Queenletter:
                break
            counter+=1
        for Other in rows[counter::]:
            if BoardDict[Other+QueenPlace[1]]== "Q":
                if Logger:
                    print("Rows"+QueenPlace+" "+(Other+QueenPlace[1]))
                AllQueenInteractions+=1
    #Up
        paralell=Queennumber+1 
        for Other in rows[counter::]:
            if(paralell>8):
                break
            if BoardDict[Other+str(paralell)]== "Q":
                if Logger:
                    print("Up"+QueenPlace+" "+(Other+str(paralell)))
                AllQueenInteractions+=1
            paralell+=1
    #Down
        paralell=counter+Queennumber-1
        morethen=paralell-len(Queens)
        Cutlist= rows
        if morethen>0:
            Cutlist= rows[morethen:]
            paralell-=morethen
        for Other in Cutlist:
            if(paralell==Queennumber):
                break
            if BoardDict[Other+str(paralell)]== "Q":
                if Logger:
                    print("Down "+QueenPlace+" "+(Other+str(paralell)))
                AllQueenInteractions+=1
            paralell-=1

    AttackningLadies= 28-AllQueenInteractions
    if Logger:
        print("Interactions:",AllQueenInteractions, "Score:",AttackningLadies)
    return AttackningLadies

#Placerar ut damerna random, skickar man in 8 4 så skapar den 4 listor med 8 tecken i varje.
def PlaceQueensrandom(NumberOfQueens,NumberOfBoards):
    Queenslist=[]
    for QueensOnBoard in range(NumberOfBoards):
        Queens=""
        for Q in range(NumberOfQueens):
            Queens+=str(randint(1, NumberOfQueens))
        Queenslist.append(Queens)
    return Queenslist

#Konverterar scoren till procent
def NormalizeToPercent(Scores):
    Sum=0
    for Score in Scores:
        Sum+=Score
    # print(Sum)
    Percent=[]
    for Score in Scores:
        Percent.append(Score/Sum*100)
    return Percent

#Skapar nya damer utifrån procent och slump för mutation.
def CreateNewQueens(Queens,Percent,Logger):
    #Select Breeding parent
    SelectQueens=[]
    for counter in range(len(Queens)):
        
        RandomNumber=randint(0, 99)
        PercentValue=0
        for P in range(len(Percent)):
            PercentValue+=Percent[P]
            # print("Parent:",P,RandomNumber)
            if RandomNumber<=PercentValue:
                
                if Logger:
                    print("Random number:",RandomNumber," Board:",P+1)
                SelectQueens.append(Queens[P])
                break
            
    if Logger:
        print("Selected:",SelectQueens)
    #Mix parents
    if len(SelectQueens)<4:
        print("Selected:",SelectQueens,Queens,Percent)
        input()
    NewQueens=[]
    startindex=0
    for counter in range(int(len(SelectQueens)/2)):
        DividePlace= randint(1, len(SelectQueens[0])) #Exempel 3, då tar man de tre första från 1an och 5 sista från tvåan och vice versa.
        NewQueens.append(SelectQueens[counter+startindex][:DividePlace]+SelectQueens[counter+1+startindex][DividePlace:])
        NewQueens.append(SelectQueens[counter+1+startindex][:DividePlace]+SelectQueens[counter+startindex][DividePlace:])
        startindex+=1
    #Mutation
    for Queen in range(len(NewQueens)):
        QasList=list(NewQueens[Queen])
        for place in range(len(QasList)):
            #Ändra slumpchansen nedan för att ställa in hur stor chans det är för mutation.
            RandomNumber=randint(0, 10)
            if RandomNumber==5:
                QasList[place]=str(randint(1, 8))
                if Logger:
                    print("Mutation:",Queen,"=>",QasList,place)
        NewQueens[Queen]="".join(QasList)
    if Logger:
        print("New Queens:",NewQueens)
            
    return NewQueens

#Steg 1
# BoardDict, BoardPlaces= PlaceOnBoard(Queens,rows,cols)
# print(BoardDict)
# fitfunction(BoardDict, BoardPlaces,True)

# Steg 2
# AllQueens=PlaceQueensrandom(len(rows),4)
# Scores=[]
# print(AllQueens)
# for OneQueen in AllQueens:
#     BoardDict, BoardPlaces= PlaceOnBoard(OneQueen,rows,cols)
#     # print(BoardDict)
#     Scores.append(fitfunction(BoardDict, BoardPlaces,False))

# print(Scores)
# Percent= NormalizeToPercent(Scores)
# print(Percent)
# # #Steg 3
# NewQueens= CreateNewQueens(AllQueens,Percent,True)
# for OneQueen in NewQueens:
#     BoardDict, BoardPlaces= PlaceOnBoard(OneQueen,rows,cols)
#     # print(BoardDict)
#     Scores.append(fitfunction(BoardDict, BoardPlaces,False))

# Steg 4
AllQueens=PlaceQueensrandom(len(rows),4)

BestScore=0
print(AllQueens)
Iteration=1
while BestScore<28:
    Scores=[]
    for OneQueen in AllQueens:
        BoardDict, BoardPlaces= PlaceOnBoard(OneQueen,rows,cols)
        # print(BoardDict)
        Scores.append(fitfunction(BoardDict, BoardPlaces,False))

    for S in range(len(Scores)):
        Score= Scores[S]
        if Score>BestScore:
            print("New best score",Score,"with", AllQueens[S],"in iteration",Iteration )
            BestScore=Score
    if Iteration%100==0:
        print(Scores, "Iternation:",Iteration)
    Percent= NormalizeToPercent(Scores)
    # print(Percent)
    AllQueens= CreateNewQueens(AllQueens,Percent,False)
    Iteration+=1
