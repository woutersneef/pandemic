#START UP THE PANDEMIC GAME

#Import libraries
import random

#Set version
version = '1.13a'

#Set the roles and shuffle the roles and give the contingency planner a store for an event card
roles = ['DISPATCHER', 'SCIENTIST', 'MEDIC', 'OPERATIONS EXPERT', 'RESEARCHER', 'QUARANTINE SPECIALIST', 'CONTINGENCY PLANNER']
stored_event_cards = []
random.shuffle(roles)
				
#Set player names or automatically generate a game with names and difficulty
difficulty = None

players_name = []
while True:
	if len(players_name) > 3:
		break
	name = input("Give the names of the players and type S to start the game (type A to automate settings):")
	if name == 'A' and len(players_name) == 0:
		players_name.append('HENK-JAN')
		players_name.append('WOUTER')
		players_name.append('PETER')
		players_name.append('ROBERT')
		difficulty = 7
		difficulty_setting = 'CHEF'
		break
	elif name == 'S':
		if len(players_name) < 2:
			print("You need at least 2 players.")
			continue
		else:	
			break
	elif len(name) < 2:
		print("A name needs at least 2 characters.")
	else:
		if name not in players_name:
			players_name.append(name)
		else:
			print("Pick a different name.")

#Set player locations, and number of actions and roles				
players_location = {}
players_actions = {}
for name in players_name:
	players_location[name] = 'ATLANTA'
for name in players_name:
	players_actions[name] = 4
players_role = {}
count = 0
for name in players_name:
	players_role[name] = roles[count]
	count = count + 1

#Set difficulty of the game
while difficulty == None:
	difficulty_setting = input("Choose the ARTZ difficulty level (ASSISTENZ, FACH, OBER, CHEF or DIREKTOR):")
	if difficulty_setting == 'ASSISTENZ':
		difficulty = 4
		break
	elif difficulty_setting =='FACH':
		difficulty = 5
		break
	elif difficulty_setting == 'OBER':
		difficulty = 6
		break
	elif difficulty_setting == 'CHEF':
		difficulty = 7
		break
	elif difficulty_setting == 'DIREKTOR':
		difficulty = 8
		break
	
#Starting Pandemic
print("################################################################################\n")
print("Starting Pandemic version", version, "first we need do some checks to see if everything is correct!")

#Create lists with cities of each color
black_cities = ['ALGIERS', 'ISTANBUL', 'CAIRO', 'BAGHDAD', 'MOSCOW', 'RIYADH', 'TEHRAN', 'KARACHI', 'MUMBAI', 'DELHI', 'CHENNAI', 'KOLKATA']
blue_cities = ['SAN FRANCISCO', 'CHICAGO', 'MONTREAL', 'NEW YORK', 'ATLANTA', 'WASHINGTON', 'LONDON', 'MADRID', 'PARIS', 'ESSEN', 'MILAN', 'ST. PETERSBURG']
red_cities = ['BANGKOK', 'JAKARTA', 'HO CHI MINH CITY', 'HONG KONG', 'MANILA', 'SYDNEY', 'TAIPEI', 'SHANGHAI', 'OSAKA', 'BEIJING', 'SEOUL', 'TOKYO']
yellow_cities = ['LOS ANGELES', 'MEXICO CITY', 'MIAMI', 'BOGOTA', 'LIMA', 'SANTIAGO', 'BUENOS AIRES', 'SAO PAULO', 'LAGOS', 'KINSHASA', 'JOHANNESBURG', 'KHARTOUM']

#Combine the cities in a list with all cities
all_cities = black_cities + blue_cities + red_cities + yellow_cities

#Set list with colors
colors_list = ['black', 'blue', 'red', 'yellow']

#Make a dictionary with cities and colors
cities_color = {}
count = 0
for city in all_cities:
	if city in black_cities:
		cities_color[all_cities[count]] = 'black'
		count = count + 1
	elif city in blue_cities:
		cities_color[all_cities[count]] = 'blue'
		count = count + 1
	elif city in red_cities:
		cities_color[all_cities[count]] = 'red'
		count = count + 1
	else:
		cities_color[all_cities[count]] = 'yellow'
		count = count + 1

#Make a list with event cards
event_cards = ['FORECAST', 'AIRLIFT', 'ONE QUIET NIGHT', 'GOVERNMENT GRANT', 'RESILIENT POPULATION']

#Random shuffle cities into an infection deck
infection_deck = []
for city in all_cities:
	infection_deck.append(city)
random.shuffle(infection_deck)

#Random shuffle cities and event cards into a player deck
player_deck = []
for city in all_cities:
	player_deck.append(city)
for event in event_cards:
	player_deck.append(event)
random.shuffle(player_deck)

