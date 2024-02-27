#!/usr/bin/env python3

# Libraries
import os
import sys
import getopt
import csv
import pandas as pd
 
def main ( argv ):

    if len(argv) < 6:
        print ( "Usage: ./names.py -i <input file name> -y <year> -o <output file name base>" )
        sys.exit(2)
    try:
        (opts, args) = getopt.getopt ( argv,"i:y:o:t:",["input=","year=","output="] )
    except getopt.GetoptError:
        print ( "Usage: ./names.py -i <input file name> -y <year> -o <output file name base>" )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ( "Usage: ./names.py -i <input file name> -y <year> -o <output file name base>" )
            sys.exit()
        elif opt in ( "-i", "--input"):
            inputFileName = arg
        elif opt in ("-y", "--year"):
            year = int(arg)
        elif opt in ("-o", "--output"):
            outputFileNameBase = arg
        elif opt in ("-t", "--IndexOfTop"):
            topNum = arg
            print(topNum)
            
    outputFileName = outputFileNameBase+str(year)+".csv"
    
    names    = []
    numbers  = []
    ranks    = []
    total    = 0

    with open ( inputFileName ) as csvDataFile:

        next ( csvDataFile ) 
        csvReader = csv.reader(csvDataFile, delimiter = ',')
        for row in csvReader:
            if int(row[0]) == year :
                tempName = row[1].strip()
                names.append(tempName)
                numbers.append(int(row[2]))
                total = total + 1
                ranks.append(total)

        print ( "There are ",total," names in ",year )
        
        if total > 0 :
            people = {'':names,' ':numbers}            
            people_df = pd.DataFrame(people)
    
            people_df.sort_values([" ",""], axis = 0, ascending=[False,False], inplace=True)

            rankedPeople_df = people_df
            rankedPeople_df.reset_index(drop=True, inplace=True)
            rankedPeople_df.index +=1
        
            print ('',rankedPeople_df [0:50])

            rankedPeople_df.to_csv(outputFileName, sep = ',', index=False, encoding = 'utf-8') #to csv

if __name__ == "__main__":
    main ( sys.argv[1:] )

