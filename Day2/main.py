# The Elf would first like to know which games would have been possible if the bag contained only 12 red cubes, 13 green cubes, and 14 blue cubes? but cube is a str like ['3 green', '1 blue', '3 red']
# def is_more_than_max_cube(cube):
# 	tmp = cube.strip(' ')
# 	tmp = tmp.split(", ")
# 	# si la derniere ligne de tmp du tableau tmp se termine par un \n alors on elenve le \n
# 	if tmp[len(tmp) - 1][len(tmp[len(tmp) - 1]) - 1] == "\n":
# 		tmp[len(tmp) - 1] = tmp[len(tmp) - 1][:-1]
# 	i = 0
# 	while i < len(tmp):
# 		tmp2 = tmp[i].split(" ")
# 		if tmp2[1] == "red":
# 			if int(tmp2[0]) > 12:
# 				print("Game " + str(index) + " is impossible")
# 				return False
# 		elif tmp2[1] == "green":
# 			if int(tmp2[0]) > 13:
# 				print("Game " + str(index) + " is impossible")
# 				return False
# 		elif tmp2[1] == "blue":
# 			if int(tmp2[0]) > 14:
# 				print("Game " + str(index) + " is impossible")
# 				return False
# 		i+=1
# 	return True

# input = open("input.txt", "r")
# index = 0
# somme = 0
# j = 0
# count = 0
# tmp = input.readline().split(":")
# while tmp != [""]:
# 	index += 1
# 	tmp[0] = tmp[1]
# 	del tmp[1]
# 	tmp2 = tmp[0].split(";")
# 	while j < len(tmp2):
# 		if is_more_than_max_cube(tmp2[j]) == True:
# 			count += 1
# 		j+=1
# 		if count != j:
# 			break
# 	if count == len(tmp2):
# 		somme += index
# 	count = 0
# 	j = 0
# 	tmp = input.readline().split(":")
# print("The number of the sum of the IDs of those games is" + str(somme))


# Partie 2
# On calcule cette pous le nombre qu'il aurait fallut au minumum pour que le jeu soit possible avec les 3 couleurs
# exemple line = 3 green, 1 blue, 3 red; 3 blue, 1 green, 3 red; 2 red, 12 green, 7 blue; 1 red, 4 blue, 5 green; 7 green, 2 blue, 2 red
def max_of_each_color(line):
	j = 0
	max_blue = 0
	max_green = 0
	max_red = 0
	while j < len(line):
		tmp = line[j].strip(' ')
		tmp = tmp.split(", ")
		# si la derniere ligne de tmp du tableau tmp se termine par un \n alors on elenve le \n
		if tmp[len(tmp) - 1][len(tmp[len(tmp) - 1]) - 1] == "\n":
			tmp[len(tmp) - 1] = tmp[len(tmp) - 1][:-1]
		i = 0
		while i < len(tmp):
			tmp2 = tmp[i].split(" ")
			if tmp2[1] == "red":
				if int(tmp2[0]) > max_red:
					max_red = int(tmp2[0])
			elif tmp2[1] == "green":
				if int(tmp2[0]) > max_green:
					max_green = int(tmp2[0])
			elif tmp2[1] == "blue":
				if int(tmp2[0]) > max_blue:
					max_blue = int(tmp2[0])
			i+=1
		j+=1
	somme = max_blue * max_green * max_red
	return somme

input = open("input.txt", "r")
index = 0
somme = 0
j = 0
count = 0
tmp = input.readline().split(":")
while tmp != [""]:
	index += 1
	tmp[0] = tmp[1]
	del tmp[1]
	tmp2 = tmp[0].split(";")
	somme += max_of_each_color(tmp2)
	print("somme = " + str(somme))
	count = 0
	j = 0
	tmp = input.readline().split(":")
print("The number of the sum of the IDs of those games is" + str(somme))
