
# V1
# f = open("input.txt", "r")
# o = open("output.txt", "a")
# nb_int = 0
# i = 0
# tmp = f.readline()
# len_tmp = len(tmp)
# while tmp != '':
# 	while len_tmp > i and nb_int <= 0:
# 		if tmp[i].isdigit() == 1 or (nb_int == 1 and tmp[i].isdigit()):	# On compte les nombres
# 			o.write(tmp[i])
# 			nb_int += 1
# 		i += 1
# 	i = len_tmp - 1
# 	nb_int = 0
# 	while i >= 0 and nb_int <= 0:
# 		if tmp[i].isdigit() == 1:
# 			o.write(tmp[i])
# 			nb_int += 1
# 		i -= 1
# 	i = 0
# 	nb_int = 0
# 	tmp = (f.readline())
# 	len_tmp = len(tmp)
# 	o.write("\n")

# # on fait la somme de chaque ligne du fichier
# o.close()
# o = open("output.txt", "r")
# tmp2 = o.readline()
# somme = 0
# while tmp2 != '':
# 	somme += int(tmp2)
# 	tmp2 = o.readline()

# print(str(somme))

# f.close()
# o.close()

# fonction qui prend en paramètre une ligne de texte et qui renvoie le premier chiffre qu'elle rencontre qu'il soit ecris en lettre ou en chiffre ex : 1 ou "one"
def first_int(str):
	i = 0
	while i < len(str):
		if str[i].isdigit() == 1:
			return (str[i])
		if len(str) - i >= 3 and str[i] == 'o' and str[i + 1] == 'n' and str[i + 2] == 'e':
			return ('1')
		if  len(str) - i >= 3 and str[i] == 't' and str[i + 1] == 'w' and str[i + 2] == 'o':
			return ('2')
		if  len(str) - i >= 5 and str[i] == 't' and str[i + 1] == 'h' and str[i + 2] == 'r' and str[i + 3] == 'e' and str[i + 4] == 'e':
			return ('3')
		if  len(str) - i >= 4 and str[i] == 'f' and str[i + 1] == 'o' and str[i + 2] == 'u' and str[i + 3] == 'r':
			return ('4')
		if  len(str) - i >= 4 and str[i] == 'f' and str[i + 1] == 'i' and str[i + 2] == 'v' and str[i + 3] == 'e':
			return ('5')
		if  len(str) - i >= 3 and str[i] == 's' and str[i + 1] == 'i' and str[i + 2] == 'x':
			return ('6')
		if  len(str) - i >= 5 and str[i] == 's' and str[i + 1] == 'e' and str[i + 2] == 'v' and str[i + 3] == 'e' and str[i + 4] == 'n':
			return ('7')
		if  len(str) - i >= 5 and str[i] == 'e' and str[i + 1] == 'i' and str[i + 2] == 'g' and str[i + 3] == 'h' and str[i + 4] == 't':
			return ('8')
		if  len(str) - i >= 4 and str[i] == 'n' and str[i + 1] == 'i' and str[i + 2] == 'n' and str[i + 3] == 'e':
			return ('9')
		i += 1
	return ('0')

def last_int(str):
	i = len(str) - 1
	while i >= 0:
		if str[i].isdigit() == 1:
			return (str[i])
		# on verifie si le chiffre est ecris en lettre et peut s'eccrire sur la longeur de la ligne comme on part de la fin de la ligne par exemple on doit attendre trois fois avant de pouvoir ecrire one
		if len(str) - i >= 3 and str[i] == 'o' and str[i + 1] == 'n' and str[i + 2] == 'e':
			return ('1')
		if len(str) - i >= 3 and str[i] == 't' and str[i + 1] == 'w' and str[i + 2] == 'o':
			return ('2')
		if len(str) - i >= 5 and str[i] == 't' and str[i + 1] == 'h' and str[i + 2] == 'r' and str[i + 3] == 'e' and str[i + 4] == 'e':
			return ('3')
		if len(str) - i >= 4 and str[i] == 'f' and str[i + 1] == 'o' and str[i + 2] == 'u' and str[i + 3] == 'r':
			return ('4')
		if len(str) - i >= 4 and str[i] == 'f' and str[i + 1] == 'i' and str[i + 2] == 'v' and str[i + 3] == 'e':
			return ('5')
		if len(str) - i >= 3 and str[i] == 's' and str[i + 1] == 'i' and str[i + 2] == 'x':
			return ('6')
		if len(str) - i >= 5 and str[i] == 's' and str[i + 1] == 'e' and str[i + 2] == 'v' and str[i + 3] == 'e' and str[i + 4] == 'n':
			return ('7')
		if len(str) - i >= 5 and str[i] == 'e' and str[i + 1] == 'i' and str[i + 2] == 'g' and str[i + 3] == 'h' and str[i + 4] == 't':
			return ('8')
		if len(str) - i >= 4 and str[i] == 'n' and str[i + 1] == 'i' and str[i + 2] == 'n' and str[i + 3] == 'e':
			return ('9')
		i -= 1
	return ('0')


# V2
f = open("input.txt", "r")
o = open("output.txt", "a")
nb_int = 0
i = 0
tmp = f.readline()
while tmp != '':
	first_int_tmp = first_int(tmp)
	last_int_tmp = last_int(tmp)
	o.write(first_int_tmp)
	o.write(last_int_tmp)
	tmp = (f.readline())
	o.write("\n")

# on fait la somme de chaque ligne du fichier
o.close()
o = open("output.txt", "r")
tmp2 = o.readline()
somme = 0
while tmp2 != '':
	somme += int(tmp2)
	tmp2 = o.readline()

print(str(somme))

f.close()
o.close()