#Create a dictionary with cities and linked cities
cities_linked = {
'ALGIERS':['MADRID', 'PARIS', 'ISTANBUL', 'CAIRO'], 
'ATLANTA':['MIAMI', 'WASHINGTON', 'CHICAGO'],
'BAGHDAD':['CAIRO', 'ISTANBUL', 'TEHRAN', 'KARACHI', 'RIYADH'],
'BANGKOK':['KOLKATA', 'CHENNAI', 'JAKARTA', 'HO CHI MINH CITY', 'HONG KONG' ],
'BEIJING':['SEOUL', 'SHANGHAI'],
'BOGOTA':['MIAMI', 'MEXICO CITY', 'LIMA', 'SAO PAULO', 'BUENOS AIRES'],
'BUENOS AIRES':['BOGOTA', 'SAO PAULO'], 
'CAIRO':['ALGIERS', 'ISTANBUL', 'BAGHDAD', 'RIYADH', 'KHARTOUM'],
'CHENNAI':['MUMBAI', 'DELHI', 'KOLKATA', 'JAKARTA', 'BANGKOK'],
'CHICAGO':['SAN FRANCISCO', 'LOS ANGELES', 'ATLANTA', 'MONTREAL', 'MEXICO CITY'],
'DELHI':['TEHRAN', 'KARACHI', 'MUMBAI', 'CHENNAI', 'KOLKATA'],
'ESSEN':['LONDON', 'PARIS', 'MILAN', 'ST. PETERSBURG'],
'HO CHI MINH CITY':['MANILA', 'BANGKOK', 'HONG KONG', 'JAKARTA'],
'HONG KONG':['SHANGHAI', 'TAIPEI', 'MANILA', 'HO CHI MINH CITY', 'BANGKOK', 'KOLKATA'],
'ISTANBUL':['MILAN', 'ST. PETERSBURG', 'MOSCOW', 'CAIRO', 'ALGIERS', 'BAGHDAD'],
'JAKARTA':['CHENNAI', 'BANGKOK', 'HO CHI MINH CITY', 'SYDNEY'],
'JOHANNESBURG':['KINSHASA', 'KHARTOUM'],
'KARACHI':['TEHRAN', 'DELHI', 'MUMBAI', 'RIYADH', 'BAGHDAD'],
'KHARTOUM':['CAIRO', 'KINSHASA', 'JOHANNESBURG', 'LAGOS'],
'KINSHASA':['LAGOS', 'KHARTOUM', 'JOHANNESBURG'],
'KOLKATA':['HONG KONG', 'BANGKOK', 'CHENNAI', 'DELHI'],
'LAGOS':['KINSHASA', 'KHARTOUM', 'SAO PAULO'],
'LIMA':['MEXICO CITY', 'BOGOTA', 'SANTIAGO'],
'LONDON':['ESSEN', 'PARIS', 'MADRID', 'NEW YORK'],
'LOS ANGELES':['SAN FRANCISCO', 'MEXICO CITY', 'SYDNEY', 'CHICAGO'], 
'MADRID':['LONDON', 'PARIS', 'NEW YORK', 'SAO PAULO', 'ALGIERS'],
'MANILA':['TAIPEI', 'HONG KONG', 'HO CHI MINH CITY', 'SYDNEY', 'SAN FRANCISCO'], 
'MEXICO CITY':['LOS ANGELES', 'LIMA', 'BOGOTA', 'MIAMI', 'CHICAGO'],
'MIAMI':['ATLANTA', 'WASHINGTON', 'BOGOTA', 'MEXICO CITY'],
'MILAN':['PARIS', 'ESSEN', 'ISTANBUL'],
'MONTREAL':['NEW YORK', 'WASHINGTON', 'CHICAGO'], 
'MOSCOW':['ST. PETERSBURG', 'TEHRAN', 'ISTANBUL'],
'MUMBAI':['KARACHI', 'DELHI','CHENNAI'],
'NEW YORK':['LONDON', 'MADRID', 'WASHINGTON', 'MONTREAL'], 
'OSAKA':['TOKYO', 'TAIPEI'],
'PARIS':['LONDON', 'ESSEN', 'MILAN', 'ALGIERS', 'MADRID'],
'RIYADH':['CAIRO', 'BAGHDAD', 'KARACHI'],
'SAN FRANCISCO':['TOKYO', 'MANILA', 'CHICAGO', 'LOS ANGELES'],
'SANTIAGO':['LIMA'],
'SAO PAULO':['BUENOS AIRES', 'BOGOTA', 'MADRID', 'LAGOS'],
'SEOUL':['BEIJING', 'SHANGHAI', 'TOKYO'],
'SHANGHAI':['BEIJING', 'SEOUL', 'TOKYO', 'TAIPEI', 'HONG KONG'], 
'ST. PETERSBURG':['ESSEN', 'ISTANBUL', 'MOSCOW'], 
'SYDNEY':['LOS ANGELES', 'MANILA', 'JAKARTA'],
'TAIPEI':['SHANGHAI', 'OSAKA', 'MANILA', 'HONG KONG'],
'TEHRAN':['MOSCOW', 'BAGHDAD', 'KARACHI', 'DELHI'],
'TOKYO':['SAN FRANCISCO', 'SEOUL', 'OSAKA', 'SHANGHAI'],
'WASHINGTON':['NEW YORK', 'MONTREAL', 'ATLANTA', 'MIAMI']}

#Check whether linked city names are correct
for k, v in cities_linked.items():
	for city in v:
		if city not in all_cities:
			print("Not a correct city:", city, "in", k)
print("Linked city name check done!")

#Check whether cities link back to each other
for k, v in cities_linked.items():
	for city in v:
		if k not in cities_linked[city]:
			print("There is an issue with this city:", k, "is not in", city)
print("Linked city links check done!")

#Set infection rate, markers and game status
infection_rate = [2, 2, 2, 3, 3, 4, 4, 5, 5]
infection_rate_marker = 0
outbreaks_marker = 0
game_status = 'Not finished'

#Make a list with cities with research stations
cities_stations = ['ATLANTA']

#Set cure status per color
colors_cure = {}
for color in colors_list:
	colors_cure[color] = 'No'

#Make a dictionary with cities and number of cubes (black, blue, red, yellow)
cities_cubes = {}
for city in range(len(all_cities)):
	cities_cubes[all_cities[city]] = {'black':0, 'blue':0, 'red':0, 'yellow':0}

#Function for adding one cube to the city in the city color (with eradicated check)
def add_cubes(city):
	for color in colors_list:
		if cities_color[city] == color:
			cities_cubes[city][color] = cities_cubes[city][color] + 1
									
#Function for displaying cubes in the city (with the city name)
def display_cubes_name(city):
	if sum(cities_cubes[city].values()) > 0:
		print(city, end = ' ')
		for color, v in cities_cubes[city].items():
			if v > 0:
				print(color, v)

#Function for displaying cubes in the city (without the city name)
def display_cubes(city):
	if sum(cities_cubes[city].values()) > 0:
		for color, v in cities_cubes[city].items():
			if v > 0:
				print(v, color, "cubes", end = ' ')
	else:
		print("No cubes in the city.")
	
#Infect 9 cites
infection_discard_pile = []
removed_from_game = []
count = 0
while count < 9:
	infected_city = infection_deck.pop(count)
	infection_discard_pile.append(infected_city)
	count = count + 1
for city in infection_discard_pile[:3]:
	add_cubes(city)
	add_cubes(city)
	add_cubes(city)
for city in infection_discard_pile[3:6]:
	add_cubes(city)
	add_cubes(city)
for city in infection_discard_pile[6:]:
	add_cubes(city)
		
#Empty dictionary and function for calculating number of disease cubes in stock
colors_cubes_stock = {}
def disease_cubes_stock():
	for color in colors_list:
		colors_cubes_stock[color] = 24
	for disease in colors_cubes_stock:
		for city in cities_cubes:
			for color in cities_cubes[city]:
				if disease == color:
					colors_cubes_stock[disease] = colors_cubes_stock[disease] - cities_cubes[city][color]

