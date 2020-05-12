# N-Queens problem
![Nqueens](https://github.com/abbjoafli/AI/blob/master/img/nQueens.png)
##Intro 
I denna uppgift kommer vi titta bitvis på [denna video](https://www.youtube.com/watch?v=JxYhc0QMVVY). Vi kommer varva varje segment med en uppgift så när du tittat på en del, gå då vidare till nästa kapitel.
De segment du ska kolla är följande:
1. Teorin 0.0 - 8.13
2. Psuedokod 8-14 - 12.23
3. Kod
   1. Steg 1 12.24 -20:25
   2. Steg 2 20:26 - 22:44
   3. Steg 3 22.45 - 27.23
   4. Steg 4 27.24 - 29.41

## Teorin
Videodel: 0.0 - 8.13
Nu när du har tittat på teorin så vill jag att du skapar psuedukod eller en uml, det vill säga diagram över vilka metoder du behöver ha för att kunna skapa ett program som kan lösa N-Queens problem.

Alltså, välj ett program, paint, powerpoint eller annat och rita upp rutor för vad din metod heter, vad man ska skicka in och vad som kommer ut. Det är även bra om du skriver några rader om vad metoden gör gå sedan vidare till nästa del.

## Psuedokod
Videodel: 8-14 - 12.23
Jämnför dina diagram med mina, har du missat något eller gjort saker på ett annat sätt? Det är helt okej att göra på andra sätt, om det håller kommer vi testa i kommande del.

## Kod
I koddelarna försöker du först och tittar sedan på videon om du fastnar eller är klar för att jämnföra och se att det blir rätt.
### Steg 1
Videodel: 12.24 -20:25

I första steget ska du skapa en spelplan där du kan placera ut dina damer, damerna ska skickas med in och du ska testa med alla fall nedan. Efter spelplanen har skapats ska du räkna ut score på damerna och skriva ner dem. 28 är full pott, 0 är ja noll.

- Queens= "24748552"
- Queens= "82417536"
- Queens= "...3333."
- Queens= "...543."
- Queens= "...345."
- Queens= "55555555"


### Steg 2
Videodel: 20:26 - 22:44

I andra steget ska vi istället placera damerna slumpmässigt på brädet. Gör en metod som skapar X antal bräden och placerar Y antal damer på det. Efter detta så vill jag att du kör metoderna du skapat i steg 1 för att räkna ut scoren på dessa. Därefter ska vi konvertera score till procent.

Testa sedan att köra detta med att du skapar 4 bräden och har lika många damer som rader.

### Steg 3
Videodel: 22.45 - 27.23

På steg tre  ska vi utifrån procenten skapa nya damer som kan användas för att komma ett steg närmare den magiska 28an.

Dessa nya damer ska köra alla steg igen som har skett innan.

### Steg 4
Videodel: 27.24 - 29.41

I sista steget ska du lägga ihop alla delar så den kör från början med random damer till att den har nåt scoren 28. Den ska vid jämna mellanrum skriva ut hur många varv den gått samt vilket score den har just då.


#Bra länkar
- [Testa själv bräda](http://www.datagenetics.com/blog/august42012/)
- [Teorin i pp](https://www.slideshare.net/SKAhsan/modified-genetic-algorithm-for-solving-nqueens-problem-54527086)
- [Teori i video](https://www.youtube.com/watch?time_continue=1&v=shfJ18BewqM&feature=emb_logo), [del två](https://www.youtube.com/watch?time_continue=66&v=7ZX6Su2Xdi0&feature=emb_logo)


#Facit

Lösningsförslag för hela NQueens problemet ligger i Exempel/8Queens.py

##Kod steg 1
- "24748552" = 24
- "82417536" = 28
- "...3333." = 22
- "...543."  = 25
- "...345."  = 25
- "55555555" = 0
