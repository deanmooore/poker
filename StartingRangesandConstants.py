
import numpy as np

class Constants:
#card ranks 1-13, suits 1-4 (52x1 matrix), maybe leave only in ranges
    deck = ['Ah', 'Kh', 'Qh', 'Jh', 'Th', '9h', '8h', '7h', '6h', '5h', '4h', '3h', '2h'
    'Ac', 'Kc', 'Qc', 'Jc', 'Tc', '9c', '8c', '7c', '6c', '5c', '4c', '3c', '2c'
    'Ad', 'Kd', 'Qd', 'Jd', 'Td', '9d', '8d', '7d', '6d', '5d', '4d', '3d', '2d'
    'As', 'Ks', 'Qs', 'Js', 'Ts', '9s', '8s', '7s', '6s', '5s', '4s', '3s', '2s']

#default inputs for bet sizes
#need to consider PIO/UPI format

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

    # #UTG player
    # UTGopen = ['']
    # UTGopen = appendrange(UTGopen.range,'22+')
    # UTGopen = appendrange(UTGopen.range,'As+')
    # #UTG+1 player
    # UTG1open = ['']
    # UTG1open = appendrange(UTGopen.range,'22+')
    # UTG1open = appendrange(UTGopen.range,'As+')
    # #CO player
    # #BTN player
    # #SB player
 

class TreeInputs:  #contains everything needed for one tree simulation
    def result(self):
        ev=0
    def result(one,two):
        ev=0
        #this is for if we have custom input
        #we will have ranges elsewhere

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
        #this is for if we have custom input
        #we will have ranges elsewhere

    def generatetree():
        #this function takes simple inputs and generates a text string corresponding to a tree we would like to run
        #add multiple versions with different numbers of variables; ie, just range inputs, range + bet options, range + bet options + bet sizes, complex
        return ''




        



