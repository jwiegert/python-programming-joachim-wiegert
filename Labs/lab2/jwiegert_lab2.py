# Laboration 2, Pikachu or Pichu?
#
# Import packages
#
import matplotlib.pyplot as plt
import re
#
# Define functions here ------------------------------------------------------------
#
# Computes distance between points and eight figure.
#

# det computedistance(data1,data2,testdata):
def computedistance(widthdata,heightdata,testdata):
    #
    # widthdata and heightdata are Npik long lists.
    # testdata contains 2 elements.
    #
    distance = []
#    distance1 = []
#    distance2 = []
#    for w1,h1,w2,h2 in zip(data1[0],data1[1],data2[0],data2[1]):
    for width,height in zip(widthdata,heightdata):
        #
        # Compute distances between Pichu and testdata
        #
        #distance1.append(((w1-testdata[0])**2 + (h1-testdata[1])**2)**0.5)
        #distance2.append(((w2-testdata[0])**2 + (h2-testdata[1])**2)**0.5)
        distance.append((\
            (width-testdata[0])**2 + (height-testdata[1])**2)**0.5)
    return distance1,distance2
#
# Identifies if testdata belongs to Pichu or Pikachu
#
def identifyfigure(pichudistance,pikachudistance,testdata):
    if min(pichudistance) > min(pikachudistance):
        # Pikachu!!
        print(f"Sample with (width,heigh) = {testdata} is classified as Pikachu")
    else:
        # Pichu!!
        print(f"Sample with (width,heigh) = {testdata} is classified as Pichu")
#
# Start of program ----------------------------------------------------------
#
# 1. Load data
#
pichufile   = open('pichu.txt'      , 'r').readlines()[1:]
pikachufile = open('pikachu.txt'    , 'r').readlines()[1:]
testfile    = open('test_points.txt', 'r').readlines()

# You forgot to close the files!!

#
# Extract data from strings (and remove parentheses)
#
pichuwidth    = [float(data.split(',')[0][1:  ]) for data in pichufile]
pichuheight   = [float(data.split(',')[1][ :-2]) for data in pichufile]
#
pikachuwidth  = [float(data.split(',')[0][1:  ]) for data in pikachufile]
pikachuheight = [float(data.split(',')[1][ :-2]) for data in pikachufile]
#
Npik          = len(pichuwidth) # Both have the same number of points...
#
# Testdata was constructed differently. This separates it into singular numbers
# and then adds together every second number into the correct number and saves
# each height and width together in sub lists.
#
# testdata-syntax: [[width,height],[width,height], ...
#
testfile = re.findall(r"\d\d",testfile[0])
testdata = [[int(testfile[n]),int(testfile[n+1])] for n in range(len(testfile)) if n%2==0]
Ntest    = len(testdata)
#
# 2. plot all points
#
plt.ion()
for ntest in range(Ntest):
    plt.plot(testdata[ntest][0],testdata[ntest][1],'yo',markerfacecolor='w',label="Testdata")
plt.plot(pichuwidth,pichuheight,'g.',label="Pichu")
plt.plot(pikachuwidth,pikachuheight,'r.',label="Pikachu")
plt.xlabel('Figure width')
plt.ylabel('Figure height')
plt.legend()
#
# 4. compute distance between test points and all points of pickachu and pichu
#    check if testpoint is closest to pickachu or pichu
#
for testpoint in testdata:
    pichudistance,pikachudistance = computedistance([pichuwidth,pichuheight],[pikachuewidth,pikachuheight],testpoint)
#    pikachudistance = computedistance(pikachuwidth,pikachuheight,testpoint)
    #
    # 5. Print out which points are which.
    #
    identifyfigure(pichudistance,pikachudistance,testpoint)
#
# 6. Let the use input a test point. Is this part of Pickachu or Pichu?
#


# I can use my function from the exercises, it needs to be modded to accept x and y-values

#
# Define function that tests the input from the user.
#
"""
def askforvalue(default):
    while True:
        inputdata = input("") or default
        try:
            inputdata = float(inputdata)
            if inputdata < 0:
                raise ValueError(f"number must be larger than 0: not {inputdata}")
            break
        except ValueError as err:
            print(f"Error; {err}:\nYour input must be a postitive number with digits (use . (point) for decimals, not , (comma)). Please try again: ")
    return inputdata
"""



# 7. ... extra problems...
