# variabler för att komma ihå namn och ålder

# läsa in namn 
name = input("skriv in ditt namn: ")
# läsa in ålder
age = int(input ("skriv in din ålder: "))
# skriva ut hej namn och du är x gammal
print ("Hejsan",name,",välkommen till mitt pogram.")
print ("Du är",age,"gammal!!")
# skriva ut om du är 18 eller inte
if age <18:
    print("Du har inte rätt ålder ännu")
else:
    print("Du har fyllt 18")