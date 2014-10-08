# constants.py
# 
# 5 May 2014
# John Hohm jh836
"""Constants for hohmbrewer

"""
import colormodel
import sys
#import beer


### WINDOW CONSTANTS (all coordinates are in pixels) ###

#: the width of the game display 
GAME_WIDTH  = 480
#: the height of the game display
GAME_HEIGHT = 620

#brew house information
EFFICIENCY=.70


# hop constants (name,aa,ounces,boil time)

HOP=['admiral', 'ahtanum', 'amarillo', 'aquila', 'b. c. goldings', 'banner',
      'bramling cross ', 'brewers gold', 'bullion', 'cascade', 'centennial',
      'challenger', 'chinook', 'citra', 'cluster', 'columbus', 'comet', 'crystal',
      'domesic hallertau', 'east kent goldings', 'eroica', 'first gold', 'fuggles',
      'galena', 'glacier', 'goldings', 'hallertau mittelfruh', 'hallertau hersbrucker',
      'herald', 'hersbrucker', 'horizon', 'huller bitterer', 'kent goldings',
      'liberty', 'lublin', 'magnum', 'millenium', 'mount hood', 'mount rainier',
      'motueka', 'nelson sauvin', 'newport', 'northdown', 'northern brewer',
      'nugget', 'olympic', 'omega', 'orion', 'pacific gem', 'perle', 'phoenix',
      'pioneer', 'pride of ringwood', 'progress', 'record', 'saaz', 'santiam',
      'satus', 'simcoe', 'sorachi ace', 'spalt', 'sterling', 'sticklebract',
      'strisselspalt', 'styrian goldings', 'super alpha', 'super styrians',
      'summit', 'talisman', 'target', 'tettnanger', 'tomahawk', 'ultra', 'vanguard',
      'warrior', 'whitbread golding', 'willamette', 'wye target', 'yamhill goldings',
      'yakima cluster', 'yeoman', 'zenith', 'zeus']

AA=['14.5', '5.5', '8.6', '7', '5', '10', '6.5', '9', '7.5', '7', '7.8', '8.5', '13',
    '11', '6.5', '15', '10', '4.3', '3.9', '5', '12', '7.5', '4.5', '13', '5.5',
    '4.5', '3.75', '4', '12', '4', '12.5', '5.75', '5', '4', '4.5', '15', '15.5',
    '4.8', '6.2', '7.0', '12.5', '15.5', '8.6', '7.8', '14', '12', '10', '7', '15.4',
    '8.2', '10', '9', '10', '6.25', '6.5', '3.5', '6.5', '13', '12.7', '11.1', '4.5',
    '8.7', '11.5', '3.5', '5.5', '13', '9', '18.5', '8', '11.5', '4.5', '15', '4.5',
    '5', '16', '6', '4.5', '10', '4', '7', '7.25', '9', '16']

ADMIRAL=['ADMIRAL', 14.5, 1.0, 60.0]
CASCADE=['CASCADE', 7.0, 1.0, 60.0]

