# -*- coding: utf-8 -*-
"""
Created on Tue May 28 21:53:45 2019

@author: benja
"""

import numpy as np
#Defining some variables later being used as iterators
Dummy = 0
ZeroRuns=0
OneRuns=0
TwoRuns=0
ThreeRuns=0
FourRuns=0
FiveRuns=0
SixPlusRuns=0
#input pitcher's outcome rates
#WalkRate=[.0967,.0988,.1034,.1086,.09,.08,.0893,.0843,.0676]
#KRate=[.2091,.2104,.2099,.2099,.2225,.2261,.2249,.3169,.3469]
#SingRate=[.1497,.1476,.1408,.1275,.1483,.147,.1456,.1017,.1105]
#DoubRate=[.0426,.0523,.0504,.0505,.046,.0458,.0457,.0262,.0316]
#TripRate=[.0061,.0055,.0037,.0042,.0035,.0053,.005,0,.0019]
#HRRate=[.0342,.0398,.0448,.048,.0375,.0347,.0292,.0320,.0206]
#GBORate=[.2308,.2228,.2235,.2256,.2261,.2305,.2302,.2195,.3105]
WalkRate=[.0907,.0998,.0978,.0973,.0930,.0939,.0898,.0884,.0896]
KRate=[.1962,.2133,.2161,.2310,.2372,.2247,.2348,.2426,.2491]
SingRate=[.1550,.1463,.1395,.1369,.1309,.1410,.1408,.1378,.1328]
DoubRate=[.0487,.0484,.0488,.0478,.0479,.0468,.0485,.0413,.0465]
TripRate=[.0068,.0052,.0035,.0030,.0041,.0043,.0031,.0035,.0027]
HRRate=[.0348,.0403,.0441,.0440,.0432,.0374,.0356,.0332,.0327]
GBORate=[.2339,.2233,.2251,.2200,.2219,.2259,.2236,.2266,.2233]

#This section creates functions for each plate appearance outcome
#Each outcome takes inputs of the base state, runs already scored, and outs
#For a given base/run/out state, it moves the runners to the new appropriate
#bases and iterates runs and outs as necessary

def OneBaseSingle(VarState,RunCount,OutCount):
    if VarState == [0,0,0]:
        VarState = [1,0,0]
    elif VarState == [1,0,0]:
        VarState = [1,1,0]
    elif VarState == [1,1,0]:
        VarState = [1,1,0]
        RunCount+=1
    elif VarState == [1,0,1]:
        VarState = [1,1,0]
        RunCount+=1
    elif VarState == [1,1,1]:
        VarState = [1,1,0]
        RunCount+=2
    elif VarState == [0,1,0]:
        VarState = [1,0,0]
        RunCount+=1
    elif VarState == [0,1,1]:
        VarState = [1,0,0]
        RunCount +=2
    elif VarState == [0,0,1]:
        VarState = [1,0,0]
        RunCount +=1
    return VarState,RunCount,OutCount

def TwoBaseSingle(VarState,RunCount,OutCount):
    if VarState == [0,0,0]:
        VarState = [1,0,0]
    elif VarState == [1,0,0]:
        VarState = [1,0,1]
    elif VarState == [1,1,0]:
        VarState == [1,0,1]
        RunCount +=1
    elif VarState == [1,0,1]:
        VarState == [1,0,1]
        RunCount+=1
    elif VarState == [1,1,1]:
        VarState = [1,0,1]
        RunCount +=2
    elif VarState == [0,1,0]:
        VarState = [1,0,0]
        RunCount +=1
    elif VarState == [0,1,1]:
        VarState = [1,0,0]
        RunCount +=2
    elif VarState == [0,0,1]:
        VarState = [1,0,0]
        RunCount +=1
    return VarState,RunCount,OutCount

def Double(VarState,RunCount,OutCount):
    if VarState == [0,0,0]:
        VarState = [0,1,0]
    elif VarState == [1,0,0]:
        VarState = [0,1,1]
    elif VarState == [1,1,0]:
        VarState = [0,1,1]
        RunCount +=1
    elif VarState == [1,0,1]:
        VarState = [0,1,1]
        RunCount+=1
    elif VarState == [1,1,1]:
        VarState = [0,1,1]
        RunCount +=2
    elif VarState == [0,1,0]:
        VarState = [0,1,0]
        RunCount +=1
    elif VarState == [0,1,1]:
        VarState = [0,1,0]
        RunCount +=2
    elif VarState == [0,0,1]:
        VarState = [0,1,0]
        RunCount +=1
    return VarState,RunCount,OutCount