disease_cubes_stock()
start_cubes = {}
start_cubes['black'] = colors_cubes_stock['black']
start_cubes['blue'] = colors_cubes_stock['blue']
start_cubes['red'] = colors_cubes_stock['red']
start_cubes['yellow'] = colors_cubes_stock['yellow']

#Give player cards to players and create player discard pile
number_of_players = len(players_name)
if number_of_players == 2:
	cards_per_player = 4
elif number_of_players == 3:
	cards_per_player = 3
else:
	cards_per_player = 2
initial_cards = number_of_players * cards_per_player
start = 0
end = cards_per_player	
players_cards = {}
for name in players_name:
	players_cards[name] = []
	players_cards[name].append
	count = 0
	while count < cards_per_player:
		card = player_deck[count]
		players_cards[name].append(card)
		count = count + 1
		player_deck.remove(card)
player_discard_pile = []

#Create list with size of piles
pile_size = 53 - initial_cards + difficulty 
pile_list = []
piles = difficulty
pile_rest = pile_size % difficulty
pile_minimum = (pile_size - pile_rest) / difficulty
while piles > 0:
	pile_list.append(pile_minimum)
	piles = piles - 1
count = 0
while pile_rest > 0:
	pile_list[count] = pile_list[count] + 1
	count = count + 1
	pile_rest = pile_rest - 1	

#Make a list with when epidemic comes and add epidemics to player deck
count = 0
start = 0
end = -1
epidemic_list = []
for pile in pile_list:
	end = end + pile	
	epidemic_position = random.randint(start, end)
	epidemic_list.append(epidemic_position)				
	start = start + pile							
for e in epidemic_list:
	player_deck.insert(e, 'EPIDEMIC')

#Function to print an overview of the board
def board_overview():
	print("\n################################################################################\n")
	
	print("Difficulty level:", difficulty_setting, "(",difficulty, "epidemic cards)")
	print("Infection rate:", infection_rate[infection_rate_marker], "(next level is", infection_rate[(infection_rate_marker+1)], ")")
	print("Infection discard pile:",)
	for i in infection_discard_pile:
		print(i, end=' ')
	if len(removed_from_game) > 0:
		print("(removed from game:",)
		for i in removed_from_game:
			print(i, end=' ')
		print(")",)
	print("\n\nTop card in player discard pile:",)
	if len(player_discard_pile) > 0:
		print(player_discard_pile[-1])
	else:
		print(" ")
	print("\nCities with research stations:", )
	for i in cities_stations:
		print( i, end=' ') 
	print(" ")
	print(" ") 
	
	print("Color   Cure for   Cubes left") 
	for (k,v), (k2, v2) in zip(colors_cure.items(), colors_cubes_stock.items()):
	    print(k, "    ", v, "     " , v2)
	

	
	
	print("\n\nPlayer cards left:", len(player_deck))
	print("Outbreaks (8 is game over):", outbreaks_marker, "\n")
	
	for name in players_name:
		print(name, "the", players_role[name] , "is in", players_location[name], "and has:")
		for card in players_cards[name]:
			print(card, end = ' ') 
			if card not in event_cards:
				print( "	", cities_color[card])
			else:
				print("		event")
		if players_role[name] == 'CONTINGENCY PLANNER':
			if len(stored_event_cards) > 0:
				print("Stored event card:", stored_event_cards[0])
		print(" ")
		
	print("Infected cities")
	for city in all_cities:
		display_cubes_name(city)	
	print(" ")
	
	return("################################################################################\n")

#FUNCTIONS FOR THE ACTIONS

#Function for the drive/ferry/shuttle flight and pawn to pawn actions
def action_drive(n, pawn):
	destinations = []
	#Add cities for drive and ferry
	for city in cities_linked[players_location[pawn]]:
		destinations.append(city)
	#Add cities for shuttle flight
	if len(cities_stations) > 1:
		if players_location[pawn] in cities_stations:
			for city in cities_stations:
				if city != players_location[pawn]:
					if city not in destinations:
						destinations.append(city)
	#Add cities for pawn to pawn action								
	if players_role[n] == 'DISPATCHER':
		for k, city in players_location.items():
			if city != players_location[pawn]:
				if city not in destinations:
					destinations.append(city)
	while True:
		goto = input("Drive/ferry/shuttle flight/move to " + str(destinations) + " or press ENTER to stay in " + players_location[pawn] + ":")
		quit_game(goto) 
		if goto == '':
			print(pawn, "is staying in", players_location[pawn])
			return
		elif goto not in destinations:
			print("Type a city that is in the list!")
		else: 
			print(pawn, "is driving to", goto)
			players_location[pawn] = goto
			players_actions[n] = players_actions[n] - 1
			print("You have", players_actions[n], "actions left")
			return

#Function for the direct flight action
def action_directflight(n, pawn):
	destinations = []
	for card in players_cards[n]:
		if card not in event_cards:
			destinations.append(card)
	while len(destinations) > 0:
		flyto = input("Direct flight to " + str(destinations) + "(hand in that card) or press ENTER to stay in " + players_location[pawn] + ":")
		if flyto == '':
			print(pawn, "is staying in", players_location[pawn])
			return	
		elif flyto not in destinations:
			print("Type a city that is in the list!")
		else: 
			print(pawn, "is flying to", flyto, ". You have to hand in that card")
			player_discard_pile.append(flyto)
			players_cards[n].remove(flyto)
			print("Cards left:", players_cards[n])
			players_location[pawn] = flyto
			players_actions[n] = players_actions[n] - 1
			print("You have", players_actions[n], "actions left")
			return
		