#
#ADMIRAL=['ADMIRAL', 14.5, 1.0, 60.0]
#AHTANUM=['AHTANUM', 5.5, 1.0, 60.0]
#AMARILLO=['AMARILLO', 7.0, 1.0, 60.0]
#AQUILA=['cascade', 7.0, 1.0, 60.0]
#B.C.GOLDINGS=['B. C. GOLDINGS', 5.0, 1.0, 60.0]
#BANNER=['BANNER', 10.0, 1.0, 60.0]
#BRAMLING_CROSS=beer.Hops('BRAMLING CROSS', 6.5, 1.0, 60.0)
#BREWERS_GOLD=beer.Hops('BREWERS GOLD', 9.0, 1.0, 60.0)
#BULLION=beer.Hops('BULLION', 7.5, 1.0, 60.0)
#CASCADE=beer.Hops('CASCADE', 7.0, 1.0, 60.0)
#CENTENNIAL=beer.Hops('CENTENNIAL', 7.8, 1.0, 60.0)
#CHALLENGER=beer.Hops('CHALLENGER', 8.5, 1.0, 60.0)
#CHINOOK =beer.Hops('cascade', 13.0, 1.0, 60.0)
#CITRA =beer.Hops('cascade', 11.0, 1.0, 60.0)
#CLUSTER =beer.Hops('cascade', 6.5, 1.0, 60.0)
#COLUMBUS =beer.Hops('cascade', 15.0, 1.0, 60.0)
#COMET =beer.Hops('cascade', 10.0, 1.0, 60.0)
#CRYSTAL =beer.Hops('cascade', 4.3, 1.0, 60.0)
#DOMESIC_HALLERTAU=beer.Hops('DOMESIC HALLERTAU', 3.9, 1.0, 60.0)
#EAST_KENT_GOLDINGS=beer.Hops('EAST KENT GOLDINGS', 5.0, 1.0, 60.0)
#EROICA =beer.Hops('cascade', 12.0, 1.0, 60.0)
#FIRST_GOLD =beer.Hops('FIRST GOLD', 7.5, 1.0, 60.0)
#FUGGLES =beer.Hops('cascade', 4.5, 1.0, 60.0)
#GALENA =beer.Hops('cascade', 13.0, 1.0, 60.0)
#GLACIER =beer.Hops('cascade', 5.5, 1.0, 60.0)
#GOLDINGS =beer.Hops('cascade', 4.5, 1.0, 60.0)
#HALLERTAU_MITTELFRUH=beer.Hops('HALLERTAU MITTELFRUH', 3.75, 1.0, 60.0)
#HALLERTAU_HERSBRUCKER=beer.Hops('HALLERTAU HERSBRUCKER', 4.0, 1.0, 60.0)
#HERALD =beer.Hops('cascade', 12.0, 1.0, 60.0)
#HERSBRUCKER =beer.Hops('cascade', 4.0, 1.0, 60.0)
#HORIZON =beer.Hops('cascade', 12.5, 1.0, 60.0)
#HULLER_BITTERER=beer.Hops('HULLER BITTERER', 5.75, 1.0, 60.0)
#KENT_GOLDINGS=beer.Hops('KENT GOLDINGS', 5.0, 1.0, 60.0)
#LIBERTY =beer.Hops('cascade', 4.0, 1.0, 60.0)
#LUBLIN =beer.Hops('cascade', 4.5, 1.0, 60.0)
#MAGNUM =beer.Hops('cascade', 15.0, 1.0, 60.0)
#MILLENIUM =beer.Hops('cascade', 15.5, 1.0, 60.0)
#MOUNT_HOOD=beer.Hops('MOUNT HOOD', 4.8, 1.0, 60.0)
#MOUNT_RAINIER=beer.Hops('MOUNT RAINIER', 6.2, 1.0, 60.0)
#MOTUEKA =beer.Hops('cascade', 7.0, 1.0, 60.0)
#NELSON_SAUVIN=beer.Hops('NELSON SAUVIN', 12.5, 1.0, 60.0)
#NEWPORT =beer.Hops('cascade', 15.5, 1.0, 60.0)
#NORTHDOWN =beer.Hops('cascade', 8.6, 1.0, 60.0)
#NORTHERN_BREWER=beer.Hops('NORTHERN BREWER', 7.8, 1.0, 60.0)
#NUGGET =beer.Hops('cascade', 14.0, 1.0, 60.0)
#OLYMPIC =beer.Hops('cascade', 12.0, 1.0, 60.0)
#OMEGA =beer.Hops('cascade', 10.0, 1.0, 60.0)
#ORION =beer.Hops('cascade', 7.0, 1.0, 60.0)
#PACIFIC_GEM=beer.Hops('PACIFIC GEM', 15.4, 1.0, 60.0)
#PERLE =beer.Hops('cascade', 8.2, 1.0, 60.0)
#PHOENIX =beer.Hops('cascade', 10.0, 1.0, 60.0)
#PIONEER =beer.Hops('cascade', 9.0, 1.0, 60.0)
#PRIDE_OF_RINGWOOD=beer.Hops('PRIDE OF RINGWOOD', 10.0, 1.0, 60.0)
#PROGRESS =beer.Hops('cascade', 6.25, 1.0, 60.0)
#RECORD =beer.Hops('cascade', 6.5, 1.0, 60.0)
#SAAZ =beer.Hops('cascade', 3.5, 1.0, 60.0)
#SANTIAM =beer.Hops('cascade', 6.5, 1.0, 60.0)
#SATUS =beer.Hops('cascade', 13.0, 1.0, 60.0)
#SIMCOE =beer.Hops('cascade', 12.7, 1.0, 60.0)
#SORACHI_ACE =beer.Hops('SORACHI ACE', 11.1, 1.0, 60.0)
#SPALT =beer.Hops('cascade', 4.5, 1.0, 60.0)
#STERLING =beer.Hops('cascade', 8.7, 1.0, 60.0)
#STICKLEBRACT=beer.Hops('STICKLEBRACT', 11.5, 1.0, 60.0)
#STRISSELSPALT=beer.Hops('STRISSELSPALT', 3.5, 1.0, 60.0)
#STYRIANGOLDINGS=beer.Hops('STYRIAN GOLDINGS', 5.5, 1.0, 60.0)
#SUPER_ALPHA=beer.Hops('SUPER ALPHA', 13.0, 1.0, 60.0)
#SUPER_STYRIANS=beer.Hops('SUPER STYRIANS', 9.0, 1.0, 60.0)
#SUMMIT=beer.Hops('SUMMIT', 18.5, 1.0, 60.0)
#TALISMAN=beer.Hops('TALISMAN', 8.0, 1.0, 60.0)
#TARGET=beer.Hops('TARGET', 11.5, 1.0, 60.0)
#TETTNANGER=beer.Hops('TETTNANGER', 4.5, 1.0, 60.0)
#TOMAHAWK=beer.Hops('TOMAHAWK', 15.0, 1.0, 60.0)
#ULTRA=beer.Hops('ULTRA', 4.5, 1.0, 60.0)
#VANGUARD=beer.Hops('VANGUARD', 5.0, 1.0, 60.0)
#WARRIOR=beer.Hops('WARRIOR', 16.0, 1.0, 60.0)
#WHITBREAD_GOLDING=beer.Hops('WHITBREAD GOLDING', 6.0, 1.0, 60.0)
#WILLAMETTE=beer.Hops('WILLAMETTE', 4.5, 1.0, 60.0)
#WYE_TARGET=beer.Hops('WYE TARGET', 10.0, 1.0, 60.0)
#YAMHILL_GOLDINGS=beer.Hops('YAMHILL GOLDINGS', 4.0, 1.0, 60.0)
#YAKIMA_LUSTER=beer.Hops('YAKIMA CLUSTER', 7.0, 1.0, 60.0)
#YEOMAN=beer.Hops('YEOMAN', 7.25, 1.0, 60.0)
#ZENITH=beer.Hops('ZENITH', 9.0, 1.0, 60.0)
#ZEUS=beer.Hops('ZEUS', 16.0, 1.0, 60.0)

