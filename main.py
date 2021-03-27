#Imports
import math
import pickle
import random as rand
import os
clear = lambda : os.system("cls")

#Basic vars
actions = 1
action = ""
age = 1
population = 2
hiddenPopulation = population
gameOn = True
ageUpdate = True
pplDied = False
modifierF = 1
modifierW = 1
prevPop = 0

#Technology
technology = []
discPointsRemaining = 0
changeP = 0
pickaxe = False
waterPit = False
waterTunnels = False
corn = False
housing = False
iron = False
glass = False
extHeat = False
copper = False
bronze = False
translation = False
expansion = False
farmer = False
leader = False
cornAmt = 25
housingAmt = cornAmt + 25
ironAmt = housingAmt + 30
farmerAmt = ironAmt + 15
glassAmt = farmerAmt + 35
extHeatAmt = glassAmt + 25
copperAmt = extHeatAmt + 25
bronzeAmt = copperAmt + 25
translationAmt = bronzeAmt + 30
leaderAmt = translationAmt + 20
expansionAmt = leaderAmt + 60
techList = []
techListPre = [cornAmt,housingAmt,ironAmt,farmerAmt,glassAmt,extHeatAmt,copperAmt,bronzeAmt,translationAmt,leaderAmt,expansionAmt]

#Resources
food = 5
trees = 1
water = 5
wood = 0
rock = 0

#Buildings
farms = 0
houses = 0

#Professions
discoverers = 0
farmers = 0
waterers = 0
soldiers = 0

#Leader
ldrNameList = ["irrelevent","Rodriguez","Napoleon","Elizabeth","Allen","Schubert","Brad","Betsy","Patricia","Kimberly","Rebecca"]
ldrName = ""
ldrStrength = 0
ldrIntellect = 0
ldrDiplomacy = 0
ldrSocials = 0

#Expansion
currency = 0
otherCivCurrency = rand.randint(30,100)
otherCivPop = 0
otherCivFood = 0
otherCivWater = 0
otherCivFarms = 0
otherCivHouses = 0
otherCivRock = 0
otherCivWood = 0
otherCivCurrency2 = rand.randint(20,110)
otherCivPop2 = 0
otherCivFood2 = 0
otherCivWater2 = 0
otherCivFarms2 = 0
otherCivHouses2 = 0
otherCivRock2 = 0
otherCivWood2 = 0
otherCivCurrency3 = rand.randint(40,90)
otherCivPop3 = 0
otherCivFood3 = 0
otherCivWater3 = 0
otherCivFarms3 = 0
otherCivHouses3 = 0
otherCivRock3 = 0
otherCivWood3 = 0
count = 3
run = True
civNames = ["Arcadia","Aunine","Mandara","Polus","Yotor","Kabia","Aksum","Minoan","Brogan","Colchis","Dunharo","Edom","Luethia","Silla","Kush","Temate","Kediri","Joseon","Malacca","Tente","Kartili","Butuan","Benikin","Sorrea","Vraba","Wessex","Merca","Peni","Terbum","Nocell","Jolof","Yallas","Dendidiri","Duryn","Lunia","Vexenburg","Evosmos","Trikala","Voula","Pyrgos"]
otherCivName = civNames[rand.randint(0,39)]
civNames.remove(otherCivName)
otherCivName2 = civNames[rand.randint(0,38)]
civNames.remove(otherCivName2)
otherCivName3 = civNames[rand.randint(0,37)]
civNames.remove(otherCivName3)
otherCivLeader = ldrNameList[rand.randint(1,10)]
ldrNameList.remove(otherCivLeader)
otherCivLeader2 = ldrNameList[rand.randint(1,9)]
ldrNameList.remove(otherCivLeader2)
otherCivLeader3 = ldrNameList[rand.randint(1,8)]
ldrNameList.remove(otherCivLeader3)

#Holds everything pertaining to other civilizations and expansion
def expansionFunc() :
	global expansion, currency, age, otherCivRock, otherCivHouses, otherCivFarms, otherCivWood, otherCivWater, otherCivFood, count, otherCivRock2, otherCivHouses2, otherCivFarms2, otherCivWood2, otherCivWater2, otherCivFood2, otherCivRock3, otherCivHouses3, otherCivFarms3, otherCivWood3, otherCivWater3, otherCivFood3, otherCivPop, otherCivPop2, otherCivPop3, run, population, otherCivCurrency, otherCivCurrency2, otherCivCurrency3, otherCivAge, otherCivAge2, otherCivAge3

	count += 1

	if expansion == True :
		if run == True :
			run = False
			otherCivPop = rand.randint(population - 45,population + 45)
			otherCivPop2 = rand.randint(population - 45,population + 45)
			otherCivPop3 = rand.randint(population - 45,population + 45)
			otherCivAge = rand.randint(-20,20)
			otherCivAge2 = rand.randint(-25,25)
			otherCivAge3 = rand.randint(-15,15)
		if count >= 3 :
			otherCivFood = int(round((rand.randint((food * rand.randint(7,10)),(food * rand.randint(11,15)))) / 10, 0))
			otherCivWater = int(round((rand.randint((water * rand.randint(7,10)),(water * rand.randint(11,15)))) / 10, 0))
			otherCivWood = int(round((rand.randint((wood * rand.randint(7,10)),(wood * rand.randint(11,15)))) / 10, 0))
			otherCivFarms = int(round((rand.randint((farms * rand.randint(7,10)),(farms * rand.randint(11,15)))) / 10, 0))
			otherCivHouses = int(round((rand.randint((houses * rand.randint(7,10)),(houses * rand.randint(11,15)))) / 10, 0))
			otherCivRock = int(round((rand.randint((rock * rand.randint(7,10)),(rock * rand.randint(11,15)))) / 10, 0))

			otherCivFood2 = int(round((rand.randint((food * rand.randint(6,11)),(food * rand.randint(10,16)))) / 10, 0))
			otherCivWater2 = int(round((rand.randint((water * rand.randint(6,11)),(water * rand.randint(10,16)))) / 10, 0))
			otherCivWood2 = int(round((rand.randint((wood * rand.randint(6,11)),(wood * rand.randint(10,16)))) / 10, 0))
			otherCivFarms2 = int(round((rand.randint((farms * rand.randint(6,11)),(farms * rand.randint(10,16)))) / 10, 0))
			otherCivHouses2 = int(round((rand.randint((houses * rand.randint(6,11)),(houses * rand.randint(10,16)))) / 10, 0))
			otherCivRock2 = int(round((rand.randint((rock * rand.randint(6,11)),(rock * rand.randint(10,16)))) / 10, 0))

			otherCivFood3 = int(round((rand.randint((food * rand.randint(8,9)),(food * rand.randint(12,14)))) / 10, 0))
			otherCivWater3 = int(round((rand.randint((water * rand.randint(8,9)),(water * rand.randint(12,14)))) / 10, 0))
			otherCivWood3 = int(round((rand.randint((wood * rand.randint(8,9)),(wood * rand.randint(12,14)))) / 10, 0))
			otherCivFarms3 = int(round((rand.randint((farms * rand.randint(8,9)),(farms * rand.randint(12,14)))) / 10, 0))
			otherCivHouses3 = int(round((rand.randint((houses * rand.randint(8,9)),(houses * rand.randint(12,14)))) / 10, 0))
			otherCivRock3 = int(round((rand.randint((rock * rand.randint(8,9)),(rock * rand.randint(12,14)))) / 10, 0))

			randomizer = rand.randint(1,3)
			if randomizer == 1 :
				otherCivCurrency += math.floor(otherCivCurrency * .1)
			elif randomizer == 2 :
				otherCivCurrency -= math.floor(otherCivCurrency * .13)
			randomizer = rand.randint(1,3)
			if randomizer == 1 :
				otherCivCurrency2 += math.floor(otherCivCurrency2 * .1)
			elif randomizer == 2 :
				otherCivCurrency2 -= math.floor(otherCivCurrency2 * .13)
			randomizer = rand.randint(1,3)
			if randomizer == 1 :
				otherCivCurrency3 += math.floor(otherCivCurrency3 * .1)
			elif randomizer == 2 :
				otherCivCurrency3 -= math.floor(otherCivCurrency3 * .13)

			count = 0

		randomizer = rand.randint(1,3)
		if randomizer == 1 :
			otherCivPop += math.floor(otherCivPop * .1)
		elif randomizer == 2 :
			otherCivPop -= math.floor(otherCivPop * .13)
		randomizer = rand.randint(1,3)
		if randomizer == 1 :
			otherCivPop2 += math.floor(otherCivPop2 * .1)
		elif randomizer == 2 :
			otherCivPop2 -= math.floor(otherCivPop2 * .13)
		randomizer = rand.randint(1,3)
		if randomizer == 1 :
			otherCivPop3 += math.floor(otherCivPop3 * .1)
		elif randomizer == 2 :
			otherCivPop3 -= math.floor(otherCivPop3 * .13)

		otherCivAge += 1
		otherCivAge2 += 1
		otherCivAge3 += 1
		
#Display information about other civs
def displayExpansion() :

	if expansion == True :
		print("\n===============================================")
		
		print("Kingdom of",otherCivName,"      Age:",otherCivAge,"\n")
		print("Leader of",otherCivName+":",otherCivLeader)
		print("Population:", otherCivPop,"\nCurrency:",otherCivCurrency,"\nFood:",otherCivFood, "\nWater:", otherCivWater,"\nWood:",otherCivWood, "\nFarms:", otherCivFarms, "\nHouses:", otherCivHouses, "\nRock:", otherCivRock,"\n")
		print("===============================================")
		
		print("Kingdom of",otherCivName2,"      Age:",otherCivAge2,"\n")
		print("Leader of",otherCivName2+":",otherCivLeader2)
		print("Population:", otherCivPop2,"\nCurrency:",otherCivCurrency2,"\nFood:",otherCivFood2, "\nWater:", otherCivWater2,"\nWood:",otherCivWood2, "\nFarms:", otherCivFarms2, "\nHouses:", otherCivHouses2, "\nRock:", otherCivRock2,"\n")
		print("===============================================")

		print("Kingdom of",otherCivName3,"      Age:",otherCivAge3,"\n")
		print("Leader of",otherCivName3+":",otherCivLeader3)
		print("Population:",otherCivPop3,"\nCurrency:",otherCivCurrency3,"\nFood:",otherCivFood3,"\nWater:",otherCivWater3,"\nWood:",otherCivWood3, "\nFarms:", otherCivFarms3, "\nHouses:", otherCivHouses3, "\nRock:", otherCivRock3,"\n")
		print("===============================================\n")

#Creates the UI used for managing the professions of your civilization
def jobManager() :
	global hiddenPopulation, discoverers, farmers, waterers, soldiers, population
	
	inLoop = True
	while inLoop == True :

		professions = discoverers + farmers + waterers + soldiers
		hiddenPopulation = population - professions
		print("--------------------------------------")
		print("Total Population:",population, "\nUnemployed Population:", hiddenPopulation,"\n")
		if corn == True and farmer == False and expansion == False :
			print("Discoverers:",discoverers)
			print("Waterers:",waterers,"\n")
		elif farmer == True and expansion == False :
			print("Discoverers:",discoverers)
			print("Waterers:",waterers)
			print("Farmers:",farmers,"\n")			
		elif expansion == True :
			print("Discoverers:",discoverers)
			print("Waterers:",waterers)
			print("Farmers:",farmers)
			print("Soldiers:",soldiers,"\n")
		else :
			print("Discoverers:",discoverers,"\n")
		inLoop2 = True
		while inLoop2 == True :

			action = input("Would you like to rearrange some of your people? Y/N:\n")
			action = action.lower()
			if action == "y" :
				inLoop3 = True
				while inLoop3 == True :

					inLoop = False
					statement = "What people would you like to change? (type 'help' for discription of each profession) :\n|1. Discoverers"
					if corn == True and farmer == False and expansion == False :
						print(statement)
						action = input("|2. Waterers\n")
					elif farmer == True and expansion == False :
						print(statement)
						action = input("|2. Waterers\n|3. Farmers\n")
					elif expansion == True :
						print(statement)
						action = input("|2. Waterers\n|3. Farmers\n|4. Soldiers\n")
					else :
						action = input(statement)
					action.lower()

					if action == "1" or action == "discoverers" :
						possibleDiscoverers = hiddenPopulation + discoverers
						print("How many people would you like to be discoverers? Max:",possibleDiscoverers)
						try:
							action = int(input("Please type a valid number:\n"))
						except:
							print("That is not an option!")
							continue
						if action <= possibleDiscoverers and action >= 0 :
							discoverers = action
							inLoop3 = False
						else :
							print("You are unable to do this action!")	

					elif action == "2" or action == "waterers" :
						possibleWaterers = hiddenPopulation + waterers
						print("How many people would you like to be waterers? Max:",possibleWaterers)
						try:
							action = int(input("Please type a valid number:\n"))
						except:
							print("That is not an option!")
							continue
						if action <= possibleWaterers and action >= 0 :
							waterers = action
							inLoop3 = False
						else :
							print("You are unable to do this action!")	

					elif action == "3" or action == "farmers" :
						possibleFarmers = hiddenPopulation + farmers
						print("How many people would you like to be farmers? Max:",possibleFarmers)
						try:
							action = int(input("Please type a valid number:\n"))
						except:
							print("That is not an option!")
							continue
						if action <= possibleFarmers and action >= 0 :
							farmers = action
							inLoop3 = False
						else :
							print("You are unable to do this action!")	

					elif action == "4" or action == "soldiers" :
						possibleSoldiers = hiddenPopulation + soldiers
						print("How many people would you like to be soldiers? Max:",possibleSoldiers)
						try:
							action = int(input("Please type a valid number:\n"))
						except:
							print("That is not an option!")
							continue
						if action <= possibleSoldiers and action >= 0 :
							soldiers = action
							inLoop3 = False
						else :
							print("You are unable to do this action!")
					
					elif action == "help" :
						print("\n\nDiscoverers: These guys use 1 wood and 1 rock per discoverer every year, but in return you gain discovery points which are crucial for unlocking future technologies.\n\nWaterers: They provide the benefit of using less water on your farms, and decreasing the amount of water your people consume; the benefit of this profession depends on the amount of them that you have.\n\nFarmers: Are extremely useful for more efficient food production, as they increase the output of food from farms depending on the amount of farmers that you have.\n\nSoldiers: Unfortunately they do not provide any direct benefits or bonuses, but when attempting to war with another civilization they are essential.\n\n")

					else :
						print("That is not an option!")

					professions = discoverers + farmers + waterers + soldiers
					hiddenPopulation = population - professions

			elif action == "n" :
				inLoop = False
				inLoop2 = False
			else :
				print("That's not an option!")

#Determines whether or not people died during the process of going from one year to the next
def didPeopleDie() :
	if population < prevPop :
		return True
	else :
		return False

#Contains the technology path for the entirety of the game
def techTree() :
	global discPointsRemaining, discoverers, cornAmt, housingAmt, ironAmt, technology, corn, age, techListPre, housing, iron, glass, glassAmt, extHeatAmt, extHeat, copperAmt, bronzeAmt, copper, bronze, translationAmt, translation, expansionAmt, currency, expansion, techList, changeP, farmerAmt, farmer, leader, leaderAmt, waterers, soldiers

	#needed to start research at age 15
	if age > 15 :
		
		#if discoverers are 1 or less then do this
		if discoverers <= 1 :
			for item in techListPre :
					item -= 1
					item -= changeP
					techList.append(item)
		#if discoverers are greater than 1 do this
		else:
			#subtracts the amount of research needed to complete a technology
			if len(techList) > 0 :
				techListPre = techList
				techList = []
			for item in techListPre :
				item -= discoverers
				item -= changeP
				techList.append(item)

		changeP = 0		
		cornAmt = techList[0]
		housingAmt = cornAmt + 25
		ironAmt = housingAmt + 30
		farmerAmt = ironAmt + 15
		glassAmt = farmerAmt + 35
		extHeatAmt = glassAmt + 25
		copperAmt = extHeatAmt + 25
		bronzeAmt = copperAmt + 25
		translationAmt = bronzeAmt + 30
		leaderAmt = translationAmt + 20
		expansionAmt = leaderAmt + 60

		#chain of if statements used for executing one-time commands that happen when the specific technology is discovered

		if cornAmt <= 0 and corn == False :
			technology.append("corn")
			corn = True
			print("We have just discovered corn and have created a new job, waterers. This should increase our food and water gathering tremendously!")

		if housingAmt <= 0 and housing == False :
			technology.append("housing")
			housing = True
			print("We have just discovered how to build houses. Since we are inside more this should decrease our food and water use!")
			
		if ironAmt <= 0 and iron == False :
			technology.append("iron")
			iron = True
			print("We have just discovered iron. This new resource should improve our tools and our resource output!")

		if farmerAmt <= 0 and farmer == False :
			technology.append("farmer")
			farmer = True
			print("We have just created a new profession, farmers. This new profession will increase the amount of output that farms create!")

		if glassAmt <= 0 and glass == False :
			technology.append("glass")
			glass = True
			print("We have just discovered glass. This new resource should improve our homes and allow us to be happier and thus consume less resources!")

		if extHeatAmt <= 0 and extHeat == False :
			technology.append("extreme heat")
			extHeat = True
			print("We have just discovered extreme heat. This new technique allows us to create complex alloys from different metals! This is a big one!")
		
		if copperAmt <= 0 and copper == False :
			technology.append("copper")
			copper = True
			print("We have just discovered copper. This new resource is vital for creating bronze, which is very important!")

		if bronzeAmt <= 0 and bronze == False :
			technology.append("bronze")
			bronze = True
			print("We have just discovered bronze. This new is very valuable and coveted by others! They will come...")

		if translationAmt <= 0 and translation == False :
			technology.append("translation")
			translation = True
			print("We have just discovered translation. This new understanding of language will allow your people to communicate with others on a whole new level.")

		if leaderAmt <= 0 and leader == False :
			technology.append("leader")
			leader = True
			print("We have just elected our first leader! This new profession will give bonuses depending on what strengths your leader has.")
			leaderElection()

		if expansionAmt <= 0 and expansion == False :
			currency = age
			technology.append("expansion")
			expansion = True
			print("We have just discovered that there are other civilizations! This could be good or possibly terrible...")
		
		#if techList is greater than 0, then decides the next tech to be discovered
		if len(techList) > 0 :
			discPointsRemaining = min(techList)
			while discPointsRemaining <= 0 :
				techList.pop(0)
				if len(techList) > 0 :
					discPointsRemaining = min(techList)
				else :
					discPointsRemaining = 1
					print("You've completed the tech tree!")
			techList = techListPre
		else :
			print("You've completed the tech tree!")

		techListPre = [cornAmt,housingAmt,ironAmt,farmerAmt,glassAmt,extHeatAmt,copperAmt,bronzeAmt,translationAmt,leaderAmt,expansionAmt]
		techList = []

#Updates the amount of discovery points needed for the next technology upgrade (also subtracts the needed wood and rock)
def updateDiscResources() :
	global rock, wood

	if wood >= discoverers and rock >= discoverers :
		wood -= discoverers
		rock -= discoverers
		techTree()
	elif wood < discoverers and rock < discoverers :
		print("You do not have enough wood and rock to continue discovering.")
	elif wood < discoverers :
		print("You do not have enough wood to continue discovering.")
	elif rock < discoverers :
		print("You do not have enough rock to continue discovering.")
	
#Checks for the food and water problems and if none subracts food and water equal to the population
def foodWater() :
	global population, food, water, houses, corn, housing, glass, modifierF,modifierW

	if corn == True :
		modifierF -= .05
	if housing == True :
		if houses >= 15 :
			modifierF -= .15
			modifierW -= .15
		else :
			modifierF -= houses * .01
			modifierW -= houses * .01
	if glass == True :
		modifierF -= .15
		modifierW -= .15
	
	if food < population or water < population:
		if food > water :
			population = water
			water = 0
			food -= int(math.ceil(population * modifierF))
		elif food < water :
			population = food
			food = 0		
			water -= int(math.floor(math.floor(population/2 * modifierW)) - (waterers * (1 - modifierW)))
		else :
			population = water
			water = 0
			food = 0
	else :
		water -= int(math.floor(math.floor(population/2 * modifierW)) - (waterers * (1 - modifierW)))
		food -= int(math.ceil(population * modifierF))

#Handles adding the food and subtracting the water for farms
def farmsProduction() :
	global farms, food, water,farmers
	
	if farms > 0 and water > 0:
		
		if water > farms :
			water -= farms
			if farmers >= 1:
				food += math.ceil(farmers * (.5 * farms))
			if waterTunnels == True and corn == True :
				food += math.floor(farms * 2)
			elif (waterTunnels == True or corn == True) and (waterTunnels == False or corn == False) :
				food += math.floor(farms * 1.5)
			else :
				food += farms

#Controls the process of creating a number of farms 0-3
def makeFarms() :
	global farms, wood, water, actions

	amtOfFarms = input("How many farms would you like? Farms cost 3 wood and 1 water. 3 max (0 is an option):\n")
	try:
		for theNumber in list(range(0,4)) :
			if (" " + str(theNumber) + " ") in (" " + amtOfFarms + " ") :
				amtOfFarmsInt = theNumber
				amtOfFarmsInt = int(amtOfFarmsInt)
				amtOfFarms = amtOfFarmsInt
	except:
		amtOfFarmsInt = int(amtOfFarmsInt)

	amtOfWood = amtOfFarms * 3
	amtOfWater = amtOfFarms
	try:

		if amtOfWood <= wood and amtOfWater <= water :
			farms += amtOfFarms
			wood -= amtOfWood
			water -= amtOfWater
		else:
			actions += 1
			print("not enough resources")
	except:
		print("Not a valid number of farms for one action!!\n------------------------")
		actions += 1
	
	if amtOfFarms == 0 :
		actions += 1

#Allows the player to make a number of houses 0-3
def makeHouse() :
	global rock, wood, actions, houses

	housesBeingBuilt = input("How many houses would you like to build? Houses cost 5 wood and 5 rock. Max 3 (0 is an option):\n")
	try:
		for theNumber in list(range(0,4)) :
			if (" " + str(theNumber) + " ") in (" " + housesBeingBuilt + " ") :
				housesBeingBuiltInt = theNumber
				housesBeingBuiltInt = int(housesBeingBuiltInt)
				housesBeingBuilt = housesBeingBuiltInt
	except:
		housesBeingBuiltInt = int(housesBeingBuiltInt)

	amtOfWood = housesBeingBuilt * 5
	amtOfRock = housesBeingBuilt * 5

	try:
		if amtOfWood <= wood and amtOfRock <= rock :
			houses += housesBeingBuilt
			wood -= amtOfWood
			rock -= amtOfRock
		else:
			actions += 1
			print("You don't have enough resources...")	
	except:
			print("Not a valid number of Houses for one action!!\n------------------------")
			actions += 1

	if housesBeingBuilt == 0 :
		actions += 1
	