#Function for the charter flight action and operations expert action
operations_move = ['No']
def action_charterflight(n, pawn):
	for card in players_cards[n]:
		if card == players_location[pawn]:
			flyto = input("Charter flight from " + card + " to:")
			if flyto == '':
				print(pawn, "is staying in", players_location[pawn])
				break
			elif flyto not in all_cities:
				print("Type a city that exists!")
			else: 
				print(pawn, "is flying to", flyto, ", you have to hand in the", players_location[pawn], "card.")
				player_discard_pile.append(players_location[pawn])
				players_cards[n].remove(players_location[pawn])
				print("Cards left:", players_cards[n])
				players_location[pawn] = flyto
				players_actions[n] = players_actions[n] - 1
				print("You have", players_actions[n], "actions left.")
	if players_location[n] in cities_stations:
		if players_role[n] == 'OPERATIONS EXPERT':
			if operations_move[-1] == 'No':
				fly_list = []
				for card in players_cards[n]:
					if card not in event_cards:
						fly_list.append(card)
				if len(fly_list) > 0:
					flyto = input("OPERATIONS EXPERT flight from " + players_location[n] + " to:")
					if flyto == '':
						print("You are staying in", players_location[n])
						return
					elif flyto not in all_cities:
						print("Type a city that exists!")
					else: 
						while True:
							print("You are flying to", flyto, ", you have to hand in a card.")
							operations_card = input("Pick the card " + str(fly_list) + " you would like to use to fly to " + flyto + ":")
							if operations_card not in fly_list:
								print("Type a card that you have!")						
								continue
							else:
								player_discard_pile.append(operations_card)
								players_cards[n].remove(operations_card)
								operations_move.append('Yes')
								print("Cards left:", players_cards[n])
								players_location[n] = flyto 
								players_actions[n] = players_actions[n] - 1
								print("You have", players_actions[n], "actions left.")
								break					
		
#Function for treating disease
def action_treating(n, pawn):
	if players_role[pawn] == 'MEDIC':
		for color, v in cities_cubes[players_location[pawn]].items():
			if colors_cure[color] == 'Yes':
				if	cities_cubes[players_location[pawn]][color] > 0:
					cities_cubes[players_location[pawn]][color] = 0
					print("MEDIC automatically cured", color, cities_cubes[players_location[pawn]][color])
					disease_cubes_stock()
					if colors_cubes_stock[color] == 24:
						print("Disease", color, "is eradicated.")
	if n == pawn:					
		if sum(cities_cubes[players_location[n]].values()) > 0:
			for color, v in cities_cubes[players_location[n]].items():
				if v > 0:
					if players_role[n] == 'MEDIC':
						max_cubes = v
					elif colors_cure[color] == 'Yes':
						max_cubes = v
					else: 
						max_cubes = min(players_actions[n], v)
					while players_actions[n] > 0:
						remove_cubes = input("Type in the number of " + color + " cubes (maximum " + str(max_cubes) + ") you would like to remove from " + players_location[n] + " (" + str(v) + " " + color + " cubes present):")
						if remove_cubes == '':
							print("No", color ,"cubes will be removed.")
							break
						try:
							remove_cubes = int(remove_cubes)
							if remove_cubes == 0:
								print("No", color ,"cubes will be removed.")
								break
							elif remove_cubes > max_cubes:
								print("The maximum amount of" ,color ,"cubes you can remove is", max_cubes, ".")
								continue
							elif remove_cubes > 0:
								cities_cubes[players_location[n]][color] = cities_cubes[players_location[n]][color] - remove_cubes
								print(remove_cubes, color, "cubes have been removed!", cities_cubes[players_location[n]][color], color, "cubes left in", players_location[n])
								disease_cubes_stock()
								if colors_cure[color] == 'Yes':
									if colors_cubes_stock[color] == 24:
										print("Disease", color, "is eradicated.")
								if players_role[n] == 'MEDIC':
									players_actions[n] = players_actions[n] - 1
								elif colors_cure[color] == 'Yes':
									players_actions[n] = players_actions[n] - 1
								else:
									players_actions[n] = players_actions[n] - remove_cubes
								print("You have", players_actions[n], "actions left.")
							break
						except:
							print("Not a number, try again.")	

#Function for building a research station
def action_building(n):
	if len(cities_stations) < 6:
		if players_role[n] == 'OPERATIONS EXPERT':
			if players_location[n] not in cities_stations:
				build = input("If you want to build a research station in " + players_location[n] + " type B, otherwise press ENTER:")
				if build == 'B':
					print("You are building a research station in", players_location[n])
					cities_stations.append(players_location[n])
					players_actions[n] = players_actions[n] - 1					
					print("You have", players_actions[n], "actions left.")
					return
				else:
					print("You are not building anything.")
					return
		for card in players_cards[n]:
			if card == players_location[n]:
				if players_location[n] not in cities_stations:
					build = input("If you want to build a research station in " + players_location[n] + " type B, otherwise press ENTER:")
					if build == 'B':
						print("You are building a research station in", players_location[n])	
						player_discard_pile.append(players_location[n])
						players_cards[n].remove(players_location[n])
						print("Cards left:", players_cards[n])
						cities_stations.append(players_location[n])
						players_actions[n] = players_actions[n] - 1					
						print("You have", players_actions[n], "actions left.")
						return
					else:
						print("You are not building anything.")
						return
	
#Function for discovering cure
def discover_cure(n):
	if players_location[n] in cities_stations:
		for color in colors_list:
			count = 0
			if players_role[n] == 'SCIENTIST':
				count = count + 1
			cure_list = []
			if colors_cure[color] == 'No':
				for card in players_cards[n]:
					if card not in event_cards:
						if cities_color[card] == color:
							count = count + 1
							cure_list.append(card)
				if count > 4:
					cure = input("If you want to invent a cure for " + color + " with (part of) " + str(cure_list) + " type C, otherwise press ENTER:")
					if cure == 'C':
						colors_cure[color] = 'Yes'
						print("You just cured", color)
						players_actions[n] = players_actions[n] - 1
						print("You have", players_actions[n], "actions left.")
						disease_cubes_stock()
						if colors_cubes_stock[color] == 24:
							print("Disease", color, "is eradicated.")
						if players_role[n] == 'SCIENTIST':
							while len(cure_list) > 4:
								keep = input("Type the name of the city of the card you would like to keep:")
								if keep not in cure_list:
									print("Type a city that is in the list.")
								else:
									cure_list.remove(keep)
						else:
							while len(cure_list) > 5:
								keep = input("Type the name of the city of the card you would like to keep:")
								if keep not in cure_list:
									print("Type a city that is in the list.")
								else:
									cure_list.remove(keep)
						for c in cure_list:
							players_cards[n].remove(c)
					else:
						print("You are not curing", color)				
						