def Triple(VarState,RunCount,OutCount):
    if VarState == [0,0,0]:
        VarState = [0,0,1]
    elif VarState == [1,0,0]:
        VarState = [0,0,1]
        RunCount +=1
    elif VarState == [1,1,0]:
        VarState = [0,0,1]
        RunCount +=2
    elif VarState == [1,0,1]:
        VarState = [0,0,1]
        RunCount+=2
    elif VarState == [1,1,1]:
        VarState = [0,0,1]
        RunCount +=3
    elif VarState == [0,1,0]:
        VarState = [0,0,1]
        RunCount +=1
    elif VarState == [0,1,1]:
        VarState = [0,0,1]
        RunCount+=2
    elif VarState == [0,0,1]:
        VarState = [0,0,1]
        RunCount +=1
    return VarState,RunCount,OutCount

def HomeRun(VarState,RunCount,OutCount):
    if VarState == [0,0,0]:
        VarState = [0,0,0]
        RunCount +=1
    elif VarState == [1,0,0]:
        VarState = [0,0,0]
        RunCount +=2
    elif VarState == [1,1,0]:
        VarState = [0,0,0]
        RunCount +=3
    elif VarState == [1,0,1]:
        VarState = [0,0,0]
        RunCount+=3
    elif VarState == [1,1,1]:
        VarState = [0,0,0]
        RunCount +=4
    elif VarState == [0,1,0]:
        VarState = [0,0,0]
        RunCount +=2
    elif VarState == [0,1,1]:
        VarState = [0,0,0]
        RunCount +=3
    elif VarState == [0,0,1]:
        VarState = [0,0,0]
        RunCount +=2
    return VarState,RunCount,OutCount

def Walk(VarState,RunCount,OutCount):
    if VarState == [0,0,0]:
        VarState = [1,0,0]
    elif VarState == [1,0,0]:
        VarState = [1,1,0]
    elif VarState == [1,1,0]:
        VarState = [1,1,1]
    elif VarState == [1,0,1]:
        VarState=[1,1,1]
    elif VarState == [1,1,1]:
        VarState = [1,1,1]
        RunCount+=1
    elif VarState == [0,1,0]:
        VarState = [1,1,0]
    elif VarState == [0,1,1]:
        VarState = [1,1,1]
    elif VarState == [0,0,1]:
        VarState = [1,0,1]
    return VarState,RunCount,OutCount

def Strikeout(VarState,RunCount,OutCount):
    OutCount+=1
    return VarState,RunCount,OutCount

def Groundout(VarState,RunCount,OutCount):
    OutCount+=1
    if OutCount == 3:
        return VarState,RunCount,OutCount
    elif VarState == [0,0,0]:
        VarState = [0,0,0]
    elif VarState == [1,0,0]:
        VarState = [0,1,0]
    elif VarState == [1,1,0]:
        VarState = [0,1,1]
    elif VarState == [1,0,1]:
        VarState = [0,1,0]
        RunCount+=1
    elif VarState == [1,1,1]:
        VarState = [0,1,1]
        RunCount +=1
    elif VarState == [0,1,0]:
        VarState = [0,0,1]
    elif VarState == [0,1,1]:
        VarState = [0,0,1]
        RunCount +=1
    elif VarState == [0,0,1]:
        VarState = [0,0,0]
        RunCount +=1
    return VarState,RunCount,OutCount

def GIDP(VarState,RunCount,OutCount):
    if OutCount == 2:
        OutCount+=1
    elif VarState == [0,0,0]:
        VarState=[0,0,0]
        OutCount+=1
    elif VarState == [1,0,0]:
        VarState=[0,0,0]
        OutCount+=2
    elif VarState == [1,1,0]:
        VarState =[0,0,1]
        OutCount+=2
    elif VarState == [1,0,1]:
        VarState = [0,0,0]
        if OutCount == 1:
            OutCount+=2
        else:
            OutCount+=2
            RunCount+=1
    elif VarState == [1,1,1]:
        VarState=[0,0,1]
        if OutCount ==1:
            OutCount+=2
        else:
            OutCount+=2
            RunCount+=1
    elif VarState == [0,1,0]:
        VarState=[0,0,1]
        OutCount+=1
    elif VarState == [0,1,1]:
        VarState = [0,0,1]
        RunCount+=1
        OutCount+=1
    elif VarState == [0,0,1]:
        VarState = [0,0,0]
        RunCount+=1
        OutCount+=1
    return VarState,RunCount,OutCount

def Flyout(VarState,RunCount,OutCount):
    OutCount+=1
    if OutCount == 3:
        return VarState,RunCount,OutCount
    elif VarState == [0,0,0]:
        VarState == [0,0,0]
    elif VarState == [1,0,0]:
        VarState == [1,0,0]
    elif VarState == [1,1,0]:
        VarState = [1,0,1]
    elif VarState == [1,0,1]:
        VarState = [1,0,0]
        RunCount+=1
    elif VarState == [1,1,1]:
        VarState = [1,0,1]
        RunCount +=1
    elif VarState == [0,1,0]:
        VarState = [0,0,1]
    elif VarState == [0,1,1]:
        VarState = [0,0,1]
        RunCount+=1
    elif VarState == [0,0,1]:
        VarState = [0,0,0]
        RunCount +=1
    return VarState,RunCount,OutCount