#Describes stats and useful information about your civilization
def surroundings() :

	if expansion == True :
		print("===================EXPANSION===================\n")
		print("Civilization Age:",age,"          Currency:",currency,"\n")
		print("Current Boss Man:",ldrName)
		print("Total Population:",population)
		print("Amount of Food:",food)
		print("Amount of Water:",water)
		print("Amount of Trees:",trees)
		print("Amount of Wood:",wood)
		if farms > 0 :
			print("Amount of Farms:",farms)
		if houses > 0 :
			print("Amount of Houses:",houses)
		if age > 3 :
			print("Amount of Rock:",rock)
		if age > 14 :
			print("Amount of Discovery Points Until Next Technology:",discPointsRemaining)
		if len(technology) > 0 :
			print("Latest Technology:")
			print("-",technology[-1])
		print("\n===============================================\n")
	else :
		print("Year",age)
		if leader == True and age > 1:
			print("Current Boss Man:",ldrName)
		print("Total Population:",population)
		print("Amount of Food:",food)
		print("Amount of Water:",water)
		print("Amount of Trees:",trees)
		print("Amount of Wood:",wood)
		if farms > 0 :
			print("Amount of Farms:",farms)
		if houses > 0 :
			print("Amount of Houses:",houses)
		if age > 3 :
			print("Amount of Rock:",rock)
		if age > 14 :
			print("Amount of Discovery Points Until Next Technology:",discPointsRemaining)
		if len(technology) > 0 :
			print("Latest Technology:")
			print("-",technology[-1])

#Adds the appropriate amount of people each year
def populationGain() :
	global population, food, water

	if food > population and water > population :
		if population >= 30 and population < 60 :
			population += math.floor(population/2.5)
		elif population >= 60 and population < 120 :
			population += math.floor(population/3)
		elif population >= 120 and population < 240 :
			population += math.floor(population/3.5)
		elif population >= 240 and population < 480 :
			population += math.floor(population/4)
		elif population >= 480 and population < 960 :
			population += math.floor(population/4.5)
		elif population >= 960 and population < 1920 :
			population += math.floor(population/5)
		elif population >= 1920 and population < 3840 :
			population += math.floor(population/5.5)
		elif population >= 3840 and population < 7680 :
			population += math.floor(population/6)
		elif population >= 7680 and population < 15360 :
			population += math.floor(population/6.5)
		elif population >= 15360 and population < 30920 :
			population += math.floor(population/7)
		else :
			population += math.floor(population/2)

	if population == 1 :
		population = 2
		print("A guy has decided that you are a good human to hang out with")

#Saves all current game data
def save() :
	global age,food,trees,water,wood,rock,population,discoverers,farms,houses,hiddenPopulation,discPointsRemaining,pickaxe,waterPit,waterTunnels,corn,housing,iron,glass,extHeat,copper,bronze,translation,techList,techListPre,cornAmt,housingAmt,ironAmt,glassAmt,extHeatAmt,copperAmt,bronzeAmt,translationAmt,technology,gameOn,ageUpdate,expansion,expansionAmt,currency,save1,save2,save3,save4,save5,action,farmer,farmers,farmerAmt,leader,leaderAmt,ldrName,ldrStrength,ldrIntellect,ldrDiplomacy,ldrSocials,prevPop,waterers, otherCivRock, otherCivHouses, otherCivFarms, otherCivWood, otherCivWater, otherCivFood, count, otherCivRock2, otherCivHouses2, otherCivFarms2, otherCivWood2, otherCivWater2, otherCivFood2, otherCivRock3, otherCivHouses3, otherCivFarms3, otherCivWood3, otherCivWater3, otherCivFood3, otherCivPop, otherCivPop2, otherCivPop3, run, population, otherCivCurrency, otherCivCurrency2, otherCivCurrency3, otherCivAge, otherCivAge2, otherCivAge3, otherCivName, otherCivName2, otherCivName3, otherCivLeader, otherCivLeader2, otherCivLeader3
	try :
		save1 = pickle.load(open("civGameSaveName1.dat", "rb"))
	except :
		save1 = "Empty"
	try :
		save2 = pickle.load(open("civGameSaveName2.dat", "rb"))
	except :
		save2 = "Empty"
	try :
		save3 = pickle.load(open("civGameSaveName3.dat", "rb"))
	except :
		save3 = "Empty"
	try :
		save4 = pickle.load(open("civGameSaveName4.dat", "rb"))
	except :
		save4 = "Empty"
	try :
		save5 = pickle.load(open("civGameSaveName5.dat", "rb"))
	except :
		save5 = "Empty"

	savesList = [save1,save2,save3,save4,save5]
	i = 0
	for item in savesList :
		i += 1
		print(str(i)+")",item)
	while gameOn == True :
		action1 = input("Which save would you like to overwrite? (Type a number):\n>> ")
		if action1 == "1" :
			pickle.dump(age, open("civGameAge.dat", "wb"))
			pickle.dump(food, open("civGameFood.dat", "wb"))
			pickle.dump(trees, open("civGameTrees.dat", "wb"))
			pickle.dump(water, open("civGameWater.dat", "wb"))
			pickle.dump(wood, open("civGameWood.dat", "wb"))
			pickle.dump(rock, open("civGameRock.dat", "wb"))
			pickle.dump(population, open("civGamePop.dat", "wb"))
			pickle.dump(discoverers, open("civGameDiscoverers.dat", "wb"))
			pickle.dump(farms, open("civGameFarms.dat", "wb"))
			pickle.dump(houses, open("civGameHouses.dat", "wb"))
			pickle.dump(hiddenPopulation, open("civGameHidPop.dat", "wb"))
			pickle.dump(discPointsRemaining, open("civGameDiscPR.dat", "wb"))
			pickle.dump(pickaxe, open("civGamePickaxe.dat", "wb"))
			pickle.dump(waterPit, open("civGameWaterPit.dat", "wb"))
			pickle.dump(waterTunnels, open("civGameWaterT.dat", "wb"))
			pickle.dump(corn, open("civGameCorn.dat", "wb"))
			pickle.dump(housing, open("civGameHousing.dat", "wb"))
			pickle.dump(iron, open("civGameIron.dat", "wb"))
			pickle.dump(glass, open("civGameGlass.dat", "wb"))
			pickle.dump(extHeat, open("civGameExtHeat.dat", "wb"))
			pickle.dump(copper, open("civGameCopper.dat", "wb"))
			pickle.dump(bronze, open("civGameBronze.dat", "wb"))
			pickle.dump(translation, open("civGameTranslation.dat", "wb"))
			pickle.dump(techList, open("civGameTechList.dat", "wb"))
			pickle.dump(techListPre, open("civGameTechListPre.dat", "wb"))
			pickle.dump(cornAmt, open("civGameCornAmt.dat", "wb"))
			pickle.dump(housingAmt, open("civGameHousingAmt.dat", "wb"))
			pickle.dump(ironAmt, open("civGameIronAmt.dat", "wb"))
			pickle.dump(glassAmt, open("civGameGlassAmt.dat", "wb"))
			pickle.dump(extHeatAmt, open("civGameExtHeatAmt.dat", "wb"))
			pickle.dump(copperAmt, open("civGameCopperAmt.dat", "wb"))
			pickle.dump(bronzeAmt, open("civGameBronzeAmt.dat", "wb"))
			pickle.dump(translationAmt, open("civGameTranslationAmt.dat", "wb"))
			pickle.dump(technology, open("civGameTechnology.dat", "wb"))
			pickle.dump(gameOn, open("civGameGameOn.dat", "wb"))
			pickle.dump(ageUpdate, open("civGameAgeUpdate.dat", "wb"))
			pickle.dump(expansion, open("civGameExpansion.dat", "wb"))
			pickle.dump(expansionAmt, open("civGameExpansionAmt.dat", "wb"))
			pickle.dump(currency, open("civGameCurrency.dat", "wb"))
			pickle.dump(farmer, open("civGameFarmer.dat", "wb"))
			pickle.dump(farmers, open("civGameFarmers.dat", "wb"))
			pickle.dump(farmerAmt, open("civGameFarmerAmt.dat", "wb"))
			pickle.dump(leader, open("civGameLeader.dat", "wb"))
			pickle.dump(leaderAmt, open("civGameLeaderAmt.dat", "wb"))
			pickle.dump(ldrName, open("civGameldrName.dat", "wb"))
			pickle.dump(ldrStrength, open("civGameldrStrength.dat", "wb"))
			pickle.dump(ldrIntellect, open("civGameldrIntellect.dat", "wb"))
			pickle.dump(ldrDiplomacy, open("civGameldrDiplomacy.dat", "wb"))
			pickle.dump(ldrSocials, open("civGameldrSocials.dat", "wb"))
			pickle.dump(prevPop, open("civGameprevPop.dat", "wb"))
			pickle.dump(waterers, open("civGameWaterers.dat", "wb"))
			pickle.dump(otherCivRock, open("civGameotherCivRock.dat", "wb"))
			pickle.dump(otherCivHouses, open("civGameotherCivHouses.dat", "wb"))
			pickle.dump(otherCivFarms, open("civGameotherCivFarms.dat", "wb"))
			pickle.dump(otherCivWood, open("civGameotherCivWood.dat", "wb"))
			pickle.dump(otherCivWater, open("civGameotherCivWater.dat", "wb"))
			pickle.dump(otherCivFood, open("civGameotherCivFood.dat", "wb"))
			pickle.dump(count, open("civGamecount.dat", "wb"))
			pickle.dump(otherCivRock2, open("civGameotherCivRock2.dat", "wb"))
			pickle.dump(otherCivHouses2, open("civGameotherCivHouses2.dat", "wb"))
			pickle.dump(otherCivFarms2, open("civGameotherCivFarms2.dat", "wb"))
			pickle.dump(otherCivWood2, open("civGameotherCivWood2.dat", "wb"))
			pickle.dump(otherCivWater2, open("civGameotherCivWater2.dat", "wb"))
			pickle.dump(otherCivFood2, open("civGameotherCivFood2.dat", "wb"))
			pickle.dump(otherCivRock3, open("civGameotherCivRock3.dat", "wb"))
			pickle.dump(otherCivHouses3, open("civGameotherCivHouses3.dat", "wb"))
			pickle.dump(otherCivFarms3, open("civGameotherCivFarms3.dat", "wb"))
			pickle.dump(otherCivWood3, open("civGameotherCivWood3.dat", "wb"))
			pickle.dump(otherCivWater3, open("civGameotherCivWater3.dat", "wb"))
			pickle.dump(otherCivFood3, open("civGameotherCivFood3.dat", "wb"))
			pickle.dump(otherCivPop, open("civGameotherCivPop.dat", "wb"))
			pickle.dump(otherCivPop2, open("civGameotherCivPop2.dat", "wb"))
			pickle.dump(otherCivPop3, open("civGameotherCivPop3.dat", "wb"))
			pickle.dump(run, open("civGamerun.dat", "wb"))
			pickle.dump(otherCivCurrency, open("civGameotherCivCurrency.dat", "wb"))
			pickle.dump(otherCivCurrency2, open("civGameotherCivCurrency2.dat", "wb"))
			pickle.dump(otherCivCurrency3, open("civGameotherCivCurrency3.dat", "wb"))
			pickle.dump(otherCivAge, open("civGameotherCivAge.dat", "wb"))
			pickle.dump(otherCivAge2, open("civGameotherCivAge2.dat", "wb"))
			pickle.dump(otherCivAge3, open("civGameotherCivAge3.dat", "wb"))
			pickle.dump(otherCivName, open("civGameotherCivName.dat", "wb"))
			pickle.dump(otherCivName2, open("civGameotherCivName2.dat", "wb"))
			pickle.dump(otherCivName3, open("civGameotherCivName3.dat", "wb"))
			pickle.dump(otherCivLeader, open("civGameotherCivLeader.dat", "wb"))
			pickle.dump(otherCivLeader2, open("civGameotherCivLeader2.dat", "wb"))
			pickle.dump(otherCivLeader3, open("civGameotherCivLeader3.dat", "wb"))
			gameOn = False
		
		elif action1 == "2" :
			pickle.dump(age, open("civGameAge2.dat", "wb"))
			pickle.dump(food, open("civGameFood2.dat", "wb"))
			pickle.dump(trees, open("civGameTrees2.dat", "wb"))
			pickle.dump(water, open("civGameWater2.dat", "wb"))
			pickle.dump(wood, open("civGameWood2.dat", "wb"))
			pickle.dump(rock, open("civGameRock2.dat", "wb"))
			pickle.dump(population, open("civGamePop2.dat", "wb"))
			pickle.dump(discoverers, open("civGameDiscoverers2.dat", "wb"))
			pickle.dump(farms, open("civGameFarms2.dat", "wb"))
			pickle.dump(houses, open("civGameHouses2.dat", "wb"))
			pickle.dump(hiddenPopulation, open("civGameHidPop2.dat", "wb"))
			pickle.dump(discPointsRemaining, open("civGameDiscPR2.dat", "wb"))
			pickle.dump(pickaxe, open("civGamePickaxe2.dat", "wb"))
			pickle.dump(waterPit, open("civGameWaterPit2.dat", "wb"))
			pickle.dump(waterTunnels, open("civGameWaterT2.dat", "wb"))
			pickle.dump(corn, open("civGameCorn2.dat", "wb"))
			pickle.dump(housing, open("civGameHousing2.dat", "wb"))
			pickle.dump(iron, open("civGameIron2.dat", "wb"))
			pickle.dump(glass, open("civGameGlass2.dat", "wb"))
			pickle.dump(extHeat, open("civGameExtHeat2.dat", "wb"))
			pickle.dump(copper, open("civGameCopper2.dat", "wb"))
			pickle.dump(bronze, open("civGameBronze2.dat", "wb"))
			pickle.dump(translation, open("civGameTranslation2.dat", "wb"))
			pickle.dump(techList, open("civGameTechList2.dat", "wb"))
			pickle.dump(techListPre, open("civGameTechListPre2.dat", "wb"))
			pickle.dump(cornAmt, open("civGameCornAmt2.dat", "wb"))
			pickle.dump(housingAmt, open("civGameHousingAmt2.dat", "wb"))
			pickle.dump(ironAmt, open("civGameIronAmt2.dat", "wb"))
			pickle.dump(glassAmt, open("civGameGlassAmt2.dat", "wb"))
			pickle.dump(extHeatAmt, open("civGameExtHeatAmt2.dat", "wb"))
			pickle.dump(copperAmt, open("civGameCopperAmt2.dat", "wb"))
			pickle.dump(bronzeAmt, open("civGameBronzeAmt2.dat", "wb"))
			pickle.dump(translationAmt, open("civGameTranslationAmt2.dat", "wb"))
			pickle.dump(technology, open("civGameTechnology2.dat", "wb"))
			pickle.dump(gameOn, open("civGameGameOn2.dat", "wb"))
			pickle.dump(ageUpdate, open("civGameAgeUpdate2.dat", "wb"))
			pickle.dump(expansion, open("civGameExpansion2.dat", "wb"))
			pickle.dump(expansionAmt, open("civGameExpansionAmt2.dat", "wb"))
			pickle.dump(currency, open("civGameCurrency2.dat", "wb"))
			pickle.dump(farmer, open("civGameFarmer2.dat", "wb"))
			pickle.dump(farmers, open("civGameFarmers2.dat", "wb"))
			pickle.dump(farmerAmt, open("civGameFarmerAmt2.dat", "wb"))
			pickle.dump(leader, open("civGameLeader2.dat", "wb"))
			pickle.dump(leaderAmt, open("civGameLeaderAmt2.dat", "wb"))
			pickle.dump(ldrName, open("civGameldrName2.dat", "wb"))
			pickle.dump(ldrStrength, open("civGameldrStrength2.dat", "wb"))
			pickle.dump(ldrIntellect, open("civGameldrIntellect2.dat", "wb"))
			pickle.dump(ldrDiplomacy, open("civGameldrDiplomacy2.dat", "wb"))
			pickle.dump(ldrSocials, open("civGameldrSocials2.dat", "wb"))
			pickle.dump(prevPop, open("civGameprevPop2.dat", "wb"))
			pickle.dump(waterers, open("civGameWaterers2.dat", "wb"))
			pickle.dump(otherCivRock, open("civGameotherCivRock2.dat", "wb"))
			pickle.dump(otherCivHouses, open("civGameotherCivHouses2.dat", "wb"))
			pickle.dump(otherCivFarms, open("civGameotherCivFarms2.dat", "wb"))
			pickle.dump(otherCivWood, open("civGameotherCivWood2.dat", "wb"))
			pickle.dump(otherCivWater, open("civGameotherCivWater2.dat", "wb"))
			pickle.dump(otherCivFood, open("civGameotherCivFood2.dat", "wb"))
			pickle.dump(count, open("civGamecount2.dat", "wb"))
			pickle.dump(otherCivRock2, open("civGameotherCivRock22.dat", "wb"))
			pickle.dump(otherCivHouses2, open("civGameotherCivHouses22.dat", "wb"))
			pickle.dump(otherCivFarms2, open("civGameotherCivFarms22.dat", "wb"))
			pickle.dump(otherCivWood2, open("civGameotherCivWood22.dat", "wb"))
			pickle.dump(otherCivWater2, open("civGameotherCivWater22.dat", "wb"))
			pickle.dump(otherCivFood2, open("civGameotherCivFood22.dat", "wb"))
			pickle.dump(otherCivRock3, open("civGameotherCivRock32.dat", "wb"))
			pickle.dump(otherCivHouses3, open("civGameotherCivHouses32.dat", "wb"))
			pickle.dump(otherCivFarms3, open("civGameotherCivFarms32.dat", "wb"))
			pickle.dump(otherCivWood3, open("civGameotherCivWood32.dat", "wb"))
			pickle.dump(otherCivWater3, open("civGameotherCivWater32.dat", "wb"))
			pickle.dump(otherCivFood3, open("civGameotherCivFood32.dat", "wb"))
			pickle.dump(otherCivPop, open("civGameotherCivPop2.dat", "wb"))
			pickle.dump(otherCivPop2, open("civGameotherCivPop22.dat", "wb"))
			pickle.dump(otherCivPop3, open("civGameotherCivPop32.dat", "wb"))
			pickle.dump(run, open("civGamerun2.dat", "wb"))
			pickle.dump(otherCivCurrency, open("civGameotherCivCurrency2.dat", "wb"))
			pickle.dump(otherCivCurrency2, open("civGameotherCivCurrency22.dat", "wb"))
			pickle.dump(otherCivCurrency3, open("civGameotherCivCurrency32.dat", "wb"))
			pickle.dump(otherCivAge, open("civGameotherCivAge2.dat", "wb"))
			pickle.dump(otherCivAge2, open("civGameotherCivAge22.dat", "wb"))
			pickle.dump(otherCivAge3, open("civGameotherCivAge32.dat", "wb"))
			pickle.dump(otherCivName, open("civGameotherCivName2.dat", "wb"))
			pickle.dump(otherCivName2, open("civGameotherCivName22.dat", "wb"))
			pickle.dump(otherCivName3, open("civGameotherCivName32.dat", "wb"))
			pickle.dump(otherCivLeader, open("civGameotherCivLeader2.dat", "wb"))
			pickle.dump(otherCivLeader2, open("civGameotherCivLeader22.dat", "wb"))
			pickle.dump(otherCivLeader3, open("civGameotherCivLeader32.dat", "wb"))
			gameOn = False	
		
		elif action1 == "3" :
			pickle.dump(age, open("civGameAge3.dat", "wb"))
			pickle.dump(food, open("civGameFood3.dat", "wb"))
			pickle.dump(trees, open("civGameTrees3.dat", "wb"))
			pickle.dump(water, open("civGameWater3.dat", "wb"))
			pickle.dump(wood, open("civGameWood3.dat", "wb"))
			pickle.dump(rock, open("civGameRock3.dat", "wb"))
			pickle.dump(population, open("civGamePop3.dat", "wb"))
			pickle.dump(discoverers, open("civGameDiscoverers3.dat", "wb"))
			pickle.dump(farms, open("civGameFarms3.dat", "wb"))
			pickle.dump(houses, open("civGameHouses3.dat", "wb"))
			pickle.dump(hiddenPopulation, open("civGameHidPop3.dat", "wb"))
			pickle.dump(discPointsRemaining, open("civGameDiscPR3.dat", "wb"))
			pickle.dump(pickaxe, open("civGamePickaxe3.dat", "wb"))
			pickle.dump(waterPit, open("civGameWaterPit3.dat", "wb"))
			pickle.dump(waterTunnels, open("civGameWaterT3.dat", "wb"))
			pickle.dump(corn, open("civGameCorn3.dat", "wb"))
			pickle.dump(housing, open("civGameHousing3.dat", "wb"))
			pickle.dump(iron, open("civGameIron3.dat", "wb"))
			pickle.dump(glass, open("civGameGlass3.dat", "wb"))
			pickle.dump(extHeat, open("civGameExtHeat3.dat", "wb"))
			pickle.dump(copper, open("civGameCopper3.dat", "wb"))
			pickle.dump(bronze, open("civGameBronze3.dat", "wb"))
			pickle.dump(translation, open("civGameTranslation3.dat", "wb"))
			pickle.dump(techList, open("civGameTechList3.dat", "wb"))
			pickle.dump(techListPre, open("civGameTechListPre3.dat", "wb"))
			pickle.dump(cornAmt, open("civGameCornAmt3.dat", "wb"))
			pickle.dump(housingAmt, open("civGameHousingAmt3.dat", "wb"))
			pickle.dump(ironAmt, open("civGameIronAmt3.dat", "wb"))
			pickle.dump(glassAmt, open("civGameGlassAmt3.dat", "wb"))
			pickle.dump(extHeatAmt, open("civGameExtHeatAmt3.dat", "wb"))
			pickle.dump(copperAmt, open("civGameCopperAmt3.dat", "wb"))
			pickle.dump(bronzeAmt, open("civGameBronzeAmt3.dat", "wb"))
			pickle.dump(translationAmt, open("civGameTranslationAmt3.dat", "wb"))
			pickle.dump(technology, open("civGameTechnology3.dat", "wb"))
			pickle.dump(gameOn, open("civGameGameOn3.dat", "wb"))
			pickle.dump(ageUpdate, open("civGameAgeUpdate3.dat", "wb"))
			pickle.dump(expansion, open("civGameExpansion3.dat", "wb"))
			pickle.dump(expansionAmt, open("civGameExpansionAmt3.dat", "wb"))
			pickle.dump(currency, open("civGameCurrency3.dat", "wb"))
			pickle.dump(farmer, open("civGameFarmer3.dat", "wb"))
			pickle.dump(farmers, open("civGameFarmers3.dat", "wb"))
			pickle.dump(farmerAmt, open("civGameFarmerAmt3.dat", "wb"))
			pickle.dump(leader, open("civGameLeader3.dat", "wb"))
			pickle.dump(leaderAmt, open("civGameLeaderAmt3.dat", "wb"))
			pickle.dump(ldrName, open("civGameldrName3.dat", "wb"))
			pickle.dump(ldrStrength, open("civGameldrStrength3.dat", "wb"))
			pickle.dump(ldrIntellect, open("civGameldrIntellect3.dat", "wb"))
			pickle.dump(ldrDiplomacy, open("civGameldrDiplomacy3.dat", "wb"))
			pickle.dump(ldrSocials, open("civGameldrSocials3.dat", "wb"))
			pickle.dump(prevPop, open("civGameprevPop3.dat", "wb"))
			pickle.dump(waterers, open("civGameWaterers3.dat", "wb"))
			pickle.dump(otherCivRock, open("civGameotherCivRock3.dat", "wb"))
			pickle.dump(otherCivHouses, open("civGameotherCivHouses3.dat", "wb"))
			pickle.dump(otherCivFarms, open("civGameotherCivFarms3.dat", "wb"))
			pickle.dump(otherCivWood, open("civGameotherCivWood3.dat", "wb"))
			pickle.dump(otherCivWater, open("civGameotherCivWater3.dat", "wb"))
			pickle.dump(otherCivFood, open("civGameotherCivFood3.dat", "wb"))
			pickle.dump(count, open("civGamecount3.dat", "wb"))
			pickle.dump(otherCivRock2, open("civGameotherCivRock23.dat", "wb"))
			pickle.dump(otherCivHouses2, open("civGameotherCivHouses23.dat", "wb"))
			pickle.dump(otherCivFarms2, open("civGameotherCivFarms23.dat", "wb"))
			pickle.dump(otherCivWood2, open("civGameotherCivWood23.dat", "wb"))
			pickle.dump(otherCivWater2, open("civGameotherCivWater23.dat", "wb"))
			pickle.dump(otherCivFood2, open("civGameotherCivFood23.dat", "wb"))
			pickle.dump(otherCivRock3, open("civGameotherCivRock33.dat", "wb"))
			pickle.dump(otherCivHouses3, open("civGameotherCivHouses33.dat", "wb"))
			pickle.dump(otherCivFarms3, open("civGameotherCivFarms33.dat", "wb"))
			pickle.dump(otherCivWood3, open("civGameotherCivWood33.dat", "wb"))
			pickle.dump(otherCivWater3, open("civGameotherCivWater33.dat", "wb"))
			pickle.dump(otherCivFood3, open("civGameotherCivFood33.dat", "wb"))
			pickle.dump(otherCivPop, open("civGameotherCivPop3.dat", "wb"))
			pickle.dump(otherCivPop2, open("civGameotherCivPop23.dat", "wb"))
			pickle.dump(otherCivPop3, open("civGameotherCivPop33.dat", "wb"))
			pickle.dump(run, open("civGamerun3.dat", "wb"))
			pickle.dump(otherCivCurrency, open("civGameotherCivCurrency3.dat", "wb"))
			pickle.dump(otherCivCurrency2, open("civGameotherCivCurrency23.dat", "wb"))
			pickle.dump(otherCivCurrency3, open("civGameotherCivCurrency33.dat", "wb"))
			pickle.dump(otherCivAge, open("civGameotherCivAge3.dat", "wb"))
			pickle.dump(otherCivAge2, open("civGameotherCivAge23.dat", "wb"))
			pickle.dump(otherCivAge3, open("civGameotherCivAge33.dat", "wb"))
			pickle.dump(otherCivName, open("civGameotherCivName3.dat", "wb"))
			pickle.dump(otherCivName2, open("civGameotherCivName23.dat", "wb"))
			pickle.dump(otherCivName3, open("civGameotherCivName33.dat", "wb"))
			pickle.dump(otherCivLeader, open("civGameotherCivLeader3.dat", "wb"))
			pickle.dump(otherCivLeader2, open("civGameotherCivLeader23.dat", "wb"))
			pickle.dump(otherCivLeader3, open("civGameotherCivLeader33.dat", "wb"))
			gameOn = False
		
		elif action1 == "4" :
			pickle.dump(age, open("civGameAge4.dat", "wb"))
			pickle.dump(food, open("civGameFood4.dat", "wb"))
			pickle.dump(trees, open("civGameTrees4.dat", "wb"))
			pickle.dump(water, open("civGameWater4.dat", "wb"))
			pickle.dump(wood, open("civGameWood4.dat", "wb"))
			pickle.dump(rock, open("civGameRock4.dat", "wb"))
			pickle.dump(population, open("civGamePop4.dat", "wb"))
			pickle.dump(discoverers, open("civGameDiscoverers4.dat", "wb"))
			pickle.dump(farms, open("civGameFarms4.dat", "wb"))
			pickle.dump(houses, open("civGameHouses4.dat", "wb"))
			pickle.dump(hiddenPopulation, open("civGameHidPop4.dat", "wb"))
			pickle.dump(discPointsRemaining, open("civGameDiscPR4.dat", "wb"))
			pickle.dump(pickaxe, open("civGamePickaxe4.dat", "wb"))
			pickle.dump(waterPit, open("civGameWaterPit4.dat", "wb"))
			pickle.dump(waterTunnels, open("civGameWaterT4.dat", "wb"))
			pickle.dump(corn, open("civGameCorn4.dat", "wb"))
			pickle.dump(housing, open("civGameHousing4.dat", "wb"))
			pickle.dump(iron, open("civGameIron4.dat", "wb"))
			pickle.dump(glass, open("civGameGlass4.dat", "wb"))
			pickle.dump(extHeat, open("civGameExtHeat4.dat", "wb"))
			pickle.dump(copper, open("civGameCopper4.dat", "wb"))
			pickle.dump(bronze, open("civGameBronze4.dat", "wb"))
			pickle.dump(translation, open("civGameTranslation4.dat", "wb"))
			pickle.dump(techList, open("civGameTechList4.dat", "wb"))
			pickle.dump(techListPre, open("civGameTechListPre4.dat", "wb"))
			pickle.dump(cornAmt, open("civGameCornAmt4.dat", "wb"))
			pickle.dump(housingAmt, open("civGameHousingAmt4.dat", "wb"))
			pickle.dump(ironAmt, open("civGameIronAmt4.dat", "wb"))
			pickle.dump(glassAmt, open("civGameGlassAmt4.dat", "wb"))
			pickle.dump(extHeatAmt, open("civGameExtHeatAmt4.dat", "wb"))
			pickle.dump(copperAmt, open("civGameCopperAmt4.dat", "wb"))
			pickle.dump(bronzeAmt, open("civGameBronzeAmt4.dat", "wb"))
			pickle.dump(translationAmt, open("civGameTranslationAmt4.dat", "wb"))
			pickle.dump(technology, open("civGameTechnology4.dat", "wb"))
			pickle.dump(gameOn, open("civGameGameOn4.dat", "wb"))
			pickle.dump(ageUpdate, open("civGameAgeUpdate4.dat", "wb"))
			pickle.dump(expansion, open("civGameExpansion4.dat", "wb"))
			pickle.dump(expansionAmt, open("civGameExpansionAmt4.dat", "wb"))
			pickle.dump(currency, open("civGameCurrency4.dat", "wb"))
			pickle.dump(farmer, open("civGameFarmer4.dat", "wb"))
			pickle.dump(farmers, open("civGameFarmers4.dat", "wb"))
			pickle.dump(farmerAmt, open("civGameFarmerAmt4.dat", "wb"))
			pickle.dump(leader, open("civGameLeader4.dat", "wb"))
			pickle.dump(leaderAmt, open("civGameLeaderAmt4.dat", "wb"))
			pickle.dump(ldrName, open("civGameldrName4.dat", "wb"))
			pickle.dump(ldrStrength, open("civGameldrStrength4.dat", "wb"))
			pickle.dump(ldrIntellect, open("civGameldrIntellect4.dat", "wb"))
			pickle.dump(ldrDiplomacy, open("civGameldrDiplomacy4.dat", "wb"))
			pickle.dump(ldrSocials, open("civGameldrSocials4.dat", "wb"))
			pickle.dump(prevPop, open("civGameprevPop4.dat", "wb"))
			pickle.dump(waterers, open("civGameWaterers4.dat", "wb"))
			pickle.dump(otherCivRock, open("civGameotherCivRock4.dat", "wb"))
			pickle.dump(otherCivHouses, open("civGameotherCivHouses4.dat", "wb"))
			pickle.dump(otherCivFarms, open("civGameotherCivFarms4.dat", "wb"))
			pickle.dump(otherCivWood, open("civGameotherCivWood4.dat", "wb"))
			pickle.dump(otherCivWater, open("civGameotherCivWater4.dat", "wb"))
			pickle.dump(otherCivFood, open("civGameotherCivFood4.dat", "wb"))
			pickle.dump(count, open("civGamecount4.dat", "wb"))
			pickle.dump(otherCivRock2, open("civGameotherCivRock24.dat", "wb"))
			pickle.dump(otherCivHouses2, open("civGameotherCivHouses24.dat", "wb"))
			pickle.dump(otherCivFarms2, open("civGameotherCivFarms24.dat", "wb"))
			pickle.dump(otherCivWood2, open("civGameotherCivWood24.dat", "wb"))
			pickle.dump(otherCivWater2, open("civGameotherCivWater24.dat", "wb"))
			pickle.dump(otherCivFood2, open("civGameotherCivFood24.dat", "wb"))
			pickle.dump(otherCivRock3, open("civGameotherCivRock34.dat", "wb"))
			pickle.dump(otherCivHouses3, open("civGameotherCivHouses34.dat", "wb"))
			pickle.dump(otherCivFarms3, open("civGameotherCivFarms34.dat", "wb"))
			pickle.dump(otherCivWood3, open("civGameotherCivWood34.dat", "wb"))
			pickle.dump(otherCivWater3, open("civGameotherCivWater34.dat", "wb"))
			pickle.dump(otherCivFood3, open("civGameotherCivFood34.dat", "wb"))
			pickle.dump(otherCivPop, open("civGameotherCivPop4.dat", "wb"))
			pickle.dump(otherCivPop2, open("civGameotherCivPop24.dat", "wb"))
			pickle.dump(otherCivPop3, open("civGameotherCivPop34.dat", "wb"))
			pickle.dump(run, open("civGamerun4.dat", "wb"))
			pickle.dump(otherCivCurrency, open("civGameotherCivCurrency4.dat", "wb"))
			pickle.dump(otherCivCurrency2, open("civGameotherCivCurrency24.dat", "wb"))
			pickle.dump(otherCivCurrency3, open("civGameotherCivCurrency34.dat", "wb"))
			pickle.dump(otherCivAge, open("civGameotherCivAge4.dat", "wb"))
			pickle.dump(otherCivAge2, open("civGameotherCivAge24.dat", "wb"))
			pickle.dump(otherCivAge3, open("civGameotherCivAge34.dat", "wb"))
			pickle.dump(otherCivName, open("civGameotherCivName4.dat", "wb"))
			pickle.dump(otherCivName2, open("civGameotherCivName24.dat", "wb"))
			pickle.dump(otherCivName3, open("civGameotherCivName34.dat", "wb"))
			pickle.dump(otherCivLeader, open("civGameotherCivLeader4.dat", "wb"))
			pickle.dump(otherCivLeader2, open("civGameotherCivLeader24.dat", "wb"))
			pickle.dump(otherCivLeader3, open("civGameotherCivLeader34.dat", "wb"))
			gameOn = False
		
		elif action1 == "5" :
			pickle.dump(age, open("civGameAge5.dat", "wb"))
			pickle.dump(food, open("civGameFood5.dat", "wb"))
			pickle.dump(trees, open("civGameTrees5.dat", "wb"))
			pickle.dump(water, open("civGameWater5.dat", "wb"))
			pickle.dump(wood, open("civGameWood5.dat", "wb"))
			pickle.dump(rock, open("civGameRock5.dat", "wb"))
			pickle.dump(population, open("civGamePop5.dat", "wb"))
			pickle.dump(discoverers, open("civGameDiscoverers5.dat", "wb"))
			pickle.dump(farms, open("civGameFarms5.dat", "wb"))
			pickle.dump(houses, open("civGameHouses5.dat", "wb"))
			pickle.dump(hiddenPopulation, open("civGameHidPop5.dat", "wb"))
			pickle.dump(discPointsRemaining, open("civGameDiscPR5.dat", "wb"))
			pickle.dump(pickaxe, open("civGamePickaxe5.dat", "wb"))
			pickle.dump(waterPit, open("civGameWaterPit5.dat", "wb"))
			pickle.dump(waterTunnels, open("civGameWaterT5.dat", "wb"))
			pickle.dump(corn, open("civGameCorn5.dat", "wb"))
			pickle.dump(housing, open("civGameHousing5.dat", "wb"))
			pickle.dump(iron, open("civGameIron5.dat", "wb"))
			pickle.dump(glass, open("civGameGlass5.dat", "wb"))
			pickle.dump(extHeat, open("civGameExtHeat5.dat", "wb"))
			pickle.dump(copper, open("civGameCopper5.dat", "wb"))
			pickle.dump(bronze, open("civGameBronze5.dat", "wb"))
			pickle.dump(translation, open("civGameTranslation5.dat", "wb"))
			pickle.dump(techList, open("civGameTechList5.dat", "wb"))
			pickle.dump(techListPre, open("civGameTechListPre5.dat", "wb"))
			pickle.dump(cornAmt, open("civGameCornAmt5.dat", "wb"))
			pickle.dump(housingAmt, open("civGameHousingAmt5.dat", "wb"))
			pickle.dump(ironAmt, open("civGameIronAmt5.dat", "wb"))
			pickle.dump(glassAmt, open("civGameGlassAmt5.dat", "wb"))
			pickle.dump(extHeatAmt, open("civGameExtHeatAmt5.dat", "wb"))
			pickle.dump(copperAmt, open("civGameCopperAmt5.dat", "wb"))
			pickle.dump(bronzeAmt, open("civGameBronzeAmt5.dat", "wb"))
			pickle.dump(translationAmt, open("civGameTranslationAmt5.dat", "wb"))
			pickle.dump(technology, open("civGameTechnology5.dat", "wb"))
			pickle.dump(gameOn, open("civGameGameOn5.dat", "wb"))
			pickle.dump(ageUpdate, open("civGameAgeUpdate5.dat", "wb"))
			pickle.dump(expansion, open("civGameExpansion5.dat", "wb"))
			pickle.dump(expansionAmt, open("civGameExpansionAmt5.dat", "wb"))
			pickle.dump(currency, open("civGameCurrency5.dat", "wb"))
			pickle.dump(farmer, open("civGameFarmer5.dat", "wb"))
			pickle.dump(farmers, open("civGameFarmers5.dat", "wb"))
			pickle.dump(farmerAmt, open("civGameFarmerAmt5.dat", "wb"))
			pickle.dump(leader, open("civGameLeader5.dat", "wb"))
			pickle.dump(leaderAmt, open("civGameLeaderAmt5.dat", "wb"))
			pickle.dump(ldrName, open("civGameldrName5.dat", "wb"))
			pickle.dump(ldrStrength, open("civGameldrStrength5.dat", "wb"))
			pickle.dump(ldrIntellect, open("civGameldrIntellect5.dat", "wb"))
			pickle.dump(ldrDiplomacy, open("civGameldrDiplomacy5.dat", "wb"))
			pickle.dump(ldrSocials, open("civGameldrSocials5.dat", "wb"))
			pickle.dump(prevPop, open("civGameprevPop5.dat", "wb"))
			pickle.dump(waterers, open("civGameWaterers5.dat", "wb"))
			pickle.dump(otherCivRock, open("civGameotherCivRock5.dat", "wb"))
			pickle.dump(otherCivHouses, open("civGameotherCivHouses5.dat", "wb"))
			pickle.dump(otherCivFarms, open("civGameotherCivFarms5.dat", "wb"))
			pickle.dump(otherCivWood, open("civGameotherCivWood5.dat", "wb"))
			pickle.dump(otherCivWater, open("civGameotherCivWater5.dat", "wb"))
			pickle.dump(otherCivFood, open("civGameotherCivFood5.dat", "wb"))
			pickle.dump(count, open("civGamecount5.dat", "wb"))
			pickle.dump(otherCivRock2, open("civGameotherCivRock25.dat", "wb"))
			pickle.dump(otherCivHouses2, open("civGameotherCivHouses25.dat", "wb"))
			pickle.dump(otherCivFarms2, open("civGameotherCivFarms25.dat", "wb"))
			pickle.dump(otherCivWood2, open("civGameotherCivWood25.dat", "wb"))
			pickle.dump(otherCivWater2, open("civGameotherCivWater25.dat", "wb"))
			pickle.dump(otherCivFood2, open("civGameotherCivFood25.dat", "wb"))
			pickle.dump(otherCivRock3, open("civGameotherCivRock35.dat", "wb"))
			pickle.dump(otherCivHouses3, open("civGameotherCivHouses35.dat", "wb"))
			pickle.dump(otherCivFarms3, open("civGameotherCivFarms35.dat", "wb"))
			pickle.dump(otherCivWood3, open("civGameotherCivWood35.dat", "wb"))
			pickle.dump(otherCivWater3, open("civGameotherCivWater35.dat", "wb"))
			pickle.dump(otherCivFood3, open("civGameotherCivFood35.dat", "wb"))
			pickle.dump(otherCivPop, open("civGameotherCivPop5.dat", "wb"))
			pickle.dump(otherCivPop2, open("civGameotherCivPop25.dat", "wb"))
			pickle.dump(otherCivPop3, open("civGameotherCivPop35.dat", "wb"))
			pickle.dump(run, open("civGamerun5.dat", "wb"))
			pickle.dump(otherCivCurrency, open("civGameotherCivCurrency5.dat", "wb"))
			pickle.dump(otherCivCurrency2, open("civGameotherCivCurrency25.dat", "wb"))
			pickle.dump(otherCivCurrency3, open("civGameotherCivCurrency35.dat", "wb"))
			pickle.dump(otherCivAge, open("civGameotherCivAge5.dat", "wb"))
			pickle.dump(otherCivAge2, open("civGameotherCivAge25.dat", "wb"))
			pickle.dump(otherCivAge3, open("civGameotherCivAge35.dat", "wb"))
			pickle.dump(otherCivName, open("civGameotherCivName5.dat", "wb"))
			pickle.dump(otherCivName2, open("civGameotherCivName25.dat", "wb"))
			pickle.dump(otherCivName3, open("civGameotherCivName35.dat", "wb"))
			pickle.dump(otherCivLeader, open("civGameotherCivLeader5.dat", "wb"))
			pickle.dump(otherCivLeader2, open("civGameotherCivLeader25.dat", "wb"))
			pickle.dump(otherCivLeader3, open("civGameotherCivLeader35.dat", "wb"))
			gameOn = False

		else :
			print("That's an invalid option!\n")

		if gameOn == False :
			action = input("What would you like to name this save?:\n>> ")
			pickle.dump(action, open("civGameSaveName"+str(action1)+".dat", "wb"))

