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
n += 1 : n = n+1
x /= 2 : x = x/2

Skapa flera variabler:
x,y,z = 1,2,3
- x=1, y=2, z=3

While statements, när man inte vet hur många loopar som behövs.

pipenv: en pip-environment
Skapa ett speciellt shell för ett speciellt projekt:
$ pipenv shell
I den katalog där projektet är. Det skapar en pipfile och en pipfile.lock, dessa innehåller info om vad som gäller för detta environment. Vilken pythonversion och vilka paket.