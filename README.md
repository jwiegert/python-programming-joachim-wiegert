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

## 2021-08-31

Om for-loops.

- "for each" loop, loopar igenom varje element i en lista.
- I en del andra språk kan det vara t.ex.
    for (int = 0; i<=10; i++)
    Den börjar på noll, och adderar på i tills den når 10.
- I python skriver man
    for i in range(10)
    Där range(10) är en lista med heltal från 0 till 9.
- I range() kan man ge start, stopp, och step size. Range är INTE en lista, det är ett "range objekt".
- range(2,15,3) kommer ge i = 2, 5, 8, 11, 14.

## 2021-09-02

Om lists.

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

## 2021-09-06

- list comprehensions med if-sats

List comprehensions ÄR aningen snabbare än forloopar. Men inte jätte, så det man ska satsa på är läsligheten i första hand. Ibland är listcomprehensions lättare att läsa, ibland inte.

- strings: 

En sträng är egentligen en lista med unicode tecken. SÅ en lsita med strängar är egentligen en lista där varje element är en lista till med tecken.

Concaternating strings: att slå ihop strängar till en ny kombination. T.ex. "kokchun" + "giang" blir "kokchungiang". (Man kan slå in mellanslag också med + " " +)

- Multiline fstring

Printa strängen som flera rader

f"""
Blabla
blabla
yadayada
"""

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