#Loads all previously saved game data
def load() :
	global age,food,trees,water,wood,rock,population,discoverers,farms,houses,hiddenPopulation,discPointsRemaining,pickaxe,waterPit,waterTunnels,corn,housing,iron,glass,extHeat,copper,bronze,translation,techList,techListPre,cornAmt,housingAmt,ironAmt,glassAmt,extHeatAmt,copperAmt,bronzeAmt,translationAmt,technology,gameOn,ageUpdate,expansion,expansionAmt,currency,save1,save2,save3,save4,save5,action,farmer,farmers,farmerAmt,leader,leaderAmt,ldrName,ldrStrength,ldrIntellect,ldrDiplomacy,ldrSocials,prevPop,waterers, otherCivRock, otherCivHouses, otherCivFarms, otherCivWood, otherCivWater, otherCivFood, count, otherCivRock2, otherCivHouses2, otherCivFarms2, otherCivWood2, otherCivWater2, otherCivFood2, otherCivRock3, otherCivHouses3, otherCivFarms3, otherCivWood3, otherCivWater3, otherCivFood3, otherCivPop, otherCivPop2, otherCivPop3, run, population, otherCivCurrency, otherCivCurrency2, otherCivCurrency3, otherCivAge, otherCivAge2, otherCivAge3, otherCivName, otherCivName2, otherCivName3, otherCivLeader, otherCivLeader2, otherCivLeader3
	try :
		save1 = pickle.load(open("civGameSaveName1.dat", "rb"))
	except :
		save1 = "Empty"
	try :
		save2 = pickle.load(open("civGameSaveName2.dat", "rb"))
	except :
		save2 = "Empty"
	try :
		save3 = pickle.load(open("civGameSaveName3.dat", "rb"))
	except :
		save3 = "Empty"
	try :
		save4 = pickle.load(open("civGameSaveName4.dat", "rb"))
	except :
		save4 = "Empty"
	try :
		save5 = pickle.load(open("civGameSaveName5.dat", "rb"))
	except :
		save5 = "Empty"

	savesList = [save1,save2,save3,save4,save5]
	i = 0
	for item in savesList :
		i += 1
		print(str(i)+")",item)
	while gameOn == True :
		action = input("Which save would you like to load? (Type a number):\n>> ")
		if action == "1" :
			age = pickle.load(open("civGameAge.dat", "rb"))
			food = pickle.load(open("civGameFood.dat", "rb"))
			trees = pickle.load(open("civGameTrees.dat", "rb"))
			water = pickle.load(open("civGameWater.dat", "rb"))
			wood = pickle.load(open("civGameWood.dat", "rb"))
			rock = pickle.load(open("civGameRock.dat", "rb"))
			population = pickle.load(open("civGamePop.dat", "rb"))
			discoverers = pickle.load(open("civGameDiscoverers.dat", "rb"))
			farms = pickle.load(open("civGameFarms.dat", "rb"))
			houses = pickle.load(open("civGameHouses.dat", "rb"))
			hiddenPopulation = pickle.load(open("civGameHidPop.dat", "rb"))
			discPointsRemaining = pickle.load(open("civGameDiscPR.dat", "rb"))
			pickaxe = pickle.load(open("civGamePickaxe.dat", "rb"))
			waterPit = pickle.load(open("civGameWaterPit.dat", "rb"))
			waterTunnels = pickle.load(open("civGameWaterT.dat", "rb"))
			corn = pickle.load(open("civGameCorn.dat", "rb"))
			housing = pickle.load(open("civGameHousing.dat", "rb"))
			iron = pickle.load(open("civGameIron.dat", "rb"))
			glass = pickle.load(open("civGameGlass.dat", "rb"))
			extHeat = pickle.load(open("civGameExtHeat.dat", "rb"))
			copper = pickle.load(open("civGameCopper.dat", "rb"))
			bronze = pickle.load(open("civGameBronze.dat", "rb"))
			translation = pickle.load(open("civGameTranslation.dat", "rb"))
			techList = pickle.load(open("civGameTechList.dat", "rb"))
			techListPre = pickle.load(open("civGameTechListPre.dat", "rb"))
			cornAmt = pickle.load(open("civGameCornAmt.dat", "rb"))
			housingAmt = pickle.load(open("civGameHousingAmt.dat", "rb"))
			ironAmt = pickle.load(open("civGameIronAmt.dat", "rb"))
			glassAmt = pickle.load(open("civGameGlassAmt.dat", "rb"))
			extHeatAmt = pickle.load(open("civGameExtHeatAmt.dat", "rb"))
			copperAmt = pickle.load(open("civGameCopperAmt.dat", "rb"))
			bronzeAmt = pickle.load(open("civGameBronzeAmt.dat", "rb"))
			translationAmt = pickle.load(open("civGameTranslationAmt.dat", "rb"))
			technology = pickle.load(open("civGameTechnology.dat", "rb"))
			gameOn = pickle.load(open("civGameGameOn.dat", "rb"))
			ageUpdate = pickle.load(open("civGameAgeUpdate.dat", "rb"))
			expansion = pickle.load(open("civGameExpansion.dat", "rb"))
			expansionAmt = pickle.load(open("civGameExpansionAmt.dat", "rb"))
			currency = pickle.load(open("civGameCurrency.dat", "rb"))
			farmer = pickle.load(open("civGameFarmer.dat", "rb"))
			farmers = pickle.load(open("civGameFarmers.dat", "rb"))
			farmerAmt = pickle.load(open("civGameFarmerAmt.dat", "rb"))
			leader = pickle.load(open("civGameLeader.dat", "rb"))
			leaderAmt = pickle.load(open("civGameLeaderAmt.dat", "rb"))
			ldrName = pickle.load(open("civGameldrName.dat", "rb"))
			ldrStrength = pickle.load(open("civGameldrStrength.dat", "rb"))
			ldrIntellect = pickle.load(open("civGameldrIntellect.dat", "rb"))
			ldrDiplomacy = pickle.load(open("civGameldrDiplomacy.dat", "rb"))
			ldrSocials = pickle.load(open("civGameldrSocials.dat", "rb"))
			prevPop = pickle.load(open("civGameprevPop.dat", "rb"))
			waterers = pickle.load(open("civGameWaterers.dat", "rb"))
			otherCivRock = pickle.load(open("civGameotherCivRock.dat", "rb"))
			otherCivHouses = pickle.load(open("civGameotherCivHouses.dat", "rb"))
			otherCivFarms = pickle.load(open("civGameotherCivFarms.dat", "rb"))
			otherCivWood = pickle.load(open("civGameotherCivWood.dat", "rb"))
			otherCivWater = pickle.load(open("civGameotherCivWater.dat", "rb"))
			otherCivFood = pickle.load(open("civGameotherCivFood.dat", "rb"))
			count = pickle.load(open("civGamecount.dat", "rb"))
			otherCivRock2 = pickle.load(open("civGameotherCivRock2.dat", "rb"))
			otherCivHouses2 = pickle.load(open("civGameotherCivHouses2.dat", "rb"))
			otherCivFarms2 = pickle.load(open("civGameotherCivFarms2.dat", "rb"))
			otherCivWood2 = pickle.load(open("civGameotherCivWood2.dat", "rb"))
			otherCivWater2 = pickle.load(open("civGameotherCivWater2.dat", "rb"))
			otherCivFood2 = pickle.load(open("civGameotherCivFood2.dat", "rb"))
			otherCivRock3 = pickle.load(open("civGameotherCivRock3.dat", "rb"))
			otherCivHouses3 = pickle.load(open("civGameotherCivHouses3.dat", "rb"))
			otherCivFarms3 = pickle.load(open("civGameotherCivFarms3.dat", "rb"))
			otherCivWood3 = pickle.load(open("civGameotherCivWood3.dat", "rb"))
			otherCivWater3 = pickle.load(open("civGameotherCivWater3.dat", "rb"))
			otherCivFood3 = pickle.load(open("civGameotherCivFood3.dat", "rb"))
			otherCivPop = pickle.load(open("civGameotherCivPop.dat", "rb"))
			otherCivPop2 = pickle.load(open("civGameotherCivPop2.dat", "rb"))
			otherCivPop3 = pickle.load(open("civGameotherCivPop3.dat", "rb"))
			run = pickle.load(open("civGamerun.dat", "rb"))
			otherCivCurrency = pickle.load(open("civGameotherCivCurrency.dat", "rb"))
			otherCivCurrency2 = pickle.load(open("civGameotherCivCurrency2.dat", "rb"))
			otherCivCurrency3 = pickle.load(open("civGameotherCivCurrency3.dat", "rb"))
			otherCivAge = pickle.load(open("civGameotherCivAge.dat", "rb"))
			otherCivAge2 = pickle.load(open("civGameotherCivAge2.dat", "rb"))
			otherCivAge3 = pickle.load(open("civGameotherCivAge3.dat", "rb"))
			otherCivName = pickle.load(open("civGameotherCivName.dat", "rb"))
			otherCivName2 = pickle.load(open("civGameotherCivName2.dat", "rb"))
			otherCivName3 = pickle.load(open("civGameotherCivName3.dat", "rb"))
			otherCivLeader = pickle.load(open("civGameotherCivLeader.dat", "rb"))
			otherCivLeader2 = pickle.load(open("civGameotherCivLeader2.dat", "rb"))
			otherCivLeader3 = pickle.load(open("civGameotherCivLeader3.dat", "rb"))
			gameOn = False
		
		elif action == "2" :
			age = pickle.load(open("civGameAge2.dat", "rb"))
			food = pickle.load(open("civGameFood2.dat", "rb"))
			trees = pickle.load(open("civGameTrees2.dat", "rb"))
			water = pickle.load(open("civGameWater2.dat", "rb"))
			wood = pickle.load(open("civGameWood2.dat", "rb"))
			rock = pickle.load(open("civGameRock2.dat", "rb"))
			population = pickle.load(open("civGamePop2.dat", "rb"))
			discoverers = pickle.load(open("civGameDiscoverers2.dat", "rb"))
			farms = pickle.load(open("civGameFarms2.dat", "rb"))
			houses = pickle.load(open("civGameHouses2.dat", "rb"))
			hiddenPopulation = pickle.load(open("civGameHidPop2.dat", "rb"))
			discPointsRemaining = pickle.load(open("civGameDiscPR2.dat", "rb"))
			pickaxe = pickle.load(open("civGamePickaxe2.dat", "rb"))
			waterPit = pickle.load(open("civGameWaterPit2.dat", "rb"))
			waterTunnels = pickle.load(open("civGameWaterT2.dat", "rb"))
			corn = pickle.load(open("civGameCorn2.dat", "rb"))
			housing = pickle.load(open("civGameHousing2.dat", "rb"))
			iron = pickle.load(open("civGameIron2.dat", "rb"))
			glass = pickle.load(open("civGameGlass2.dat", "rb"))
			extHeat = pickle.load(open("civGameExtHeat2.dat", "rb"))
			copper = pickle.load(open("civGameCopper2.dat", "rb"))
			bronze = pickle.load(open("civGameBronze2.dat", "rb"))
			translation = pickle.load(open("civGameTranslation2.dat", "rb"))
			techList = pickle.load(open("civGameTechList2.dat", "rb"))
			techListPre = pickle.load(open("civGameTechListPre2.dat", "rb"))
			cornAmt = pickle.load(open("civGameCornAmt2.dat", "rb"))
			housingAmt = pickle.load(open("civGameHousingAmt2.dat", "rb"))
			ironAmt = pickle.load(open("civGameIronAmt2.dat", "rb"))
			glassAmt = pickle.load(open("civGameGlassAmt2.dat", "rb"))
			extHeatAmt = pickle.load(open("civGameExtHeatAmt2.dat", "rb"))
			copperAmt = pickle.load(open("civGameCopperAmt2.dat", "rb"))
			bronzeAmt = pickle.load(open("civGameBronzeAmt2.dat", "rb"))
			translationAmt = pickle.load(open("civGameTranslationAmt2.dat", "rb"))
			technology = pickle.load(open("civGameTechnology2.dat", "rb"))
			gameOn = pickle.load(open("civGameGameOn2.dat", "rb"))
			ageUpdate = pickle.load(open("civGameAgeUpdate2.dat", "rb"))
			expansion = pickle.load(open("civGameExpansion2.dat", "rb"))
			expansionAmt = pickle.load(open("civGameExpansionAmt2.dat", "rb"))
			currency = pickle.load(open("civGameCurrency2.dat", "rb"))
			farmer = pickle.load(open("civGameFarmer2.dat", "rb"))
			farmers = pickle.load(open("civGameFarmers2.dat", "rb"))
			farmerAmt = pickle.load(open("civGameFarmerAmt2.dat", "rb"))
			leader = pickle.load(open("civGameLeader2.dat", "rb"))
			leaderAmt = pickle.load(open("civGameLeaderAmt2.dat", "rb"))
			ldrName = pickle.load(open("civGameldrName2.dat", "rb"))
			ldrStrength = pickle.load(open("civGameldrStrength2.dat", "rb"))
			ldrIntellect = pickle.load(open("civGameldrIntellect2.dat", "rb"))
			ldrDiplomacy = pickle.load(open("civGameldrDiplomacy2.dat", "rb"))
			ldrSocials = pickle.load(open("civGameldrSocials2.dat", "rb"))
			prevPop = pickle.load(open("civGameprevPop2.dat", "rb"))
			waterers = pickle.load(open("civGameWaterers2.dat", "rb"))
			otherCivRock = pickle.load(open("civGameotherCivRock2.dat", "rb"))
			otherCivHouses = pickle.load(open("civGameotherCivHouses2.dat", "rb"))
			otherCivFarms = pickle.load(open("civGameotherCivFarms2.dat", "rb"))
			otherCivWood = pickle.load(open("civGameotherCivWood2.dat", "rb"))
			otherCivWater = pickle.load(open("civGameotherCivWater2.dat", "rb"))
			otherCivFood = pickle.load(open("civGameotherCivFood2.dat", "rb"))
			count = pickle.load(open("civGamecount2.dat", "rb"))
			otherCivRock2 = pickle.load(open("civGameotherCivRock22.dat", "rb"))
			otherCivHouses2 = pickle.load(open("civGameotherCivHouses22.dat", "rb"))
			otherCivFarms2 = pickle.load(open("civGameotherCivFarms22.dat", "rb"))
			otherCivWood2 = pickle.load(open("civGameotherCivWood22.dat", "rb"))
			otherCivWater2 = pickle.load(open("civGameotherCivWater22.dat", "rb"))
			otherCivFood2 = pickle.load(open("civGameotherCivFood22.dat", "rb"))
			otherCivRock3 = pickle.load(open("civGameotherCivRock32.dat", "rb"))
			otherCivHouses3 = pickle.load(open("civGameotherCivHouses32.dat", "rb"))
			otherCivFarms3 = pickle.load(open("civGameotherCivFarms32.dat", "rb"))
			otherCivWood3 = pickle.load(open("civGameotherCivWood32.dat", "rb"))
			otherCivWater3 = pickle.load(open("civGameotherCivWater32.dat", "rb"))
			otherCivFood3 = pickle.load(open("civGameotherCivFood32.dat", "rb"))
			otherCivPop = pickle.load(open("civGameotherCivPop2.dat", "rb"))
			otherCivPop2 = pickle.load(open("civGameotherCivPop22.dat", "rb"))
			otherCivPop3 = pickle.load(open("civGameotherCivPop32.dat", "rb"))
			run = pickle.load(open("civGamerun2.dat", "rb"))
			otherCivCurrency = pickle.load(open("civGameotherCivCurrency2.dat", "rb"))
			otherCivCurrency2 = pickle.load(open("civGameotherCivCurrency22.dat", "rb"))
			otherCivCurrency3 = pickle.load(open("civGameotherCivCurrency32.dat", "rb"))
			otherCivAge = pickle.load(open("civGameotherCivAge2.dat", "rb"))
			otherCivAge2 = pickle.load(open("civGameotherCivAge22.dat", "rb"))
			otherCivAge3 = pickle.load(open("civGameotherCivAge32.dat", "rb"))
			otherCivName = pickle.load(open("civGameotherCivName2.dat", "rb"))
			otherCivName2 = pickle.load(open("civGameotherCivName22.dat", "rb"))
			otherCivName3 = pickle.load(open("civGameotherCivName32.dat", "rb"))
			otherCivLeader = pickle.load(open("civGameotherCivLeader2.dat", "rb"))
			otherCivLeader2 = pickle.load(open("civGameotherCivLeader22.dat", "rb"))
			otherCivLeader3 = pickle.load(open("civGameotherCivLeader32.dat", "rb"))
			gameOn = False
		
		elif action == "3" :
			age = pickle.load(open("civGameAge3.dat", "rb"))
			food = pickle.load(open("civGameFood3.dat", "rb"))
			trees = pickle.load(open("civGameTrees3.dat", "rb"))
			water = pickle.load(open("civGameWater3.dat", "rb"))
			wood = pickle.load(open("civGameWood3.dat", "rb"))
			rock = pickle.load(open("civGameRock3.dat", "rb"))
			population = pickle.load(open("civGamePop3.dat", "rb"))
			discoverers = pickle.load(open("civGameDiscoverers3.dat", "rb"))
			farms = pickle.load(open("civGameFarms3.dat", "rb"))
			houses = pickle.load(open("civGameHouses3.dat", "rb"))
			hiddenPopulation = pickle.load(open("civGameHidPop3.dat", "rb"))
			discPointsRemaining = pickle.load(open("civGameDiscPR3.dat", "rb"))
			pickaxe = pickle.load(open("civGamePickaxe3.dat", "rb"))
			waterPit = pickle.load(open("civGameWaterPit3.dat", "rb"))
			waterTunnels = pickle.load(open("civGameWaterT3.dat", "rb"))
			corn = pickle.load(open("civGameCorn3.dat", "rb"))
			housing = pickle.load(open("civGameHousing3.dat", "rb"))
			iron = pickle.load(open("civGameIron3.dat", "rb"))
			glass = pickle.load(open("civGameGlass3.dat", "rb"))
			extHeat = pickle.load(open("civGameExtHeat3.dat", "rb"))
			copper = pickle.load(open("civGameCopper3.dat", "rb"))
			bronze = pickle.load(open("civGameBronze3.dat", "rb"))
			translation = pickle.load(open("civGameTranslation3.dat", "rb"))
			techList = pickle.load(open("civGameTechList3.dat", "rb"))
			techListPre = pickle.load(open("civGameTechListPre3.dat", "rb"))
			cornAmt = pickle.load(open("civGameCornAmt3.dat", "rb"))
			housingAmt = pickle.load(open("civGameHousingAmt3.dat", "rb"))
			ironAmt = pickle.load(open("civGameIronAmt3.dat", "rb"))
			glassAmt = pickle.load(open("civGameGlassAmt3.dat", "rb"))
			extHeatAmt = pickle.load(open("civGameExtHeatAmt3.dat", "rb"))
			copperAmt = pickle.load(open("civGameCopperAmt3.dat", "rb"))
			bronzeAmt = pickle.load(open("civGameBronzeAmt3.dat", "rb"))
			translationAmt = pickle.load(open("civGameTranslationAmt3.dat", "rb"))
			technology = pickle.load(open("civGameTechnology3.dat", "rb"))
			gameOn = pickle.load(open("civGameGameOn3.dat", "rb"))
			ageUpdate = pickle.load(open("civGameAgeUpdate3.dat", "rb"))
			expansion = pickle.load(open("civGameExpansion3.dat", "rb"))
			expansionAmt = pickle.load(open("civGameExpansionAmt3.dat", "rb"))
			currency = pickle.load(open("civGameCurrency3.dat", "rb"))
			farmer = pickle.load(open("civGameFarmer3.dat", "rb"))
			farmers = pickle.load(open("civGameFarmers3.dat", "rb"))
			farmerAmt = pickle.load(open("civGameFarmerAmt3.dat", "rb"))
			leader = pickle.load(open("civGameLeader3.dat", "rb"))
			leaderAmt = pickle.load(open("civGameLeaderAmt3.dat", "rb"))
			ldrName = pickle.load(open("civGameldrName3.dat", "rb"))
			ldrStrength = pickle.load(open("civGameldrStrength3.dat", "rb"))
			ldrIntellect = pickle.load(open("civGameldrIntellect3.dat", "rb"))
			ldrDiplomacy = pickle.load(open("civGameldrDiplomacy3.dat", "rb"))
			ldrSocials = pickle.load(open("civGameldrSocials3.dat", "rb"))
			prevPop = pickle.load(open("civGameprevPop3.dat", "rb"))
			waterers = pickle.load(open("civGameWaterers3.dat", "rb"))
			otherCivRock = pickle.load(open("civGameotherCivRock3.dat", "rb"))
			otherCivHouses = pickle.load(open("civGameotherCivHouses3.dat", "rb"))
			otherCivFarms = pickle.load(open("civGameotherCivFarms3.dat", "rb"))
			otherCivWood = pickle.load(open("civGameotherCivWood3.dat", "rb"))
			otherCivWater = pickle.load(open("civGameotherCivWater3.dat", "rb"))
			otherCivFood = pickle.load(open("civGameotherCivFood3.dat", "rb"))
			count = pickle.load(open("civGamecount3.dat", "rb"))
			otherCivRock2 = pickle.load(open("civGameotherCivRock23.dat", "rb"))
			otherCivHouses2 = pickle.load(open("civGameotherCivHouses23.dat", "rb"))
			otherCivFarms2 = pickle.load(open("civGameotherCivFarms23.dat", "rb"))
			otherCivWood2 = pickle.load(open("civGameotherCivWood23.dat", "rb"))
			otherCivWater2 = pickle.load(open("civGameotherCivWater23.dat", "rb"))
			otherCivFood2 = pickle.load(open("civGameotherCivFood23.dat", "rb"))
			otherCivRock3 = pickle.load(open("civGameotherCivRock33.dat", "rb"))
			otherCivHouses3 = pickle.load(open("civGameotherCivHouses33.dat", "rb"))
			otherCivFarms3 = pickle.load(open("civGameotherCivFarms33.dat", "rb"))
			otherCivWood3 = pickle.load(open("civGameotherCivWood33.dat", "rb"))
			otherCivWater3 = pickle.load(open("civGameotherCivWater33.dat", "rb"))
			otherCivFood3 = pickle.load(open("civGameotherCivFood33.dat", "rb"))
			otherCivPop = pickle.load(open("civGameotherCivPop3.dat", "rb"))
			otherCivPop2 = pickle.load(open("civGameotherCivPop23.dat", "rb"))
			otherCivPop3 = pickle.load(open("civGameotherCivPop33.dat", "rb"))
			run = pickle.load(open("civGamerun3.dat", "rb"))
			otherCivCurrency = pickle.load(open("civGameotherCivCurrency3.dat", "rb"))
			otherCivCurrency2 = pickle.load(open("civGameotherCivCurrency23.dat", "rb"))
			otherCivCurrency3 = pickle.load(open("civGameotherCivCurrency33.dat", "rb"))
			otherCivAge = pickle.load(open("civGameotherCivAge3.dat", "rb"))
			otherCivAge2 = pickle.load(open("civGameotherCivAge23.dat", "rb"))
			otherCivAge3 = pickle.load(open("civGameotherCivAge33.dat", "rb"))
			otherCivName = pickle.load(open("civGameotherCivName3.dat", "rb"))
			otherCivName2 = pickle.load(open("civGameotherCivName23.dat", "rb"))
			otherCivName3 = pickle.load(open("civGameotherCivName33.dat", "rb"))
			otherCivLeader = pickle.load(open("civGameotherCivLeader3.dat", "rb"))
			otherCivLeader2 = pickle.load(open("civGameotherCivLeader23.dat", "rb"))
			otherCivLeader3 = pickle.load(open("civGameotherCivLeader33.dat", "rb"))
			gameOn = False
		
		elif action == "4" :
			age = pickle.load(open("civGameAge4.dat", "rb"))
			food = pickle.load(open("civGameFood4.dat", "rb"))
			trees = pickle.load(open("civGameTrees4.dat", "rb"))
			water = pickle.load(open("civGameWater4.dat", "rb"))
			wood = pickle.load(open("civGameWood4.dat", "rb"))
			rock = pickle.load(open("civGameRock4.dat", "rb"))
			population = pickle.load(open("civGamePop4.dat", "rb"))
			discoverers = pickle.load(open("civGameDiscoverers4.dat", "rb"))
			farms = pickle.load(open("civGameFarms4.dat", "rb"))
			houses = pickle.load(open("civGameHouses4.dat", "rb"))
			hiddenPopulation = pickle.load(open("civGameHidPop4.dat", "rb"))
			discPointsRemaining = pickle.load(open("civGameDiscPR4.dat", "rb"))
			pickaxe = pickle.load(open("civGamePickaxe4.dat", "rb"))
			waterPit = pickle.load(open("civGameWaterPit4.dat", "rb"))
			waterTunnels = pickle.load(open("civGameWaterT4.dat", "rb"))
			corn = pickle.load(open("civGameCorn4.dat", "rb"))
			housing = pickle.load(open("civGameHousing4.dat", "rb"))
			iron = pickle.load(open("civGameIron4.dat", "rb"))
			glass = pickle.load(open("civGameGlass4.dat", "rb"))
			extHeat = pickle.load(open("civGameExtHeat4.dat", "rb"))
			copper = pickle.load(open("civGameCopper4.dat", "rb"))
			bronze = pickle.load(open("civGameBronze4.dat", "rb"))
			translation = pickle.load(open("civGameTranslation4.dat", "rb"))
			techList = pickle.load(open("civGameTechList4.dat", "rb"))
			techListPre = pickle.load(open("civGameTechListPre4.dat", "rb"))
			cornAmt = pickle.load(open("civGameCornAmt4.dat", "rb"))
			housingAmt = pickle.load(open("civGameHousingAmt4.dat", "rb"))
			ironAmt = pickle.load(open("civGameIronAmt4.dat", "rb"))
			glassAmt = pickle.load(open("civGameGlassAmt4.dat", "rb"))
			extHeatAmt = pickle.load(open("civGameExtHeatAmt4.dat", "rb"))
			copperAmt = pickle.load(open("civGameCopperAmt4.dat", "rb"))
			bronzeAmt = pickle.load(open("civGameBronzeAmt4.dat", "rb"))
			translationAmt = pickle.load(open("civGameTranslationAmt4.dat", "rb"))
			technology = pickle.load(open("civGameTechnology4.dat", "rb"))
			gameOn = pickle.load(open("civGameGameOn4.dat", "rb"))
			ageUpdate = pickle.load(open("civGameAgeUpdate4.dat", "rb"))
			expansion = pickle.load(open("civGameExpansion4.dat", "rb"))
			expansionAmt = pickle.load(open("civGameExpansionAmt4.dat", "rb"))
			currency = pickle.load(open("civGameCurrency4.dat", "rb"))
			farmer = pickle.load(open("civGameFarmer4.dat", "rb"))
			farmers = pickle.load(open("civGameFarmers4.dat", "rb"))
			farmerAmt = pickle.load(open("civGameFarmerAmt4.dat", "rb"))
			leader = pickle.load(open("civGameLeader4.dat", "rb"))
			leaderAmt = pickle.load(open("civGameLeaderAmt4.dat", "rb"))
			ldrName = pickle.load(open("civGameldrName4.dat", "rb"))
			ldrStrength = pickle.load(open("civGameldrStrength4.dat", "rb"))
			ldrIntellect = pickle.load(open("civGameldrIntellect4.dat", "rb"))
			ldrDiplomacy = pickle.load(open("civGameldrDiplomacy4.dat", "rb"))
			ldrSocials = pickle.load(open("civGameldrSocials4.dat", "rb"))
			prevPop = pickle.load(open("civGameprevPop4.dat", "rb"))
			waterers = pickle.load(open("civGameWaterers4.dat", "rb"))
			otherCivRock = pickle.load(open("civGameotherCivRock4.dat", "rb"))
			otherCivHouses = pickle.load(open("civGameotherCivHouses4.dat", "rb"))
			otherCivFarms = pickle.load(open("civGameotherCivFarms4.dat", "rb"))
			otherCivWood = pickle.load(open("civGameotherCivWood4.dat", "rb"))
			otherCivWater = pickle.load(open("civGameotherCivWater4.dat", "rb"))
			otherCivFood = pickle.load(open("civGameotherCivFood4.dat", "rb"))
			count = pickle.load(open("civGamecount4.dat", "rb"))
			otherCivRock2 = pickle.load(open("civGameotherCivRock24.dat", "rb"))
			otherCivHouses2 = pickle.load(open("civGameotherCivHouses24.dat", "rb"))
			otherCivFarms2 = pickle.load(open("civGameotherCivFarms24.dat", "rb"))
			otherCivWood2 = pickle.load(open("civGameotherCivWood24.dat", "rb"))
			otherCivWater2 = pickle.load(open("civGameotherCivWater24.dat", "rb"))
			otherCivFood2 = pickle.load(open("civGameotherCivFood24.dat", "rb"))
			otherCivRock3 = pickle.load(open("civGameotherCivRock34.dat", "rb"))
			otherCivHouses3 = pickle.load(open("civGameotherCivHouses34.dat", "rb"))
			otherCivFarms3 = pickle.load(open("civGameotherCivFarms34.dat", "rb"))
			otherCivWood3 = pickle.load(open("civGameotherCivWood34.dat", "rb"))
			otherCivWater3 = pickle.load(open("civGameotherCivWater34.dat", "rb"))
			otherCivFood3 = pickle.load(open("civGameotherCivFood34.dat", "rb"))
			otherCivPop = pickle.load(open("civGameotherCivPop4.dat", "rb"))
			otherCivPop2 = pickle.load(open("civGameotherCivPop24.dat", "rb"))
			otherCivPop3 = pickle.load(open("civGameotherCivPop34.dat", "rb"))
			run = pickle.load(open("civGamerun4.dat", "rb"))
			otherCivCurrency = pickle.load(open("civGameotherCivCurrency4.dat", "rb"))
			otherCivCurrency2 = pickle.load(open("civGameotherCivCurrency24.dat", "rb"))
			otherCivCurrency3 = pickle.load(open("civGameotherCivCurrency34.dat", "rb"))
			otherCivAge = pickle.load(open("civGameotherCivAge4.dat", "rb"))
			otherCivAge2 = pickle.load(open("civGameotherCivAge24.dat", "rb"))
			otherCivAge3 = pickle.load(open("civGameotherCivAge34.dat", "rb"))
			otherCivName = pickle.load(open("civGameotherCivName4.dat", "rb"))
			otherCivName2 = pickle.load(open("civGameotherCivName24.dat", "rb"))
			otherCivName3 = pickle.load(open("civGameotherCivName34.dat", "rb"))
			otherCivLeader = pickle.load(open("civGameotherCivLeader4.dat", "rb"))
			otherCivLeader2 = pickle.load(open("civGameotherCivLeader24.dat", "rb"))
			otherCivLeader3 = pickle.load(open("civGameotherCivLeader34.dat", "rb"))
			gameOn = False
		
		elif action == "5" :
			age = pickle.load(open("civGameAge5.dat", "rb"))
			food = pickle.load(open("civGameFood5.dat", "rb"))
			trees = pickle.load(open("civGameTrees5.dat", "rb"))
			water = pickle.load(open("civGameWater5.dat", "rb"))
			wood = pickle.load(open("civGameWood5.dat", "rb"))
			rock = pickle.load(open("civGameRock5.dat", "rb"))
			population = pickle.load(open("civGamePop5.dat", "rb"))
			discoverers = pickle.load(open("civGameDiscoverers5.dat", "rb"))
			farms = pickle.load(open("civGameFarms5.dat", "rb"))
			houses = pickle.load(open("civGameHouses5.dat", "rb"))
			hiddenPopulation = pickle.load(open("civGameHidPop5.dat", "rb"))
			discPointsRemaining = pickle.load(open("civGameDiscPR5.dat", "rb"))
			pickaxe = pickle.load(open("civGamePickaxe5.dat", "rb"))
			waterPit = pickle.load(open("civGameWaterPit5.dat", "rb"))
			waterTunnels = pickle.load(open("civGameWaterT5.dat", "rb"))
			corn = pickle.load(open("civGameCorn5.dat", "rb"))
			housing = pickle.load(open("civGameHousing5.dat", "rb"))
			iron = pickle.load(open("civGameIron5.dat", "rb"))
			glass = pickle.load(open("civGameGlass5.dat", "rb"))
			extHeat = pickle.load(open("civGameExtHeat5.dat", "rb"))
			copper = pickle.load(open("civGameCopper5.dat", "rb"))
			bronze = pickle.load(open("civGameBronze5.dat", "rb"))
			translation = pickle.load(open("civGameTranslation5.dat", "rb"))
			techList = pickle.load(open("civGameTechList5.dat", "rb"))
			techListPre = pickle.load(open("civGameTechListPre5.dat", "rb"))
			cornAmt = pickle.load(open("civGameCornAmt5.dat", "rb"))
			housingAmt = pickle.load(open("civGameHousingAmt5.dat", "rb"))
			ironAmt = pickle.load(open("civGameIronAmt5.dat", "rb"))
			glassAmt = pickle.load(open("civGameGlassAmt5.dat", "rb"))
			extHeatAmt = pickle.load(open("civGameExtHeatAmt5.dat", "rb"))
			copperAmt = pickle.load(open("civGameCopperAmt5.dat", "rb"))
			bronzeAmt = pickle.load(open("civGameBronzeAmt5.dat", "rb"))
			translationAmt = pickle.load(open("civGameTranslationAmt5.dat", "rb"))
			technology = pickle.load(open("civGameTechnology5.dat", "rb"))
			gameOn = pickle.load(open("civGameGameOn5.dat", "rb"))
			ageUpdate = pickle.load(open("civGameAgeUpdate5.dat", "rb"))
			expansion = pickle.load(open("civGameExpansion5.dat", "rb"))
			expansionAmt = pickle.load(open("civGameExpansionAmt5.dat", "rb"))
			currency = pickle.load(open("civGameCurrency5.dat", "rb"))
			farmer = pickle.load(open("civGameFarmer5.dat", "rb"))
			farmers = pickle.load(open("civGameFarmers5.dat", "rb"))
			farmerAmt = pickle.load(open("civGameFarmerAmt5.dat", "rb"))
			leader = pickle.load(open("civGameLeader5.dat", "rb"))
			leaderAmt = pickle.load(open("civGameLeaderAmt5.dat", "rb"))
			ldrName = pickle.load(open("civGameldrName5.dat", "rb"))
			ldrStrength = pickle.load(open("civGameldrStrength5.dat", "rb"))
			ldrIntellect = pickle.load(open("civGameldrIntellect5.dat", "rb"))
			ldrDiplomacy = pickle.load(open("civGameldrDiplomacy5.dat", "rb"))
			ldrSocials = pickle.load(open("civGameldrSocials5.dat", "rb"))
			prevPop = pickle.load(open("civGameprevPop5.dat", "rb"))
			waterers = pickle.load(open("civGameWaterers5.dat", "rb"))
			otherCivRock = pickle.load(open("civGameotherCivRock5.dat", "rb"))
			otherCivHouses = pickle.load(open("civGameotherCivHouses5.dat", "rb"))
			otherCivFarms = pickle.load(open("civGameotherCivFarms5.dat", "rb"))
			otherCivWood = pickle.load(open("civGameotherCivWood5.dat", "rb"))
			otherCivWater = pickle.load(open("civGameotherCivWater5.dat", "rb"))
			otherCivFood = pickle.load(open("civGameotherCivFood5.dat", "rb"))
			count = pickle.load(open("civGamecount5.dat", "rb"))
			otherCivRock2 = pickle.load(open("civGameotherCivRock25.dat", "rb"))
			otherCivHouses2 = pickle.load(open("civGameotherCivHouses25.dat", "rb"))
			otherCivFarms2 = pickle.load(open("civGameotherCivFarms25.dat", "rb"))
			otherCivWood2 = pickle.load(open("civGameotherCivWood25.dat", "rb"))
			otherCivWater2 = pickle.load(open("civGameotherCivWater25.dat", "rb"))
			otherCivFood2 = pickle.load(open("civGameotherCivFood25.dat", "rb"))
			otherCivRock3 = pickle.load(open("civGameotherCivRock35.dat", "rb"))
			otherCivHouses3 = pickle.load(open("civGameotherCivHouses35.dat", "rb"))
			otherCivFarms3 = pickle.load(open("civGameotherCivFarms35.dat", "rb"))
			otherCivWood3 = pickle.load(open("civGameotherCivWood35.dat", "rb"))
			otherCivWater3 = pickle.load(open("civGameotherCivWater35.dat", "rb"))
			otherCivFood3 = pickle.load(open("civGameotherCivFood35.dat", "rb"))
			otherCivPop = pickle.load(open("civGameotherCivPop5.dat", "rb"))
			otherCivPop2 = pickle.load(open("civGameotherCivPop25.dat", "rb"))
			otherCivPop3 = pickle.load(open("civGameotherCivPop35.dat", "rb"))
			run = pickle.load(open("civGamerun5.dat", "rb"))
			otherCivCurrency = pickle.load(open("civGameotherCivCurrency5.dat", "rb"))
			otherCivCurrency2 = pickle.load(open("civGameotherCivCurrency25.dat", "rb"))
			otherCivCurrency3 = pickle.load(open("civGameotherCivCurrency35.dat", "rb"))
			otherCivAge = pickle.load(open("civGameotherCivAge5.dat", "rb"))
			otherCivAge2 = pickle.load(open("civGameotherCivAge25.dat", "rb"))
			otherCivAge3 = pickle.load(open("civGameotherCivAge35.dat", "rb"))
			otherCivName = pickle.load(open("civGameotherCivName5.dat", "rb"))
			otherCivName2 = pickle.load(open("civGameotherCivName25.dat", "rb"))
			otherCivName3 = pickle.load(open("civGameotherCivName35.dat", "rb"))
			otherCivLeader = pickle.load(open("civGameotherCivLeader5.dat", "rb"))
			otherCivLeader2 = pickle.load(open("civGameotherCivLeader25.dat", "rb"))
			otherCivLeader3 = pickle.load(open("civGameotherCivLeader35.dat", "rb"))
			gameOn = False
		else :
			print("That's an invalid option!\n")

