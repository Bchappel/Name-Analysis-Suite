#!/usr/bin/env python3

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd
 
def main ( argv ):

    if len(argv) < 4:
        print ( "Usage: ./analysisClass.py -f <input file name> -m <input file name> -c <input file name> -y <year>" )
        sys.exit(2)
    try:
        (opts, args) = getopt.getopt ( argv,"f:m:y:c:",["input="] )
    except getopt.GetoptError:
        print ( "Usage: ./analysisClass.py -f <input file name> -m <input file name> -c <input file name> -y <year>" )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ( "Usage: ./analysisClass.py -f <input file name> -m <input file name> -c <input file name> -y <year>" )
            sys.exit()
        elif opt in ( "-f", "--input"):
            inputFileName = arg
        elif opt in ( "-m", "--input2"):
            inputFileName2 = arg
        elif opt in ( "-c", "--input3"):
            inputFileName3 = arg
        elif opt in ( "-y", "--year"):
            years = int(arg)

    names  = {'a'}
    names1 = {'b'}
    classNames = {'c'}

    with open ( inputFileName) as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            if int(row[0]) == years:
                names.add(row[1])
                
    with open ( inputFileName2) as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            if int(row[0]) == years:
                names1.add(row[1])
                
    with open ( inputFileName3) as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            classNames.add(row[0])
                       
                    
    intersectionClass = names.intersection(classNames)
    intersectionClass2 = names1.intersection(classNames)
    finalset = intersectionClass.union(intersectionClass2)
    finalset2 = (sorted(finalset))
    
    for i in range (len(finalset2)):
        print(list(finalset2)[i])
    
    
if __name__ == "__main__":
    main (sys.argv[1:])