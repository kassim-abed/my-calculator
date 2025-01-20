# Addition
def addition(user_choice_1, user_choice_3):
    return user_choice_1 + user_choice_3

# Soustraction
def soustraction(user_choice_1, user_choice_3):
    return user_choice_1 - user_choice_3

# Multiplication
def multiplication(user_choice_1, user_choice_3):
    return user_choice_1 * user_choice_3

# Division
def division(user_choice_1, user_choice_3):
    return user_choice_1 / user_choice_3

while True:
    user_choice_1 = input("Entrer un premier nombre :")
    print(user_choice_1)
    try :
        user_choice_1 = float(user_choice_1)
        break
    except:
        print("Réponse invalide")


while True:
    user_choice_2 = input("Sélectionner l'opération: \n 1:Addition \n 2:Soustraction \n 3:Multiplication \n 4:Division\n")


    user_choice_3 = input("Entrer un second nombre :")
    print(user_choice_3)
    
    try:
        user_choice_3 = float(user_choice_3)
        if user_choice_2 == "1" :
            print(user_choice_1, "+", user_choice_3, "=", addition(user_choice_1, user_choice_3))
            user_choice_1 = addition(user_choice_1, user_choice_3)

        elif user_choice_2 == "2" :
            print(user_choice_1, "-", user_choice_3, "=", soustraction(user_choice_1, user_choice_3))
            user_choice_1 = soustraction(user_choice_1, user_choice_3)

        elif user_choice_2 == "3" :
            print(user_choice_1, "*", user_choice_3, "=", multiplication(user_choice_1, user_choice_3))
            user_choice_1 = multiplication(user_choice_1, user_choice_3)

        elif user_choice_2 == "4" :
            print(user_choice_1, "/", user_choice_3, "=", division(user_choice_1, user_choice_3))
            user_choice_1 = division(user_choice_1, user_choice_3)
        else:
            print("calcul impossible (pas d'operateur)")
    except:
            print("Réponse invalide")
            continue
    
    
    next = input("Continuer ? \n 1:Oui / 2:Non \n ")
    if next == "1":
        continue
    elif next == "2":
        break