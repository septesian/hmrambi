#*******************************************************************************
#
# This an ancient game.
#
# 10 REM *** CONVERTED FROM THE ORIGINAL FOCAL PROGRAM AND MODIFIED
# 20 REM *** FOR EDUSYSTEM 70 BY DAVID AHL, DIGITAL
# 30 REM *** MODIFIED FOR 8K MICROSOFT BASIC BY PETER TURNBULL
#
# Well, now it has been translated from basic into pyhton
#
# Translation:		Colin Finnis				8/4/2013
#
#*******************************************************************************
from random import random
import pdb

# Need to seed random

def notEnoughSeed(): print "Humurabi: Think again. You have only %d bushels of grain. Now then!" % bushels
def notEnoughAcres (): print "Humurabi: Think again. You have only %d acres. Now then!"  % acres

#*******************************************************************************
# Name:			fink
#
# Description:	Tell user they have been impeaced etc
#
# Return:		nono
#
# Parameters:	none
#
# Inputs:		none
#
# Outputs:		none
#
#*******************************************************************************

def fink():
	print "Due to this extreme mismanagment you have not only"
	print "been impeached and thrown out of office but you have"
	print "also been declared 'NATIONAL FINK' !!"

#*******************************************************************************
# Name:			rnd
#
# Description:	Produce a random number in a specified range.
#
# Return:		The generated random number.
#
# Parameters:	range		- A number specify the range in which the random
#							  number is to lie.
#
# Inputs:		none
#
# Outputs:		none
#
#*******************************************************************************

def rnd(range):
	return int(random() * range) + 1

#*******************************************************************************
# Name:			inputNumber
#
# Description:	Input a number from console. Continue until number entered.
#
# Return:		Number entered from console.
#
# Parameters:	prompt		- Text prompt for input.
#
# Inputs:		none
#
# Outputs:		none
#
#*******************************************************************************

def inputNumber(prompt):
	value = None
	while value is None:
		try:
			value = int(raw_input(prompt))
		except ValueError:
			print 'Please enter a number!'
	return value

#*******************************************************************************
#
# Main
#
#*******************************************************************************

population = 100
migrated = 0
totStarved = 0
avgStarved = 0
bushels = 2800
acres = 1000

print "Try your hand at governing Ancient Sumeria"
print "successfully for a 10 year term of office."
print ""
print "Population is %d" % population
print "The city owns %d acres." % acres
print "You have %d bushels in store." % bushels
print ""

# Now start looping through the years.

year = 1
endState = 0
while year < 11 and endState == 0:
	tradeValue = 17 + rnd(10)

	# Find out how many acres to buy
		
	done = False
	while done == False :
		print "Land is trading at %d bushels per acre." % tradeValue
		buy = inputNumber ("How many acres do you wish to buy?")
		if buy < 0:
			endState = 1
			done = True
		elif (buy * tradeValue) > bushels :
			notEnoughSeed()
		else :
			bushels -= (buy * tradeValue)
			acres += buy
			done = True

	# If we didnt buy find out how many acres to sell
	
	done = False
	while done == False and buy == 0 and endState == 0:
		sell = inputNumber ("How many acres do you wish to sell?")
		if sell < 0:
			endState = 1
			done = True
		elif sell > acres :
			noteEnoughAcres()
		else :
			bushels += (sell * tradeValue)
			acres -= sell
			done = True

	# Now how much are we going to feed the people
	
	done = False
	while done == False and endState == 0:
		feed = inputNumber("How many bushels do you wish to feed the people?")
		if feed < 0:
			endstate = 1
			done = True
		elif feed > bushels :
			notEnoughSeed()
		else :
			bushels -= feed
			done = True
		
	# How many acres are we going plant

	done = False
	while done == False and endState == 0:
		plant = inputNumber("How many acres do you wish to plant with seed?")
		if plant < 0:
			endState = 1
			done = True
		elif plant > acres :
			notEnoughAcres()
		elif (plant/2) > bushels :
			notEnoughSeed()
		elif (plant/10) > population :
			print "But you only have %d people to tend the fields. Now then!" % population
		else :
			bushels -= int(plant/2)
			done = True
	
	if endState == 0:
		
		# Calculate how things went this year

		# Check the state of the population. We need 20 bushels for each person.
		# If more than 45% died of startvation its impeachment.
		
		curStarved = population - int((feed/20))
		totStarved += curStarved
		avgStarved = (((year - 1) * avgStarved) + ((curStarved * 100)/population))/ year
		
		if curStarved/population > .45:
			endState = 2
		else:
			population = population - curStarved
			totStarved += curStarved

			# How did the harvest go
			
			curYield = rnd(5)
			harvest = plant * curYield

			# Rats ate.
			
			ratsAte = bushels/rnd(5)

			# Update the stores

			bushels += harvest - ratsAte

			# Has there been a plague set proability at 15%
			
			if rnd(20) <= 3 :
				population = population/2
				print "A horrible plague struck! half the people died!"

			# Add migrants to population
			
			migrated = int(rnd(5) * (20 * acres + bushels)/population/100 + 1)
			population += migrated

			# Make your report.
			
			print ""
			print "Hamurabi: I beg to report to you in year %d, " % year
			print "%d people starved %d came to the city" % (curStarved, migrated)
			print ""
			print "Population is now %d" % population
			print "The city now owns %d acres." % acres
			print "You have harvested %d bushels per acre." % curYield
			print "Rats ate %d bushels." % ratsAte
			print "You now have %d bushels in store." % bushels
			print ""
	
	year+= 1
# Final reports and summing up where relevant.

if endState == 1:
	print "Hamurabi: I cannot do what you wish."
	print "Get yourself another steward!!!!!"
elif endState == 2:
	print "You starved %d people in one year!!!" % curStarved
	fink()
else:
	acresPer = acres/population
	print "In your 10-year term of office, %d percent of the population" % avgStarved
	print "on average starved per year, i.e,, a total of %d people died!!" % totStarved
	print "You started with 10 acres per person and ended with %d acres per person" % acresPer
	if avgStarved > 33  or acresPer < 7 :
		fink()			
	elif avgStarved > 10 or acresPer < 9 :
		print "Your heavy-handed performace smacks of nero and Ivan IV."
		print "The people (remainig) find you an unpleasant ruler, and,"
		print "frankly, hate your guts."
	elif avgStarved > 3 or acresPer < 10:
		print "Your performance could have been somewhat better, but"
		print "really wasn't too bad at all."
		print "%d people would dearly like to see you assasinated, but" % int((population * .8) * random())
		print "we all have our trivial problems."
	else:
		print "A fantastic performance!!! Charlemange, Disraeli and"
		print "Jefferson combinde could not have done better!"
print ""
print "So long for now."		
		
