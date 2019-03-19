def Fragensteller(Frage, richtige_Antwort):
    i = 1
    while i != 2:
        Benutzerantwort = input(Frage)
        if Benutzerantwort == richtige_Antwort:
            print("!!!RICHTIG!!!")
            i = 2
        else:
            print("...Rate weiter...")

Fragensteller("Wann hat Lore Geburtstag?", "10.08.")
Fragensteller("Wie lautet die Telefon Nummer der Polizei?", "110")
