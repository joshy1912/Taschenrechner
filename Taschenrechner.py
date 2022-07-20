#Bnutzereingabe Steuern:
Zahl1 = int(input("1. Zahl:"))
Zahl2 = int(input("2. Zahl:"))
Rechenzeichen = input("Addieren (+), Subtrahieren? (-), Multiplizieren? (*), Dividieren? (/):")
#Ergebnis berechnen:
Ergebins = 0
if Rechenzeichen == "+":
    Ergebins= Zahl1+Zahl2
if Rechenzeichen == "-":
    Ergebins= Zahl1-Zahl2
if Rechenzeichen == "*":
    Ergebins= Zahl1*Zahl2
if Rechenzeichen == "/":
    Ergebins= Zahl1/Zahl2
#Ergebnis ausgeben:
print("das Ergebnis ist", Ergebins)