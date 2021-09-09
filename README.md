# Python-programming-course

Repository for problems, labs, and assigments for courses in Python programming.

# Lecture notes

## 2021-08-24

Strings: normally uses "", but '' is practically the same. Be consistent!

print(f"text {variable} test"), a newer and more versatile way of printing outputs. With e.g. {variable:.3f} you round to 3 decimals (as in C).

float(VARIABLE) > changes variable class to float
int(VARIABLE)   > ... to integer, etc

if conditions:
    statement1
    statement2
    statement3
else:
    statement1
    statement2
    statement3

if condition1 and condition2:
    THEN HAPPENS THIS
else:
    IF only 1 of 0 conditions are true this happens.

if conditions1 or condition2:
    if 1 or 2 is true, this happens.
else:
    If 0 are true, this happens

## 2021-08-26

Push: laddar upp det som man har på datorn.
Pull: hämtar hem det som finns på huben, t.ex. om man jobbat hemifrån på en annan dator...

random as rnd
rnd.seed() för att välja seed
rnd.randint(x,y) slumpat heltal mellan x och y.

Assignment operators:
- n += 1 : n = n+1
- x /= 2 : x = x/2

Skapa flera variabler:
- x,y,z = 1,2,3
- x=1, y=2, z=3

While statements, när man inte vet hur många loopar som behövs.

pipenv: en pip-environment
Öppna ett speciellt shell för ett speciellt projekt:
 
 - $ pipenv shell

I den katalog där projektet är. Det skapar en pipfile och en pipfile.lock, dessa innehåller info om vad som gäller för detta environment, vilken pythonversion och vilka paket.

- Exit pipenv: > exit

- Gå tillbaka till pipenv: $ pipenv shell, är jag redan i katalogen med pipfile etc så återgår den till shell'et jag redan har där. Annars skapar den ett nytt där jag är.

Installera paket till det pipenv jag är i är då bara att skriva

- $ pipenv install PACKAGENAME

så hamnar den i listan av paket i pipfile. Och tvärtom, uninstall

- $ pipenv uninstall PACKAGENAME

Med pipenv kan man nyttja t.ex. en "requirements.txt" som listar requirements såsom det skrivs i en pipfile. Det är bara att copypastea en sån lista till ens enviroment, och sen skriver man

- $ pipenv install -r ./[LÄNKTILLREQUIREMENTS.TXT]

I pipfile, under packages, står versionsnamn till höger, står det t.ex. numpy = "*" så kör den den senaste versionen.

## 2021-08-31 : Om for-loops.

- "for each" loop, loopar igenom varje element i en lista.
- I en del andra språk kan det vara t.ex.
    for (int = 0; i<=10; i++)
    Den börjar på noll, och adderar på i tills den når 10.
- I python skriver man
    for i in range(10)
    Där range(10) är en lista med heltal från 0 till 9.
- I range() kan man ge start, stopp, och step size. Range är INTE en lista, det är ett "range objekt".
- range(2,15,3) kommer ge i = 2, 5, 8, 11, 14.

## 2021-09-02 : Om lists.

I en lista i Python kan man lägga in nästan vad som helst, strängar, ints, floats.

- a = ['a', 'hej där', 5, 5.3, '5', True]

Pythonindex börjar med 0, så a går här från a[0,4]. Men len(a) = 5. a:s index här är antingen

-  0  1  2  3  4

eller

- -5 -4 -3 -2 -1

List comprehenion: Svart magi för att formulera listor på en enda rad istället för med forloops.

- a = [x**2 for x in range(1,10)] - ger en lista med kvadraterna av 1-10. Kan också göra lista i lista så här

- a = [[x**2 for _ in range(1,10)] for x in range(1,1)] ger en 10x10matris där raderna är fyllda med kvadraterna av 1-10.

if-satser får man också ha med.

## 2021-09-06 : strings

- Googla på "string methods in python" så hittas en massa kommandon man kan använda för strängar: https://www.w3schools.com/python/python_ref_string.asp

- list comprehensions med if-sats

List comprehensions ÄR aningen snabbare än forloopar. Men inte jätte, så det man ska satsa på är läsligheten i första hand. Ibland är listcomprehensions lättare att läsa, ibland inte.

- strings: 

En sträng är egentligen en lista med unicode tecken. SÅ en lsita med strängar är egentligen en lista där varje element är en lista till med tecken.

Concaternating strings: att slå ihop strängar till en ny kombination. T.ex. "kokchun" + "giang" blir "kokchungiang". (Man kan slå in mellanslag också med + " " +)

- Multiline fstring

Printa strängen som flera rader

```py
f"""
Blabla
blabla
yadayada
"""
```

Kommer printas exakt så. För loopar och annat är det dock lämpligare att använda \n för newline.

FYI \b innebär backspace, dvs sudda ut det som skrivits precis innan.

- Split

Går att dela upp en lång sträng med ett speciellt tecken, t.ex. kommatecken eller mellanslag (default)

bamba = "chili sin carne, köttbullar, fisk, pannkakor, taco".split(",")

- zip

Går att loopa genom två listor samtidigt

for x,y in zip(xlist,ylist):
    x är elementen i xlist
    y är elementen i ylist

