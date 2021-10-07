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

Hur man hanterar oväntade fel.

- Exempel: Motverka att användaren kan skriva in felaktigheter. En som inte är så bra på att använda datorn.

Använd : "Try block", "except block", "raise".

Detta till skillnad från att sätta upp en massa if-satser som försöker förutse felaktigheter, Med try: (kombinerat med except och rise) kan man både leta efter allmänna fel och specifika fel. Och man kan få koden att fortsätta förbi felet.

Detta ska användas i lab2!

# 2021-09-13 Filhantering

(Dagens föreläsning använder filerna i Code-Along/files/)

Använd inte bara

> f = open( .... )

använd

> with open( .... ) as f

Det sköter felhantering och stänger automatisk filen sen. Apropå path-hantering, open() här är en relativ path men kan också vara en absolut path. 

(Jag bör testa att skriva
> '../../blabla/hej/etc' 
Funkar det att backa så att säga? LÄgga till r''?)

Olika options till open()

- 'r' = read
- 'w' = write
- 'a' = append (add to existing files)
- 'x' = create file (gives error if file already exists, so that you don't accidently overwrite a file)

Olika sätt att printa ut filen sen:

> print(text)

Ger hur textfilen ser ut

> print(repr(text))

Ger hur textfilen ser ut för python, så här finns \n och annan kod inlagd. Sånt vi vill rensa, så vi behöver inspektera detta innan dåju.

> file.read()

Ger en enda lång sträng av filen

> file.readlines()

Ger en lista där varje rad är ett element i listan (och varje element i listan är en sträng)

### Strategi för att rensa t.ex. quotes.txt

- Inspektera filen

- Ta bort blanksteg och \n för och efter textremsor

- Ta bort onödiga blanksteg mellan ord

- Lägg till siffror till citaten

- Extrahera och lista författare/upphovsmakarna.

Användbart:

> set

tar ut de unika elementen av en lista

```py
set([4,4,4,1,1,1,2,3,4]) == [4,1,2,3]
```

# 2021-09-14 Dictionary

Verktyg för att organisera data. Består av "key:value pair". Man har någon nyckel och får ut något värde. Baseras på datastrukturer och går väldigt snabbt att använda (prestanda: O(1)). Man sätter alltså upp en uppsättning key-words och assign'ar data till dem, listor, strängar etc, vad man vill. Går att anropa sen:

> dictionaryname['dictionarykeyword']

returnerar vad som finns i dictionary under det keyword.

### Dictionary comprehension

Ungefär som list comprehension, fast med dictionary istället. Skrivs ungefär likadant, exempel:

> gradecount = {key: 0 for key in gradelimits}

"key" är keyword som plockas från gradelimits här. 0 är en placeholder med antal personer med visst poäng i det här fallet. Den anopas och ändras lätt med t.ex.

> gradecount[grade] = 10

där grade är ett keyword, i det här fallet ett betyg som exempel

> gradecount['F'] = 10

är 10st har F. {'F': 10}.

# 2021-09-16

Tillägnat Lab2 idag.

Figur: olika färger och punkter för de olika data, plus gärna en titel och legend.

# 2021-09-20 : Objektorienterad programmering OOP

Objektorienterad programmering i Python. Liknande men ändå annorlunda än i andra programmeringsspråk.

Exempel, frågeformulär i klassen: I kursen tycker jag att

- Intressant: Det mer pythoneska sättet att koda på, t.ex.

- Svårt: att komma ihåg alla möjliga inbyggda kommandon och inte uppfinna hjulet på nytt!!

Frågeformuläret i sig är ett "class", eller en "Blueprint". När den är ifylld, dvs instantierad av studenterna så är det ett objekt. Då blir det ett objekt per student. Ett "object" är ett "instances of a class".

Skillnad mot t.ex. listor och dictionary är att en class är mer versatil. En class kan innehålla metoder, t.ex. ett antagningsformulär kan innehålla att den automatiskt beräknar dina poäng och förutser om du blir antagen. Man kan säga att listor, dictionary, int, float, string, alla är class'er.

Exempel2: En person kan ha i ett program

```py
obj = employee()
obj.title = "Teacher"
obj.name  = "Kokchun"
```

Men ett annat program

```py
obj = PetOwner()
obj.pets = ["Fish","cat","budgie"]
```

I python funkar det då som exempel antagnignsformulär: Frågorna är: 

- Skola, program, namn, tackat ja?

```py
obj = Antagning("Cool school", "AI", "Göran Bord", False)
```

För staticmethod, se exercise10-1!

Ett

> @staticmethod

används för metoder som inte använder sig av t.ex. self.metod(). Det är sånt som ska vara gemensamt för alla klasser som är kopplade. Felhantering är klokt att ha som staticmethods t.ex.. De har aldrig en self-input, utan bara ett eller flera "value"-inputs.

### Good practice

För functions och classes: Type checking

Skriv ut om det förväntas float/int/str på de olika variablerna till en funktion t.ex.. Och vad som returneras är också bra att jag

```py
def function(var1: float, var2: int, namn: str) -> float/int/str:
    # KOD HÄR
    return blabla
```

Konvention:

Class har stor bokstav i början på första och andra ordet.

Variabler och funktioner har alltid små bokstäver.

# 2021-09-21 : polymorphism och operator overloading

- Igår: OOP: Introducerade class, objects, attributes, properties (getter, setter), @-decorators, @staticmethod (för att ha error-handling o sånt som är gemensam för alla), encapsulation (underscore _ för att visa att data är privata), dunder-repper __repre__ (här lägger man meddelanden till sig själv och andra utvecklare), dunder-dict __dict__ för att komma åt class'ens attribut.

- Igår: också lite good practice. Funktioner har små bokstäver, class'er har stora bokstäver i början av ord etc...

- Polymorphism: "Flera former"

Funktioner och operatorer som går att använda på olika sorters datatyper för olika ändamål, + operatorn kan concatenate strängar och addera siffror, len() funktionen kan mäta längden av strängar och listor. Etc.

- inherit class: en class kan "ärva" attribut och metoder från en annan class.

```py
class FirstClass:
    blabla
    def method():

class AnotherClass(FirstClass):
    etc
    # Does not have method(), but can use method() from FirstClass.
```

- Operator overloading

```py
+,-,/,//,%,*,**,<,<=,> etc
```
Med class kan man temporärt ta över en operator så att man kan använda den på en egenhändigt gjord datatyp som man definierar i sin class.

T.ex. kan man göra en metod i en klass som är

> def __add__(self, other):

Och därefter definiera vad + ska göra med två stycken datatyper från ens class, ena är self och andra är other. T.ex. ungefär.

>> return self.element + other.element

# 2021-09-23 : OOP lite mer overloading och mer inheritance

Apropå kommentarer och "doc-string"

```py
# blablabla
```

är kommentarer som är till för en själv när man skriver koden. Det är förtydliganden.

```py
""" Blablabla """
```

Är dokumentation, sammanfattning för andra utvecklare av vad t.ex. en funktion eller metod gör.

Olika metoder för att overload'a operatorer: __add__, __sub__, __mul__, __div__, __pow__ (**), __eq__ (==) etc, och så kan man ha rmul, rdic etc för att göra dem kommunikativa.

### Flödesscheman odyl

diagrams.net är bra. Det går att koppla till github. Då kan man rita enkla flödesscheman för att ge t.ex. ens chef när man vill visa hur man tänker programmera något, eller hur ens program fungerar. Kallas för UML.

Apropå Parent-classes. Man kan koppla klasser men man ska vara försiktig med hur mycket man gör det. Det kan bli "parent-child-explosion", att man kopplar en lång kedja av klasser. Ändrar man något i en parent ändrar man ju då i samma sak i alla child klasses.

# 2021-09-27 : privata attribut, UML, matplotlib

### Kommentar om "effektiva koder":

- Börja med att skriva enkelt och ineffektivt, lös problemet.
- Skriv om och återanvänd kod med funktioner och klasser.
- Minska ev onödiga forloopar. Kolla över dina variabler, behöver du spara alla, eller alla listor du har etc.
- Använd "time it" för att kolla hur lång tid olika delar tar.

### OOP rep/sammanfattning

Påminn: Ett objekt är en instans av en klass.

- Klass: "person": +namn +ålder, och metoder, hej()
- Objekt: p1,p2,p3: p1 = person("Greta", 21)

När man skapar objektet, personen p1, så körs __init__(self, namn, ålder). Används ofta för att ge ett initialt värde till de olika parametrarna. Därför man skriver self.namn = namn.

När man skriver klassen (och ritar i UMLer) så specar man först klassnamnet, attributen, och sen metoder, samt om de är publika + på UML) eller privata (- i UML).

