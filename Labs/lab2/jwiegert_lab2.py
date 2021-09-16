# Laboration 2, Pikachu or Pichu?
# Identify if sample data belong to Pikachu or Pichu with the help of example data.
#
# Import packages
#
import matplotlib.pyplot as plt
import random as rnd
import re
import sys
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
    # dataX[0] are width-data (floats)
    # dataX[1] are height-data (floats)
    # testdata is a list with 2 floats, [width,height]
    #
    distance1 = []
    distance2 = []
    for w1,h1,w2,h2 in zip(data1[0],data1[1],data2[0],data2[1]):
        #
        # Compute distances between Pichu and testdata
        #
        distance1.append(((w1-testdata[0])**2 + (h1-testdata[1])**2)**0.5)
        distance2.append(((w2-testdata[0])**2 + (h2-testdata[1])**2)**0.5)
    # returns two lists with floats, distance between test and data1 and data2.
    return distance1,distance2
#
# Identifies if testdata belongs to Pichu or Pikachu ------------------------------
# (Yes, this is hardcoded to check for Pikachu or Pichu...)
#
def identifyfigure(pichudistance,pikachudistance,testdata):
    #
    # This function checks if testdata belongs to Pichu or Pikachu by using identity
    # of the nearest point to the testdata.
    #
    # pichudistance and pikachudistance are lists with floats, distance between
    # testdata and either figure's all points.
    # testdata is a list with 2 floats, [width,height]
    #
    # Identify who it is and return the name as a string
    if min(pichudistance) > min(pikachudistance):
        identity = "Pikachu"
    else:
        identity = "Pichu"
    return identity
#
# Function that uses the 5-nearest-method (problem2) ------------------------
# (Yes, this is also hardcoded to check for Pikachu or Pichu...)
#
def identifyfivenearest(pichudistance,pikachudistance,testdata):
    #
    # Identify if point in testdata belong to Pichu or Pikachu by using
    # majority-identity of 5 nearest point.
    # pichudistance and pikachudistance are lists with floats, distance between
    # testdata and either figure's all points.
    # testdata is a list with 2 floats, [width,height]
    #
    # First we list all distances and corresponding figure names into one list
    figuredistances = []
    for pichudist in pichudistance:
        figuredistances.append(f"{pichudist}:pichu")
    for pikachudist in pikachudistance:
        figuredistances.append(f"{pikachudist}:pikachu")
    # Sort list by distance
    figuredistances.sort()
    # Check 5 first elements and count number of Pichu/Pikachu
    pichucounter,pikachucounter = 0,0
    for nn in range(5):
        if figuredistances[nn].split(":")[1] == 'pichu':
            pichucounter   += 1
        if figuredistances[nn].split(":")[1] == 'pikachu':
            pikachucounter += 1
    # Identify who is who and return the name as a string
    if pichucounter > pikachucounter:
        identity = "Pichu"
    else:
        identity = "Pikachu"
    return identity
#
# Define function that asks for and tests input from the user ---------------------------
#
def askforvalue(defaultwidth,defaultheight):
    #
    # Default values are one float each
    #
    # Ask for and check width-input.
    masterrormessage = "Your input must be a postitive number with digits (use . (point) for decimals, not , (comma) - and no quotation marks. Please try again: "
    while True:
        width = input("Please write a width (with digits and point as decimal point): ") or defaultwidth
        try:
            width = float(width)
            if width < 0:
                raise ValueError(f"width must be larger than 0: not {width}")
            break
        except ValueError as err:
            print(f"Error; {err}:\n{masterrormessage}")
    # Ask for (and test) height input
    while True:
        height = input("Please write a height (with digits and point as decimal point): ") or defaultheight
        try:
            height = float(height)
            if height < 0:
                raise ValueError(f"height must be larger than 0: not {height}")
            break
        except ValueError as err:
            print(f"Error; {err}:\n{masterrormessage}")
    # Return width and height values
    print(f"Your input values (width,height) are ({width},{height})")
    return width,height

# Final accuracy function here.

