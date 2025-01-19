import os
while True: 
    a = input("calcul (A + B), 'clear' pour vider l'historique : ").split()
    if a[0].lower() == 'clear': open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'historique.txt'), 'w').close(); continue
    if len(a) != 3 or not (a[0].replace('.', '', 1).replace('-', '', 1).isdigit()) or not (a[2].replace('.', '', 1).replace('-', '', 1).isdigit()) or a[1] not in {'+', '-', '*', '/'}: exit('Entrée invalide')
    operateur = {'+': lambda x, y: x + y, '-': lambda x, y: x - y, '*': lambda x, y: x * y, '/': lambda x, y: x / y if y != 0 else 'Tié un fada ou quoi ?! on divise pas par 0'}
    print(operateur[a[1]](float(a[0]), float(a[2])))
    with open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'historique.txt'), 'a') as file:
        file.write(f"Calcul: {' '.join(a)}\nResultat: {operateur[a[1]](float(a[0]), float(a[2]))}\n\n")

#exec("while True: a=input(\"calcul (A + B), 'clear' pour vider l'historique : \").split();open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'historique.txt'),'w').close()if a[0].lower()=='clear'else(exit('Entrée invalide')if len(a)!=3 or not(a[0].replace('.', '', 1).replace('-', '', 1).isdigit())or not(a[2].replace('.', '', 1).replace('-', '', 1).isdigit())or a[1] not in {'+','-','*','/'}else(print((r:={'+' : lambda x,y: x+y,'-' : lambda x,y: x-y,'*' : lambda x,y: x*y,'/' : lambda x,y: x/y if y != 0 else 'Tié un fada ou quoi ?! on divise pas par 0'}[a[1]](float(a[0]),float(a[2]))))or open(os.path.join(os.path.dirname(os.path.abspath(__file__)),'historique.txt'),'a').write(f\"Calcul: {a}\\nResultat: {r}\\n\\n\")))")