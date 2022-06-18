nested_dict = {
    "Cricket" : {"Ashwin R": 37, "Jasprit Bumrah": 28, "Yuzvendra Chahal": 31, "Deepak Chahar": 29, "Shikhar Dhawan": 36, "Virat Kohli": 33},
    "Football" : {"Manvir Singh": 28, "Rahim Ali": 32, "Liston Colaco": 33, "Jeakson Singh" :28, "Chinglensana Singh": 36, "Amrinder Singh": 29}
}


list_of_players = list(nested_dict.items())

print("List of Players: ", list_of_players)

list_of_keys = list(nested_dict)

print("List of Keys: ", list_of_keys)

print("Single Item: ", nested_dict["Cricket"]["Virat Kohli"])

print("List of Players Dict: ", nested_dict)

del nested_dict["Cricket"]["Ashwin R"]
del nested_dict["Football"]["Amrinder Singh"]

nested_dict["Football"]["Amrinder Singh"] = 34

print("List of Players: ", list_of_players)