my_list = [1, 2, 4, 4, 1, 4, 2, 6, 2, 9]

yeni_liste = []

for sayi in my_list:
    if sayi not in yeni_liste:
        yeni_liste.append(sayi)

print("The list with unique elements only:")
print(yeni_liste)
