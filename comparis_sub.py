# création d'un programe permettant de comparé avec et sans abonnement et de s'avoir à patire de quand
# il est avantageux de prendre l'abo et combien on économise comparé à sans l'abo
# By Dixlan
# creation of a program allowing to compare with and without subscription and to know from when it is advantageous
# to take the subscription and how much you save compared to without the subscription.

from time import sleep

question = True
question_its_right = True

print(
    "\nBienvenue, ce logiciel vous permet de s'avoir si prendre un abonnement pour un service est avantageux ou non...\n")
sleep(1)

while question:
    whitout_sub = int(input("Combien devez vous payé sans abonnement par jours ?: "))
    sub_price = int(input("Combien vous coute l'abonement ?: "))
    sub_avantage = int(input("Combien deverez vous payé par jours avec l'abonnement ?: "))
    duration = int(input("Pendant combien de jours aller vous utiliser ce service ?: "))

    while question_its_right:
        print("\nPrix sans abonement/j :", whitout_sub, ".-")
        print("Prix de l'abonement :", sub_price, ".-")
        print("Prix de avec l'abonnement/j :", sub_avantage, ".-")
        print("Nombre de jours :", duration)
        right = input("\nC'est exacte ? [y/n]: ")

        if right == "y":
            print("\nRéponse enregistré : oui\n")
            question = False
            question_its_right = False
        elif right == "n":
            question = True
            question_its_right = True
            print("\nRéponse enregistré : non\n")
        else:
            print("Mauvais entrée veuillez indiquer, soit 'y' pour oui ou 'n' pour non \n")


def get_total_sub_and_free():
    total_sub_price = 0
    total_free_price = 0
    trying = 0
    day = 0
    print("Avec abonnement  /  Sans abonnement")
    total_sub_price += sub_price
    while trying <= duration:
        day += 1
        trying += 1
        total_sub_price = total_sub_price + sub_avantage
        total_free_price = total_free_price + whitout_sub
        print("jours", day, total_sub_price, ".-    /   ", total_free_price, ".-")

    difference_sub = total_free_price - total_sub_price
    difference_free = total_sub_price - total_free_price

    if total_free_price > total_sub_price:
        print("\nIl est plus aventageux de prendre l'abonnement car vous gagnerez :", difference_sub, ".-")
    else:
        print("Il est préférable de ne pas prendre d'abonnement car vous perderez :", difference_free, ".-")


get_total_sub_and_free()