Med hjälp av properties kommer man åt privata attribut. En property har en getter och en setter. Inne i Getter och/eller setter kan man lägga koder, t.ex. felhantering.

- Inkapsling
- Docstrings & type hinting
- Polymorphism - ad hoc polymorphism eller operator overloading.: Att en operator/funktion jobbar olika beroende på om man använder en vanlig variabel eller ett objekt från vår eget designade klass. Exempel, plus-operatorn jobbar olika beroende på om det är siffror eller strängar.
- Arv och komposition

### Privata attribut

Se 13_privateattributes.ipynb

- name mangling: har man dunder på ens attribut så kör python en name mangling och ändrar namnet på attributet. Detta gör den svårare att råka ändra på attributet felaktigt.

Köra med enkel eller dubbel _? Var konsekvent.

### Plotta med matplotlib

Två stilar

- Matlab-stil
- OOP-approach

Man kan kolla om ens funktioner/klasser är funktion eller klass om man håller inne ctrl och trycker på funktionsnamnet, då öppnar VS källkoden för funktionen. I Matplotlibs fall verkar den innehålla både vanliga funktioner men också klasser (finns i pyplot.py)

OOP-approachen har en del fördelar iom att man inte behöver rada upp så många properties efter varandra, bara lägga alla i objekten för sina plots eller subplots. Men för enkla plots är det bra med matlabstilen. Den kan man använda i början o sen när man renar sina koder lite kan man översätta det till objekt.

