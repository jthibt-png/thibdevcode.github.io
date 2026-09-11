print("CALCULATRICE")
numb1 = float(input())
op1 = input("")
num2 = float(input())
if op1 == "+":
    Résultat = numb1 + num2
    print(f"Résultat : {Résultat}")
elif op1 == "off":   
    print("See you next time !")
elif op1 == "-":
    Résultat = numb1 - num2
    print(f"Résultat : {Résultat}")
elif op1 == "/":   
    Résultat = numb1 / num2
    print(f"Résultat : {Résultat}")
elif op1 == "*":
    Résultat = numb1 * num2
    print(f"Résultat : {Résultat}")           
else:
      print("Cette opération n'est pas valide")
while numb1 != "off":
    numb1 = float(input())
    op1 = input("")
    num2 = float(input())
if op1 == "+":
    Résultat = numb1 + num2
    print(f"Résultat : {Résultat}")
elif op1 == "-":
    Résultat = numb1 - num2
    print(f"Résultat : {Résultat}")
elif op1 == "/":   
    Résultat = numb1 / num2
    print(f"Résultat : {Résultat}")
elif op1 == "*":
    Résultat = numb1 * num2
    print(f"Résultat : {Résultat}")
elif op1 == "off":   
    print("See you next time !")
else:
    print("Cette opération n'est pas valide")

def addition(a,b):
    return a + b
def soustraction(a,b):
    return a - b
def multiplication(a,b):
    return a * b
def division(a,b):
    return a / b
while True:
    numb1 = input()
    if numb1 == "off":
        print("See you next time !")
        break
    resultat = float(numb1)
    
    while True:
        op1 = input("")
        if op1 == "=":
            break
        num2 = float(input())
        if op1 == "+":
            resultat = addition(resultat, num2)
        elif op1 == "-":
            resultat =  soustraction(resultat, num2)
        elif op1 == "/":  
            if num2 == 0:
                print("Il est impossible de diviser par zéro.") 
                continue
            resultat = division(resultat, num2)
        elif op1 == "*":
            resultat = multiplication(resultat, num2)           
        else:
            print("Cette opération n'est pas valide")
            continue
    print(f"resultat : {resultat}")             