#adjunct constants name=[kind,fermentables,moisture]
GRAIN=['acid malt', 'amber dry extract', 'amber liquid extract', 'amber malt',
       'aromatic malt', 'barley hulls', 'barley flaked', 'barley raw',
       'barley torrefied', 'biscuit malt', 'black patent',
       'black barley (stout)', 'brown malt', 'brown sugar dark', 'brown sugar light',
       'brumalt', 'candi sugar - amber', 'candi sugar - clear', 'candi sugar - dark',
       'cane (beet) sugar', 'carapils', 'caraamber', 'carafoam',
       'crystal malt 10l', 'crystal malt 20l',
       'crystal malt - 30l', 'crystal malt 40l',
       'crystal malt 60l', 'crystal malt 80l',
       'crystal malt 120l', 'caramunich malt', 'carared',
       'caravienne malt', 'chocolate malt', 'chocolate malt', 'dextrose',
       'corn syrup', 'flaked corn', 'dark dry extract', 'dark liquid extract',
       'dememera sugar', 'extra light dry extract', 'grits', 'honey', 'invert sugar',
       'light dry extract', 'maple syrup', 'melanoiden malt', 'mild malt',
       'lactose', 'molasses', 'munich', 'munich - 10l',
       'munich malt - 20l', 'oats', 'oats malted', 'pale liquid extract',
       'pale malt (2 row) bel', 'pale malt', 'pale malt (2 row) us',
       'pale malt (6 row) us', 'peat smoked malt', 'pilsner (2 row) bel',
       'pilsner (2 row) ger', 'pilsner (2 row) uk', 'pilsner liquid extract',
       'rice extract syrup', 'rice hulls', 'rice flaked', 'roasted barley',
       'rye malt', 'rye flaked', 'smoked malt', 'special b', 'special roast',
       'sucrose', 'toasted malt', 'turbinado', 'victory malt',
       'vienna', 'wheat dry extract', 'wheat liquid extract', 'wheat',
       'wheat malt, dark', 'wheat malt ger', 'wheat flaked', 'wheat roasted',
       'wheat torrified', 'white wheat malt', 'caraaroma']

