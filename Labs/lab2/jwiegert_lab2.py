# Laboration 2, Pikachu or Pichu?
# Identify if sample data belong to Pikachu or Pichu with the help of example data.
#
# Import packages
#
import matplotlib.pyplot as plt
import random as rnd
import re
import os
#
# Define functions here ------------------------------------------------------------
# Computes distance between points and figure --------------------------------------
#
def computedistance(data1,data2,testdata):
    #
    # This function computes distance between data1/data2 and testdata.
    # Output are distance1 and distance2.
    #
    # data1 and data2 are 2*Npik long lists.
    # dataX[0] are width-data
    # dataX[1] are height-data
    # testdata contains 2 elements, [width,height]
    #
    distance1 = []
    distance2 = []
    for w1,h1,w2,h2 in zip(data1[0],data1[1],data2[0],data2[1]):
        #
        # Compute distances between Pichu and testdata
        #
        distance1.append(((w1-testdata[0])**2 + (h1-testdata[1])**2)**0.5)
        distance2.append(((w2-testdata[0])**2 + (h2-testdata[1])**2)**0.5)
    return distance1,distance2
#
# Identifies if testdata belongs to Pichu or Pikachu ------------------------------
# (Yes, this is hardcoded to check for Pikachu or Pichu...)
#
def identifyfigure(pichudistance,pikachudistance,testdata):
    #
    # This function checks if testdata belongs to Pichu or Pikachu
    #
    if min(pichudistance) > min(pikachudistance):
        # Pikachu!!
        print(f"Sample with (width,heigh) = {testdata} is classified as Pikachu")
    else:
        # Pichu!!
        print(f"Sample with (width,heigh) = {testdata} is classified as Pichu")
#
# Function that uses the 5-nearest-method (problem2) ------------------------
# (Yes, this is also hardcoded to check for Pikachu or Pichu...)
#
def identifyfivenearest(pichudistance,pikachudistance):
    # First we list all distances and corresponding figure names
    # (Could only get this to work with forloops, not with listcomprehension)
    figuredistances = []
    for pichudist in pichudistance:
        figuredistances.append(f"{pichudist}:pichu")
    for pikachudist in pikachudistance:
        figuredistances.append(f"{pikachudist}:pikachu")
    # Sort list (by distance)
    figuredistances.sort()
    # Check 5 first elements and count number of Pichu/Pikachu
    pichucounter = 0
    pikachucounter = 0
    for nn in range(5):
        if figuredistances[nn].split(":")[1] == 'pichu':
            pichucounter += 1
        if figuredistances[nn].split(":")[1] == 'pikachu':
            pikachucounter += 1
    # Identify who is who!
    if pichucounter > pikachucounter:
        print("It's Pichu! (Using five nearest-method)")
    else:
        print("It's Pikachu! (Using five nearest-method)")
#
# Define function that tests the input from the user -------------------------------
#
def askforvalue(defwidth,defheight):
    #
    # Ask for (and test) width input
    #
    while True:
        width = input("\nPlease write a width (with digits and point as decimal point): ") or defwidth
        try:
            width = float(width)
            if width < 0:
                raise ValueError(f"width must be larger than 0: not {width}")
            break
        except ValueError as err:
            print(f"Error; {err}:\nYour input must be a postitive number with digits (use . (point) for decimals, not , (comma)). Please try again: ")
    #
    # Ask for (and test) height input
    #
    while True:
        height = input("\nPlease write a height (with digits and point as decimal point): ") or defheight
        try:
            height = float(height)
            if height < 0:
                raise ValueError(f"height must be larger than 0: not {height}")
            break
        except ValueError as err:
            print(f"Error; {err}:\nYour input must be a postitive number with digits (use . (point) for decimals, not , (comma)). Please try again: ")
    #
    # Return width and height values.
    #
    return width,height

