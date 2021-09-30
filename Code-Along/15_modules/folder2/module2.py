# we want to import say_hello1
# which means we want to go up from folder2 and into folder1...
from sys import path
path.append("folder1")
#from folder1.module1 import say_hello1
import module1
# Because our working directory for these py files are ../15_modules/ it's enough
# to append folder1 like this.


def say_hello2():
    print(f"{__name__} says hello...")

# because of path.append above we can now use module1

module1.say_hello1()
