## exo2
année_actuelle = int(input("entrer année_actuelle"))
naissance = int(input("entrer naissance"))
age = année_actuelle - naissance
print(age)

##exo3
prix_chaussure = 70
prix_jean = 59
prix_t_shirt = 20
total = prix_jean + prix_t_shirt + prix_chaussure
print("total est de {}".format(total*0.80))

##exo
number_1 = float(input("tapez nombre"))
number_2 = float(input("tapez nombre"))
resultat = (number_1 + number_2)
print(resultat)

##exo5
prenom = input("quel est ton prenom").upper()
nom = input("quel est ton nom").upper()
print(nom[0] + nom[-1])
print(prenom[0] + prenom[-1])
print(nom[0] + nom[-1] + prenom[0] + prenom[-1])
age =float(input("quel est ton age"))

print(round(age/33))