- Indexering

Så en sträng är en list med unicode-tecken.

[]-operatorn används för att komma åt specifika element i en lista.

slicing-operatorn (:) använder för att komma åt sekvenser av index.

För en sträng så ger sträng[0] första tecknet. [1] andra tecknet etc. Så kan man plocka ut enstaka ord.

Går att söka på strängar också med STRÄNG.find("word") - det ger index för den första bokstaven av ordet.

- Ändra datatyp hos strängar

En sträng med siffror: ['1','2','3']

Går inte att ändra med int(sträng)

Ett sätt är att använda listcomprehension:

sträng = [float(x) for x in sträng]

Men om ett av elementen INTE är en siffra då? Lägg till ifsats med STRÄNG.isdigit(), vilket ger True eller False.

- Regular expressions

Med vanliga strängar kan man leta efter specifika ord eller siffror. Men med regexp kan man leta efter MÖNSTER som är vnaliga för det man letar efter, t.ex. telefonnummer eller emailadresser.

- Exempel, telefonnummer: 031-548652

Detta har 3 siffror, bindestreck och 6 siffror: ddd-dddddd. Här är d en del av ett set: d tillhör {0,1,2,3,4,5,6,7,8,9}

Behöver paketet regular expresions

import re

re.findall(blabla, sträng) är kortfattad syntax (se codealong).

Eller googla lite efter t.ex. "find phone numbers with python regular expressions". Så kan man få list på patterns som man kan söka efter.

# 2021-09-07 : funktioner bl.a.

Samt "kod i discord" och intro till lab2.

- om man vill skriva kod i discord så att det blir snyggt formaterat:

```py
KOD HÄR
```

- funktioner:

Väldigt enkelt: input parametrar in, ut är "return", samma som x -> f(x).

I python finns olika typer av funktioner, med och utan både input och returnvärden. Men det är ett sätt att strukturera upp sin kod. Man kan på så vis återanvända kod istället för att copy-pastea samma kodsnutt flera gånger.

En funktion utan returnvärde i andra språk skulle använda sig av "void"-kommandot. Men inte i python. Det är bara att skriva på.

- funktioners syntax

Exempel, funktion som tar fram största av 2 tal.

```py
def biggest(num1, num2):
    if num1 > num2:
        return num1
    else:
        return num2

print(biggest(3,6))
```

keywords för att starta funktioner: "def FUNKTIONSNAMN( INPUTPARAMETRAR )". "def" = "define", definiera funktionsnamnet.

Sedan ett funktionsblock. Satser odyl.

Sen har vi return-satser, alltså vad ska funktionen returnera?

Input-parametrar till en funktion kallas för "argument".

Man kan inte tvinga funktionen att bara använda en viss datatyp. Men man kan spec'a i help'en till ens funktion vad den ska ha för datatyper som input.

Variablar och parametrar i en funktion är lokala! Så de existerar bara inne i funktionen. Jag kan inte åkalla variabler från en funktion

- Defaultvärden går att definiera i en funktion så man måste inte ha input alltid ens.

def funktionsnamn(variabal1 = x, variabel2 = y)

Dessa värden går att skriva över gneom att anropa funktionen och ge egna värde. Men man kan också skriva funktionen utan inputs såhär.

- funktioner i egna filer

Det går att göra! Man kan ha många funktioner i en och samma fil. Sen måste man ladda in den med pythons klassiska import (ligger i samma katalog då). T.ex.

```py
import MINAFUNKTION as FÖRKORTNING
```

- Arbitrary arguments.

Om man inte vet hur många argument som ska in i funktionen kan man använda sig av arbitrary arguments: *args:

```py
def FUNKTION(*ARGUMENTNAMN):
```

Denna blir som en tuple då, den är som en lista, kan vara vilken längd som helst.

- anonyma funktioner

Behöver inte definieras med def. Istället använder man sig av lambda-funktionen, t.ex.

```py
cube = lambda x: x**3
print(cube(3)) # gives 3**3 = 27.
```

Man kan ha en lambda-funktion i en funktion. Då blir syntaxen att man anropar en funktion i en funktion. (se ipynb-filen, 6_functions)

# 2021-09-09 : felhantering/error handling

Feltyper

- syntax error: syntaxfel alltså, python förstår inte koden.

```py
NameError: name 'prin' is not defined
```

- Logiska fel: svåra att hitta, koden funkar utan problem men man får oväntade resultat. Man har råkat skriva fel nånstans, t.ex. fel ekvation, missar nån kvadrat eller nåt.

- Exception error: Python vet vad den ska göra men kan inte göra det. Error-meddelanden är då väldigt specifika, t.ex. "index out of range".

- Man kan skriva över keywords i python. Så man kan döpa variabler till kommandon, t.ex. "print = namn" gör att print blir en variabel. Nu blir det omöjligt att köra print tills man startar om python och hittar felet. Kan bli svårt att hitta...

- Man kan döpa en pythonfil till samma namn som en modul eller bibliotek. T.ex. kan man råka ha ett script som heter "math.py". "import math" importerar då DEN filen och inte math-modulen! Mycket farligt!
