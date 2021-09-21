# Laboration 2, Pikachu or Pichu?
# Identify if sample data belong to Pikachu or Pichu with the help of example data.
#
import matplotlib.pyplot as plt
import random as rnd
import re
import sys
#
# ========= Define functions here ==========
# Computes distance between points and figure
#
def computedistance(data1,data2,testdata):
    # This function computes distance between data1/data2 and testdata.
    # Output are distance1 and distance2.
    #
    # data1 and data2 are 2*Npik long lists.
    # dataX[0] are width-data (floats)
    # dataX[1] are height-data (floats)
    # testdata is a list with 2 floats, [width,height]

    # Compute distances from data1 & data2 (eg Pichu and Pikachu) to testdata
    distance1 = []
    distance2 = []
    for w1,h1,w2,h2 in zip(data1[0],data1[1],data2[0],data2[1]):
        distance1.append(((w1-testdata[0])**2 + (h1-testdata[1])**2)**0.5)
        distance2.append(((w2-testdata[0])**2 + (h2-testdata[1])**2)**0.5)

    # returns two lists with floats, distance between test and data1 and data2.
    return distance1,distance2
#
# ---------- Identifies if testdata belongs to Pichu or Pikachu ----------
# (Yes, this is hardcoded to check for Pikachu or Pichu...)
#
def identifyfigure(pichudistance,pikachudistance):
    # This function checks if testdata belongs to Pichu or Pikachu by using identity
    # of the smallest distance
    #
    # pichudistance and pikachudistance are lists with floats and are the distances
    # between testdata and either figure's points.

    # Identify who it is (which one is nearest) and return the name as a string
    if min(pichudistance) > min(pikachudistance):
        identity = "Pikachu"
    else:
        identity = "Pichu"

    return identity
#
# ---------- Function that uses the 5-nearest-method (problem2) ----------
# (Yes, this is also hardcoded to check for Pikachu or Pichu...)
#
def identifyfivenearest(pichudistance,pikachudistance):
    # Identify if point in testdata belong to Pichu or Pikachu by using
    # majority-identity of 5 nearest point.
    # pichudistance and pikachudistance are lists with floats and are distances
    # between testdata and either figure's points.

    # First we combine all distances and corresponding figure names into one list
    # Then we sort combined list by distance
    figuredistances = []
    for pichudist in pichudistance:
        figuredistances.append(f"{pichudist}:Pichu")
    for pikachudist in pikachudistance:
        figuredistances.append(f"{pikachudist}:Pikachu")
    figuredistances.sort()

    # Check 5 first elements and count number of Pichu and Pikachu
    pichucounter,pikachucounter = 0,0
    for nn in range(5):
        if figuredistances[nn].split(":")[1] == "Pichu":
            pichucounter   += 1
        if figuredistances[nn].split(":")[1] == "Pikachu":
            pikachucounter += 1

    # Identify who it is (who is in majority) and return the name as a string
    if pichucounter > pikachucounter:
        identity = "Pichu"
    else:
        identity = "Pikachu"
    return identity
#
# ---------- Define function that asks for and tests input from the user ----------
#
def askforvalue(defaultwidth,defaultheight):
    # Default values are one float each, changed in the main code

    # Ask for and check width-input.
    masterrormessage = "Your input must be a postitive number with digits (use . (point) for decimals, not , (comma) - and no quotation marks. Please try again: "
    while True:
        width = input(f"Please write a width (with digits and point as decimal point. Default is {defaultwidth}): ") or defaultwidth
        try:
            width = float(width)
            if width < 0:
                raise ValueError(f"width must be larger than 0: not {width}")
            break
        except ValueError as err:
            print(f"\nError; {err}:\n{masterrormessage}")

    # Ask for (and test) height input
    while True:
        height = input(f"Please write a height (with digits and point as decimal point. Default is {defaultheight}): ") or defaultheight
        try:
            height = float(height)
            if height < 0:
                raise ValueError(f"height must be larger than 0: not {height}")
            break
        except ValueError as err:
            print(f"\nError; {err}:\n{masterrormessage}")

    # Return width and height values
    print(f"Your input values (width,height) are ({width},{height})")
    return width,height

