import random
# my_list = [1, 2, 3, 4, 5]
# print(random.choice(my_list))

def roll():
    min_value = 1 
    max_value = 6
    roll = random.randint(min_value, max_value)

    return roll
    
# value = roll()
# print(value)

while True:
    players = input("Enter the number of players (1-4): ")
    if players.isdigit():
        players = int(players)
        if 2<= players <= 4:
            break
        else:
            print('Must be between 2 - 4 players.')
    else:
        print("invalid")
    
print()    