#Determines if a random event will happen and what happens in that event
def randomEvents() :
	global food, water, rock, wood, population, age, discPointsRemaining, techList, changeP

	randomEventChance = rand.randint(1,8)
	if randomEventChance < 3:
		#happens if ages are 1 - 10
		if age >= 1 and age <= 10:
			randomEventID = rand.randint(1,5)
			#adds food
			if randomEventID == 1:
				print("\n-------Your people have found a grove of berry bushes YAY!-------\n\n + 10 food\n")
				food += 10
			#adds water
			elif randomEventID == 2:
				print("\n-------There was a rainstorm and your people managed to collect alot of water!-------\n\n + 10 water\n")
				water += 10
			elif randomEventID == 3:
				print("\n-------Your people found recently fallen trees in the forest! Wierdly there were no broken tree spots-------\n\n + 10 wood\n")
				wood += 10
			elif randomEventID == 4:
				print("\n-------A wild beast killed one of our people!-------\n\n - 1 population\n")
				population -= 1
			elif randomEventID == 5 :
				print("\n-------A refugee came out of the woods and decided to stay-------\n\n + 1 population\n")
				population += 1 
		
		#happens if ages are 11 - 20
		if age >= 11 and age <= 20:
			randomEventID = rand.randint(1,7)
			#adds food
			if randomEventID == 1:
				print("\n-------Your people have found a group of meat birds YAS!-------\n\n + 20 food\n")
				food += 20
			#adds water
			elif randomEventID == 2:
				print("\n-------The people found a group of coconut bushes!-------\n\n + 15 water \n + 10 food\n")
				water += 15
				food += 10
			elif randomEventID == 3:
				print("\n-------Your people have recently found fallen BIG trees in the forest! Wierdly there were no broken tree spots-------\n\n + 15 wood\n")
				wood += 15
			elif randomEventID == 4:
				print("\n-------A tree fell on a few people while food time was happening-------\n\n - 3 population\n")
				if population >= 3:
					population -= 3
				else:
					population = 0
			elif randomEventID == 5:
				print("\n-------OH NOs our storage had a leak and things became unusable-------\n\n- 5 wood\n- 3 rock\n- 5 food \n- 5 water\n")
				if wood >= 5 :
					wood -= 5
				else :
					wood = 0
				if rock >= 3 :
					rock -= 3
				else :
					rock = 0
				if food >= 5 :
					food -= 5
				else :
					food = 0
				if water >= 5 :
					water -= 5
				else :
					water = 0
			elif randomEventID == 6:
				print("\n-------ROCKS FELL FROM THE SKY BRO!-------\n\n + 15 rock\n")
				rock += 15
			elif randomEventID == 7:
					if population >= 8 :
						print("\n-------Many people came out of the forest and stayed. Perhaps too many-------\n\n + 10 population\n")
						population += 10
					else:
						print("\n-------People came out of the woods and stayed-------\n\n + 3 population\n")
						population += 3
		
		#happens if ages are 21 - 30
		if age >= 21 and age <= 30:
			randomEventID = rand.randint(1,8)
			#adds food
			if randomEventID == 1:
				print("\n-------Your people have found a pineapple and apple tree grafted together.!-------\n\n + 30 food\n")
				food += 30
			#adds water and food
			elif randomEventID == 2:
				print("\n-------The people found a group of water beast in a source of fresh water!-------\n\n + 25 water \n + 20 food\n")
				water += 25
				food += 20
			elif randomEventID == 3:
				print("\n-------Your people have recently found fallen HUGE trees in the forest! Wierdly there were no broken tree spots-------\n\n + 30 wood\n")
				wood += 30
			elif randomEventID == 4:
				print("\n-------A small BOOM happened during cleaning time-------\n\n - 10 population\n")
				if population >= 10:
					population -= 10
				else:
					population = 0
			elif randomEventID == 5:
				print("\n-------The peoples storage room roof collapsed and many things were destroyed-------\n\n- 20 wood\n- 12 rock\n- 15 food \n- 20 water\n")
				if wood >= 20 :
					wood -= 20
				else :
					wood = 0
				if rock >= 12 :
					rock -= 12
				else :
					rock = 0
				if food >= 15 :
					food -= 15
				else :
					food = 0
				if water >= 20 :
					water -= 20
				else :
					water = 0
			elif randomEventID == 6:
				print("\n-------BIG ROCKS FELL FROM THE SKY BRO!-------\n\n + 30 rock\n")
				rock += 30
			elif randomEventID == 7:
				if wood >= discoverers and rock >= discoverers:
					print("\n-------The discoverers made a pretty big break through on the current technology-------\n\n + 10 discovery points\n")
					changeP = 10
			elif randomEventID == 8:
					if population >= 16 :
						print("\n-------Many people came from far and wide to live with your people. Perhaps too many-------\n\n + 15 population\n")
						population += 15
					else:
						print("\n-------People came out of the woods and stayed-------\n\n + 6 population\n")
						population += 6
		
		#happens if ages are 31 - 40
		if age >= 31 and age <= 40:
			randomEventID = rand.randint(1,8)
			#adds food
			if randomEventID == 1:
				print("\n-------Your people have found a herd of meat beasts YAS!-------\n\n + 40 food\n")
				food += 40
			#adds 
			elif randomEventID == 2:
				print("\n-------Your people found a small oasis!-------\n\n + 35 water \n + 15 food\n")
				water += 35
				food += 15
			elif randomEventID == 3:
				print("\n-------Your people have recently found fallen MASSIVE trees in the forest!-------\n\n + 25 wood\n")
				wood += 25
			elif randomEventID == 4:
				print("\n-------A small epidemic swept through you civilation!-------\n\n - population halved!\n")
				population = math.floor(population / 2)
			elif randomEventID == 5:
				print("\n-------OH NO our storage had a leak and things became unusable-------\n\n- 10 wood\n- 8 rock\n- 10 food \n- 10 water\n")
				if wood >= 10 :
					wood -= 10
				else :
					wood = 0
				if rock >= 8 :
					rock -= 8
				else :
					rock = 0
				if food >= 10 :
					food -= 10
				else :
					food = 0
				if water >= 10 :
					water -= 10
				else :
					water = 0
			elif randomEventID == 6:
				print("\n-------ROCKS FELL FROM THE SKY BRO!-------\n\n + 30 rock\n")
				rock += 30
			elif randomEventID == 7:
				if wood >= discoverers and rock >= discoverers :
					print("\n-------The discoverers made a break through on the current technology-------\n\n + 15 discovery points\n")
					changeP = 15
			elif randomEventID == 8:
					if population >= 24 :
						print("\n-------Many people came from far and wide to live with your people. Perhaps too many-------\n\n + 20 population\n")
						population += 20
					else:
						print("\n-------People came out of the woods and stayed-------\n\n + 9 population\n")
						population += 9
		
		#happens if ages are 41 - 50
		if age >= 41 and age <= 50:
			randomEventID = rand.randint(1,9)
			#adds food
			if randomEventID == 1:
				print("\n-------In celebration of you, your people have cooked a feast!-------\n\n + 50 food\n")
				food += 50
			#adds food and water
			elif randomEventID == 2:
				print("\n-------Your people found a large oasis!-------\n\n + 45 water \n + 20 food\n")
				water += 45
				food += 20
			#adds wood
			elif randomEventID == 3:
				print("\n-------Your people have recently found fallen GIGANTIC trees in the forest!-------\n\n + 35 wood\n")
				wood += 35
			#cuts population into a third
			elif randomEventID == 4:
				print("\n-------A huge epidemic swept through you civilation!-------\n\n - population reduced to a third!\n")
				population = math.floor(population / 3)
			#lose 15 wood, 15 food, 15 water, 13 rock
			elif randomEventID == 5:
				print("\n-------OH NO our storage had a leak and things became unusable-------\n\n- 15 wood\n- 13 rock\n- 15 food \n- 15 water\n")
				if wood >= 15 :
					wood -= 15
				else :
					wood = 0
				if rock >= 13 :
					rock -= 13
				else :
					rock = 0
				if food >= 15 :
					food -= 15
				else :
					food = 0
				if water >= 15 :
					water -= 15
				else :
					water = 0
			elif randomEventID == 6:
				print("\n-------HUGE ROCKS FELL FROM THE SKY BROOO!-------\n\n + 40 rock\n")
				rock += 40
			elif randomEventID == 7:
				if wood >= discoverers and rock >= discoverers :
					print("\n-------The discoverers made a break through on the current technology-------\n\n + 20 discovery points\n")
					changeP = 20
			elif randomEventID == 8:
				if population >= 32 :
					print("\n-------Many people came from far and wide to live with your people. Perhaps too many-------\n\n + 25 population\n")
					population += 25
				else:
					print("\n-------People came out of the woods and stayed-------\n\n + 12 population\n")
					population += 12
			elif randomEventID == 9 and leader == True :
				leaderElection()
				
