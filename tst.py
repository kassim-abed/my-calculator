def cacutatrice(resultat, a, b, signe):
    if signe == "+":
        resultat = (a + b)
    elif signe == "-":
        resultat = (a - b)
    elif signe == "*":
        resultat = (a * b)
    elif signe == "/" and b != 0:
        resultat = (a / b)
    elif signe == "%" and b != 0:
        resultat = (a % b)
    elif signe == "//" and b != 0:
        resultat = (a // b)
    elif signe == "**":
        resultat = (a ** b)
    elif signe == "racine":
        resultat = (a**0.5)
    else:
        print("une valeur n'est pas valide")
    return resultat

def caractere(input_string):
    if "**" in input_string:
        char_to_find = "**"
    elif "*" in input_string:
        char_to_find = "*"
    elif "/" in input_string:
        char_to_find = "/"
    elif "-" in input_string:
        char_to_find = "-"
    elif "+" in input_string:
        char_to_find = "+"
    else:
        char_to_find = None


    terms = input_string.split()
    if char_to_find in input_string:

        a = None
        signe = None
        b = None
        resultat = None

        for i in range(len(terms)):
            if char_to_find in terms[i]:
                a = int(terms[i-1])
                signe = terms[i]
                b = int(terms[i+1])
                break

        resultat = cacutatrice(resultat, a, b, signe)

        input_string = input_string.replace(f"{a} {signe} {b}", f"{resultat}")
    return input_string

input_string = input("calcul : ")
signes = ["**", "*", "/", "//", "%", "+", "-"]
count_signes = 0
for signe in signes:
    count_signes += input_string.count(signe)
for _ in range (count_signes):
    input_string = caractere(input_string)
print(f"{input_string}")