#Function for sharing knowledge (giving or taking cards)
def share_knowledge(n):
	other_players = []
	same_location = []
	share_cards = []
	for p in players_name:
		if p != n:
			other_players.append(p)
	for o in other_players:
		if players_location[o] == players_location[n]:
			same_location.append(o)
	if len(same_location) > 0:
	#Researcher role (give any 1 of your city cards)
		if players_role[n] == 'RESEARCHER':
			for card in players_cards[n]:
				if card not in event_cards:
					share_cards.append(card)
			if len(share_cards) > 0:
				if len(same_location) > 1:
					give_to = input("If you want to give a card to " + str(same_location) + " type the players name, otherwise press ENTER:")
					if give_to == '':
						return
					elif give_to not in same_location:
						print("Type a player that is in the same location!")
				else:
					give_to = same_location[0]
				give_card = input("Type the name of the city " + str(share_cards) + " you want to give to " + give_to + ", or press ENTER:")
				if give_card not in share_cards:
					print("Type a card that is in the list!")
				else:
					players_cards[n].remove(give_card)
					players_cards[give_to].append(give_card)
					players_actions[n] = players_actions[n] - 1
					print("You have", players_actions[n], "actions left.")
		#Give card that matches the city
		else:
			for card in players_cards[n]:
				if card == players_location[n]:
					give_card = card
					if len(same_location) > 1:
						give_to = input("If you want to give " + give_card + " to " + str(same_location) + " type the players name, otherwise press ENTER:")
						if give_to == '':
							break
						elif give_to not in same_location:
							print("Type a player that is in the same location!")
						else:
							players_cards[n].remove(give_card)
							players_cards[give_to].append(give_card)
							players_actions[n] = players_actions[n] - 1
							print("You have", players_actions[n], "actions left.")
					else:
						give_to = input("If you want to give " + give_card + " to " + same_location[0] + " type G, otherwise press ENTER:")
						if give_to == 'G':
							give_to = same_location[0]
							players_cards[n].remove(give_card)
							players_cards[give_to].append(give_card)
							players_actions[n] = players_actions[n] - 1
							print("You have", players_actions[n], "actions left.")
		#Researcher role (take any 1 of your city cards)
		if players_actions[n] > 0:			
			for p in same_location:
				if players_role[p] == 'RESEARCHER':
					for card in players_cards[p]:
						if card not in event_cards:
							share_cards.append(card)
					if len(share_cards) > 0:
						take_card = input("Type the name of the city " + str(share_cards) + " you want to take from " + p + ", or press ENTER:")
						if take_card == '':
							break
						elif take_card not in share_cards:
							print("Type a card that is in the list!")
						else:
							players_cards[p].remove(take_card)
							players_cards[n].append(take_card)
							players_actions[n] = players_actions[n] - 1
							print("You have", players_actions[n], "actions left.")
			#Take card that matches the city	
			for p in same_location:
				for card in players_cards[p]:
					if card == players_location[n]:
						take_card = card
						take_from = input("If you want to take " + card + " from " + p + " type T, otherwise press ENTER:")
						if take_from == 'T':
							take_from = players_location[n]
							players_cards[n].append(take_card)
							players_cards[p].remove(take_card)
							players_actions[n] = players_actions[n] - 1
							print("You have", players_actions[n], "actions left.")	

#FUNCTIONS FOR DRAWING CARDS AND INFECTING CITIES
		
#Function for infecting cities
def infect_cities():
	count = 0
	prevent = 'No'
	prevent_role = None
	while count < infection_rate[infection_rate_marker]:
		card = infection_deck.pop(0)
		infection_discard_pile.append(card)
		color = cities_color[card]
		for k, v in players_location.items():
			if v in cities_linked[card] or v == card:
				if players_role[k] == 'QUARANTINE SPECIALIST':
					prevent = 'Yes'
					prevent_role = players_role[k]
			elif v == card:
				if players_role[k] == 'MEDIC':
					if colors_cure[color] == 'Yes':
						prevent = 'Yes' 
						prevent_role = players_role[k]
		if prevent == 'Yes':
			print("Card drawn:", card, "Luckely", prevent_role, "prevents infection disease cube placements.")
			count = count + 1
			prevent = 'No'		
		#elif card in :
		#	print "Card drawn:", card, "Already an outbreak."
		#	count = count + 1
		else:	
			if cities_cubes[card][color] == 3:
				print("Card drawn:", card, color, "OUTBREAK!")
				outbreak(card, color)
				del chain_outbreak[:]	
				count = count + 1
			else:
				if colors_cure[color] == 'Yes' and colors_cubes_stock[color] == 24:
					print("Card drawn:", card, color, "is eradicated, no cubes added.")
					count = count + 1	
				else:
					add_cubes(card)
					print("Card drawn:", card, "infected with 1", color, "cube. Now in total",) 
					display_cubes(card)
					count = count + 1	
		event_card_check()	
	return

#Function for outbreak which takes as argument the outbreak city
chain_outbreak = []
total_outbreak = []
outbreak_prevent = []
def outbreak(city, color):
	print("Outbreak in", city, ", cities affected:", cities_linked[city])
	chain_outbreak.append(city)
	total_outbreak.append(city)
	for k, v in players_role.items():
		if v == 'QUARANTINE SPECIALIST':
			outbreak_prevent.append(players_location[k])
			for link in cities_linked[players_location[k]]:
				outbreak_prevent.append(link)
		if v == 'MEDIC':
			if colors_cure[color] == 'Yes':
				outbreak_prevent.append(players_location[k])
	for link in cities_linked[city]:
		if link not in outbreak_prevent:
			cities_cubes[link][color] = cities_cubes[link][color] + 1	
		else:
			print("QUARANTINE SPECIALIST or MEDIC prevents outbreak disease cube placements in", link)
	for link in cities_linked[city]:	
		if cities_cubes[link][color] > 3:
			cities_cubes[link][color] = 3
			if link not in chain_outbreak:
				outbreak(link, color)
			else: 
				print("Already an outbreak in", link, "no new outbreak.")	
		print("There are now", cities_cubes[link][color], color, "cubes in", link)
	del outbreak_prevent[:]
		
#Function for drawing 2 player cards
def draw_player_cards(n):
	epidemics_drawn = 0
	count = 0
	while count < 2:
		card_given = player_deck.pop(0)
		if card_given == 'EPIDEMIC':
			print("EPIDEMIC!", len(player_deck), "cards left in the player deck!")
			epidemics_drawn = epidemics_drawn + 1
			count = count + 1
			continue
		else:
			players_cards[n].append(card_given)
			print(card_given, "drawn from player deck.", len(player_deck), "cards left in the player deck!")
			count = count + 1
	return epidemics_drawn
		
