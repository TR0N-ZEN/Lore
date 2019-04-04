def Fragensteller(x, y): 
    i = 1
    while i != 2:
        Benutzerantwort = input(x)
        if Benutzerantwort == y:
          print("!!!RICHTIG!!!") 
          i = 2
        else:
            print("...Rate weiter...")

Fragensteller("10.08.", "Irgendwas")
Fragensteller("11", "H")
Fragensteller("F", "WAS")