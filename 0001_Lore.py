def Lotto(Frage, antwort):
    z = 1
    while z != 2:
        q =input(Frage)
        if q == antwort:
            print("RICHTIG")
            z = 2  
        else:
            print("ENDE")
                  

Lotto("Wie viel Wasser in Prozent umgibt die Erde?", "70%")
      