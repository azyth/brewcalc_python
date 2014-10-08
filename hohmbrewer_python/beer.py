# beer.py
# John Hohm jh836
# 5 May 2014
"""Beer"""
from constants import *
#from game2d import *
import random # To randomly generate the ball velocity
import math



class Beer(object):
    """An instance of a beer.
    vol default is Liters
    temp default is Farinehight
    weight default is pounds
    
    Instance Variables
        name: name of the beer,used to create brewsheet [string]
        hops: list of Hops in beer
        grain: list of Grain or adjuncts in beer[list]
        pounds: amount of grain being used in pounds [float]
        SG: value of sugar content i beer [float]
        ibu: float values of the total IBU in beer [float]
        yeast: type of yeast [str]
        vol: size of finished batch in liters[float]
        fermentation: list of fermentation information
        temp: current temperature of the Beer in celcius [float] room temp default
        water: amount of liquid in the beer currently in liters [float]
        mash: list of mash step temperatures [list of floats]
        wateradditions: list of amounts of water added to mash[list of floats]
        additiontemps: list of tempatures for self.wateradditions[list of floats]
    """
    
    def __init__(self):
        '''initializer for Beer'''
        self.name=None
        self.hops=[]
        self.grain=[]
        self.pounds=0.0         #in lbs
        self.SG=1.0
        self.ibu=0.0
        self.yeast=None
        self.vol=0.0            # finished size in L
        self.fermentation=[]    
        self.temp=15.0          #current temp in F
        self.water=0.0          #h20 currently in beer in L
        self.mash=[]            #in F
        self.wateradditions=[]  #in L
        self.additiontemps=[]   #in F
        
    def add_hop(self,name,oz=None,boiltime=None,aa=None):
        '''adds a default of one ounce of given hop type to beer for 60 mins of boil,
        if oz or time is input it will correct the hop addition to the given amounts.
        
        pre: name must match a Hops object listed in constants. 
        '''
        
        #self.hops.append(Hops(name[0],name[1],name[2],name[3]))
        self.hops.append(Hops(name,oz,boiltime,aa))

        if aa != None:
            self.hops[-1].aa=float(AA[HOP.index(name)])
        if oz != None:
            self.hops[-1].amount=oz
        if boiltime != None:
            self.hops[-1].boil_time=boiltime
        #sort self.hops so longest boil time is first in list
        #self.hops.sort(key=lambda Hops: self.hops.boil_time, reverse=True)
    
    def add_grain(self,name,kind,lbs):
        '''adds fermentables to self.grain list then sorts list to have
        name: name of additive [string]
        kind: fermentable type [ variable listed in constants file]
        lbs: pounds added [float]
        '''
        self.grain.append(Grain(name,kind,lbs))
        #for g in self.grain:
        #    if name == g.name:
        #        g.amount+=lbs
        #    else:
        #        self.grain.append(Grain(name,kind,lbs))
        #sort so largest amount is first
        #self.grain.sort(key=lambda Grain: self.grain.amount, reverse=False)
        
    def print_hops(self):
        '''returns a list of strings of all the hop additions 
        format is '60 mins: 1 oz of CASCADE (10 IBU)' in decending order of time. 
        '''
        total=[]
        for h in self.hops:
            total.append(str(h.boil_time)+' mins: '+str(h.amount)+' oz of '+
                         str(h.name)+' ('+str(round(self.calc_ibu(h),4))+')')
        return total
    
    def print_grain(self):
        '''returns a list of strings of all the fermentables
        format '1 pound of marris otter (1.010)
        '''
        total=[]
        for g in self.grain:
            total.append(str(g.amount)+' pound of '+str(g.name)+
                         ' ('+str(round(self.gravity(g.amount,g.fermentables),4))+')')
        return total
    
    def print_beer(self):
        '''creates a txt file with a full print out of the Beer. basically a brew
        sheet. 
        '''
        bs=open(self.name,'w')
        bs.write('Brew sheet for '+self.name+'\n\n\n')
        bs.write(str(round(convert(self.vol,'quart')/4),3)+' Gallon Batch')
        bs.write('\nProjected Specific Gravity is '+str(round(self.SG,4)))
        bs.write('\nInternational Bittering Units: '+str(round(self.ibu,2)))
        
        
        #grain bill
        bs.write('\n\nTotal pounds of grain: '+str(self.pounds))
        bs.write('\nGrain:\n')
        grainlist=self.print_grain()
        for x in grainlist:
            bs.write('    '+x+'\n')
        #mash schedule
        bs.write('\nMash Schedule:\n')
        for x in range(len(self.mash)):
            bs.write('Mash step '+str(x+1)+'    Target '+str(self.mash[x])+
                     ' degrees: Add '+str(self.wateradditions[x])+' liters of '+
                     str(self.additiontemps[x])+' degree water\n')
        #hop addition
        bs.write('\nHops:\n')
        hoplist=self.print_hops()
        for x in hoplist:
            bs.write('    '+x+'\n')
        
        bs.write('\nYeast: '+self.yeast)
        bs.write('\n\nFermentation information: \n')
        for x in self.fermentation:
            bs.write('    '+x+'\n')
        
        bs.close()
        
        
    def gravity(self,pounds,fermentables):
        '''calculates SG added to beer by an additive
        
        gravity points*pounds*efficiency(.70)/vol(gal)
        '''
        
        return ((pounds*fermentables)*EFFICIENCY)/(convert(self.vol,'quart')/4)*.001
        
        #for additive in self.grain:
        #    self.SG+=((additive.amount*additive.fermentables)*EFFICIENCY)/self.vol
        #self.SG+=(pounds*adjuct)
        
    def calc_ibu(self,hop=None):
        '''calculates the ibu from listed hops in Beer and updates self.ibu if
        hop is none, otherwise it calculates and returns the IBU for given hop object
        
        '''
        if hop==None:
            #incase program must calculate ibu multiple times, prevents ibu from growing
            if self.ibu != 0.0: self.ibu=0
            
            #self.hops is a list of Hops(which are also lists)
            #[[name,aa,ounces,boil time],[name,aa,ounces,boil time]]
            
            for hop in self.hops:
                ibu=(((hop.aa*hop.amount)*(1.65*.000125**(self.SG-1.0))*
                    (((1-math.e**(-.04*hop.boil_time))/4.15))*75)/
                    (convert(self.vol,'quart')/4))
                self.ibu+=ibu
                
        else:
            return (((hop.aa*hop.amount)*(1.65*.000125**(self.SG-1.0))*
                    (((1-math.e**(-.04*hop.boil_time))/4.15))*75)/
                    (convert(self.vol,'quart')/4))
    
    def calc_strike(self,target,vol):
        '''calculates strike temperature
        *Not used*
        '''
        strike=((.2/(vol/self.pounds))*(target-self.temp)+target)
        
        self.water+=vol
        #self.mash.append(target)
        #if strike > 170:
        #    print 'CAUTION water temp above safe range for amalase'
        #    print 'but...'
        
        #print 'Add ' + str(vol) + ' liters of ' + str(strike) + ' degree water'
    
    def calc_mash(self,target,vol):
        '''calculates the tempature of water addition to the mash tun while mashing
        to acheive desired tempature'''
        
        #initial=float(initial)
        #
        #liters=float(liters)
        #target=float(target)
        #vol=float(vol)
        #
        #target=float(raw_input('what is your target mash tempature?'))
        #vol=float(raw_input('How many liter of H2O are you adding?'))
        
        mash=((target-self.temp)*(.2*self.pounds+self.water)/vol)+target
        self.temp=target
        self.water+=vol
        #self.mash.append(target)
        #print 'Add ' + str(vol) + ' liters of ' + str(mash) + ' degree water'
        return mash
    
    def set_mash(self,vol,target):
        '''propigates the mash list and wateradditions list
        vol is liters
        target is degrees farinheight
        '''
        self.mash.append(target)
        self.wateradditions.append(vol)
        self.additiontemps.append(self.calc_mash(target,vol))
        #self.water+=vol
    
    def exe(self):
        ''' executes the compiling of the brew. asks for multiple inputs to compile
        the brew then saves the brew in a txt file. 
        '''
        #name of beer
        self.name=raw_input('what is this beer called?\n')
        #what size batch
        self.vol=convert(float(raw_input('what size batch will this be?(gallons)\n'))*4,'L')
        #add grain
        grain='notdone'
        while grain!='done':
            grain=raw_input('add a grain or fermentable now? enter "done" when finished\n'+
                        'format: name,type of fermentable,pounds adding\n')
            if grain!='done':
                grain=grain.split(',')
                if grain[1] in GRAIN:    
                    self.add_grain(grain[0],grain[1],float(grain[2]))
                else:
                    print grain[1] +' is not an acceptable type of additive.\n'
        
        for g in self.grain:
            self.SG+=self.gravity(g.amount,g.fermentables)
            self.pounds+=g.amount
        print self.grain
        #add hops
        hop='notdone'
        while hop!='done':
            hop=raw_input('add another Hop now? enter "done" when finished\n'+
                        'format: name,oz,boil time,(aa may be entered if different'+
                        'then avg\n')
            if hop!='done':
                hop=hop.split(',')
                if hop[0] in HOP:
                    if len(hop)==3:
                        self.add_hop(hop[0],float(hop[1]),float(hop[2]))
                    elif len(hop)==4:
                        self.add_hop(hop[0],float(hop[1]),float(hop[2]),float(hop[3]))
                else:
                    print hop[0]+' is not an acceptable type of hops.\n'
        
        #calculate ibus
        self.calc_ibu()
        
        #calculate mash schedule, how many mash steps
        steps=raw_input('how many mash steps? (start-->145-->boil is 1) \n')
        for x in range(int(steps)):
           vol=float(raw_input('how many liters of h20 are you adding? \n'))
           target=float(raw_input('what is your target temperature?\n'))
           self.set_mash(vol,target)
        loss=self.pounds*.5
        boiloff=3.5#float(raw_input('how long will you boil for?(mins)\n'))
        final=loss+boiloff+self.vol-self.water
        self.set_mash(final,180)
        
        
        
        
        
        #what yeast using
        self.yeast=raw_input('what yeast are you using?\n')
        #cool to yeast specific range
        
        #any fermentaion information
        ferm='notdone'
        while ferm!='done':
            ferm=raw_input('would you like to enter any fermentaion information?\n'+
                           'enter "done" when finished\n')
            if ferm!='done':
                self.fermentation.append(ferm)
        
        
        #self.print_beer()
        self.print_beer()
        