#Function for resolving epidemic
shuffle_deck = []
def resolve_epidemics(epidemics, marker):
	prevent = 'No'
	prevent_role = None
	if epidemics > 0:
		while epidemics > 0:
			marker = marker + 1
			card = infection_deck.pop(-1)
			color = cities_color[card]
			for k, v in players_location.items():
				if v in cities_linked[card] or v == card:
					if players_role[k] == 'QUARANTINE SPECIALIST':
						prevent = 'Yes'
						prevent_role = players_role[k]
				elif v == card:
					if players_role[k] == 'MEDIC':
						if colors_cure[color] == 'Yes':
							prevent = 'Yes' 
							prevent_role = players_role[k]			
			if prevent == 'Yes':
				print("Epidemic card infection: Luckely", prevent_role, "prevents epidemic disease cube placements in" ,card)
				prevent = 'No'
				infection_discard_pile.append(card)
			#elif card in chain_outbreak:
			#	print "Epidemic card infection: Already an outbreak in", card
			#	infection_discard_pile.append(card)			
			else:	
				if cities_cubes[card][color] > 0:
					cities_cubes[card][color] = 3
					infection_discard_pile.append(card)
					print("Epidemic card infection:", card, color, "OUTBREAK!")
					outbreak(card, color)
					del chain_outbreak[:]	
				else:
					infection_discard_pile.append(card)
					if colors_cure[color] == 'Yes' and colors_cubes_stock[color] == 24:
						print("Epidemic card infection:", card, color, "is eradicated, no cubes added in", card)
					else:		
						add_cubes(card)
						add_cubes(card)
						add_cubes(card)		
						print("Epidemic card infection:", card, "infected with 3 cubes. Now in total",) 
						display_cubes(card)
			epidemics = epidemics - 1
			event_card_check()
			random.shuffle(infection_discard_pile)
			for card in infection_discard_pile:
				shuffle_deck.append(card)
			del infection_discard_pile[:]
			random.shuffle(shuffle_deck)
			for card in shuffle_deck:
				infection_deck.insert(0, card)
			del shuffle_deck[:]
			event_card_check()
			if epidemics > 0:
				event_card_check()
	return marker

#Function for discarding to 7 player cards
def discard_cards(n):
	while len(players_cards[n]) > 7:
		print("You have", len(players_cards[n]) ,"player cards (maximum is 7).")
		event_card_check()
		if len(players_cards[n]) < 8:
			break
		for card in players_cards[n]:
			print(card,)  
			if card not in event_cards:
				print(cities_color[card])
			else:
				print("event")
		discard = input("Type the name of the city or event if you want to discard that card:")
		if discard not in players_cards[n]:
			print("Type a city that is in the list.")
		elif discard in players_cards[n]:
			print ("You are discarding", discard)
			print ("\n################################################################################\n")
			players_cards[n].remove(discard)
			player_discard_pile.append(discard)				
	return

#Check whether cubes are out of stock
diseases_out_of_stock = 'No'
def cubes_out_of_stock():
	min_val = min(colors_cubes_stock.values())
	color = [k for k, v in colors_cubes_stock.items() if v == min_val]
	if min_val < 0:
		return color[0]
	else:
		return 'No'			

#FUNCTIONS FOR EVENT CARDS

#Function to check whether event cards are in player cards
def event_card_check():
	event_check = []
	for n in players_name:
		for card in players_cards[n]:
			if card in event_cards:
				event_check.append(card)
	if len(event_check) > 0:	
		event = input("To play an event card type E.")
		if event == 'E':
			play_event_card()
	
#Play event card function
one_quiet_night = ['No']
def play_event_card():
	while True:
		player_event_cards = []
		used_event_cards = []
		player_event_letters = []
		event_cards_owner = []
		removed_event_cards = []
		for n in players_name: 
			for card in players_cards[n]:
				if card in event_cards:
					player_event_cards.append(card)
					event_cards_owner.append(n)
					player_event_letters.append(card[0])
		for card in stored_event_cards:
			player_event_cards.append(card)
			player_event_letters.append(card[0])
			event_cards_owner.append('CONTINGENCY PLANNER')
		if len(player_event_cards) == 0:
			print("You have no event cards to play.")
			break
		else: 
			print("You can play one or more of the cards:",) 
			for card, owner in zip(player_event_cards, event_cards_owner):
				print(card, "(" , owner, ")")	
			play_card = input("Type the first letter of the card if you want to play that card or type Q to quit:")
			if play_card in player_event_letters:
				if play_card == 'A':
					play_card = 'AIRLIFT'
					print("Play", play_card)
					event_airlift()
					if play_card in stored_event_cards:
						removed_event_cards.append(play_card)
						stored_event_cards.remove(play_card)
					else:
						used_event_cards.append(play_card)
						player_discard_pile.append(play_card)
				elif play_card == 'F':
					play_card = 'FORECAST'
					print("Play", play_card)
					event_forecast()
					if play_card in stored_event_cards:
						removed_event_cards.append(play_card)
						stored_event_cards.remove(card)
					else:
						used_event_cards.append(play_card)
						player_discard_pile.append(play_card)
				elif play_card == 'G':
					play_card = 'GOVERNMENT GRANT'
					print("Play", play_card)
					event_government_grant()
					if play_card in stored_event_cards:
						removed_event_cards.append(play_card)
						stored_event_cards.remove(play_card)
					else:
						used_event_cards.append(play_card)
						player_discard_pile.append(play_card)
				elif play_card == 'O':
					play_card = 'ONE QUIET NIGHT'
					print("Play", play_card)
					one_quiet_night.append('Yes')
					print("No cities will be infected.")
					if play_card in stored_event_cards:
						removed_event_cards.append(play_card)
						stored_event_cards.remove(play_card)
					else:
						used_event_cards.append(play_card)
						player_discard_pile.append(play_card)
				elif play_card == 'R':	
					play_card = 'RESILIENT POPULATION'
					print("Play", play_card)
					used = event_resilient_population()
					if used == 'Yes':
						if play_card in stored_event_cards:
							removed_event_cards.append(play_card)
							stored_event_cards.remove(play_card)
						else:
							used_event_cards.append(play_card)
							player_discard_pile.append(play_card)
					else: 
						print("You did not use", play_card, "so you keep it.")
			for n in players_name: 
				for card in players_cards[n]:
					if card in used_event_cards:
						players_cards[n].remove(card)		
			if play_card == 'Q':
				break
	return

