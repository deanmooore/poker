# this file takes a ReportExport from poker tracker and checks results vs. an optimal strategy
# outputs: .csv file with each street (F,T,R) opportunity and checks the results against PIO solver (takes much longer), eventually own model
# import as pack into piosolver, check actions; OR just check output manually

from PokerMath import *

def main():
    reportlocation = r'C:\Users\Dean\Documents\Poker\PokerMath\ReportExport_hands.csv'    #export file of hand history
    report = TreeInputs.loadhandhistory(reportlocation)
    results = []    #stores results in array with labels accompanying
    for x in [1]:     #loop over each hand
        TreeOutputs.tellPIO(1,2,3,4)
        results = []    #update results at each output
main()