### Lab3

Enhetstester, i kontrast mot manuella tester som vi gjort hitills. Två approacher:

- gör inte allt på en gång utan testa under kodandets gång va :)
- sätt upp alla tester först innan man skriver koden. Tanken är att det ska fail'a varenda gång tills koden är klar. Kräver en hel del abstrakt tänkande.

Tillhör iof VG-uppgifterna men det är bra att ha gjort.

# 2021-09-28 : Enhetstestning

Finns flera bibliotek men vi använder standardbiblioteker: "unittest". Finns också "pytest" och andra men de flesta bygger på unittest. 

Se Code-along/14_unitesting/

Testerna där är ganska snälla tester som kollar enkla saker. I vanliga fall vill man köra mer rigorösa tester.

### Test driven development

En iterativ process:

Skapa testerna först, kollar om testerna fallerar, vilket de gör såklart i början för koden är inte skriven än. Så skriver man koden för att se till att testerna, ett efter ett inte ska fallera. På det viset betar man av alla tester man har gjort. Testerna blir som en checklista över vad koden ska klara av, vilket man skriver först.

En annan variant är att man har olika nivåer av tester. Flera teams utvecklar olika delar till samma produkt. Varje team har sin uppsättnings tester. Sen när varje teams koder klarar alla respektive testar kopplar man ihop de olika teamens koder så har man en uppsättning integration tests.

# 2021-09-30 : Moduler

> __name__

blir 

> __main__ 

när den körs i samma script, men om __name__ i en annan py-fil, t.ex. en med funktioner, klasser, eller andra moduler, så blir __name__ o den modulen samma som namnet på modulen (filnamn odyl). Se Code-Along/15_modules. 

När man har flera moduler i paralella kataloger och andra ställen:

```py
from sys import path
path.append('Relative path')
import module_in_relative_path
```

Vad det innebär är ju att "path" är ens arbetskatalog. path.append lägger till en annan katalogs innehåll till arbetskatalogen så att man kan importera vad som finns där.

```py
```


