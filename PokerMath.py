
import numpy as np
import csv 
import pandas.io
import wexpect
import os

class Board:    #this stores object of board with constants for deck, possible flop cards based on hand, etc.
    def __init__(self):
        #card ranks 1-13, suits 1-4 (52x1 matrix), maybe leave only in ranges
        self.deck = ['Ah', 'Kh', 'Qh', 'Jh', 'Th', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h'
        'Ac', 'Kc', 'Qc', 'Jc', 'Tc', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c'
        'Ad', 'Kd', 'Qd', 'Jd', 'Td', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d'
        'As', 'Ks', 'Qs', 'Js', 'Ts', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s']
        self.betintputEXAMPLE = [] #need list of bet size defaults
        self.rangedefaultEXAMPLE = [] #blank range of size needed for UPI/PIO format
    def trimflopforhand():  #trim deck considering hand cards
        return []
    def removecard():   #pass deck return deck without that card
        return []

class Ranges:   #change this to: always have every card, set values from 0-1.
    def __init__(self):  #initialize everything
        self.deck = ['Ah', 'Kh', 'Qh', 'Jh', 'Th', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h'
        'Ac', 'Kc', 'Qc', 'Jc', 'Tc', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c'
        'Ad', 'Kd', 'Qd', 'Jd', 'Td', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d'
        'As', 'Ks', 'Qs', 'Js', 'Ts', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s']
        self.r1 = []    #range player 1
        self.r2 = []    #range player 2
        self.p1 = []    #positon player 1
        self.p2 = []    #position player 2

    def onecardrange(c1,c2):    #int version, returns range in PIO form with two input cards (x/52)
        range = np.zeros(1326)
        locr = c1*c2
        range[locr] = 1
        return range 

    def onecardrange_s(c1,c2):    #string version, returns range in PIO form with two input cards 
        deckr = Ranges.deck
        range = np.zeros(1326)
        loc1 = deckr.find(c1)   #use if string
        loc2 = deckr.find(c2)   #use if string
        locr = loc1*loc2
        range[locr] = 1
        return range 

    def multicardrange(c,d,e):   #not sure how to fit this in yet
        emptyrange = np.zeros(1326)
        return emptyrange
 
class PreFlopBuild: #contains objects/constants necessary to calculate a preflop range for use elsewhere
    def __init__(self):
        allpositions = []
        r1 = [] #pxpxN matrix where p is player position #s and N is the # of betting (3/4/5/all-in) options available
        r2 = []
        p1 = []
        p2 = []
    def onerange(position1,position2): #creates range of specific combo
        #set all positions to be 1x1
        #define ranges based on these two spots
        return []
    def listofranges(positions1,positions2): #creates ranges from a given list, returns in same order
        #positions set to all permutations of the list given
        #define ranges based on these two spots
        return []
    def allranges(): #creates ranges from all possible positions
        #positions set to all permutations of the list given
        #define ranges based on these two spots
        return []

class TreeInputs:  #contains everything needed for one tree simulation
    def __init__(self):
        ev=[]
    def result(self):
        ev=0
    def result(one,two):
        ev=0
        #this is for if we have custom input
        #we will have ranges elsewhere

    def loadhandhistory(loc): #loads csv file of hands using panda given location
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
        holecards2 = history.iloc[:,holecard2_column]
        turncards = history.iloc[:,turncard_column]
        rivercards = history.iloc[:,rivercard_column]
        return history

    def converthandhistory(his):
        return []

class TreeOutputs:  #everything returned from one simulation
    def __init__(self):  #initialize everything
        self.EV_IP = []
        self.EV_OOP = []
        self.OOPs_MES = []
        self.IPs_MES = []
        self.exploitable_for = []
        
    def result(data):    #import string returned from window, set variables equal to values in output
        results = TreeOutputs
        data_r = str(data[::-1])             #reverse string so find finds last case rather than first

        EV_OOP_loc = data_r.find('EV OOP'[::-1])   #location of EV_OOP
        EV_OOP_s = ''   #EV as string
        for x in range(EV_OOP_loc-8,EV_OOP_loc-2):    #add characters corresponding to EV value
            EV_OOP_s = EV_OOP_s + str(data_r[x])
        results.EV_OOP = float(EV_OOP_s[::-1])

        EV_IP_loc = data_r.find('EV IP'[::-1])   
        EV_IP_s = ''   #EV as string
        for x in range(EV_IP_loc-8,EV_IP_loc-2):   
            EV_IP_s = EV_OOP_s + str(data_r[x])
        results.EV_IP = float(EV_IP_s[::-1])

        OOPs_MES_loc = data_r.find('OOP\'s MES'[::-1])   #location of OOP's MES
        OOPs_MES_s = ''   #EV as string
        for x in range(OOPs_MES_loc-8,OOPs_MES_loc-2):    #add characters corresponding to EV value
            OOPs_MES_s = OOPs_MES_s + str(data_r[x])
        results.OOPs_MES = float(OOPs_MES_s[::-1])

        IPs_MES_loc = data_r.find('IP\'s MES'[::-1])   #location of IP's MES
        IPs_MES_s = ''   #EV as string
        for x in range(IPs_MES_loc-8,IPs_MES_loc-2):    #add characters corresponding to EV value
            IPs_MES_s = IPs_MES_s + str(data_r[x])
        results.IPs_MES = float(IPs_MES_s[::-1])

        exploitable_for_loc = data_r.find('Exploitable for'[::-1])   #exploitable for: value, basically how accurate result it
        exploitable_for_s = ''   
        for x in range(exploitable_for_loc-8,exploitable_for_loc-2):    #add characters corresponding to EV value
            exploitable_for_s = exploitable_for_s + str(data_r[x])
        results.exploitable_for = float(exploitable_for_s[::-1])

        return results
        #pointless change <---- delete
        #this is for if we have custom input
        #we will have ranges elsewhere

    def generatetree():
        #this function takes simple inputs and generates a text string corresponding to a tree we would like to run
        #add multiple versions with different numbers of variables; ie, just range inputs, range + bet options, range + bet options + bet sizes, complex
        return ''
    
    def tellPIO(r1,r2,p1,p2):   #for given ranges, player positions, runs an EV calculation
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

        #put in custom ranges, more lines for specific things based on r1/r2/p1/p2
        #put in custom bet options
        #put in custom sizes

        results = TreeOutputs.result(output)#fit the things above to this object
        #print(results.EV_OOP)   #test output
        #print(output)           #test output
        solver.sendline('exit') #exit program
        return results

class PokerMath(Board,Ranges,TreeInputs,TreeOutputs,PreFlopBuild):  #parent class to hold the above
    pass


        
