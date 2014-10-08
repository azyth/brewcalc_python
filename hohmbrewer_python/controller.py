# controller.py
# John Hohm jh836
# 5 May 2014
"""Primary module for Hohmbrew application

"""
#from constants import *
#from game2d import *
from beer import *



class Brew(object):
    '''creates a new beer assumes a 60 min boil
    '''
    def __init__(self):
        '''initilizer'''
        self=Beer()
        
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
    






#class Brew(Game):
#    """Creates a new brew
#    """
#    
#    
#    def init(self):
#        """Initialize """
#        self.beer=Beer()
#
#    def update(self):
#        """updates"""
#        
#        pass
#    def draw(self):
#        """Draws the game objects to the view.
#        
#        """
#        print 'Hops:' + self.beer.hops
#        print 'Specific Gravity:' + self.beer.SG
#        print 'IBUs:' + self.beer.ibu
#        #self._welcome.draw(self.view)
#        
#    