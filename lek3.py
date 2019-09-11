print("Välkommen till mitt program där du kan räkna")
operator = input("Välj räknesätt(+ - * /): ")
total = 0
try:
    num1 = int(input("Mata in ett heltal: "))
except:
    print("Du måste skriva in en siffra")
    num1 = 0
try:
    num2 = int(input("Mata in ett till heltal: "))
except:
    print("Du måste skriva in en siffra")
    num2 = 0

if operator == "+":
    total = num1 + num2
elif operator == "-":
    total = num1 - num2
elif operator == "*":
    total = num1 * num2
elif operator == "/":
    try:
        total = num1 / num2 
    except (ZeroDivisionError):
        print("Du kan inte dela med 0 ju!")
else:
    print("FEL")

print("Välkommen till mitt program där du kan räkna")
operator = input("Välj räknesätt(+ - * /): ")
total = 0
try:
    num1 = int(input("Mata in ett heltal: "))
except:
    print("Du måste skriva in en siffra")
    num1 = 0
try:
    num2 = int(input("Mata in ett till heltal: "))
except:
    print("Du måste skriva in en siffra")
    num2 = 0

if operator == "+":
    total = num1 + num2
elif operator == "-":
    total = num1 - num2
elif operator == "*":
    total = num1 * num2
elif operator == "/":
    try:
        total = num1 / num2 
    except ZeroDivisionError as error:
        print(error)
else:
    print("FEL")
