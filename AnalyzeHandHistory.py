# this file takes a ReportExport from poker tracker and checks results vs. an optimal strategy
# outputs: .csv file with each street (F,T,R) opportunity and checks the results against PIO solver (takes much longer), eventually own model
# import as pack into piosolver, check actions; OR just check output manually

from StartingRangesandConstants import *
import numpy as np
import csv 
import pandas.io
import wexpect
import os

def main():
    reportlocation = r'C:\Users\Dean\Documents\Poker\PokerMath\ReportExport_hands.csv'    #export file of hand history
    report = LoadHands(reportlocation)
    results = []    #stores results in array with labels accompanying
    for x in [1]:     #loop over each hand
        tellPIO(1,2,3,4)
        results = []    #update results at eeach output

def LoadHands(loc): #loads csv file of hands through panda #maybe make "report" object?
    history = pandas.io.parsers.read_csv(loc)
    holecard1_column = 2    #need to do automatically ie search later on
    holecard2_column = 3    #need to do automatically ie search later on
    flop1_column = 4        #need to do automatically ie search later on
    flop2_column = 5        #need to do automatically ie search later on
    flop3_column = 6        #need to do automatically ie search later on
    turncard_column = 7     #need to do automatically ie search later on
    rivercard_column = 8    #need to do automatically ie search later on

    flopcards1 = history.iloc[:,flop1_column]
    flopcards2 = history.iloc[:,flop2_column]
    flopcards3 = history.iloc[:,flop3_column]
    holecards1 = history.iloc[:,holecard1_column]
    holecards1 = history.iloc[:,holecard2_column]
    turncards = history.iloc[:,turncard_column]
    rivercards = history.iloc[:,rivercard_column]

    hands = history.iloc[:,7]
    return history

def tellPIO(r1,r2,p1,p2):   #r1: range 1, r2: range 2, p1: 
    
    os.chdir("C:\\PioSOLVER\\")   #change to PIO directory  
    inputs = TreeInputs.result(1,2)
    solver = wexpect.spawn('PioSOLVER2-pro.exe',timeout=1000)    #run PIO solver
    
    #test it works
    solver.sendline('echo dean') #sends code to scan for later
    solver.sendline('is_ready')
    solver.expect('is_ready ok!')

    #send default/basic range as starting point
    solver.sendline('load_script_silent C:\\Users\\Dean\\Documents\\Poker\\PokerMath\\SampleScript.txt')    #script to load ranges they give
                    #^edit so I use the TreeInputs.results and the default is the above
    solver.expect('load_script_silent ok!')
    output = solver.before  #capture output to be converted into data

    #put in custom ranges
    #put in custom bet options
    #put in custom sizes

    results = TreeOutputs.result(output)#fit the things above to this object
    print(results.EV_OOP)   #test output
    print(output)           #test output
    solver.sendline('exit') #exit program
    return results

main()