# Sökalgoritmer i träd
![Sökalgoritmer](https://github.com/abbjoafli/AI/blob/master/img/tree.PNG?raw=true)
##Intro
I denna uppgift kommer vi titta bitvis på [denna video](https://www.youtube.com/watch?v=1IO_zn6vVms). Vi kommer varva varje segment med en uppgift så när du tittat på en del, gå då vidare till nästa kapitel.
De segment du ska kolla är följande:
1. Teori (DFS, BFS, Uniform) 0.0 - 10.08
2. Psuedokod och implementering av DFS 10.09 - 14.33
3. Kod
   1. Breadth First Search 14.33 - 16.05
   2. Uniform Cost Search 16.06 - 17.39
4. Teori (Greedy, A*) 17.40 - 24.30
5. Kod
   1. Greedy Best Search 24.31 - 26.56
   2. A* Search 16.06 - 17.39

## Teorin (DFS, BFS, Uniform) 
Videodel: 0.0 - 10.08
Efter att ha tittat på teorin delen så ska vi räkna ut vilken väg vi tar med de olika sökalgoritmerna vi nu har gått igenom. Desa är depthFirstSearch, breadthFirstSearch och uniformCostSearch. Titta på kartan nedan och försök lista ut vilken väg varje algoritm väljer på **sträckan Stockholm till Katrineholm**. Tänk på att det kan variera beroende på vilken ordning man väljer sina val. Ska man vara ordentlig ska man enlight DFS gå enlight principen LIFO (Last in first out) och BFS enligt FIFO(First in first out) så var konsekvent i vilken ordning du räknar alternativen för rättvisa resultat!
![Karta](https://github.com/abbjoafli/AI/blob/master/img/Sverigekartan.PNG)

Nu när du har bestämt vägarna för de tre algoritmerna så vill jag att vi leker med den mycket verkliga tanken att en vulkan mellan Eskilstuna och Katrineholm får ett utrbrott och flöder vägen med varm magma. Räka ut vägarna nu med vägen mellan Eskilstuna och Katrineholm bortplockad.
![Karta](https://github.com/abbjoafli/AI/blob/master/img/Sverigekartan2.PNG)

## Psuedokod och implementering av DFS
Videodel: 10.09 - 14.33
Innan du tittar på nästa del så fundera hur du skulle kunna skapa en Depth first search utan att använda rekursion (att den anropar sig själv). Vilka moment måste finnas med för man ska få det att fungera? Klura inte förlänge utan gå vidare till att titta på videon för att se hur jag har gjort och implementera koden i ett python program.

För att kunna göra koddelarna så ladda ner utils.py från example mappen och använd dess Stack, Queue och PriorityQueue funktioner.

## Kod
### Breadth First Search
Videodel: 14.33 - 16.05
Försök själv med att använda depthFirstSearch koden som grund och implementera Breadth First search. Titta på videon efter eller om du fastnar för tips och kontroll.

### Uniform Cost Search
Videodel: 16.06 - 17.39
Försök själv med att använda depthFirstSearch koden som grund och implementera Breadth First search. Titta på videon efter eller om du fastnar för tips och kontroll.

## Teorin (Greedy, A*)
Videodel: 17.40 - 24.30
Nu gör vi samma som i första teoridelen fast för Greedy och A*
![Karta](https://github.com/abbjoafli/AI/blob/master/img/Sverigekartan.PNG)

Såklart både med raka vägar och med vulkan scenariona!
![Karta](https://github.com/abbjoafli/AI/blob/master/img/Sverigekartan2.PNG)

## Kod
### Greedy Best Search
Videodel: 24.31 - 26.56
Försök själv med att använda depthFirstSearch koden som grund och implementera Greedy Best Search. Titta på videon efter eller om du fastnar för tips och kontroll.

### A* Search
Videodel: 26.56 - 29.08
Försök själv med att använda depthFirstSearch koden som grund och implementera A* Search. Titta på videon efter eller om du fastnar för tips och kontroll.

#Facit

Lösningsförslag för hela Trädsökningsproblemet ligger i Exempel/graph.py

## Teorin
Dictionarin
```python
cities3 = {
    'Stockholm' : [['Strängnäs',9],['Västerås',10]],
    'Västerås' : [['Stockholm',10],['Köping',4],['Eskilstuna',7]],
    'Strängnäs' :[['Stockholm',9],['Eskilstuna',5]],
    'Kungsör' : [['Köping',3],['Eskilstuna',5],['Katrineholm',5]],
    'Köping' : [['Kungsör',3],['Västerås',4]],
    'Katrineholm' : [['Kungsör',5],['Eskilstuna',6]],
    'Eskilstuna' : [['Kungsör',5],['Västerås',5],['Strängnäs',5],['Katrineholm',6]],
}
```
### DFS, BFS Uniform
#### Resultat Stockholm - Katrineholm
```python
depthFirstSearch
Stockholm to Katrineholm ['Västerås', 'Eskilstuna', 'Katrineholm']

breadthFirstSearch
Stockholm to Katrineholm ['Strängnäs', 'Eskilstuna', 'Katrineholm'] Cost: 20

uniformCostSearch
Stockholm to Katrineholm ['Strängnäs', 'Eskilstuna', 'Katrineholm'] Cost: 20

```
#### Resultat Stockholm - Katrineholm med vulkan mellan Eskilstuna - Katrineholm
```python
depthFirstSearch
Stockholm to Katrineholm ['Västerås', 'Eskilstuna', 'Kungsör', 'Katrineholm']

breadthFirstSearch
Stockholm to Katrineholm ['Strängnäs', 'Eskilstuna', 'Kungsör', 'Katrineholm'] Cost: 24

uniformCostSearch
Stockholm to Katrineholm ['Västerås', 'Köping', 'Kungsör', 'Katrineholm'] Cost: 22
```


### Greedy, A*
#### Resultat Stockholm - Katrineholm
```python
greedyBestFindSearch
Stockholm to Katrineholm ['Strängnäs', 'Eskilstuna', 'Katrineholm'] Cost: 20

aStarSearch
Stockholm to Katrineholm ['Strängnäs', 'Eskilstuna', 'Katrineholm'] Cost: 20

```
#### Resultat Stockholm - Katrineholm med vulkan mellan Eskilstuna - Katrineholm
```python
greedyBestFindSearch
Stockholm to Katrineholm ['Strängnäs', 'Eskilstuna', 'Kungsör', 'Katrineholm'] Cost: 24

aStarSearch
Stockholm to Katrineholm ['Västerås', 'Köping', 'Kungsör', 'Katrineholm'] Cost: 22

```
