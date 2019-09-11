# en slumpgenetator
# pogram som rullar en träning

import random # laddar in random klassen så vi kan använda den

print("Vill du rulla en tärning?") # meddelande till användaren 

# försök läsa in sides som en int, vid fel sätt sides till 1
try:
    sides =int(input("Hur många sidor: "))
except:
    print("Tärnignen behöver 1+ sidor")
    sides = 1

run = "y" # vi använder run värdet för att fortsätta köra pogrammet 

while run.lower() == "y":
    randomNumber = random.randint(1, sides) # slumpa ett tal mellan 1 och sides 
    print(randomNumber) # skriv ut

#fråga om använder vill fortsätta rulla tärningen 
    run = input("Vill du rulla en till tärning: Y/N")
