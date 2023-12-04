def part1(grid):
	grid = [line.split(": ")[1] for line in grid]
	count = 0
	i = 0
	sum = 0
	while i < len(grid):
		# On sépare la ligne en nombres gagnants et nombres choisis
		winners, chosen = grid[i].split(" | ")
		# On convertit les nombres en ensembles
		winners = winners.split(" ")
		# si il y a des nombre vide on les enleve TOUS
		winners = list(filter(None, winners))
		chosen = chosen.split(" ")
		chosen = list(filter(None, chosen))
		# On compte le nombre de nombres gagnants qui sont dans les nombres choisis
		for chosen in chosen:
			if chosen in winners:
				count += 1
		# en fonction de nombre de nombres gagnants on fait **2 a cahque fois donc 1 nombre gagant = 1, 2 nombre gagant = 4, 3 nombre gagant = 8, 4 nombre gagant = 16
		if count > 0:
			sum += 2 ** (count - 1)
		count = 0
		i += 1
	return sum

def part2(grid):
	total_cartes  = {}
	sum_wins = 0
	count = 0
	for i, line in enumerate(grid):
		inutile, line = line.strip().split(": ")
		winners, chosen = line.split(" | ")
		winners = list(filter(None, winners.split(" ")))
		chosen = list(filter(None, chosen.split(" ")))
		for chosen in chosen:
			if chosen in winners:
				count += 1
		total_cartes[i] = total_cartes.get(i, 0) + 1
		for j in range(i + 1, i + count + 1):
			total_cartes[j] = total_cartes.get(j, 0) + total_cartes[i]
		count = 0
	sum_wins = sum(total_cartes.values())
	return sum_wins

# on prends chaque ligne et on enleve le le debut de la ligne jusqu'a la premiere occurence de ": " et on enleve le dernier caractere de la ligne qui est un "\n"
with open("input.txt", "r") as file:
	grid = [line.strip() for line in file.readlines()]

print(part1(grid))
print(part2(grid))

