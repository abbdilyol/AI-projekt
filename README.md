# Chatbot

## Projektet
Det jag har gjort är en chatbot som man skulle kunna prata/ha en konversation med och kanske fråga den om saker som t.ex. väder, tid, fakta osv. Det var meningen att man skulle kunna prata med och att den skulle kunna prata med dig men eftersom att ljudkortet på min dator inte fungerar kan den inte spela upp ljud och har problem med att läsa av ljud (text to speech). 

I själva AI delen av min kod har jag använt biblioteket chatterbot som i sin tur använder olika språkbibliotek som nltk och NLP. Chatterbot innehåller färdiga funktioner och program som du kanske behöver modifiera lite samt träna. Länk till documentation finns här: https://chatterbot.readthedocs.io/en/stable/. 

I början använde jag ett sämre dataset och fraser för att träna min bot och då kunde den inte meningar bortom "hello" och "greetings". Efter det hittade jag ett väldigt stort dataset som to ca 7 timmar att träna boten på. Detta dataset var för stort och det tog en haltimme för boten att svara på en enkel fras som "Hi". Till slut bestämde jag mig för att leta runt lite mer på ChatterBots hemsida och hittade de språk och textfilerna som behövdes för att göra en helt ok chatbot. 

## Metoden
Innan jag bestämde mig för att använda ChatterBot gick jag igenom en massa idéer. I början tänkte jag följa en guide som visade hur man faktiskt gjorde sin egna chatbot genom att skriva en kod som gör beslut baserat på sin träning. Det gick bra men jag insåg att jag saknade väldigt mycket data och att jag skulle vara tvungen att hårdkoda många delar av boten. På det sättet som typ alla botar fungerar på är att man har en låt oss säga "språkfil" som innehåller en massa tänkbara fraser från en användare samt botens svar på användarens input. Denna fil skulle ta väldigt lång tid att skriva och det skulle vara omöjligt att göra den bra eftersom man måste ha alla tänkbara saker som användade skrive men man vill också att svaren som boten ger ska vara varierade och inte att den svarar samma sak hela tiden.

Jag bestämde mig för att inte fortsätta på detta sätt men var istället inställd på att hitta färdiga "språkfiler" och träna med de. Det är väldigt svårt att hitta såna filer och de man hittar är ju inte Alexa eller google assistant kvalité. De är kanske 50 hårdkodade rader som baserar sig på att användarens frågor handlar om en fiskresturang eller nåt. 

Efter att jag insåg att det inte gick att hitta några "språkfiler" tänkte jag göra min egen med googles Dialogflow som låter dig träna din egen Google assistant på "språkfiler" som redan finns.  Jag insåg att om jag skulle göra ett python script som tränar på data från google skulle jag inte göra min egen AI för att google redan gjort det så jag struntade i detta också

Till slut hittade jag ChatterBot hemsidan tack vare en vän (https://github.com/abbkhepho). Det uppstod fortfarande problem som jag skrev högre upp vid sista stycket i "Projekt". Vid dethär laget hade jag inte mycket tid på att bekanta mig med koden jag hittade och försökte istället träna AI och lägga till extra funktioner. De extra funktionerna jag la till är att man ska kunna spela en låt från youtube, man kan få information om något från Wikipedia, man kan få veta väder eller tid i en stad och man kan få dagens top 10 nyheter från BBC.

## Resultatet
Resultatet är inte så bra men det är helt ok med tanke på allting som finns. De botar som såna som jag gör är inte bra om man inte hårdkodar de eller tar 99% av all kod/data från andra företag/bibliotek. 

## Reflektion
Om jag hade hittad chatterbot metoden omedelbart skulle jag kunna spendera mer tid på att lära mig biblioteket samt kunna göra ett projekt som jag lite mer kontroll över än att bara kopiera. Jag tänkte till exempel ha med att min bot skulle kuna utföra matematiska beräkningar men jag han inte kolla på den funktionen helt och hållet. 

Det var iallafall mycket som jag hade tänkt ha med men som inte gick för att jag spenderade 80% av min tid för att ta reda på hur jag skulle gå till väga. Trots att min bot inte är jättebra så är den ändå varierad och kan nästan konversera helt ok. 
