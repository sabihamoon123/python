# modifying global
enemies =1 

def increase_enemies():
    # global enemies
    # enemies += 2
    print(f"Enemies inside the function: {enemies}")
    return enemies + 1

enemies = increase_enemies()
print(f"Enemies outside the function: {enemies}")

#local scope

# def drink_potion():
#     potion_strength = 2
#     print(potion_strength)

# drink_potion()
# print(potion_strength)

# global scope

# player_health = 10
# def game():
#     def drink_potion():
#         potion_strength = 2
#         print(player_health)

#     drink_potion()
# print(player_health)

# There is no block scope

# game_level = 3
# def game():
#     enemies= ["Skeleton", "Zombie", "Alien"]
#     if game_level < 5:
#         new_enemy = enemies[0]

#     print(new_enemy)
# game()