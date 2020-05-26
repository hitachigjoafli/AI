# Sökalgoritmer i labyrint
![Sökalgoritmer](https://github.com/abbjoafli/AI/blob/master/img/Labyrint.PNG?raw=true)
## Intro
I denna uppgift kommer vi titta bitvis på [denna video](https://www.youtube.com/watch?v=VS7XxEeWahU). Vi kommer varva varje segment med en uppgift så när du tittat på en del, gå då vidare till nästa kapitel.
De segment du ska kolla är följande:
1. Teori 0:0 - 4:15
2. Skapa Board 4:16 - 9:38
3. Ändra i metoderna 9:39 - 11:43
4. Skapa grafisk värld 11:44 - 14:09
5. Skapa musen 14:10 -19:17
6. Körning av koden 19:18 -21:59

## Teorin
Videodel: 0.0 - 4:15
Nu när du har tittat på teorin så vill jag att du funderar hur du skulle kunna skapa ett bräde samt nodes som håller värden och möjliga actions. när du har gjort detta eller fastnat så kika på nästa del för tips.
## Skapa Board
Videodel: 4:16 - 9:38
När du har fått det här att fungera så vill jag att du skapar minst tre olika versioner av din labyrint, en "tom" med bara samma värden på alla steg. En med väggar som blockar framkomst möjligheterna en aning och en med olika värden på noderna som tvingar algoritmen att göra val.
Efter detta ska du ändra i metoderna så du får dessa att fungera med Labyrinten istället för sökträden från förra videon.

## Ändra i metoderna
Videodel: 9:39 - 11:43
Fungerar metoderna? Uppdaterade du DFS så även den räknar hur mycket "kostnad" dess val gör. Om inte så gör gärna det också. Nu vill vi lägga alla vägar i en array som sedan kommer användas för att stegvis visa upp hur vår AI rör sig genom banan.

 För detta ska vi skapa en grafiska världen som musen lever i. Jag använder TKinter, ett inbyggt python bibliotek som det finns mycket dokumentation om på internet.
 Här är finns några [färger](http://www.science.smith.edu/dftwiki/index.php/Color_Charts_for_TKinter) man kan använda för att visa höjd skillnad.

Vill man ha tips så använde jag ** C.create_rectangle ** för att skapa mitt labyrintmönster.


## Skapa grafisk värld
Videodel:  11:44 - 14:09
När du skapat den grafiska världen så är det dags för att skapa musen, Musen i mitt fall är bara en liten rektangel. Gör den gärna bättre med en bild om du vill. Den rör sig genom en metod som heter getCoord och räknar ut positionerna på kartan utifrån dens Boardposition * storleken på blocken.

Vill man ha tips så använde jag ** C.move(Mouse, MovementX, MovementY) ** för att flytta musen, då MovementX är nästa positions värde minus denna.


## Bygga vidare
Här är några möjliga sätt att bygga vidare på övningen.
- Färga vägen musen går med olika färger för att visa de olika algoritmernas färd.
- Lägg ut fler mål.
- Ändra målet när det är nått och få musen att gå vidare.

# Facit
Facit på koden ligger i exempelkod!