#Deals with the bug that allows you to keep extra people in jobs when they should actually be dead or unemployed
def loseJobs() :
	global unemployedMax, discoverersMax, farmersMax, discoverers, farmers, waterers, waterersMax
	
	if age > 15 and didPeopleDie == True :
		availablePop = population
		discoverers = 0
		farmers = 0
		waterers = 0
		unemployed = 0

		while availablePop >= 0 :
			whoLives = rand.randint(1,4)
			if whoLives == 1 and discoverers < int(discoverersMax) :
				discoverers += 1
				availablePop -= 1
			elif whoLives == 2 and farmers < int(farmersMax) :
				farmers += 1
				availablePop -= 1
			elif whoLives == 3 and waterers < int(waterersMax) :
				waterers += 1
				availablePop -= 1
			elif whoLives == 4 and unemployed < int(unemployedMax) :
				unemployed += 1
				availablePop -= 1
			else :
				unemployed += 1
				availablePop -= 1

#Saves current max amount of people in every profession
def saveProfessions() :
	global unemployedMax, discoverersMax, farmersMax, waterersMax

	unemployedMax = hiddenPopulation
	discoverersMax = discoverers
	farmersMax = farmers
	waterersMax = waterers

#Determines the leader's traits and changes specific things depending on those traits
def leaderEffects() :
	global changeP,modifierF,modifierW,food

	if leader == True :
		
		#decides benefits from strength
		if ldrStrength <= 20 :
			#no benefits
			pass
		elif ldrStrength > 20 and ldrStrength <= 40 :
			#some small benefits
			if farmers >= 1:
				food += math.floor(farmers * (.2 * farms))
		elif ldrStrength > 40 and ldrStrength <= 60 :
			#some decent benefits
			if farmers >= 1:
				food += math.floor(farmers * (.5 * farms))
		elif ldrStrength > 60 and ldrStrength <= 80 :
			#some good benefits
			if farmers >= 1:
				food += math.floor(farmers * (.7 * farms))
		elif ldrStrength > 80 and ldrStrength < 100 :
			#some great benefits
			if farmers >= 1:
				food += math.floor(farmers * (1 * farms))
		elif ldrStrength == 100 :
			#some epic benefits
			if farmers >= 1:
				food += math.floor(farmers * (2 * farms))

		#decides benefits from intellect
		if ldrIntellect <= 20 :
			#no benefits
			pass
		elif ldrIntellect > 20 and ldrIntellect <= 40 :
			#some small benefits
			changeP += discoverers * .2
		elif ldrIntellect > 40 and ldrIntellect <= 60 :
			#some decent benefits
			changeP += discoverers * .5
		elif ldrIntellect > 60 and ldrIntellect <= 80 :
			#some good benefits
			changeP += discoverers * .7
		elif ldrIntellect > 80 and ldrIntellect < 100 :
			#some great benefits
			changeP += discoverers * 1
		elif ldrIntellect == 100 :
			#some epic benefits
			changeP += discoverers * 2

		#decides benefits from diplomacy
		if ldrDiplomacy <= 20 :
			#no benefits
			pass
		elif ldrDiplomacy > 20 and ldrDiplomacy <= 40 :
			#some small benefits
			pass
		elif ldrDiplomacy > 40 and ldrDiplomacy <= 60 :
			#some decent benefits
			pass
		elif ldrDiplomacy > 60 and ldrDiplomacy <= 80 :
			#some good benefits
			pass
		elif ldrDiplomacy > 80 and ldrDiplomacy <= 100 :
			#some great benefits
			pass

		#decides benefits from social skills
		if ldrSocials <= 20 :
			#no benefits
			pass
		elif ldrSocials > 20 and ldrSocials <= 40 :
			#some small benefits
			modifierF -= .06
			modifierW -= .06
		elif ldrSocials > 40 and ldrSocials <= 60 :
			#some decent benefits
			modifierF -= .1
			modifierW -= .1
		elif ldrSocials > 60 and ldrSocials <= 80 :
			#some good benefits
			modifierF -= .13
			modifierW -= .13
		elif ldrSocials > 80 and ldrSocials < 100 :
			#some great benefits
			modifierF -= .15
			modifierW -= .15
		elif ldrSocials == 100 :
			#Le Epico benefits
			modifierF -= .2
			modifierW -= .2