class Hops(object):
    """Instance is
    
    compiled into list and sorted by boil time, 
    
    Instance Variables
        name:
        aa:
        amount:
        boil_time:
        
    if a certain hop is called then it can use the constants to pull the AA% and
    IBU info. 
    """
    

    def __init__(self,name,amount,boil_time,aa):
        '''Initializer for Hops
        '''
        self.name=name
        self.aa=aa
        self.amount=amount
        self.boil_time=boil_time
        
    def load_hop(self, name):
        '''adds a hop not in the constants list of hops
        '''
        aa=float(raw_input('what is the alpha acid %? exm:6 or 14/n'))
        oz=float(raw_input('how many ounces of hops are you adding?/n'))
        #gravity=float(raw_input('what is the specific gravity of your wort? exm: 1.101/n'))
        time=float(raw_input('how many minutes will these be boiled for?/n'))
        #vol=float(raw_input('how many gallons will this boil end at?/n'))
        pass


class Grain(object):
    '''instance is a grain object

    instance variables
        name: name of additive [string]
        kind: type of grain or fermentable additive
        fermentables: % fermentable sugars in additive
        moisture: moisture content of additive in liters
        amount: pounds of additive [float]
        
    '''
    
    def __init__(self,name,kind,amount):
        '''initializer for grain'''
        self.name=name
        self.kind=kind
        self.fermentables=float(FERMENTABLES[GRAIN.index(kind)])
        self.moisture=0.0
        self.amount=amount
        

# some useful conversion functions

def calc_sg():
    '''converts brix to specific gravity'''
    pass

def calc_brix():
    '''converts specific gravity to brix'''
    pass

def convert(number,convert_to):
    '''a conversion tool between metric and standard, using a two part argument,
    it can tell what you are trying to convert
    
    Key:(all must be entered as strings)
    F: fareinheight
    C: celsius
    quart: quarts
    L: liters
    g: grams
    lbs: pounds
    
    
    Examples:
    convert(2,'L') will convert 2 quarts to Liters
    convert(98,'C') will convert 98 degrees fareinheight to celcius
    
    pre: convert to must be a str of one of the variables in Key, 
    '''
    #calls the 
    key=['F','C','quart','L','g','lbs']
    modifier=[0,0,1.05669,0.946353,453.592,0.00220462]
    
    if convert_to=='F':
        return (number*1.8)+32
    elif convert_to=='C':
        return ((number-32)*5)/9
    else:
        return number*modifier[key.index(convert_to)]
    
    #C=((F-32)*5)/9
    #F=(C*1.8)+32
    #L=quart*0.946353
    #quart=L*1.05669
    #lbs=g*453.592
    #g=lbs*0.00220462
    