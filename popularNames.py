#!/usr/bin/env python3
#takes time to run, just wait!
# Libraries
import os
import sys
import getopt
import csv
import pandas as pd
 
def main ( argv ):

    if len(argv) < 4:
        print ( "Usage: ./popularNames.py -i <input file name> -n <second input file name>" )
        sys.exit(2)
    try:
        (opts, args) = getopt.getopt ( argv,"i:n:",["input="] )
    except getopt.GetoptError:
        print ( "Usage: ./popularNames.py -i <input file name> -n <second input file name>" )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ( "Usage: ./popularNames.py -i <input file name> -n <second input file name>" )
            sys.exit()
        elif opt in ( "-i", "--input"):
            inputFileName = arg
        elif opt in ( "-n", "--input2"):
            inputFileName2 = arg
              
    years    = []
    names    = []
    names2   = []
    numbers  = []
    ranks    = {}
    newlist = []
    
    ranked = 0

    with open ( inputFileName ) as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
                names.append(row[1])
            
    with open ( inputFileName2 ) as csvDataFile:
        csvReader2 = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader2:
                names2.append(row[0])
                ranks[row[0]] = 0
        
    for name in names2:
        if names.count(name) == 103:
            newlist.append(name)
            
    with open ( inputFileName ) as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            ranks[row[1]] = ranks[row[1]]+ int(row[3])
            
    for name in newlist:
        print(name+','+str(ranks[name]//103))


if __name__ == "__main__":
    main ( sys.argv[1:] )
