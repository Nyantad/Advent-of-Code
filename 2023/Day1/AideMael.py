def is_number(contenu, i):
    if (contenu[i].isdigit()):
            return contenu[i]
    if (len (contenu) >= i + 2):
        if( (contenu[i] == 'o' and contenu[i + 1] == 'n' and contenu[i + 2] == 'e')):
            return '1';
        if ((contenu[i] == 't' and contenu[i + 1] == 'w' and contenu[i + 2] == 'o')):
            return '2';
        if ((contenu[i] == 's' and contenu[i + 1] == 'i' and contenu[i + 2] == 'x')):
            return '6';
    if (len (contenu) >= i + 3):
        if ((contenu[i] == 'n' and contenu[i + 1] == 'i' and contenu[i + 2] == 'n' and contenu[i + 3] == 'e')):
            return '9';
        if ((contenu[i] == 'z' and contenu[i + 1] == 'e' and contenu[i + 2] == 'r' and contenu[i + 3] == 'o')):
            return '0';
        if ((contenu[i] == 'f' and contenu[i + 1] == 'o' and contenu[i + 2] == 'u' and contenu[i + 3] == 'r')):
            return '4';
        if ((contenu[i] == 'f' and contenu[i + 1] == 'i' and contenu[i + 2] == 'v' and contenu[i + 3] == 'e')):
            return '5';
    if (len (contenu) >= i + 4):
        if ((contenu[i] == 't' and contenu[i + 1] == 'h' and contenu[i + 2] == 'r' and contenu[i + 3] == 'e' and contenu[i + 4] == 'e')):
            return '3';
        if ((contenu[i] == 's' and contenu[i + 1] == 'e' and contenu[i + 2] == 'v' and contenu[i + 3] == 'e' and contenu[i + 4] == 'n')):
            return '7';
    if (len (contenu) >= i + 5):
        if ((contenu[i] == 'h' and contenu[i + 1] == 'e' and contenu[i + 2] == 'i' and contenu[i + 3] == 'g' and contenu[i + 4] == 'h' and contenu[i + 5] == 't')):
            return '8';
    return 0;

fichier = open('input.txt', 'r')
contenu = fichier.readline()
file_to_delete = open("output.txt",'w')
file_to_delete.close()
output = open("output.txt", "a")
while (contenu != ''):
    i = 0
    j = 0
    charset = 0;
    while (i < len(contenu)):
        if (j == 0 and is_number(contenu, i)):
            j = 1
            charset = is_number(contenu, i)
            output.write(str(charset))
        elif(is_number(contenu, i)):
            charset = is_number(contenu, i)
        i += 1
    output.write(str(charset))
    output.write('\n')
    contenu = fichier.readline()
# output.close()
# output = open("output.txt", "r")
# num = output.readline()
# somme = 0
# while num != '':
#     somme += int(num)
#     num = output.readline()
# print(str(somme))
