print( 2 < 1 )
print( 2 > 1 )

mot_de_passe = input(" Quel est votre mot de passe ")


if len(mot_de_passe) < 6:
    print("mot de passe trop court")
elif mot_de_passe == '123456':
    print("c'est bon")
else:
    print("le mot de passe n'est pas bon")

print("le programme est terminé")