#Controls choosing the leader
def leaderElection() :
	global ldrStrength, ldrIntellect, ldrDiplomacy, ldrSocials, ldrName, ldrNameList

	done = False

	if leader == True :
		ldrNameIndex = rand.randint(1,10)
		ldrName = ldrNameList[ldrNameIndex]
		ldrNameList.remove(ldrName)
		ldrStrength = rand.randint(1, 100)
		ldrIntellect = rand.randint(1, 100)
		ldrDiplomacy = rand.randint(1, 100)
		ldrSocials = rand.randint(1, 100)

		ldrNameIndex2 = rand.randint(1,9)
		ldrName2 = ldrNameList[ldrNameIndex2]
		ldrNameList.remove(ldrName2)
		ldrStrength2 = rand.randint(1, 100)
		ldrIntellect2 = rand.randint(1, 100)
		ldrDiplomacy2 = rand.randint(1, 100)
		ldrSocials2 = rand.randint(1, 100)
		
		ldrNameIndex3 = rand.randint(1,8)
		ldrName3 = ldrNameList[ldrNameIndex3]
		ldrNameList.remove(ldrName3)
		ldrStrength3 = rand.randint(1, 100)
		ldrIntellect3 = rand.randint(1, 100)
		ldrDiplomacy3 = rand.randint(1, 100)
		ldrSocials3 = rand.randint(1, 100)
		
		print("\n-----------ELECTION-------------")
		print("1.",ldrName)
		print("Strength:",ldrStrength)
		print("Intellect:",ldrIntellect)
		print("Diplomacy:",ldrDiplomacy)
		print("Socials:",ldrSocials)
		print("--------------------------------")
		print("2.",ldrName2)
		print("Strength:",ldrStrength2)
		print("Intellect:",ldrIntellect2)
		print("Diplomacy:",ldrDiplomacy2)
		print("Socials:",ldrSocials2)
		print("--------------------------------")
		print("3.",ldrName3)
		print("Strength:",ldrStrength3)
		print("Intellect:",ldrIntellect3)
		print("Diplomacy:",ldrDiplomacy3)
		print("Socials:",ldrSocials3)
		print("--------------------------------\n")

		while done == False :

			action = input("Which leader would you like to elect? (type help for what each stat does!):\n>> ")
			action = action.lower()
			if action == "1" or action == ldrName :
				done = True
			elif action == "2" or action == ldrName2 :
				ldrName = ldrName2
				ldrDiplomacy = ldrDiplomacy2
				ldrIntellect = ldrIntellect2
				ldrSocials = ldrSocials2
				ldrStrength = ldrStrength2
				done = True
			elif action == "3" or action == ldrName3 :
				ldrName = ldrName3
				ldrStrength = ldrStrength3
				ldrIntellect = ldrIntellect3
				ldrDiplomacy = ldrDiplomacy3
				ldrSocials = ldrSocials3
				done = True
			elif action == "help" :
				print("\n-Strength: corralates to more farm production.\n-Intellect: corralates to more discovery points.\n-Diplomacy: is a work in progress at the moment.\n-Socials: corralates to a decrease in food intake because people are happier, so they eat less food.\n")
			else :
				print("That's an invalid response!\n")

#The main update function that controls everything needed to go from one age to the next
def update() :
	global age, actions, ageUpdate, prevPop
	age += 1
	prevPop = population
	clear()
	randomEvents()
	leaderEffects()
	saveProfessions()
	foodWater()
	loseJobs()
	populationGain()
	farmsProduction()
	updateDiscResources()
	expansionFunc()
	surroundings()
	actions = 1
	ageUpdate = True

loading = input("Would you like to load previously saved progress?: Y/N")
loading.lower()

if loading == "y" :
	load()

print("\n\n===At any time during the game you may type 'save' and all of your progress will be saved===\n\n")
gameOn = True
surroundings()

