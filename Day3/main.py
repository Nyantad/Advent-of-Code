# Version: 1.0
# A little bit more complexe

# input = open("input.txt", "r")
# output = open("output.txt", "r+")
# output.truncate()
# output.close()
# output = open("output.txt", "a")


# # symbol = *+=-&#%/@
# tabDouble = input.read().split("\n")

# # on check si les nombre dans le tableau de tableau sont coller a des symboles par exemple :
# # 6541.....54*...45*
# # ....*.....54...68
# # Ici seulement le dernier chiffre 68 n'est pas valide car il n'est pas coller a un symbole que ce soit en diagonale ou en ligne et pour chaque nombre et pas chiffre coller a un symbole on l'ajoute a somme
# i = 0
# j = 0

# # on check si les nombre dans le tableau de tableau sont coller a des symboles sans depasser du tableau grace a i et j qui sont les coordonnes du tableau
# def check_around_case(tabDouble, i , j, symbol_check):
# 	if i == 0 and j == 0:
# 		if tabDouble[i][j+1] == symbol_check or tabDouble[i+1][j] == symbol_check or tabDouble[i+1][j+1] == symbol_check:
# 			return True
# 	elif i == 0 and j == len(tabDouble[i]) - 1:
# 		if tabDouble[i][j-1] == symbol_check or tabDouble[i+1][j] == symbol_check or tabDouble[i+1][j-1] == symbol_check:
# 			return True
# 	elif i == len(tabDouble[i]) - 1 and j == 0:
# 		if tabDouble[i][j+1] == symbol_check or tabDouble[i-1][j] == symbol_check or tabDouble[i-1][j+1] == symbol_check:
# 			return True
# 	elif i == len(tabDouble[i]) - 1 and j == len(tabDouble[i]) - 1:
# 		if tabDouble[i][j-1] == symbol_check or tabDouble[i-1][j] == symbol_check or tabDouble[i-1][j-1] == symbol_check:
# 			return True
# 	elif i == 0:
# 		if tabDouble[i][j-1] == symbol_check or tabDouble[i][j+1] == symbol_check or tabDouble[i+1][j] == symbol_check or tabDouble[i+1][j-1] == symbol_check or tabDouble[i+1][j+1] == symbol_check:
# 			return True
# 	elif i == len(tabDouble[i]) - 1:
# 		if tabDouble[i][j-1] == symbol_check or tabDouble[i][j+1] == symbol_check or tabDouble[i-1][j] == symbol_check or tabDouble[i-1][j-1] == symbol_check or tabDouble[i-1][j+1] == symbol_check:
# 			return True
# 	elif j == 0:
# 		if tabDouble[i-1][j] == symbol_check or tabDouble[i+1][j] == symbol_check or tabDouble[i][j+1] == symbol_check or tabDouble[i-1][j+1] == symbol_check or tabDouble[i+1][j+1] == symbol_check:
# 			return True
# 	elif j == len(tabDouble[i]) - 1:
# 		if tabDouble[i-1][j] == symbol_check or tabDouble[i+1][j] == symbol_check or tabDouble[i][j-1] == symbol_check or tabDouble[i-1][j-1] == symbol_check or tabDouble[i+1][j-1] == symbol_check:
# 			return True
# 	else:
# 		if tabDouble[i-1][j] == symbol_check or tabDouble[i+1][j] == symbol_check or tabDouble[i][j-1] == symbol_check or tabDouble[i][j+1] == symbol_check or tabDouble[i-1][j-1] == symbol_check or tabDouble[i-1][j+1] == symbol_check or tabDouble[i+1][j-1] == symbol_check or tabDouble[i+1][j+1] == symbol_check:
# 			return True
# 	return False