#
# Start of program ----------------------------------------------------------
#
# 1. Load data
#
with open('pichu.txt'      , 'r') as fpichu,\
     open('pikachu.txt'    , 'r') as fpikachu,\
     open('test_points.txt', 'r') as ftest:
    # Extract data and skip the header line.
    pichufile   = fpichu.readlines()[1:]
    pikachufile = fpikachu.readlines()[1:]
    # No header line in testfile, extract all the line(s)
    testfile    = ftest.readlines()
# Extract data from strings and remove parentheses
# (perhaps more effective as forloops instead of listcomprehension)
pichuwidth    = [float(data.split(',')[0][1:  ]) for data in pichufile]
pichuheight   = [float(data.split(',')[1][ :-2]) for data in pichufile]
pikachuwidth  = [float(data.split(',')[0][1:  ]) for data in pikachufile]
pikachuheight = [float(data.split(',')[1][ :-2]) for data in pikachufile]
# Check number of coordinates. Both figures have the same number of points/coordinates, 50 each.
if len(pichuwidth) != len(pikachuwidth) or len(pichuwidth)+len(pikachuwidth) != 100:
    sys.exit("Error: number of data points of Pichu and Pikachu is not 50 each. Stops here. Check your data files: 'pichu.txt' and 'pikachu.txt'.")
Npik = len(pichuwidth)
#
# Testdata is constructed differently.
# Separate it into singular numbers and then add together every second number
# into the correct number and save each height and width together in sublists.
# testdata-syntax: [[width,height],[width,height], ... ]
#
testfile = re.findall(r"\d\d",testfile[0])
testdata = [[int(testfile[n]),int(testfile[n+1])] for n in range(len(testfile)) if n%2==0]
# Number of test coordinates
Ntest    = len(testdata)
#
# 2. plot all points -------------------------------------------------------------
# Test data as yellow rings
# Pichu as green x's
# Pikachu as red dots
# User input as blue rings (see later)
#
plt.ion()
plt.title("Pichu and Pikachu's widths and heights")
for ntest in range(Ntest):
    if ntest == 0:
        plt.plot(testdata[ntest][0],testdata[ntest][1],'yo',markerfacecolor='w',label="Testdata")
    else:
        plt.plot(testdata[ntest][0],testdata[ntest][1],'yo',markerfacecolor='w')
plt.plot(pichuwidth,pichuheight,'gx',label="Pichu")
plt.plot(pikachuwidth,pikachuheight,'r.',label="Pikachu")
plt.xlabel("Figure width (cm)")
plt.ylabel("Figure height (cm)")
plt.legend()
#
# 3. compute distance between test points and all points of pickachu and pichu
#    check if testpoint is closest to pickachu or pichu
#
for testpoint in testdata:
    pichudistance,pikachudistance = \
        computedistance([pichuwidth,pichuheight],[pikachuwidth,pikachuheight],testpoint)
    # 4. Print out which points are which.
    identity = identifyfigure(pichudistance,pikachudistance,testpoint)
    print(f"Sample with (width,heigh) = {testpoint} is classified as {identity}")
print("")
#
# 6. Let the use input a test point. Is this part of Pickachu or Pichu? ------------
# Ask and test input data (default values are modified here)
#
userwidth,userheight = askforvalue(22,35)
# Compute distance
pichudistance,pikachudistance = \
        computedistance([pichuwidth,pichuheight],[pikachuwidth,pikachuheight],[userwidth,userheight])
