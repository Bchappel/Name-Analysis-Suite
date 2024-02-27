#!/usr/bin/env python3
# Libraries
import os
import sys
import getopt
import csv
import pandas as pd
 
def main ( argv ):

    if len(argv) < 4:
        print ( "Usage: ./analysisNames.py -i <input file name> -n <first name>" )
        sys.exit(2)
    try:
        (opts, args) = getopt.getopt ( argv,"i:n:",["input="] )
    except getopt.GetoptError:
        print ( "Usage: ./analysisNames.py -i <input file name> -n <first name>" )
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ( "Usage: ./analysisNames.py -i <input file name> -n <first name>" )
            sys.exit()
        elif opt in ( "-i", "--input"):
            inputFileName = arg
        elif opt in ( "-n", "--name"):
            names1 = (arg)

    years    = []
    names    = []
    numbers  = []
    ranks    = []
    total    = 0

    with open ( inputFileName ) as csvDataFile:
        csvReader = csv.reader(csvDataFile, delimiter=',')
        for row in csvReader:
            if (row[1]) == names1:
                years.append(int(row[0]))
                names.append(row[1])
                numbers.append(int(row[2]))
                ranks.append(row[3])
                total = total + 1
    
        if total > 0 :
            people = {'Year':years, 'Name':names,'Number':numbers,'Rank':ranks}
            people_df = pd.DataFrame(people)
         
            ind = 0
            while ind < total:
                if len(people_df.loc[ind,'Name']) < 8 :
                    print ( str(people_df.loc[ind,'Year'])+""+','+""+str(people_df.loc[ind,'Rank']) )
                else :
                    print ( str(people_df.loc[ind,'Year'])+""+','+""+str(people_df.loc[ind,'Rank']) )
                ind = ind + 1

if __name__ == "__main__":
    main ( sys.argv[1:] )