#Main game loop	
while gameOn == True:
	
	while actions == 1 :			
	
		#ages 1 - 10
		if gameOn == True :
			#age 1 options
			
			if age == 1 :
					action = input(" |1. Grow Tree (2x trees) \n |2. Chop Tree (minus tree for wood)\n")
					action.lower()
					if action == "1" or  action == "grow tree" :
						trees = trees * 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						trees -= 1
						wood += 5
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					elif action == "haha":
						food = 99999999999
						trees = 99999999999
						water = 999999999999
						wood = 99999999999
						
					else :
						age = 1
						print("That's not an option!")

			#age 2 options
			elif age == 2 :
					action = input(" |1. Fish\n |2. Grow Tree\n |3. Shake Trees (gives some food and wood)\n")
					action.lower()
					if action == "1" or action == "fish" :
						food += 5
						water += population
						actions -= 1
					elif action == "2" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 1
						actions -= 1
					elif action == "3" or action == "shake trees" :
						if trees == 0 :
							age = 2
							print("You have no trees to shake!")
						else :
							food += trees * 2
							wood += trees
							actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						age = 2
						print("That's not an option!")

			#age 3 options
			elif age == 3 :
					print("Someone recently tripped on a strange solid object. They have decided to name it rock.")
					action = input(" |1. Grow Tree\n |2. Chop Tree\n |3. Mine Rock\n |4. Shake Trees\n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 1
						actions -= 1
					elif action == "2" or action == "chop tree" :
						trees -= 1
						wood += 5
						actions -= 1
					elif action == "3" or action == "mine rock" :
						rock += 3
						actions -= 1
					elif action == "4" or action == "shake trees" :
						if trees == 0 :
							age = 3
							print("You have no trees to shake!")
						else :
							food += trees * 2
							wood += trees
							actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					elif action == "taco":
						rock += 9999999999999999
						
					else :
						age = 3
						print("That's not an option!")

			#age 4 options
			elif age == 4 :
					action = input(" |1. Grow Tree\n |2. Chop Tree\n |3. Mine Rock\n |4. Fish\n |5. Make Pickaxe (you gain more resources)\n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 1
						actions -= 1
					elif action == "2" or action == "chop tree" :
						trees -= 1
						wood += 5
						actions -= 1
					elif action == "3" or action == "mine rock" :
						rock += 3
						actions -= 1
					elif action == "4" or action == "fish" :
						food += 5
						water += population
						actions -= 1
					elif action == "5" or action == "make pickaxe" :
						technology.append("pickaxe")
						pickaxe = True
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						age = 4
						print("That's not an option4!")

			#age 5 options
			elif age == 5 :
					action = input(" |1. Grow Tree\n |2. Chop Tree\n |3. Mine Rock\n |4. Fish\n |5. Make Pickaxe\n |6. Explore (Gives food, water, wood, and rock)\n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							if pickaxe == True :
								trees += 2
							else :
								trees += 1
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if pickaxe == True :
							trees -= 1
							wood += 10
						else :
							trees -= 1
							wood += 5
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if pickaxe == True :
							rock += 6
						else :
							rock += 3
						actions -= 1
					elif action == "4" or action == "fish" :
						if pickaxe == True :
							food += 12
							water += population * 2
						else :
							food += 6
							water += population
						actions -= 1
					elif action == "5" or action == "make pickaxe" :
						if pickaxe == True :
							age = 5
							print("You already have this technology!")
						else :
							technology.append("pickaxe")
							pickaxe = True
							actions -= 1
					elif action == "6" or action == "explore" :
						if pickaxe == True :
							wood += 4
							food += 6
							rock += 4
						else :
							wood += 2
							food += 3
							rock += 2
						water += 5
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						age = 5
						print("That's not an option!")

			#age 6 options
			elif age == 6 :
					action = input(" |1. Grow Tree\n |2. Chop Tree\n |3. Mine Rock\n |4. Fish\n |5. Make Pickaxe\n |6. Explore\n |7. Make Farm (food per year but takes 1 water per farm)\n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							if pickaxe == True :
								trees += 2
							else :
								trees += 1
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if pickaxe == True :
							trees -= 1
							wood += 10
						else :
							trees -= 1
							wood += 5
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if pickaxe == True :
							rock += 6
						else :
							rock += 3
						actions -= 1
					elif action == "4" or action == "fish" :
						if pickaxe == True :
							food += 12
							water += population * 2
						else :
							food += 6
							water += population
						actions -= 1
					elif action == "5" or action == "make pickaxe" :
						if pickaxe == True :
							age = 6
							print("You already have this technology!")
						else :
							technology.append("pickaxe")
							pickaxe = True
							actions -= 1
					elif action == "6" or action == "explore" :
						if pickaxe == True :
							wood += 4
							food += 6
							rock += 4
						else :
							wood += 2
							food += 3
							rock += 2
						water += 5
						actions -= 1
					elif action == "7" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							age = 6				
							print("You don't have enough resources!")
					elif action == "save" :
						save()
						actions -= 1
					else :
						age = 6
						print("That's not an option!")

			#age 7 options
			elif age == 7 :
					action = input(" |1. Grow Tree\n |2. Chop Tree\n |3. Mine Rock\n |4. Fish\n |5. Make Pickaxe\n |6. Explore\n |7. Make Farm\n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							if pickaxe == True :
								trees += 2
							else :
								trees += 1
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if pickaxe == True :
							trees -= 1
							wood += 10
						else :
							trees -= 1
							wood += 5
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if pickaxe == True :
							rock += 6
						else :
							rock += 3
						actions -= 1
					elif action == "4" or action == "fish" :
						if pickaxe == True :
							food += 12
							water += population * 2
						else :
							food += 6
							water += population
						actions -= 1
					elif action == "5" or action == "make pickaxe" :
						if pickaxe == True :
							age = 7
							print("You already have this technology!")
						else :
							technology.append("pickaxe")
							pickaxe = True
							actions -= 1
					elif action == "6" or action == "explore" :
						if pickaxe == True :
							wood += 4
							food += 6
							rock += 4
						else :
							wood += 2
							food += 3
							rock += 2
						water += 5
						actions -= 1
					elif action == "7" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							age = 7			
							print("You don't have enough resources!")
					elif action == "save" :
						save()
						actions -= 1
					else :
						age = 7
						print("That's not an option!")

			#age 8 options
			elif age == 8 :
					action = input(" |1. Grow Tree\n |2. Chop Tree\n |3. Mine Rock\n |4. Fish\n |5. Make Pickaxe\n |6. Explore\n |7. Make Farm\n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							if pickaxe == True :
								trees += 2
							else :
								trees += 1
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if pickaxe == True :
							trees -= 1
							wood += 10
						else :
							trees -= 1
							wood += 5
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if pickaxe == True :
							rock += 6
						else :
							rock += 3
						actions -= 1
					elif action == "4" or action == "fish" :
						if pickaxe == True :
							food += 12
							water += population * 2
						else :
							food += 6
							water += population
						actions -= 1
					elif action == "5" or action == "make pickaxe" :
						if pickaxe == True :
							age = 8
							print("You already have this technology!")
						else :
							technology.append("pickaxe")
							pickaxe = True
							actions -= 1
					elif action == "6" or action == "explore" :
						if pickaxe == True :
							wood += 4
							food += 6
							rock += 4
						else :
							wood += 2
							food += 3
							rock += 2
						water += 5
						actions -= 1
					elif action == "7" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							age = 8
							print("You don't have enough resources!")
					elif action == "save" :
						save()
						actions -= 1
					else :
						age = 8
						print("That's not an option!")

			#age 9 options
			elif age == 9 :
					action = input(" |1. Grow Tree\n |2. Chop Tree\n |3. Mine Rock\n |4. Fish\n |5. Make Pickaxe\n |6. Explore\n |7. Make Farm\n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							if pickaxe == True :
								trees += 2
							else :
								trees += 1
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if pickaxe == True :
							trees -= 1
							wood += 10
						else :
							trees -= 1
							wood += 5
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if pickaxe == True :
							rock += 6
						else :
							rock += 3
						actions -= 1
					elif action == "4" or action == "fish" :
						if pickaxe == True :
							food += 12
							water += population * 2
						else :
							food += 6
							water += population
						actions -= 1
					elif action == "5" or action == "make pickaxe" :
						if pickaxe == True :
							age = 9
							print("You already have this technology!")
						else :
							technology.append("pickaxe")
							pickaxe = True
							actions -= 1
					elif action == "6" or action == "explore" :
						if pickaxe == True :
							wood += 4
							food += 6
							rock += 4
						else :
							wood += 2
							food += 3
							rock += 2
						water += 5
						actions -= 1
					elif action == "7" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							age = 9		
							print("You don't have enough resources!")
					elif action == "save" :
						save()
						actions -= 1
					else :
						age = 9
						print("That's not an option!")
			
			#age 10 options
			elif age == 10 :
					print("While mining rock we found water deep in ground, and we will make water pit.")
					if pickaxe == False :
						action = input(" |1. Grow Tree\n |2. Chop Tree\n |3. Mine Rock\n |4. Fish\n |5. Explore\n |6. Make Farm\n |7. Make Water pit\n |8. Make Pickaxe\n")
					else :
						action = input(" |1. Grow Tree\n |2. Chop Tree\n |3. Mine Rock\n |4. Fish\n |5. Explore\n |6. Make Farm\n |7. Make Water Pit (doubles the water you get)\n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							if pickaxe == True :
								trees += 2
							else :
								trees += 1
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if pickaxe == True :
							trees -= 1
							wood += 10
						else :
							trees -= 1
							wood += 5
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if pickaxe == True :
							rock += 6
						else :
							rock += 3
						actions -= 1
					elif action == "4" or action == "fish" :
						if pickaxe == True :
							food += 12
							water += population * 2
						else :
							food += 6
							water += population
						actions -= 1
					elif action == "8" or action == "make pickaxe" :
						if pickaxe == True :
							age = 10
							print("You already have this technology!")
						else :
							technology.append("pickaxe")
							pickaxe = True
							actions -= 1
					elif action == "5" or action == "explore" :
						if pickaxe == True :
							wood += 4
							food += 6
							rock += 4
						else :
							wood += 2
							food += 3
							rock += 2
						water += 5
						actions -= 1
					elif action == "6" or action == "make farm":
						print(action)
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							age = 10		
							print("You don't have enough resources!")
					elif action == "7" or action == "make water pit":
						technology.append("water pit")
						waterPit = True
						rock += 3
						water += 3
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						age = 10
						print("That's not an option!")
		
		#ages 11 - 20
		if gameOn == True :
			#age 11 options
			if age == 11 :
					if pickaxe == False :
						action = input(" |1. Grow Tree\n |2. Chop Tree\n |3. Mine Rock\n |4. Fish\n |5. Explore\n |6. Make Farm\n |7. Embark on a water expedition (gives lots of water)\n |8. Make Water pit\n |9. Make Pickaxe\n")
					else :
						action = input(" |1. Grow Tree\n |2. Chop Tree\n |3. Mine Rock\n |4. Fish\n |5. Explore\n |6. Make Farm\n |7. Embark on a water expedition\n |8. Make Water Pit\n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							if pickaxe == True :
								trees += 2
							else :
								trees += 1
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if pickaxe == True :
							trees -= 1
							wood += 10
						else :
							trees -= 1
							wood += 5
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if pickaxe == True :
							rock += 6
						else :
							rock += 3
						actions -= 1
					elif action == "4" or action == "fish" :
						if pickaxe == True :
							food += 12
						else :
							food += 6
						water += population
						actions -= 1
					elif action == "9" or action == "make pickaxe" :
						if pickaxe == True :
							age = 11
							print("You already have this technology!")
						else :
							technology.append("pickaxe")
							pickaxe = True
							actions -= 1
					elif action == "5" or action == "explore" :
						if pickaxe == True :
							wood += 4
							food += 6
							rock += 4
						else :
							wood += 2
							food += 3
							rock += 2
						if waterPit == True :
							water += 10
						else :
							water += 5
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							age = 11	
							print("You don't have enough resources!")
					elif action == "8" or action == "make water pit" :
						if waterPit == False :
							technology.append("water pit")
							waterPit = True
							rock += 3
							water += 3
							actions -= 1
						else :
							age = 11
							print("You already have this technology!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						age = 11
						print("That's not an option!")

			#age 12 options
			elif age == 12 :
					if pickaxe == False :
						action = input(" |1. Grow Tree\n |2. Chop Tree\n |3. Mine Rock\n |4. Fish\n |5. Explore\n |6. Make Farm\n |7. Embark on a water expedition\n |8. Make Water pit\n |9. Make Pickaxe\n")
					else :
						action = input(" |1. Grow Tree\n |2. Chop Tree\n |3. Mine Rock\n |4. Fish\n |5. Explore\n |6. Make Farm\n |7. Embark on a water expedition\n |8. Make Water Pit\n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							if pickaxe == True :
								trees += 2
							else :
								trees += 1
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if pickaxe == True :
							trees -= 1
							wood += 10
						else :
							trees -= 1
							wood += 5
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if pickaxe == True :
							rock += 6
						else :
							rock += 3
						actions -= 1
					elif action == "4" or action == "fish" :
						if pickaxe == True :
							food += 12
						else :
							food += 6
						water += population
						actions -= 1
					elif action == "9" or action == "make pickaxe" :
						if pickaxe == True :
							age = 12
							print("You already have this technology!")
						else :
							technology.append("pickaxe")
							pickaxe = True
							actions -= 1
					elif action == "5" or action == "explore" :
						if pickaxe == True :
							wood += 4
							food += 6
							rock += 4
						else :
							wood += 2
							food += 3
							rock += 2
						if waterPit == True :
							water += 10
						else :
							water += 5
						actions -= 1
					elif action == "6" or action == "make farm":

						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							age = 12
							print("You don't have enough resources!")
					elif action == "8" or action == "make water pit":
						if waterPit == True :
							age = 12
							print("You already have this technology!")
						else:
							technology.append("water pit")
							waterPit = True
							rock += 3
							water += 3
							actions -= 1
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						age = 12
						print("That's not an option!")
					
			#age 13 options
			elif age == 13 :
					if pickaxe == False :
						action = input(" |1. Grow Tree\n |2. Chop Tree\n |3. Mine Rock\n |4. Fish\n |5. Explore\n |6. Make Farm\n |7. Embark on a water expedition\n |8. Make Water pit\n |9. Make Pickaxe\n")
					else :
						action = input(" |1. Grow Tree\n |2. Chop Tree\n |3. Mine Rock\n |4. Fish\n |5. Explore\n |6. Make Farm\n |7. Embark on a water expedition\n |8. Make Water Pit\n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							if pickaxe == True :
								trees += 2
							else :
								trees += 1
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if pickaxe == True :
							trees -= 1
							wood += 10
						else :
							trees -= 1
							wood += 5
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if pickaxe == True :
							rock += 6
						else :
							rock += 3
						actions -= 1
					elif action == "4" or action == "fish" :
						if pickaxe == True :
							food += 12
						else :
							food += 6
						water += population
						actions -= 1
					elif action == "9" or action == "make pickaxe" :
						if pickaxe == True :
							age = 13
							print("You already have this technology!")
						else :
							technology.append("pickaxe")
							pickaxe = True
							actions -= 1
					elif action == "5" or action == "explore" :
						if pickaxe == True :
							wood += 4
							food += 6
							rock += 4
						else :
							wood += 2
							food += 3
							rock += 2
						if waterPit == True :
							water += 10
						else :
							water += 5
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							age = 13
							print("You don't have enough resources!")
					elif action == "8" or action == "make water pit":
						if waterPit == True :
							age = 13
							print("You already have this technology!")
						else:
							technology.append("water pit")
							waterPit = True
							rock += 3
							water += 3
							actions -= 1
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						age = 13
						print("That's not an option!")

			#age 14 options
			elif age == 14 :
					ageUpdate == True
					if pickaxe == False :
						action = input(" |1. Grow Tree\n |2. Chop Tree\n |3. Mine Rock\n |4. Fish\n |5. Explore\n |6. Make Farm\n |7. Embark on a water expedition\n |8. Make Water pit\n |9. Make Pickaxe\n")
					else :
						action = input(" |1. Grow Tree\n |2. Chop Tree\n |3. Mine Rock\n |4. Fish\n |5. Explore\n |6. Make Farm\n |7. Embark on a water expedition\n |8. Make Water Pit\n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							if pickaxe == True :
								trees += 2
							else :
								trees += 1
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if pickaxe == True :
							trees -= 1
							wood += 10
						else :
							#Its the bestest year right here
							#Its the year were in EZ
							trees -= 1
							wood += 5
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if pickaxe == True :
							rock += 6
						else :
							rock += 3
						actions -= 1
					elif action == "4" or action == "fish" :
						if pickaxe == True :
							food += 12
						else :
							food += 6
						water += population
						actions -= 1
					elif action == "9" or action == "make pickaxe" :
						if pickaxe == True :
							ageUpdate = False
							print("You already have this technology!")
						else :
							technology.append("pickaxe")
							pickaxe = True
							actions -= 1
					elif action == "5" or action == "explore" :
						if pickaxe == True :
							wood += 4
							food += 6
							rock += 4
						else :
							wood += 2
							food += 3
							rock += 2
						if waterPit == True :
							water += 10
						else :
							water += 5
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "8" or action == "make water pit":
						if waterPit == True :
							ageUpdate = False
							print("You already have this technology!")
						else:
							technology.append("water pit")
							waterPit = True
							rock += 3
							water += 3
							actions -= 1
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 15 options
			elif age == 15 :
					ageUpdate == True
					print("We found a new way to discover new technologies. We have now assigned people to become discoverers. Also the discoverers quickly discover there first thing!! A way to water farms better. We'll call it water tunnels.")
					if waterTunnels == False :
						technology.append("water tunnels")
						waterTunnels = True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager (doesnt cost an action) \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							if pickaxe == True :
								trees += 2
							else :
								trees += 1
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if pickaxe == True :
							trees -= 1
							wood += 10
						else :
							trees -= 1
							wood += 5
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if pickaxe == True :
							rock += 10
						else :
							rock += 5
						actions -= 1
					elif action == "4" or action == "fish" :
						if pickaxe == True :
							food += 16
						else :
							food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if pickaxe == True :
							wood += 6
							food += 8
							rock += 6
						else :
							wood += 3
							food += 4
							rock += 3
						if waterPit == True :
							water += 14
						else :
							water += 7
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 16 options
			elif age == 16 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							if pickaxe == True :
								trees += 2
							else :
								trees += 1
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if pickaxe == True :
							trees -= 1
							wood += 10
						else :
							trees -= 1
							wood += 5
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if pickaxe == True :
							rock += 10
						else :
							rock += 5
						actions -= 1
					elif action == "4" or action == "fish" :
						if pickaxe == True :
							food += 16
						else :
							food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if pickaxe == True :
							wood += 6
							food += 8
							rock += 6
						else :
							wood += 3
							food += 4
							rock += 3
						if waterPit == True :
							water += 16
						else :
							water += 8
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 17 options
			elif age == 17 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							if pickaxe == True :
								trees += 2
							else :
								trees += 1
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if pickaxe == True :
							trees -= 1
							wood += 10
						else :
							trees -= 1
							wood += 5
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if pickaxe == True :
							rock += 10
						else :
							rock += 5
						actions -= 1
					elif action == "4" or action == "fish" :
						if pickaxe == True :
							food += 16
						else :
							food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if pickaxe == True :
							wood += 6
							food += 8
							rock += 6
						else :
							wood += 3
							food += 4
							rock += 3
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 18 options
			elif age == 18 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							if pickaxe == True :
								trees += 2
							else :
								trees += 1
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if pickaxe == True :
							trees -= 1
							wood += 10
						else :
							trees -= 1
							wood += 5
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if pickaxe == True :
							rock += 10
						else :
							rock += 5
						actions -= 1
					elif action == "4" or action == "fish" :
						if pickaxe == True and corn == True :
							food += 24
						elif (pickaxe == True or corn == True) and (corn == False or pickaxe == False) :
							food += 16
						else :
							food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if pickaxe == True and corn == True :
							wood += 6
							food += 12
							rock += 6
						elif (pickaxe == True or corn == True) and (corn == False or pickaxe == False) :
							wood += 6
							food += 8
							rock += 6
						else :
							wood += 3
							food += 4
							rock += 3
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 19 options
			elif age == 19 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							if pickaxe == True :
								trees += 2
							else :
								trees += 1
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if pickaxe == True :
							trees -= 1
							wood += 10
						else :
							trees -= 1
							wood += 5
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if pickaxe == True :
							rock += 10
						else :
							rock += 5
						actions -= 1
					elif action == "4" or action == "fish" :
						if pickaxe == True and corn == True :
							food += 24
						elif (pickaxe == True or corn == True) and (corn == False or pickaxe == False) :
							food += 16
						else :
							food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if pickaxe == True and corn == True :
							wood += 6
							food += 12
							rock += 6
						elif (pickaxe == True or corn == True) and (corn == False or pickaxe == False) :
							wood += 6
							food += 8
							rock += 6
						else :
							wood += 3
							food += 4
							rock += 3
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 20 options
			elif age == 20 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition\n|8. Job manager \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							if pickaxe == True :
								trees += 2
							else :
								trees += 1
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if pickaxe == True :
							trees -= 1
							wood += 10
						else :
							trees -= 1
							wood += 5
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if pickaxe == True :
							rock += 10
						else :
							rock += 5
						actions -= 1
					elif action == "4" or action == "fish" :
						if pickaxe == True and corn == True :
							food += 24
						elif (pickaxe == True or corn == True) and (corn == False or pickaxe == False) :
							food += 16
						else :
							food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if pickaxe == True and corn == True :
							wood += 6
							food += 12
							rock += 6
						elif (pickaxe == True or corn == True) and (corn == False or pickaxe == False) :
							wood += 6
							food += 8
							rock += 6
						else :
							wood += 3
							food += 4
							rock += 3
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

		#ages 21 - 30
		if gameOn == True :
			#age 21 options
			if age == 21 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							if pickaxe == True :
								trees += 2
							else :
								trees += 1
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if pickaxe == True :
							trees -= 1
							wood += 10
						else :
							trees -= 1
							wood += 5
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if pickaxe == True :
							rock += 10
						else :
							rock += 5
						actions -= 1
					elif action == "4" or action == "fish" :
						if pickaxe == True and corn == True :
							food += 24
						elif (pickaxe == True or corn == True) and (corn == False or pickaxe == False) :
							food += 16
						else :
							food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if pickaxe == True and corn == True :
							wood += 6
							food += 12
							rock += 6
						elif (pickaxe == True or corn == True) and (corn == False or pickaxe == False) :
							wood += 6
							food += 8
							rock += 6
						else :
							wood += 3
							food += 4
							rock += 3
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 22 options
			elif age == 22 :
					if pickaxe == False :
						pickaxe = True
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						trees -= 1
						wood += 10
						actions -= 1
					elif action == "3" or action == "mine rock" :
						rock += 10
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							food += 24
						else :
							food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							wood += 6
							food += 12
							rock += 6
						else :
							wood += 3
							food += 4
							rock += 3
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 23 options
			elif age == 23 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						trees -= 1
						wood += 10
						actions -= 1
					elif action == "3" or action == "mine rock" :
						rock += 10
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							food += 24
						else :
							food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							wood += 6
							food += 12
							rock += 6
						else :
							wood += 3
							food += 4
							rock += 3
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 24 options
			elif age == 24 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						trees -= 1
						wood += 10
						actions -= 1
					elif action == "3" or action == "mine rock" :
						rock += 10
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							food += 24
						else :
							food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							wood += 6
							food += 12
							rock += 6
						else :
							wood += 3
							food += 4
							rock += 3
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 25 options
			elif age == 25 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						trees -= 1
						wood += 10
						actions -= 1
					elif action == "3" or action == "mine rock" :
						rock += 10
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							food += 24
						else :
							food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							wood += 6
							food += 12
							rock += 6
						else :
							wood += 3
							food += 4
							rock += 3
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 26 options
			elif age == 26 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						trees -= 1
						wood += 10
						actions -= 1
					elif action == "3" or action == "mine rock" :
						rock += 10
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							food += 24
						else :
							food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							wood += 6
							food += 12
							rock += 6
						else :
							wood += 3
							food += 4
							rock += 3
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 27 options
			elif age == 27 :
					ageUpdate == True
					i = 0
					if i == 0 :
						print("We can now build houses for ourselves; the more houses you have the less resources you use!")
						i += 1
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house (People consume less food and water) \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						trees -= 1
						wood += 10
						actions -= 1
					elif action == "3" or action == "mine rock" :
						rock += 10
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							food += 24
						else :
							food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							wood += 6
							food += 12
							rock += 6
						else :
							wood += 3
							food += 4
							rock += 3
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 28 options
			elif age == 28 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						trees -= 1
						wood += 10
						actions -= 1
					elif action == "3" or action == "mine rock" :
						rock += 10
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							food += 24
						else :
							food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							wood += 6
							food += 12
							rock += 6
						else :
							wood += 3
							food += 4
							rock += 3
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 29 options
			elif age == 29 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						trees -= 1
						wood += 10
						actions -= 1
					elif action == "3" or action == "mine rock" :
						rock += 10
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							food += 24
						else :
							food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							wood += 6
							food += 12
							rock += 6
						else :
							wood += 3
							food += 4
							rock += 3
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":

						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 30 options
			elif age == 30 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						trees -= 1
						wood += 10
						actions -= 1
					elif action == "3" or action == "mine rock" :
						rock += 10
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							food += 24
						else :
							food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							wood += 6
							food += 12
							rock += 6
						else :
							wood += 3
							food += 4
							rock += 3
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":

						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")
		
		#ages 31 - 40
		if gameOn == True :
			#age 31 options
			if age == 31 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if iron == True :
							wood += 20
						else :
							wood += 10
						trees -= 1
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if iron == True :
							rock += 20
						else :
							rock += 10
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							if iron == True :
								food += 48
							else :
								food += 24
						else :
							if iron == True :
								food += 16
							else :
								food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							food += 12
						else :
							food += 4
						if iron == True :
							wood += 12
							rock += 12
						else :
							wood += 6
							rock += 6
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 32 options
			elif age == 32 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if iron == True :
							wood += 20
						else :
							wood += 10
						trees -= 1
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if iron == True :
							rock += 20
						else :
							rock += 10
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							if iron == True :
								food += 48
							else :
								food += 24
						else :
							if iron == True :
								food += 16
							else :
								food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							food += 12
						else :
							food += 4
						if iron == True :
							wood += 12
							rock += 12
						else :
							wood += 6
							rock += 6
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":
						print(action)
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 33 options
			elif age == 33 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if iron == True :
							wood += 20
						else :
							wood += 10
						trees -= 1
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if iron == True :
							rock += 20
						else :
							rock += 10
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							if iron == True :
								food += 48
							else :
								food += 24
						else :
							if iron == True :
								food += 16
							else :
								food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							food += 12
						else :
							food += 4
						if iron == True :
							wood += 12
							rock += 12
						else :
							wood += 6
							rock += 6
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":
						print(action)
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 34 options
			elif age == 34 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if iron == True :
							wood += 20
						else :
							wood += 10
						trees -= 1
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if iron == True :
							rock += 20
						else :
							rock += 10
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							if iron == True :
								food += 48
							else :
								food += 24
						else :
							if iron == True :
								food += 16
							else :
								food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							food += 12
						else :
							food += 4
						if iron == True :
							wood += 12
							rock += 12
						else :
							wood += 6
							rock += 6
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":
						print(action)
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 35 options
			elif age == 35 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if iron == True :
							wood += 20
						else :
							wood += 10
						trees -= 1
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if iron == True :
							rock += 20
						else :
							rock += 10
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							if iron == True :
								food += 48
							else :
								food += 24
						else :
							if iron == True :
								food += 16
							else :
								food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							food += 12
						else :
							food += 4
						if iron == True :
							wood += 12
							rock += 12
						else :
							wood += 6
							rock += 6
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":
						print(action)
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 36 options
			elif age == 36 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if iron == True :
							wood += 20
						else :
							wood += 10
						trees -= 1
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if iron == True :
							rock += 20
						else :
							rock += 10
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							if iron == True :
								food += 48
							else :
								food += 24
						else :
							if iron == True :
								food += 16
							else :
								food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							food += 12
						else :
							food += 4
						if iron == True :
							wood += 12
							rock += 12
						else :
							wood += 6
							rock += 6
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":
						print(action)
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 37 options
			elif age == 37 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if iron == True :
							wood += 20
						else :
							wood += 10
						trees -= 1
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if iron == True :
							rock += 20
						else :
							rock += 10
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							if iron == True :
								food += 48
							else :
								food += 24
						else :
							if iron == True :
								food += 16
							else :
								food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							food += 12
						else :
							food += 4
						if iron == True :
							wood += 12
							rock += 12
						else :
							wood += 6
							rock += 6
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":
						print(action)
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 38 options
			elif age == 38 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if iron == True :
							wood += 20
						else :
							wood += 10
						trees -= 1
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if iron == True :
							rock += 20
						else :
							rock += 10
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							if iron == True :
								food += 48
							else :
								food += 24
						else :
							if iron == True :
								food += 16
							else :
								food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							food += 12
						else :
							food += 4
						if iron == True :
							wood += 12
							rock += 12
						else :
							wood += 6
							rock += 6
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":
						print(action)
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 39 options
			elif age == 39 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if iron == True :
							wood += 30
						else :
							wood += 15
						trees -= 1
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if iron == True :
							rock += 30
						else :
							rock += 15
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							if iron == True :
								food += 48
							else :
								food += 24
						else :
							if iron == True :
								food += 16
							else :
								food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							food += 12
						else :
							food += 4
						if iron == True :
							wood += 20
							rock += 20
						else :
							wood += 10
							rock += 10
						if waterPit == True :
							water += 18
						else :
							water += 9
						actions -= 1
					elif action == "6" or action == "make farm":
						print(action)
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")
				
			#age 40 options
			elif age == 40 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if iron == True :
							wood += 30
						else :
							wood += 15
						trees -= 1
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if iron == True :
							rock += 30
						else :
							rock += 15
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							if iron == True :
								food += 48
							else :
								food += 24
						else :
							if iron == True :
								food += 16
							else :
								food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							food += 15
						else :
							food += 5
						if iron == True :
							wood += 20
							rock += 20
						else :
							wood += 10
							rock += 10
						if waterPit == True :
							water += 20
						else :
							water += 10
						actions -= 1
					elif action == "6" or action == "make farm":
						print(action)
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")
		
		#ages 41 - 50
		if gameOn == True :
			#age 41 options
			if age == 41 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if iron == True :
							if extHeat == True :
								wood += 60
							else :
								wood += 30
						else :
							if extHeat == True :
								wood += 30
							else :
								wood += 15
						trees -= 1
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if iron == True :
							if extHeat == True :
								rock += 60
							else :
								rock += 30
						else :
							if extHeat == True :
								rock += 30
							else :
								rock += 15
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							if iron == True :
								if extHeat == True :
									food += 96
								else :
									food += 48
							else :
								if extHeat == True :
									food += 48
								else :
									food += 24
						else :
							if iron == True :
								food += 16
							else :
								food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							food += 15
						else :
							food += 5
						if iron == True :
							if extHeat == True :
								wood += 40
								rock += 40
							else :
								wood += 20
								rock += 20
						else :
							if extHeat == True :
								wood += 20
								rock += 20
							else :
								wood += 10
								rock += 10
						if waterPit == True :
							water += 20
						else :
							water += 10
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 42 options
			elif age == 42 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if iron == True :
							if extHeat == True :
								wood += 60
							else :
								wood += 30
						else :
							if extHeat == True :
								wood += 30
							else :
								wood += 15
						trees -= 1
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if iron == True :
							if extHeat == True :
								rock += 60
							else :
								rock += 30
						else :
							if extHeat == True :
								rock += 30
							else :
								rock += 15
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							if iron == True :
								if extHeat == True :
									food += 96
								else :
									food += 48
							else :
								if extHeat == True :
									food += 48
								else :
									food += 24
						else :
							if iron == True :
								food += 16
							else :
								food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							food += 15
						else :
							food += 5
						if iron == True :
							if extHeat == True :
								wood += 40
								rock += 40
							else :
								wood += 20
								rock += 20
						else :
							if extHeat == True :
								wood += 20
								rock += 20
							else :
								wood += 10
								rock += 10
						if waterPit == True :
							water += 20
						else :
							water += 10
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 43 options
			elif age == 43 :
				ageUpdate == True
				action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
				action.lower()
				if action == "1" or action == "grow tree" :
					if trees != 0 :
						trees = trees * 2
					else : 
						trees += 2
					actions -= 1
				elif action == "2" or action == "chop tree" :
					if iron == True :
						if extHeat == True :
							wood += 60
						else :
							wood += 30
					else :
						if extHeat == True :
							wood += 30
						else :
							wood += 15
					trees -= 1
					actions -= 1
				elif action == "3" or action == "mine rock" :
					if iron == True :
						if extHeat == True :
							rock += 60
						else :
							rock += 30
					else :
						if extHeat == True :
							rock += 30
						else :
							rock += 15
					actions -= 1
				elif action == "4" or action == "fish" :
					if corn == True :
						if iron == True :
							if extHeat == True :
								food += 96
							else :
								food += 48
						else :
							if extHeat == True :
								food += 48
							else :
								food += 24
					else :
						if iron == True :
							food += 16
						else :
							food += 8
					water += population
					actions -= 1
				elif action == "5" or action == "explore" :
					if corn == True :
						food += 15
					else :
						food += 5
					if iron == True :
						if extHeat == True :
							wood += 40
							rock += 40
						else :
							wood += 20
							rock += 20
					else :
						if extHeat == True :
							wood += 20
							rock += 20
						else :
							wood += 10
							rock += 10
					if waterPit == True :
						water += 20
					else :
						water += 10
					actions -= 1
				elif action == "6" or action == "make farm":
					if wood > 2 and water > 0 :
						makeFarms()
						actions -= 1
					else :
						ageUpdate = False
						print("You don't have enough resources!")
				elif action == "7" or action == "embark on a water expedition" :
					if waterPit == True :
						water += population * 4
					else :
						water += population * 2
					actions -= 1
				elif action == "8" or action == "job manager" :
					jobManager()
				elif action == "9" or action == "build house" :
					makeHouse()
					actions -= 1
				elif action == "save" :
					save()
					actions -= 1
				else :
					ageUpdate = False
					print("That's not an option!")

			#age 44 options
			if age == 44 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if iron == True :
							if extHeat == True :
								wood += 60
							else :
								wood += 30
						else :
							if extHeat == True :
								wood += 30
							else :
								wood += 15
						trees -= 1
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if iron == True :
							if extHeat == True :
								rock += 60
							else :
								rock += 30
						else :
							if extHeat == True :
								rock += 30
							else :
								rock += 15
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							if iron == True :
								if extHeat == True :
									food += 96
								else :
									food += 48
							else :
								if extHeat == True :
									food += 48
								else :
									food += 24
						else :
							if iron == True :
								food += 16
							else :
								food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							food += 15
						else :
							food += 5
						if iron == True :
							if extHeat == True :
								wood += 40
								rock += 40
							else :
								wood += 20
								rock += 20
						else :
							if extHeat == True :
								wood += 20
								rock += 20
							else :
								wood += 10
								rock += 10
						if waterPit == True :
							water += 20
						else :
							water += 10
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 45 options
			if age == 45 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if iron == True :
							if extHeat == True :
								wood += 60
							else :
								wood += 30
						else :
							if extHeat == True :
								wood += 30
							else :
								wood += 15
						trees -= 1
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if iron == True :
							if extHeat == True :
								rock += 60
							else :
								rock += 30
						else :
							if extHeat == True :
								rock += 30
							else :
								rock += 15
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							if iron == True :
								if extHeat == True :
									food += 96
								else :
									food += 48
							else :
								if extHeat == True :
									food += 48
								else :
									food += 24
						else :
							if iron == True :
								food += 16
							else :
								food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							food += 15
						else :
							food += 5
						if iron == True :
							if extHeat == True :
								wood += 40
								rock += 40
							else :
								wood += 20
								rock += 20
						else :
							if extHeat == True :
								wood += 20
								rock += 20
							else :
								wood += 10
								rock += 10
						if waterPit == True :
							water += 20
						else :
							water += 10
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 46 options
			if age == 46 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if iron == True :
							if extHeat == True :
								wood += 60
							else :
								wood += 30
						else :
							if extHeat == True :
								wood += 30
							else :
								wood += 15
						trees -= 1
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if iron == True :
							if extHeat == True :
								rock += 60
							else :
								rock += 30
						else :
							if extHeat == True :
								rock += 30
							else :
								rock += 15
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							if iron == True :
								if extHeat == True :
									food += 96
								else :
									food += 48
							else :
								if extHeat == True :
									food += 48
								else :
									food += 24
						else :
							if iron == True :
								food += 16
							else :
								food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							food += 15
						else :
							food += 5
						if iron == True :
							if extHeat == True :
								wood += 40
								rock += 40
							else :
								wood += 20
								rock += 20
						else :
							if extHeat == True :
								wood += 20
								rock += 20
							else :
								wood += 10
								rock += 10
						if waterPit == True :
							water += 20
						else :
							water += 10
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 47 options
			if age == 47 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if iron == True :
							if extHeat == True :
								wood += 60
							else :
								wood += 30
						else :
							if extHeat == True :
								wood += 30
							else :
								wood += 15
						trees -= 1
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if iron == True :
							if extHeat == True :
								rock += 60
							else :
								rock += 30
						else :
							if extHeat == True :
								rock += 30
							else :
								rock += 15
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							if iron == True :
								if extHeat == True :
									food += 96
								else :
									food += 48
							else :
								if extHeat == True :
									food += 48
								else :
									food += 24
						else :
							if iron == True :
								food += 16
							else :
								food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							food += 15
						else :
							food += 5
						if iron == True :
							if extHeat == True :
								wood += 40
								rock += 40
							else :
								wood += 20
								rock += 20
						else :
							if extHeat == True :
								wood += 20
								rock += 20
							else :
								wood += 10
								rock += 10
						if waterPit == True :
							water += 20
						else :
							water += 10
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 48 options
			if age == 48 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if iron == True :
							if extHeat == True :
								wood += 60
							else :
								wood += 30
						else :
							if extHeat == True :
								wood += 30
							else :
								wood += 15
						trees -= 1
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if iron == True :
							if extHeat == True :
								rock += 60
							else :
								rock += 30
						else :
							if extHeat == True :
								rock += 30
							else :
								rock += 15
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							if iron == True :
								if extHeat == True :
									food += 96
								else :
									food += 48
							else :
								if extHeat == True :
									food += 48
								else :
									food += 24
						else :
							if iron == True :
								food += 16
							else :
								food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							food += 15
						else :
							food += 5
						if iron == True :
							if extHeat == True :
								wood += 40
								rock += 40
							else :
								wood += 20
								rock += 20
						else :
							if extHeat == True :
								wood += 20
								rock += 20
							else :
								wood += 10
								rock += 10
						if waterPit == True :
							water += 20
						else :
							water += 10
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 49 options
			if age == 49 :
					ageUpdate == True
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
					action.lower()
					if action == "1" or action == "grow tree" :
						if trees != 0 :
							trees = trees * 2
						else : 
							trees += 2
						actions -= 1
					elif action == "2" or action == "chop tree" :
						if iron == True :
							if extHeat == True :
								wood += 60
							else :
								wood += 30
						else :
							if extHeat == True :
								wood += 30
							else :
								wood += 15
						trees -= 1
						actions -= 1
					elif action == "3" or action == "mine rock" :
						if iron == True :
							if extHeat == True :
								rock += 60
							else :
								rock += 30
						else :
							if extHeat == True :
								rock += 30
							else :
								rock += 15
						actions -= 1
					elif action == "4" or action == "fish" :
						if corn == True :
							if iron == True :
								if extHeat == True :
									food += 96
								else :
									food += 48
							else :
								if extHeat == True :
									food += 48
								else :
									food += 24
						else :
							if iron == True :
								food += 16
							else :
								food += 8
						water += population
						actions -= 1
					elif action == "5" or action == "explore" :
						if corn == True :
							food += 15
						else :
							food += 5
						if iron == True :
							if extHeat == True :
								wood += 40
								rock += 40
							else :
								wood += 20
								rock += 20
						else :
							if extHeat == True :
								wood += 20
								rock += 20
							else :
								wood += 10
								rock += 10
						if waterPit == True :
							water += 20
						else :
							water += 10
						actions -= 1
					elif action == "6" or action == "make farm":
						if wood > 2 and water > 0 :
							makeFarms()
							actions -= 1
						else :
							ageUpdate = False
							print("You don't have enough resources!")
					elif action == "7" or action == "embark on a water expedition" :
						if waterPit == True :
							water += population * 4
						else :
							water += population * 2
						actions -= 1
					elif action == "8" or action == "job manager" :
						jobManager()
					elif action == "9" or action == "build house" :
						makeHouse()
						actions -= 1
					elif action == "save" :
						save()
						actions -= 1
					else :
						ageUpdate = False
						print("That's not an option!")

			#age 50 options
			if age == 50 :
				ageUpdate == True
				action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
				action.lower()
				if action == "1" or action == "grow tree" :
					if trees != 0 :
						trees = trees * 2
					else : 
						trees += 2
					actions -= 1
				elif action == "2" or action == "chop tree" :
					if iron == True :
						if extHeat == True :
							wood += 60
						else :
							wood += 30
					else :
						if extHeat == True :
							wood += 30
						else :
							wood += 15
						trees -= 1
					actions -= 1
				elif action == "3" or action == "mine rock" :
					if iron == True :
						if extHeat == True :
							rock += 60
						else :
							rock += 30
					else :
						if extHeat == True :
							rock += 30
						else :
							rock += 15
					actions -= 1
				elif action == "4" or action == "fish" :
					if corn == True :
						if iron == True :
							if extHeat == True :
								food += 96
							else :
								food += 48
						else :
							if extHeat == True :
								food += 48
							else :
								food += 24
					else :
						if iron == True :
							food += 16
						else :
							food += 8
					water += population
					actions -= 1
				elif action == "5" or action == "explore" :
					if corn == True :
						food += 15
					else :
						food += 5
					if iron == True :
						if extHeat == True :
							wood += 40
							rock += 40
						else :
							wood += 20
							rock += 20
					else :
						if extHeat == True :
							wood += 20
							rock += 20
						else :
							wood += 10
							rock += 10
					if waterPit == True :
						water += 20
					else :
						water += 10
					actions -= 1
				elif action == "6" or action == "make farm":
					if wood > 2 and water > 0 :
						makeFarms()
						actions -= 1
					else :
						ageUpdate = False
						print("You don't have enough resources!")
				elif action == "7" or action == "embark on a water expedition" :
					if waterPit == True :
						water += population * 4
					else :
						water += population * 2
					actions -= 1
				elif action == "8" or action == "job manager" :
					jobManager()
				elif action == "9" or action == "build house" :
					makeHouse()
					actions -= 1
				elif action == "save" :
					save()
					actions -= 1
				else :
					ageUpdate = False
					print("That's not an option!")

		#ages 51 - 60
		if gameOn == True :
			#age 51 options
			if age == 51 :
				ageUpdate == True
				if expansion == False :
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
				else :
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n|10. Neighboring civilizations tab\n")
				action.lower()
				if action == "1" or action == "grow tree" :
					if trees != 0 :
						trees = trees * 2
					else : 
						trees += 2
					actions -= 1
				elif action == "2" or action == "chop tree" :
					if iron == True :
						if extHeat == True :
							wood += 60
						else :
							wood += 30
					else :
						wood += 15
					trees -= 1
					actions -= 1
				elif action == "3" or action == "mine rock" :
					if iron == True :
						if extHeat == True :
							rock += 60
						else :
							rock += 30
					else :
						rock += 15
					actions -= 1
				elif action == "4" or action == "fish" :
					if corn == True :
						if iron == True :
							if extHeat == True :
								food += 96
							else :
								food += 48
						else :
							food += 24
					else :
						food += 12
					water += population
					actions -= 1
				elif action == "5" or action == "explore" :
					if corn == True :
						food += 15
					else :
						food += 5
					if iron == True :
						if extHeat == True :
							wood += 40
							rock += 40
						else :
							wood += 20
							rock += 20
					else :
						wood += 10
						rock += 10
					if waterPit == True :
						water += 20
					else :
						water += 10
					actions -= 1
				elif action == "6" or action == "make farm":
					if wood > 2 and water > 0 :
						makeFarms()
						actions -= 1
					else :
						ageUpdate = False
						print("You don't have enough resources!")
				elif action == "7" or action == "embark on a water expedition" :
					if waterPit == True :
						water += population * 4
					else :
						water += population * 2
					actions -= 1
				elif action == "8" or action == "job manager" :
					jobManager()
				elif action == "9" or action == "build house" :
					makeHouse()
					actions -= 1
				elif action == "10" or action == "neighboring civilizations tab" :
					displayExpansion()
				elif action == "save" :
					save()
					actions -= 1
				else :
					ageUpdate = False
					print("That's not an option!")
			
			#age 52 options
			if age == 52 :
				ageUpdate == True
				if expansion == False :
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
				else :
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n|10. Neighboring civilizations tab\n")
				action.lower()
				if action == "1" or action == "grow tree" :
					if trees != 0 :
						trees = trees * 2
					else : 
						trees += 2
					actions -= 1
				elif action == "2" or action == "chop tree" :
					if iron == True :
						if extHeat == True :
							wood += 60
						else :
							wood += 30
					else :
						wood += 15
					trees -= 1
					actions -= 1
				elif action == "3" or action == "mine rock" :
					if iron == True :
						if extHeat == True :
							rock += 60
						else :
							rock += 30
					else :
						rock += 15
					actions -= 1
				elif action == "4" or action == "fish" :
					if corn == True :
						if iron == True :
							if extHeat == True :
								food += 96
							else :
								food += 48
						else :
							food += 24
					else :
						food += 12
					water += population
					actions -= 1
				elif action == "5" or action == "explore" :
					if corn == True :
						food += 15
					else :
						food += 5
					if iron == True :
						if extHeat == True :
							wood += 40
							rock += 40
						else :
							wood += 20
							rock += 20
					else :
						wood += 10
						rock += 10
					if waterPit == True :
						water += 20
					else :
						water += 10
					actions -= 1
				elif action == "6" or action == "make farm":
					if wood > 2 and water > 0 :
						makeFarms()
						actions -= 1
					else :
						ageUpdate = False
						print("You don't have enough resources!")
				elif action == "7" or action == "embark on a water expedition" :
					if waterPit == True :
						water += population * 4
					else :
						water += population * 2
					actions -= 1
				elif action == "8" or action == "job manager" :
					jobManager()
				elif action == "9" or action == "build house" :
					makeHouse()
					actions -= 1
				elif action == "10" or action == "neighboring civilizations tab" :
					displayExpansion()
				elif action == "save" :
					save()
					actions -= 1
				else :
					ageUpdate = False
					print("That's not an option!")
			
			#age 52 options
			if age == 52 :
				ageUpdate == True
				if expansion == False :
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
				else :
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n|10. Neighboring civilizations tab\n")
				action.lower()
				if action == "1" or action == "grow tree" :
					if trees != 0 :
						trees = trees * 2
					else : 
						trees += 2
					actions -= 1
				elif action == "2" or action == "chop tree" :
					if iron == True :
						if extHeat == True :
							wood += 60
						else :
							wood += 30
					else :
						wood += 15
					trees -= 1
					actions -= 1
				elif action == "3" or action == "mine rock" :
					if iron == True :
						if extHeat == True :
							rock += 60
						else :
							rock += 30
					else :
						rock += 15
					actions -= 1
				elif action == "4" or action == "fish" :
					if corn == True :
						if iron == True :
							if extHeat == True :
								food += 96
							else :
								food += 48
						else :
							food += 24
					else :
						food += 12
					water += population
					actions -= 1
				elif action == "5" or action == "explore" :
					if corn == True :
						food += 15
					else :
						food += 5
					if iron == True :
						if extHeat == True :
							wood += 40
							rock += 40
						else :
							wood += 20
							rock += 20
					else :
						wood += 10
						rock += 10
					if waterPit == True :
						water += 20
					else :
						water += 10
					actions -= 1
				elif action == "6" or action == "make farm":
					if wood > 2 and water > 0 :
						makeFarms()
						actions -= 1
					else :
						ageUpdate = False
						print("You don't have enough resources!")
				elif action == "7" or action == "embark on a water expedition" :
					if waterPit == True :
						water += population * 4
					else :
						water += population * 2
					actions -= 1
				elif action == "8" or action == "job manager" :
					jobManager()
				elif action == "9" or action == "build house" :
					makeHouse()
					actions -= 1
				elif action == "10" or action == "neighboring civilizations tab" :
					displayExpansion()
				elif action == "save" :
					save()
					actions -= 1
				else :
					ageUpdate = False
					print("That's not an option!")
			
			#age 54 options
			if age == 54 :
				ageUpdate == True
				if expansion == False :
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
				else :
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n|10. Neighboring civilizations tab\n")
				action.lower()
				if action == "1" or action == "grow tree" :
					if trees != 0 :
						trees = trees * 2
					else : 
						trees += 2
					actions -= 1
				elif action == "2" or action == "chop tree" :
					if iron == True :
						if extHeat == True :
							wood += 60
						else :
							wood += 30
					else :
						wood += 15
					trees -= 1
					actions -= 1
				elif action == "3" or action == "mine rock" :
					if iron == True :
						if extHeat == True :
							rock += 60
						else :
							rock += 30
					else :
						rock += 15
					actions -= 1
				elif action == "4" or action == "fish" :
					if corn == True :
						if iron == True :
							if extHeat == True :
								food += 96
							else :
								food += 48
						else :
							food += 24
					else :
						food += 12
					water += population
					actions -= 1
				elif action == "5" or action == "explore" :
					if corn == True :
						food += 15
					else :
						food += 5
					if iron == True :
						if extHeat == True :
							wood += 40
							rock += 40
						else :
							wood += 20
							rock += 20
					else :
						wood += 10
						rock += 10
					if waterPit == True :
						water += 20
					else :
						water += 10
					actions -= 1
				elif action == "6" or action == "make farm":
					if wood > 2 and water > 0 :
						makeFarms()
						actions -= 1
					else :
						ageUpdate = False
						print("You don't have enough resources!")
				elif action == "7" or action == "embark on a water expedition" :
					if waterPit == True :
						water += population * 4
					else :
						water += population * 2
					actions -= 1
				elif action == "8" or action == "job manager" :
					jobManager()
				elif action == "9" or action == "build house" :
					makeHouse()
					actions -= 1
				elif action == "10" or action == "neighboring civilizations tab" :
					displayExpansion()
				elif action == "save" :
					save()
					actions -= 1
				else :
					ageUpdate = False
					print("That's not an option!")
			
			#age 55 options
			if age == 5552 :
				ageUpdate == True
				if expansion == False :
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
				else :
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n|10. Neighboring civilizations tab\n")
				action.lower()
				if action == "1" or action == "grow tree" :
					if trees != 0 :
						trees = trees * 2
					else : 
						trees += 2
					actions -= 1
				elif action == "2" or action == "chop tree" :
					if iron == True :
						if extHeat == True :
							wood += 60
						else :
							wood += 30
					else :
						wood += 15
					trees -= 1
					actions -= 1
				elif action == "3" or action == "mine rock" :
					if iron == True :
						if extHeat == True :
							rock += 60
						else :
							rock += 30
					else :
						rock += 15
					actions -= 1
				elif action == "4" or action == "fish" :
					if corn == True :
						if iron == True :
							if extHeat == True :
								food += 96
							else :
								food += 48
						else :
							food += 24
					else :
						food += 12
					water += population
					actions -= 1
				elif action == "5" or action == "explore" :
					if corn == True :
						food += 15
					else :
						food += 5
					if iron == True :
						if extHeat == True :
							wood += 40
							rock += 40
						else :
							wood += 20
							rock += 20
					else :
						wood += 10
						rock += 10
					if waterPit == True :
						water += 20
					else :
						water += 10
					actions -= 1
				elif action == "6" or action == "make farm":
					if wood > 2 and water > 0 :
						makeFarms()
						actions -= 1
					else :
						ageUpdate = False
						print("You don't have enough resources!")
				elif action == "7" or action == "embark on a water expedition" :
					if waterPit == True :
						water += population * 4
					else :
						water += population * 2
					actions -= 1
				elif action == "8" or action == "job manager" :
					jobManager()
				elif action == "9" or action == "build house" :
					makeHouse()
					actions -= 1
				elif action == "10" or action == "neighboring civilizations tab" :
					displayExpansion()
				elif action == "save" :
					save()
					actions -= 1
				else :
					ageUpdate = False
					print("That's not an option!")
			
			#age 56 options
			if age == 56 :
				ageUpdate == True
				if expansion == False :
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
				else :
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n|10. Neighboring civilizations tab\n")
				action.lower()
				if action == "1" or action == "grow tree" :
					if trees != 0 :
						trees = trees * 2
					else : 
						trees += 2
					actions -= 1
				elif action == "2" or action == "chop tree" :
					if iron == True :
						if extHeat == True :
							wood += 60
						else :
							wood += 30
					else :
						wood += 15
					trees -= 1
					actions -= 1
				elif action == "3" or action == "mine rock" :
					if iron == True :
						if extHeat == True :
							rock += 60
						else :
							rock += 30
					else :
						rock += 15
					actions -= 1
				elif action == "4" or action == "fish" :
					if corn == True :
						if iron == True :
							if extHeat == True :
								food += 96
							else :
								food += 48
						else :
							food += 24
					else :
						food += 12
					water += population
					actions -= 1
				elif action == "5" or action == "explore" :
					if corn == True :
						food += 15
					else :
						food += 5
					if iron == True :
						if extHeat == True :
							wood += 40
							rock += 40
						else :
							wood += 20
							rock += 20
					else :
						wood += 10
						rock += 10
					if waterPit == True :
						water += 20
					else :
						water += 10
					actions -= 1
				elif action == "6" or action == "make farm":
					if wood > 2 and water > 0 :
						makeFarms()
						actions -= 1
					else :
						ageUpdate = False
						print("You don't have enough resources!")
				elif action == "7" or action == "embark on a water expedition" :
					if waterPit == True :
						water += population * 4
					else :
						water += population * 2
					actions -= 1
				elif action == "8" or action == "job manager" :
					jobManager()
				elif action == "9" or action == "build house" :
					makeHouse()
					actions -= 1
				elif action == "10" or action == "neighboring civilizations tab" :
					displayExpansion()
				elif action == "save" :
					save()
					actions -= 1
				else :
					ageUpdate = False
					print("That's not an option!")
			
			#age 57 options
			if age == 57 :
				ageUpdate == True
				if expansion == False :
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
				else :
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n|10. Neighboring civilizations tab\n")
				action.lower()
				if action == "1" or action == "grow tree" :
					if trees != 0 :
						trees = trees * 2
					else : 
						trees += 2
					actions -= 1
				elif action == "2" or action == "chop tree" :
					if iron == True :
						if extHeat == True :
							wood += 60
						else :
							wood += 30
					else :
						wood += 15
					trees -= 1
					actions -= 1
				elif action == "3" or action == "mine rock" :
					if iron == True :
						if extHeat == True :
							rock += 60
						else :
							rock += 30
					else :
						rock += 15
					actions -= 1
				elif action == "4" or action == "fish" :
					if corn == True :
						if iron == True :
							if extHeat == True :
								food += 96
							else :
								food += 48
						else :
							food += 24
					else :
						food += 12
					water += population
					actions -= 1
				elif action == "5" or action == "explore" :
					if corn == True :
						food += 15
					else :
						food += 5
					if iron == True :
						if extHeat == True :
							wood += 40
							rock += 40
						else :
							wood += 20
							rock += 20
					else :
						wood += 10
						rock += 10
					if waterPit == True :
						water += 20
					else :
						water += 10
					actions -= 1
				elif action == "6" or action == "make farm":
					if wood > 2 and water > 0 :
						makeFarms()
						actions -= 1
					else :
						ageUpdate = False
						print("You don't have enough resources!")
				elif action == "7" or action == "embark on a water expedition" :
					if waterPit == True :
						water += population * 4
					else :
						water += population * 2
					actions -= 1
				elif action == "8" or action == "job manager" :
					jobManager()
				elif action == "9" or action == "build house" :
					makeHouse()
					actions -= 1
				elif action == "10" or action == "neighboring civilizations tab" :
					displayExpansion()
				elif action == "save" :
					save()
					actions -= 1
				else :
					ageUpdate = False
					print("That's not an option!")
			
			#age 58 options
			if age == 58 :
				ageUpdate == True
				if expansion == False :
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
				else :
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n|10. Neighboring civilizations tab\n")
				action.lower()
				if action == "1" or action == "grow tree" :
					if trees != 0 :
						trees = trees * 2
					else : 
						trees += 2
					actions -= 1
				elif action == "2" or action == "chop tree" :
					if iron == True :
						if extHeat == True :
							wood += 60
						else :
							wood += 30
					else :
						wood += 15
					trees -= 1
					actions -= 1
				elif action == "3" or action == "mine rock" :
					if iron == True :
						if extHeat == True :
							rock += 60
						else :
							rock += 30
					else :
						rock += 15
					actions -= 1
				elif action == "4" or action == "fish" :
					if corn == True :
						if iron == True :
							if extHeat == True :
								food += 96
							else :
								food += 48
						else :
							food += 24
					else :
						food += 12
					water += population
					actions -= 1
				elif action == "5" or action == "explore" :
					if corn == True :
						food += 15
					else :
						food += 5
					if iron == True :
						if extHeat == True :
							wood += 40
							rock += 40
						else :
							wood += 20
							rock += 20
					else :
						wood += 10
						rock += 10
					if waterPit == True :
						water += 20
					else :
						water += 10
					actions -= 1
				elif action == "6" or action == "make farm":
					if wood > 2 and water > 0 :
						makeFarms()
						actions -= 1
					else :
						ageUpdate = False
						print("You don't have enough resources!")
				elif action == "7" or action == "embark on a water expedition" :
					if waterPit == True :
						water += population * 4
					else :
						water += population * 2
					actions -= 1
				elif action == "8" or action == "job manager" :
					jobManager()
				elif action == "9" or action == "build house" :
					makeHouse()
					actions -= 1
				elif action == "10" or action == "neighboring civilizations tab" :
					displayExpansion()
				elif action == "save" :
					save()
					actions -= 1
				else :
					ageUpdate = False
					print("That's not an option!")
			
			#age 59 options
			if age == 59 :
				ageUpdate == True
				if expansion == False :
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
				else :
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n|10. Neighboring civilizations tab\n")
				action.lower()
				if action == "1" or action == "grow tree" :
					if trees != 0 :
						trees = trees * 2
					else : 
						trees += 2
					actions -= 1
				elif action == "2" or action == "chop tree" :
					if iron == True :
						if extHeat == True :
							wood += 60
						else :
							wood += 30
					else :
						wood += 15
					trees -= 1
					actions -= 1
				elif action == "3" or action == "mine rock" :
					if iron == True :
						if extHeat == True :
							rock += 60
						else :
							rock += 30
					else :
						rock += 15
					actions -= 1
				elif action == "4" or action == "fish" :
					if corn == True :
						if iron == True :
							if extHeat == True :
								food += 96
							else :
								food += 48
						else :
							food += 24
					else :
						food += 12
					water += population
					actions -= 1
				elif action == "5" or action == "explore" :
					if corn == True :
						food += 15
					else :
						food += 5
					if iron == True :
						if extHeat == True :
							wood += 40
							rock += 40
						else :
							wood += 20
							rock += 20
					else :
						wood += 10
						rock += 10
					if waterPit == True :
						water += 20
					else :
						water += 10
					actions -= 1
				elif action == "6" or action == "make farm":
					if wood > 2 and water > 0 :
						makeFarms()
						actions -= 1
					else :
						ageUpdate = False
						print("You don't have enough resources!")
				elif action == "7" or action == "embark on a water expedition" :
					if waterPit == True :
						water += population * 4
					else :
						water += population * 2
					actions -= 1
				elif action == "8" or action == "job manager" :
					jobManager()
				elif action == "9" or action == "build house" :
					makeHouse()
					actions -= 1
				elif action == "10" or action == "neighboring civilizations tab" :
					displayExpansion()
				elif action == "save" :
					save()
					actions -= 1
				else :
					ageUpdate = False
					print("That's not an option!")
			
			#age 60 options
			if age == 60 :
				ageUpdate == True
				if expansion == False :
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n")
				else :
					action = input("|1. Grow Tree \n|2. Chop Tree \n|3. Mine Rock \n|4. Fish \n|5. Explore \n|6. Make Farm \n|7. Embark on a water expedition \n|8. Job manager \n|9. Build house \n|10. Neighboring civilizations tab\n")
				action.lower()
				if action == "1" or action == "grow tree" :
					if trees != 0 :
						trees = trees * 2
					else : 
						trees += 2
					actions -= 1
				elif action == "2" or action == "chop tree" :
					if iron == True :
						if extHeat == True :
							wood += 60
						else :
							wood += 30
					else :
						wood += 15
					trees -= 1
					actions -= 1
				elif action == "3" or action == "mine rock" :
					if iron == True :
						if extHeat == True :
							rock += 60
						else :
							rock += 30
					else :
						rock += 15
					actions -= 1
				elif action == "4" or action == "fish" :
					if corn == True :
						if iron == True :
							if extHeat == True :
								food += 96
							else :
								food += 48
						else :
							food += 24
					else :
						food += 12
					water += population
					actions -= 1
				elif action == "5" or action == "explore" :
					if corn == True :
						food += 15
					else :
						food += 5
					if iron == True :
						if extHeat == True :
							wood += 40
							rock += 40
						else :
							wood += 20
							rock += 20
					else :
						wood += 10
						rock += 10
					if waterPit == True :
						water += 20
					else :
						water += 10
					actions -= 1
				elif action == "6" or action == "make farm":
					if wood > 2 and water > 0 :
						makeFarms()
						actions -= 1
					else :
						ageUpdate = False
						print("You don't have enough resources!")
				elif action == "7" or action == "embark on a water expedition" :
					if waterPit == True :
						water += population * 4
					else :
						water += population * 2
					actions -= 1
				elif action == "8" or action == "job manager" :
					jobManager()
				elif action == "9" or action == "build house" :
					makeHouse()
					actions -= 1
				elif action == "10" or action == "neighboring civilizations tab" :
					displayExpansion()
				elif action == "save" :
					save()
					actions -= 1
				else :
					ageUpdate = False
					print("That's not an option!")

	if actions == 0 and ageUpdate == True :
		update()
	if population == 0:
		print("All your people are dead :( \nTry Again...")
		gameOn = False


 