FERMENTABLES=['27', '44', '36', '35', '36', '00', '32', '28', '36', '36', '25',
              '25', '32', '46', '46', '33', '36', '36', '36', '46', '33', '35',
              '33', '35', '35', '35', '34', '34', '34', '33', '33', '35', '34',
              '28', '34', '46', '36', '37', '44', '36', '46', '44', '37', '35',
              '46', '44', '30', '37', '37', '35', '36', '37', '35', '35', '37',
              '37', '36', '37', '36', '36', '35', '34', '36', '37', '36', '36',
              '32', '00', '32', '25', '29', '36', '37', '30', '33', '46', '33',
              '44', '34', '36', '44', '36', '37', '39', '39', '35', '25', '36',
              '40', '33']

#srm is fucked up, fix later with grain.txt
SRM=['27', '44', '36', '35', '36', '00', '32', '28', '36', '36', '25', '25', '32',
     '46', '46', '33', '36', '36', '36', '46', '33', '35', '33', '35', '35', '35',
     '34', '34', '34', '33', '33', '35', '34', '28', '34', '46', '36', '37', '44',
     '36', '46', '44', '37', '35', '46', '44', '30', '37', '37', '35', '36', '37',
     '35', '35', '37', '37', '36', '37', '36', '36', '35', '34', '36', '37', '36',
     '36', '32', '00', '32', '25', '29', '36', '37', '30', '33', '46', '33', '44',
     '34', '36', '44', '36', '37', '39', '39', '35', '25', '36', '40'
     '00', '00', '00']

MOISTURE=[.04,.1,.04]

MARRIS_OTTER=['barley',35,5]
BARLEY=35
WHEAT=0
CARA_BARLEY=0
COCO_BARLEY=0
BLACK_BARLEY=0
MALT_SYRUP=0
HONEY=0
SUCROSE=46
DEXTROSE=0
CORN=0

#.5 L/lb h20 absorbed by grain
#1.5-2.0 L/lb proper mash water ratio

# add yeast information here




### USE COMMAND LINE ARGUMENTS TO CHANGE NUMBER OF BRICKS IN ROW"""

"""sys.argv is a list of the command line arguments when you run
python. These arguments are everything after the work python. So
if you start the game typing

    python breakout.py 3 4 
    
Python puts ['breakout.py', '3', '4'] into sys.argv. Below, we 
take advantage of this fact to change the constants BRICKS_IN_ROW
and BRICK_ROWS

Sounds are by default enabled, but may be disabled by entering False
as a fourth argument
   python breakout.py 3 4 False
"""

try:
   if (not sys.argv is None and len(sys.argv) >= 3):
        bs_in_row  = int(sys.argv[1])
        brick_rows = int(sys.argv[2])
        if (bs_in_row > 0 and brick_rows > 0):
            # ALTER THE CONSTANTS
            BRICKS_IN_ROW  = bs_in_row
            BRICK_ROWS     = brick_rows
            BRICK_WIDTH    = GAME_WIDTH / BRICKS_IN_ROW - BRICK_SEP_H
   if sys.argv[3]:
      ENABLE_SOUND=sys.argv[3]
        
except: # Leave the constants alone
   pass