#
# ========== Start of program ==========
#

# Load data
with open('pichu.txt'      , 'r') as fpichu,\
     open('pikachu.txt'    , 'r') as fpikachu,\
     open('test_points.txt', 'r') as ftest:
    
    # Extract data and skip the header line.
    pichufile   = fpichu.readlines()[1:]
    pikachufile = fpikachu.readlines()[1:]
    
    # No header line in testfile, extract all the line(s)
    testfile    = ftest.readlines()

# Check number of coordinates. Both figures have the same number of points/coordinates, 50 each.
# Exits the program on errors.
if len(pichufile) != len(pikachufile) or len(pichufile)+len(pikachufile) != 100:
    sys.exit("Error: number of data points of Pichu and/or Pikachu is not 50 each. Stops here. Check your data files: 'pichu.txt' and 'pikachu.txt'.")
Npik = len(pichufile)

# Extract data from strings and remove parentheses
# (perhaps more effective to use forloops instead of listcomprehension, but this works nicely)
# Meaning of indeces:
# pichudata[0] and pikachudata[0] = widths
# pichudata[1] and pikachudata[1] = heights
pichudata = [
    [float(data.split(',')[0][1:  ]) for data in pichufile],
    [float(data.split(',')[1][ :-2]) for data in pichufile]]
pikachudata = [
    [float(data.split(',')[0][1:  ]) for data in pikachufile],
    [float(data.split(',')[1][ :-2]) for data in pikachufile]]

# Testdata is constructed differently:
# I extract every double-digit (testdata contain double-digit integers) and save each height
# and width together in sublists.
# testdata-syntax: [[width,height],[width,height], ... ]
testfile = re.findall(r"\d\d",testfile[0])
testdata = [[int(testfile[n]),int(testfile[n+1])] for n in range(len(testfile)) if n%2==0]
Ntest    = len(testdata) # Number of test-coordinates

#
# ---------- Plot all points ----------
#
# Test data as yellow rings
# Pichu as green x's
# Pikachu as red dots
# User input as blue rings (after userinput-part later)

plt.ion()
plt.title("Pichu and Pikachu's widths and heights")

# Due to my testdata-format I loop to extract the widths and heights.
for ntest in range(Ntest):

    if ntest == 0:
        plt.plot(testdata[ntest][0],testdata[ntest][1],'yo',markerfacecolor='w',label="Testdata")
    else:
        plt.plot(testdata[ntest][0],testdata[ntest][1],'yo',markerfacecolor='w')

plt.plot(pichudata[0]  ,pichudata[1]  ,'gx',label="Pichu")
plt.plot(pikachudata[0],pikachudata[1],'r.',label="Pikachu")

plt.xlabel("Figure width (cm)")
plt.ylabel("Figure height (cm)")
plt.legend()

# Identify testdata:
for testpoint in testdata:
    # Compute distance between test points and all points of pickachu and pichu
    pichudistance,pikachudistance = computedistance(pichudata, pikachudata, testpoint)

    # Check if testpoint is closest to pickachu or pichu
    identity = identifyfigure(pichudistance,pikachudistance)

    print(f"Sample with (width,heigh) = {testpoint} is classified as {identity}")
print("")

#
# ---------- Let the use input a test point. Is this part of Pickachu or Pichu? ----------
# Problem 1
#

# Ask and test input data (default values are modified here)
userwidth,userheight = askforvalue(22,35)

# Compute distance
pichudistance,pikachudistance = computedistance(pichudata,pikachudata,[userwidth,userheight])

# Identify figure, is the user input Pichu or Pikachu?
print("")
identity = identifyfigure(pichudistance,pikachudistance)
print(f"Sample with (width,heigh) = {[userwidth,userheight]} is classified as {identity}")

#
# --------- Change in algorithm ----------
# Problem 2
# Take 5 points that are closest to the test point and the majority of these decide which 
# figure the test point belongs to.

