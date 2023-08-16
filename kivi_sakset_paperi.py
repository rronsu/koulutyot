import random

lista = ["kivi", "sakset", "paperi"]

player = False

while player == False:
    player = input("kivi, sakset, paperi? ")
    computer = lista[random.randint(0, 2)]  
    
    if player == computer:
        print("Tasapeli!")
    elif player == "kivi":
        if computer == "paperi":
            print("Hävisit!")
        else:
            print("Voitit!")
    elif player == "paperi":
        if computer == "sakset":
            print("Hävisit!")
        else:
            print("Voitit!")
    elif player == "sakset":
        if computer == "kivi":
            print("Hävisit!")
        else:
            print("Voitit!")
    else:
        print("älä oo noi tyhmä valitse joku noist kolmest tai yritä ees kirjottaa oikein :)")
        
    player = False