#Function for taking a discarded player event card as contingency planner
def take_event_card_contingency(n):
	event_cards_letters = []
	if players_role[n] == 'CONTINGENCY PLANNER':
		if len(stored_event_cards) == 0:
			for card in player_discard_pile:
				if card in event_cards:
					event_cards_letters.append(card[0])
			if len(event_cards_letters) > 0:
				print("You can take a discarded player card:",)
				for card in player_discard_pile:
					if card in event_cards:
						print(card,)
				print(" ")
				take = input("Type the first letter of the card if you want to take, otherwise press ENTER:")
				if take in event_cards_letters:
					if take == 'A':
						take = 'AIRLIFT'
					elif take == 'F':
						take = 'FORECAST'
					elif take == 'G': 
						take = 'GOVERNMENT GRANT'
					elif take == 'O': 
						take = 'ONE QUIET NIGHT'
					elif take == 'R': 
						take = 'RESILIENT POPULATION'
					stored_event_cards.append(take)
					player_discard_pile.remove(take)	
					print(take, "is now stored on your role card.")
					players_actions[n] = players_actions[n] - 1
					print("You have", players_actions[n], "actions left.")			
				else:
					return	
					
#Function for the government grant event card			
def event_government_grant():
	if len(cities_stations) > 5:
		print("There are already 6 research stations, you can not use this card anymore!")
	else:
		while True:
			build_station = input("Type the name of the city where you would like to build a research station:")
			if build_station not in all_cities:
				print("Type a city that exists!")
				continue
			if build_station in cities_stations:
				print(build_station, "already has a research station.")
				continue
			cities_stations.append(build_station)
			print("You are building a research station in", build_station)
			print(cities_stations)
			break

#Function for the airlift event card
def event_airlift():
	while True:
		for n in players_name:
			print(n, players_location[n])
		move = input("Type the name of the player you would like to move:")
		if move not in players_name:
			print("Type a player that exists!")
			continue
		else:
			move_to = input("Type the name of the city where you would like to move " + move + " to:")
			if move_to not in all_cities:
				print("Type a city that exists!")
				continue				
			elif move_to is players_location[move]:
				print(move, "is already in that city.")
				continue
			else:	
				players_location[move] = move_to
				print(move, "is now in", players_location[move])
				#The medic's automatic removal if he is moved by airlift
				if players_role[move] == 'MEDIC':
					for color, v in cities_cubes[move_to].items():
						if colors_cure[color] == 'Yes':
							if	cities_cubes[move_to][color] > 0:
								cities_cubes[move_to][color] = 0
								print("MEDIC automatically cured", color, cities_cubes[move_to][color])
								disease_cubes_stock()
								if colors_cubes_stock[color] == 24:
									print("Disease", color, "is eradicated.")
				break
				
#Function for the forecast event card
def event_forecast():
	while True:
		deck_look = []
		for card in infection_deck[0:6]:
			print(card,)
			display_cubes(card)
			deck_look.append(card)
		del infection_deck[0:6]
		print("Rearrange the top 6 cards of the Infection Deck.")
		count = 6
		while count > 0:
			if count == 6:
				position = 'last'
			elif count == 1:
				position = 'first'
			else:
				position = str(count)
			card = input("Infected " + position + ":")
			if card in deck_look:
				deck_look.remove(card)
				infection_deck.insert(0, card)
				count = count - 1
			elif card in infection_deck:
				print("Give a card that is still available!")
				continue
			else:
				print("Give a card that is in the list!")
				continue
		print("Top of the infection deck:", infection_deck[0:6])
		agree = input("Type C if you want to change the order, otherwise press ENTER:")
		if agree == 'C':
			continue
		else:
			break
		
#Function for the resilient population card
def event_resilient_population():
	if len(infection_discard_pile) > 0:
		print("Infection discard pile:",)
		print(infection_discard_pile)
		remove = input("Type the name of the city where you would like to remove from the infection discard pile:")
		if remove in infection_discard_pile:
			infection_discard_pile.remove(remove)
			removed_from_game.append(remove)
			used = 'Yes'
			return used
		else:
			print("Type a name of a city that is in the infection discard pile.")
	else: 
		print("There are no cards in the information discard pile.")
		used = 'No' 
		return used

#PLAY THE GAME AND SHOW RESULTS OF THE GAME

#Tests to test the game
#players_cards[0].append('BOGOTA')
#players_cards[0].append('BOGOTA')
#players_cards[0].append('BOGOTA')
#players_cards[1].append('CHENNAI')
#players_cards[1].append('CHENNAI')
#players_cards['WOUTER'].append('RESILIENT POPULATION')
#players_cards['WOUTER'].append('FORECAST')	
#players_cards['MARJOLEIN'].append('ATLANTA')
#players_location['PETER'] = 'MIAMI'
#players_role['PETER'] = 'RESEARCHER'
#players_cards['MARJOLEIN'].append('FORECAST')
#cities_cubes['MIAMI']['red'] = 2
#cities_cubes['MIAMI']['blue'] = 1
#colors_cure['blue'] = 'Yes'

#Highscores
def highscores():	
	results = 'pan_results.txt'
	rs = open(results)
	won = 0
	games = 0
	highscores = []
	highplayers = []
	for line in rs:
		line = line.rstrip()
		if line.startswith('Players:'):
			games = games + 1
			score_start = line.index('Score')
			score_end = line.index('Version')
			players_end = line.index('Roles')
			highscores.append(int(line[score_start + 7:score_end - 1]))
			highplayers.append(line[0:players_end -1])
			if 'Won' in line:
				won = won + 1
	if highscores[-1] == max(highscores):
		print("You have a new HIGHSCORE!")
	print("\nHIGHSCORES")
	count = 0
	ranking = 1
	if games < 10:
		count = count + (10 - games)	
	while count < 10:
		n = highscores.index(max(highscores))
		print(ranking,)
		print(highscores.pop(n),)
		print(highplayers.pop(n))
		ranking = ranking + 1
		count = count + 1
	print("\nThere were", won, "games won out of", games, ". That's", int(((won/games)*100)), "percent.")