# Identify figure, is the user input Pichu or Pikachu?
print("")
identity = identifyfigure(pichudistance,pikachudistance,[userwidth,userheight])
print(f"Sample with (width,heigh) = {[userwidth,userheight]} is classified as {identity}")
#
# 7. Change in algorithm --------------------------------------------------------------
#    Take 5 points that are closest to the test point and the class the majority of these belong to
#    decide which figure the test point belongs to.
# Check the user input again.
#
print("\nAgain with Five-nearest-method and your input sample:")
identity = identifyfivenearest(pichudistance,pikachudistance,[userwidth,userheight])
print(f"Sample with (width,heigh) = {[userwidth,userheight]} is classified as {identity}!")
#
# Add user input to figure! (Was not part of Lab but I think this would be neat :) )
#
plt.plot(userwidth,userheight,'bo',markerfacecolor='w',label="User input")
plt.legend()
#
# Bonus problems --------------------------------------------------------------------
#
input("\nWe now start with the bonus problems. Press Enter to continue...")
#
# 1. seperate original data randomly to two sets.
#    a) 90 trainingdata, 45 are pikachu, 45 are pichu
#    b) 10 are testdata (5 pikachu and 5 are pichu)
#
# Create five lists, two with training data for each figure and one for test data
trainingpichuwidth,trainingpichuheight     = [],[]
trainingpikachuwidth,trainingpikachuheight = [],[]
testdata                                   = []
Ntests                                     = 10 # Total number of test data points
# Randomize the original data
rnd.shuffle(pichuwidth)  ,rnd.shuffle(pichuheight)
rnd.shuffle(pikachuwidth),rnd.shuffle(pikachuheight)
# Extract data (and clean them a bit remove perentheses and spaces)
for nn in range(Npik-int(Ntests*0.5)):
    # Half of testdata points are Pichu
    if nn < Ntests*0.5:
        testdata.append(f"{pichuwidth[nn],pichuheight[nn]}:Pichu".strip("(").replace(")","").replace(" ",""))
    # Save the rest in the training data separately
    else:
        trainingpichuwidth.append(pichuwidth[nn])
        trainingpichuheight.append(pichuheight[nn])
    # Pick five of Pikachu for testdata
    if nn < Ntests*0.5:
        testdata.append(f"{pikachuwidth[nn],pikachuheight[nn]}:Pikachu".strip("(").replace(")","").replace(" ",""))
    # The rest in the training data
    else:
        trainingpikachuwidth.append(pikachuwidth[nn])
        trainingpikachuheight.append(pikachuheight[nn])
# Randomize the test data (not really necessary here)
rnd.shuffle(testdata)
#
# Compute accuracy of both identify-methods: i.e. compute
#
#            nTP + nTN
# accuracy = ---------
#              Total
#
# where nTP = number of correct Pikachu-identifiers
#       nTN = number of correct Pichu-identifies
#     Total = total number of attempts.
#
nearestcounter  = [0,0] # Counter for nearest-point-algorithm
fivenearcounter = [0,0] # Counter for five-nearest-algorithm
for data in testdata:
    # 0. Extract data from testdata/trainingdata
    testwidth    = float(data.split(":")[0].split(",")[0])
    testheight   = float(data.split(":")[0].split(",")[1])
    testidentity = data.split(":")[1]
    # 1. Compute distance between testdata and original data
    pichudistance,pikachudistance = computedistance([trainingpichuwidth,trainingpichuheight], [trainingpikachuwidth,trainingpikachuheight], [testwidth,testheight])
    # 2. Check identity and count the number of correct answers (using nearest-point-method)
    estimatedname = identifyfigure(pichudistance, pikachudistance, [testwidth,testheight])
    if testidentity == estimatedname and testidentity == "Pichu":
        nearestcounter[0] += 1
    if testidentity == estimatedname and testidentity == "Pikachu":
        nearestcounter[1] += 1
    # 3. Check identity again, but with 5-nearestmethod
    estimatedname = identifyfivenearest(pichudistance,pikachudistance, [testwidth,testheight])
    if testidentity == estimatedname and testidentity == "Pichu":
        fivenearcounter[0] += 1
    if testidentity == estimatedname and testidentity == "Pikachu":
        fivenearcounter[1] += 1
# 4. Compute and return accuracies
accuracynearest  = sum(nearestcounter )/Ntests
accuracyfivenear = sum(fivenearcounter)/Ntests
print(f"\nTest data: Accuracy when using nearest-point-method: {accuracynearest}")
print(f"Test data: Accuracy when using five-nearest-point-method: {accuracyfivenear}")
print("\nEnd of program?")
