import random
import Classes

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

#Places three locations locations on the map
for location_id in locations:
    placed = False
    while placed == False:
        row, column = random.randint(0, 4), random.randint(0, 4)
        if game_map[row][column] == 0:
            game_map[row][column] = location_id
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
    move = input("\nMove (w/a/s/d): ").lower()

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
    if destination in [1, 2, 3]:
        print(f"*** You found location {destination}! ***")

        if destination == 1:
            Classes.Question1.askQuestion()
        
        elif destination == 2:
            Classes.Question2.askQuestion()

        elif destination == 3:
            Classes.Question3.askQuestion()
            


    #Updates the map
    game_map[old_row][old_column] = 0
    game_map[player_row][player_column] = 'P'

    #Reprints the updated map
    for row in game_map:
        print(" ".join(map(str, row)))