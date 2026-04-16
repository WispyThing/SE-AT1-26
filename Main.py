import random
import Classes

print("Welcome to Oscar's super duper ultra mega cool educational game about tests (and some other stuff)!\nYou must travel around the map using w, a, s, and d, which moves your character (P) to reach the three main locations (1, 2 and 3) to win!\nYou can also go to minigame locations (M) to score some extra points!")
print("")

game_map = [
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0]
]

#Places a character on map
game_map[random.randint(0, 4)][random.randint(0, 4)] = 'P'


#List of locations to place
locations = [1, 2, 3]

#List of locations which have been visited by the player
visited_locations = []

#Places three locations locations on the map
for location_id in locations:
    placed = False
    while placed == False:
        row = random.randint(0, 4)
        column = random.randint(0, 4)
        if game_map[row][column] == 0:
                game_map[row][column] = location_id
                placed = True

#Pretty much just copy pasted the code above and tweaked it so we have three new minigame locations
for M in locations:
    placed = False
    while placed == False:
        row = random.randint(0, 4)
        column = random.randint(0, 4)
        if game_map[row][column] == 0:
                game_map[row][column] = 'M'
                placed = True


for row in game_map:
    #Had to look up how to do this wizadry but it gets rid of all the ugly parts of the map
    print(" ".join(map(str, row)))

#Find where the player was randomly placed
for row in range(5):
    for column in range(5):
        if game_map[row][column] == 'P':
            player_row = row
            player_column = column

#Movement Loop
while True:
    #Takes users input to move, little tail on the end allows them to use capitals letters and it will still work!
    print("")
    move = input("Move (w/a/s/d): ").lower()
    print("")

    #Store old position to clear it
    old_row = player_row
    old_column = player_column

    #Update coordinates with boundary checks
    if move == 'w' and player_row > 0:
        player_row -= 1
    elif move == 's' and player_row < 4:
        player_row += 1
    elif move == 'a' and player_column > 0:
        player_column -= 1
    elif move == 'd' and player_column < 4:
        player_column += 1
    
    #Checks if the player has moved to a location before overwriting
    destination = game_map[player_row][player_column]
    
    #Asks the questions
    if destination in [1, 2, 3]:
        
        #Puts to location in in the "visited_locations" array so that we can trigger the win condition
        visited_locations.append(destination)

        print(f"You found location {destination}!")
        print("")

        if destination == 1:
            Classes.Question1.askQuestion()
            
        elif destination == 2:
            Classes.Question2.askQuestion()

        elif destination == 3:
            Classes.Question3.askQuestion()

    #Begins a minigame
    elif destination == 'M':
        print("You found a minigame!")
        print("")
        Classes.minigameSelection()       
    
    #The win condition, if the length of the "visited_locations" array is 3 (meaning all three locations have been visited) the game ends
    if len(visited_locations) == 3:
        print(f"You completed all locations! You win! Your score is {Classes.score}!")
        break



    #Updates the map
    game_map[old_row][old_column] = 0
    game_map[player_row][player_column] = 'P'

    #Reprints the updated map
    for row in game_map:
        print(" ".join(map(str, row)))