# Check the user input again.
print("\nAgain with Five-nearest-method and your input sample:")
identity = identifyfivenearest(pichudistance,pikachudistance)
print(f"Sample with (width,heigh) = {[userwidth,userheight]} is classified as {identity}!")

# Add user input to figure! (Was not part of Lab but I think this would be neat :) )
plt.plot(userwidth,userheight,'bo',markerfacecolor='w',label="User input")
plt.legend()

#
# Bonus problems -----------------------------------------------------------------------
# Problem 3
input("\nWe now start with the bonus problems. Press Enter to continue...")

# Seperate original data randomly to two sets.
# a) 90 trainingdata, 45 are pikachu, 45 are pichu
# b) 10 are testdata (5 pikachu and 5 are pichu)

# Create 3 lists, 2 with training data and 1 for test data
trainingpichu   = [[],[]]
trainingpikachu = [[],[]]
testdata        = []
Ntests          = 10 # Total number of test data points

# Randomize the original data
rnd.shuffle(pichudata)
rnd.shuffle(pikachudata)

# Extract data, save "correct answer" with testdata (clean them a bit remove perentheses and spaces)
for nn in range(Npik):
    if nn < Ntests*0.5:
        # Half of testdata points are Pichu
        testdata.append(f"{pichudata[0][nn],pichudata[1][nn]}:Pichu".strip("(").replace(")","").replace(" ",""))
    else:
        # Save the rest Pichus in the training data separately
        trainingpichu[0].append(pichudata[0][nn])
        trainingpichu[1].append(pichudata[1][nn])
    
    if nn < Ntests*0.5:
        # Half of testdata points are Pikachu
        testdata.append(f"{pikachudata[0][nn],pikachudata[1][nn]}:Pikachu".strip("(").replace(")","").replace(" ",""))
    else:
        # The rest Pikachus in the training data
        trainingpikachu[0].append(pikachudata[0][nn])
        trainingpikachu[1].append(pikachudata[1][nn])

# Problem 4
# Compute accuracy of both identify-methods: i.e. compute
#
#            nTP + nTN
# accuracy = ---------
#              Total
#
# where nTP = number of correct Pikachu-identifiers
#       nTN = number of correct Pichu-identifiers
#     Total = total number of attempts (i.e. len(testdata))

# Necessary "counter"-variables
nearestcounter  = [0,0] # Counter for nearest-point-algorithm
fivenearcounter = [0,0] # Counter for five-nearest-algorithm

for data in testdata:
    # Extract data from testdata
    testwidth    = float(data.split(":")[0].split(",")[0])
    testheight   = float(data.split(":")[0].split(",")[1])
    testidentity = data.split(":")[1]

    # Compute distance between testdata and training data
    pichudistance,pikachudistance = computedistance(trainingpichu, trainingpikachu, [testwidth,testheight])

    # Check identity and count the number of correct answers (using nearest-point-method)
    estimatedname = identifyfigure(pichudistance, pikachudistance)
    #print(f"(nearest point) Real: {testidentity} Estimated: {estimatedname}") # Troubleshoot-print
    if testidentity == estimatedname and testidentity == "Pichu":
        nearestcounter[0] += 1
    if testidentity == estimatedname and testidentity == "Pikachu":
        nearestcounter[1] += 1

    # Check identity again, but with 5-nearestmethod
    estimatedname = identifyfivenearest(pichudistance, pikachudistance)
    #print(f"(5-near) Real: {testidentity} Estimated: {estimatedname}") # Troubleshoot-print
    if testidentity == estimatedname and testidentity == "Pichu":
        fivenearcounter[0] += 1
    if testidentity == estimatedname and testidentity == "Pikachu":
        fivenearcounter[1] += 1

# Compute and return accuracies according to equation in comments above.
accuracynearest  = sum(nearestcounter )/Ntests
accuracyfivenear = sum(fivenearcounter)/Ntests
print(f"\nAccuracy when using nearest-point-method: {accuracynearest}")
print(f"Accuracy when using five-nearest-point-method: {accuracyfivenear}")
print("\nEnd of program")
