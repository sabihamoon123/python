# capitals = {
#     "France" : "Paris",
#     "Germany" : "Berlin",
# }

# # Nesting a list in a dictionary

# travel_log = {
#     "France" : {"cities_visited":["Paris","Lille","Dijon"], "total_visited":12},
#     "Germany" : {"cities_visited":["Berlin","Hamburg","Stuttgart"], "total_visited":5},
# }

Country = input()
total_visited = int(input())
list_of_cities = eval(input())

travel_log = [
    {
        "Country":"France" , 
        "cities":["Paris","Lille","Dijon"], 
        "total_visited":12
    },
    {
        "Country":"Germany" ,
        "cities":["Berlin","Hamburg","Stuttgart"], "total_visited":5},
]

def add_new_country(name, time_visited, cities_visited):
    new_country = {}
    new_country["Country"] = name
    new_country["total_visited"] = time_visited
    new_country["cities"] = cities_visited
    travel_log.append(new_country)

add_new_country(Country, total_visited, list_of_cities)
print(f"I've been to {travel_log[2]['Country']} {travel_log[2]['total_visited']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")