#
# Start of program ----------------------------------------------------------
#
# 1. Load data
#
with open('pichu.txt'      , 'r') as fpichu,\
     open('pikachu.txt'    , 'r') as fpikachu,\
     open('test_points.txt', 'r') as ftest:
    #
    # Extract data and skip the header line.
    #
    pichufile   = fpichu.readlines()[1:]
    pikachufile = fpikachu.readlines()[1:]
    testfile    = ftest.readlines()
#
# Extract data from strings and remove parentheses
#
pichuwidth    = [float(data.split(',')[0][1:  ]) for data in pichufile]
pichuheight   = [float(data.split(',')[1][ :-2]) for data in pichufile]
#
pikachuwidth  = [float(data.split(',')[0][1:  ]) for data in pikachufile]
pikachuheight = [float(data.split(',')[1][ :-2]) for data in pikachufile]
#
# Number of coordinates
Npik          = len(pichuwidth) # Both have the same number of points
#
# Testdata is constructed differently.
# This separates it into singular numbers and then adds together every second
# number into the correct number and saves each height and width together in sublists.
#
# testdata-syntax: [[width,height],[width,height], ...
#
testfile = re.findall(r"\d\d",testfile[0])
testdata = [[int(testfile[n]),int(testfile[n+1])] for n in range(len(testfile)) if n%2==0]
# Number of test coordinates
Ntest    = len(testdata)
#
# 2. plot all points
#
plt.ion()
for ntest in range(Ntest):
    if ntest == 0:
        plt.plot(testdata[ntest][0],testdata[ntest][1],'yo',markerfacecolor='w',label="Testdata")
    else:
        plt.plot(testdata[ntest][0],testdata[ntest][1],'yo',markerfacecolor='w')
plt.plot(pichuwidth,pichuheight,'g.',label="Pichu")
plt.plot(pikachuwidth,pikachuheight,'r.',label="Pikachu")
plt.xlabel('Figure width')
plt.ylabel('Figure height')
plt.legend()
#
# 3. compute distance between test points and all points of pickachu and pichu
#    check if testpoint is closest to pickachu or pichu
#
for testpoint in testdata:
    pichudistance,pikachudistance = \
        computedistance([pichuwidth,pichuheight],[pikachuwidth,pikachuheight],testpoint)
    #
    # 5. Print out which points are which.
    #
    identifyfigure(pichudistance,pikachudistance,testpoint)
#
# 6. Let the use input a test point. Is this part of Pickachu or Pichu?
#
# Ask and test input data (default values are 1.0 and 1.0 here)
userwidth,userheight = askforvalue(22,35)
# Compute distance
pichudistance,pikachudistance = \
        computedistance([pichuwidth,pichuheight],[pikachuwidth,pikachuheight],[userwidth,userheight])
# Identify figure
print("")
identifyfigure(pichudistance,pikachudistance,[userwidth,userheight])
#
# Add user input to figure! (Was not part of Lab but I think this would be neat)
#
plt.plot(userwidth,userheight,'bo',markerfacecolor='w',label="User input")
plt.legend()
#
# 7. Change in algorithm
#    Take 5 points that are closest to the test point and the class the majority of these belong to
#    decide which figure the test point belongs to.
#
# Check the previous user input again.
#
print("\nAgain with Five-nearest-method and your input sample:")
identifyfivenearest(pichudistance,pikachudistance)
#
# Bonus problems -----------------------------------------------------------------
#
input("\nWe now start with the bonus problems. Press Enter to continue...")

#
# 1. seperate original data randomly to two sets.
#    a) 90 trainingdata, 45 are pikachu, 45 are pichu
#    b) 10 are testdata (5 pikachu and 5 are pichu)
#

# I should combine and randomize these 4 lists.
# I could use strings or a dict, so that each line in the list says
# 'width,height:name'
#pichuwidth
#pichuheight
#
#pikachuwidth
#pikachuheight





# Separate into two lists
trainingdata,testdata       = [],[]
pichucounter,pikachucounter = 0,0

for data in figuredistances:
    