def Lineout(VarState,RunCount,OutCount):
    OutCount+=1
    return VarState,RunCount,OutCount

#setting a few more iterating variables to 0
Action = 0
TotalRuns=0
TotalInnings=0
Stranded=0

#This is the core loop.
#The first line sets the number of simulations to run.
#Inside the loop, numpy generates a random number between 0 and 1.
#Each outcome is assigned a range via the batted ball outcomes of each type
#of batted ball in 2018 multiplied by the pitcher's likelihood of producing
#that outcome.
#It then calls the appropriate plate appearance result function to move bases,
#runs, and outs as appropriate.
#When the inning is over (3 outs are reached),the loop records the number of
#runs scored (both in a running tally and by bucket) and starts over.
for i in range(1000000):
    Inning=0
    Hitter=0
    Runs=0
    Outs=0
    Bases= [0,0,0]
    while Inning<9:
        while Outs <3:
            Action = np.random.random()
            if Action < WalkRate[Hitter%9]:
                Dummy= Walk(Bases,Runs,Outs)
                Bases = Dummy[0]
                Runs = Dummy[1]
                Outs = Dummy[2]
            elif Action <(WalkRate[Hitter%9]+KRate[Hitter%9]):
                Dummy=Strikeout(Bases,Runs,Outs)
                Bases = Dummy[0]
                Runs = Dummy[1]
                Outs = Dummy[2]
            elif Action <(WalkRate[Hitter%9]+KRate[Hitter%9]+SingRate[Hitter%9]/2):
                Dummy=TwoBaseSingle(Bases,Runs,Outs)
                Bases = Dummy[0]
                Runs = Dummy[1]
                Outs = Dummy[2]
            elif Action <(WalkRate[Hitter%9]+KRate[Hitter%9]+SingRate[Hitter%9]):
                if Outs == 2:
                    Dummy=TwoBaseSingle(Bases,Runs,Outs)
                    Bases = Dummy[0]
                    Runs = Dummy[1]
                    Outs = Dummy[2]
                else:
                    Dummy=OneBaseSingle(Bases,Runs,Outs)
                    Bases = Dummy[0]
                    Runs = Dummy[1]
                    Outs = Dummy[2]
            elif Action <(WalkRate[Hitter%9]+KRate[Hitter%9]+SingRate[Hitter%9]+DoubRate[Hitter%9]):
                Dummy=Double(Bases,Runs,Outs)
                Bases = Dummy[0]
                Runs = Dummy[1]
                Outs = Dummy[2]
            elif Action <(WalkRate[Hitter%9]+KRate[Hitter%9]+SingRate[Hitter%9]+DoubRate[Hitter%9]+TripRate[Hitter%9]):
                Dummy=Triple(Bases,Runs,Outs)
                Bases = Dummy[0]
                Runs = Dummy[1]
                Outs = Dummy[2]
            elif Action <(WalkRate[Hitter%9]+KRate[Hitter%9]+SingRate[Hitter%9]+DoubRate[Hitter%9]+TripRate[Hitter%9]+HRRate[Hitter%9]):
                Dummy=HomeRun(Bases,Runs,Outs)
                Bases = Dummy[0]
                Runs = Dummy[1]
                Outs = Dummy[2]
            elif Action <(WalkRate[Hitter%9]+KRate[Hitter%9]+SingRate[Hitter%9]+DoubRate[Hitter%9]+TripRate[Hitter%9]+HRRate[Hitter%9]+GBORate[Hitter%9]/2):
                Dummy=Groundout(Bases,Runs,Outs)
                Bases = Dummy[0]
                Runs = Dummy[1]
                Outs = Dummy[2]
            elif Action <(WalkRate[Hitter%9]+KRate[Hitter%9]+SingRate[Hitter%9]+DoubRate[Hitter%9]+TripRate[Hitter%9]+HRRate[Hitter%9]+GBORate[Hitter%9]):
                Dummy=GIDP(Bases,Runs,Outs)
                Bases = Dummy[0]
                Runs = Dummy[1]
                Outs = Dummy[2]
            else: 
                Dummy=Flyout(Bases,Runs,Outs)
                Bases = Dummy[0]
                Runs = Dummy[1]
                Outs = Dummy[2]
            if Outs == 3 and Hitter ==8:
                Stranded+=Bases[0]+Bases[1]+Bases[2]
            Hitter+=1
            
        TotalRuns+=Runs
        Runs=0
        Outs=0
        Bases=[0,0,0]
        Inning+=1
    i+=1


#Outputs
print(TotalRuns/1000000.0)
print(Stranded)