#Calculate and write the results
def results(difficulty, game_status, outbreaks_marker, version):
    #Calculate the number of cubes left
    cubes_left = 0
    for color, cubes in colors_cubes_stock.items():
	    cubes_left = cubes_left + cubes
	
    #Calculate the score
    if game_status == 'Won':
	    score = (200 + (cubes_left / 1.0) + (len(player_deck) * 3.0) - (outbreaks_marker * 5.0)) * (difficulty * 10)
    else:
	    score = (200 + (cubes_left / 1.0) - (len(player_deck) * 3.0) - (outbreaks_marker * 5.0)) * (difficulty * 10)
    score = int(score)
    print("Your SCORE is", score)

    #Write to results
    roles_list = []
    for players, roles in players_role.items():
	    roles_list.append(roles)
    save = open('pan_results.txt', 'a')
    save.write("\n")
    save.write("Players: ")
    save.write(str(players_name))
    save.write(" Roles: ")
    save.write(str(roles_list))
    save.write(" Diff: ")
    save.write(str(difficulty))
    save.write(" Result: ")
    save.write(game_status)
    save.write(" Cubes left: ")
    save.write(str(cubes_left))
    save.write(" Cards left: ")
    save.write(str(len(player_deck)))
    save.write(" Outbreaks: ")
    save.write(str(outbreaks_marker))
    save.write(" Score: ")
    save.write(str(score))
    save.write(" Version: ")
    save.write(version)
    save.write(" Epidemic list: ")
    save.write(str(epidemic_list))    
    save.write(" Start cubes black: ")
    save.write(str(start_cubes['black']))
    save.write(" Start cubes blue: ") 
    save.write(str(start_cubes['blue']))
    save.write(" Start cubes red: ")
    save.write(str(start_cubes['red']))
    save.write(" Start cubes yellow: ")
    save.write(str(start_cubes['yellow']))
    save.close()

#Calculate score and quit the game
def quit_game(end):
	if end == 'QUIT':
	
	    #Write to results
		if len(player_deck) >= 52-(len(players_name)*2*2):
		    print("You QUIT the game, not enough rounds played to calculate and set a SCORE.")
		else:
		    game_status = 'Quit'
		    results(difficulty, game_status, outbreaks_marker, version)
		
		#Quit the game
		quit()

#Play the game
print(board_overview())
play_game = 'Yes'
turns = 0
while play_game == 'Yes':
	for n in players_name:
		turns = turns + 1
		print(n, "the", players_role[n], "in", players_location[n], ". It is turn", turns, ", you have 4 actions.")
		print(" ")
		#Do the player actions
		while players_actions[n] > 0:
			discover_cure(n)
			if players_actions[n] > 0:
				share_knowledge(n)
			if players_actions[n] > 0:
				action_treating(n, n)
			if players_actions[n] > 0:
				action_building(n)
			#Player moving actions
			if players_actions[n] > 0:
				action_drive(n, n)
			if players_actions[n] > 0:
				action_charterflight(n, n)	
			if players_actions[n] > 0:
				action_directflight(n, n)
			#Contingency planner can take a card from the player discard pile
			if players_actions[n] > 0:
				take_event_card_contingency(n)
			#Dispatcher can move other pawn
			if players_actions[n] > 0:
				if players_role[n] == 'DISPATCHER':
					pawn = input("Type the name of the other player you want to move:")
					if pawn in players_name:
						if pawn != n:
							while True:							
								if players_actions[n] > 0:
									action_drive(n, pawn)
									action_treating(n, pawn)
								if players_actions[n] > 0:
									action_charterflight(n, pawn)
									action_treating(n, pawn)	
								if players_actions[n] > 0:
									action_directflight(n, pawn)
									action_treating(n, pawn)
								if players_actions[n] == 0:
									break
								end = input("To end moving " + pawn + " type Q.")
								if end == 'Q':
									break		
			#Medic automatically cures
			for p in players_role:
				if players_role[p] == 'MEDIC':
					for color, v in cities_cubes[players_location[p]].items():
						if colors_cure[color] == 'Yes':
							if	cities_cubes[players_location[p]][color] > 0:
								cities_cubes[players_location[p]][color] = 0
								print("MEDIC automatically cured", color, cities_cubes[players_location[p]][color])
								disease_cubes_stock()
								if colors_cubes_stock[color] == 24:
									print("Disease", color, "is eradicated.")
			end = input("For event cards type E, to end your turn type Q.")
			quit_game(end)	
			if end == 'Q':
				break
			elif end == 'E':
				play_event_card()
			else:
				continue
		print("\n################################################################################\n")
		#Do a win or loss check
		if all(cure == 'Yes' for cure in colors_cure.values())	== True:
			print("Cures to all 4 diseases are discovered. The players WIN!")
			game_status = 'Won'
			break
		if len(player_deck) < 2:
			print("Only", len(player_deck), "cards in the player deck left (your team runs out of time), GAME OVER!")
			game_status = 'Lost'
			break
		disease_cubes_stock()
		#Draw the player cards, resolve epidemics and discard cards
		epidemics_drawn = draw_player_cards(n)
		infection_rate_marker = resolve_epidemics(epidemics_drawn, infection_rate_marker)	
		if len(players_cards[n]) > 7:
			discard_cards(n)
		#Only an event card check when there are no epidemics drawn				
		if epidemics_drawn == 0:
			event_card_check()
		#Infect cities if there is no one quiet night
		if one_quiet_night[-1] == 'No': 
			infect_cities()
		else:
			one_quiet_night.append('No')
		#Do a loss check
		disease_cubes_stock()
		outbreaks_marker = len(total_outbreak)
		diseases_out_of_stock = cubes_out_of_stock()
		if diseases_out_of_stock != 'No':
			print("The disease cubes of", diseases_out_of_stock, "are out of stock (the disease has spread too much), GAME OVER!")
			game_status = 'Lost'
			break
		if outbreaks_marker > 7:
			print("8 outbreaks occur (a worldwide panic happens), GAME OVER!")
			game_status = 'Lost'
			break
		print(board_overview())		
		#Give the player 4 new actions and give the operations expert a new operations move
		for n in players_actions:
			players_actions[n] = 4		
		operations_move.append('No')
	#Get out of the loop if the game is lost or won
	if game_status != 'Not finished':
		break	

#Show the result of the game
print(board_overview()) 
if game_status == 'Lost':
	print("\nTHE PLAYERS LOSE, TOO BAD!\n")
elif game_status == 'Not finished':
	print("\nTHE GAME HAS NOT BEEN FINISHED!\n")
else:
	print("\nTHE PLAYERS WIN, AWESOME!\n")	

#Calculate and write results
results(difficulty, game_status, outbreaks_marker, version)

#Show the highscores
highscores()