# count = 0
# somme = 0
# skip_next = False
# while i < len(tabDouble):
# 	while j < len(tabDouble[i]):
# 		if j < len(tabDouble[i]) and tabDouble[i][j].isdigit() :
# 			while j < len(tabDouble[i])and tabDouble[i][j].isdigit() :
# 				count += 1
# 				if check_around_case(tabDouble, i, j, "*") or check_around_case(tabDouble, i, j, "+") or check_around_case(tabDouble, i, j, "-") or check_around_case(tabDouble, i, j, "/") or check_around_case(tabDouble, i, j, "=") or check_around_case(tabDouble, i, j, "#") or check_around_case(tabDouble, i, j, "&") or check_around_case(tabDouble, i, j, "%") or check_around_case(tabDouble, i, j, "/") or check_around_case(tabDouble, i, j, "@") or check_around_case(tabDouble, i, j, "$"):
# 					while j < len(tabDouble[i]) and tabDouble[i][j].isdigit() :
# 						count += 1
# 						j += 1
# 					# On a lu le nombre en entier et on l'ajoute a somme
# 					somme += int(tabDouble[i][j-count+1:j])
# 					output.write(tabDouble[i][j-count+1:j] + "\n")
# 				if  j < len(tabDouble[i]) and tabDouble[i][j] != '.' and tabDouble[i][j] != '*' and tabDouble[i][j] != '+' and tabDouble[i][j] != '-' and tabDouble[i][j] != '/' and tabDouble[i][j] != '=' and tabDouble[i][j] != '#' and tabDouble[i][j] != '&' and tabDouble[i][j] != '%' and tabDouble[i][j] != '@' and tabDouble[i][j] != '$':
# 					j += 1
# 			if j < len(tabDouble[i]) and (tabDouble[i][j] == '.' or tabDouble[i][j] == '*' or tabDouble[i][j] == '+' or tabDouble[i][j] == '-' or tabDouble[i][j] == '/' or tabDouble[i][j] == '=' or tabDouble[i][j] == '#' or tabDouble[i][j] == '&' or tabDouble[i][j] == '%' or tabDouble[i][j] == '@' or tabDouble[i][j] == '$'):
# 					count = 0
# 			skip_next = True  # Ne pas incrémenter j après cela
# 		# la on arrive au premier . si on vient de finir un nombre alors il faut passer ce point la et continuer le programme sinon on passe au nombre suivant
# 		if skip_next == True:
# 			skip_next = False
# 		else:
# 			j += 1
# 	if count != 0:
# 		count = 0
# 	i += 1
# 	j = 0


# print("somme : ", somme)
# input.close()
# output.close()


# version 2.0
# All redone for part 2
def adjacent_positions(x, y, gear_grid):
	adjacent_positions = []
	for dx in [-1, 0, 1]:
		for dy in [-1, 0, 1]:
			if dx == 0 and dy == 0:
				continue
			nx = x + dx
			ny = y + dy
			if 0 <= nx < len(gear_grid[0]) and 0 <= ny < len(gear_grid):
				adjacent_positions.append((nx, ny))
	return adjacent_positions

def calculate_gear(gear_grid):
	total_gear_product = 0
	adjacent_gear_parts = {}
	for y in range(len(gear_grid)):
		x = 0
		while x < len(gear_grid[y]):
			if not gear_grid[y][x].isdigit():
				x += 1
				continue
			gear_part = gear_grid[y][x]
			adj_positions = adjacent_positions(x, y, gear_grid)
			for nx in range(x + 1, len(gear_grid[y])):
				if not gear_grid[y][nx].isdigit():
					break
				gear_part += gear_grid[y][nx]
				adj_positions.extend(adjacent_positions(nx, y, gear_grid))
				x += 1
			for nx, ny in adj_positions:
				if gear_grid[ny][nx] == "*":
					if (nx, ny) not in adjacent_gear_parts:
						adjacent_gear_parts[(nx, ny)] = []
					adjacent_gear_parts[(nx, ny)].append(int(gear_part))
					break
			x += 1

	for parts in adjacent_gear_parts.values():
		if len(parts) == 2:
			total_gear_product += parts[0] * parts[1]
	return total_gear_product

with open("input.txt", "r") as file:
	gear_grid = [line.strip() for line in file.readlines()]
print(calculate_gear(gear_grid))

