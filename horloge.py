# Importer le temps de la bibliothèque -------------------
import time

# Heure en tuple 
heure_tuple = (0,0,0)
heure_present = list(heure_tuple)

# Demander l'utilisateur de régler l'heure
heure = int(input("Régler l'heure : "))
minute = int(input("Régler minute : "))
seconde = int(input("Régler seconde : "))

# Paramètrer l'alarme
alarme = None

# Class ----------------------------

class clock(): 
    
    def afficher_heure():
        global heure_present
        format_heure = "{:02}:{:02}:{:02}".format(heure_present[0], heure_present[1], heure_present[2])
        print(format_heure)

    def regler_heure(new_heure, new_minute, new_seconde):
        global heure_present
        heure_present = [new_heure, new_minute, new_seconde]
        clock.afficher_heure

    def regler_alarme():
        global alarme
        alarme_reponse = input("Souhaitez vous activer l'alarme ? (Oui = Y et non = N) : ")

        if alarme_reponse == "Y":
            new_heure = int(input ("Régler l'heure : ")) 
            new_minutes = int(input("Régler les minutes : "))
            new_seconde = int (input ("Régler les secondes : "))
            alarme =[new_heure, new_minutes, new_seconde]
            print (f"L'alarme est bien configurée {alarme[0]}, {alarme[1]}, {alarme[2]} ")

        elif alarme_reponse == "N": 
            clock.afficher_heure()
            clock.actualiser_heure()

        else: 
            print ("Mettre Y ou N à la question")
            clock.regler_alarme()          

    def verifier_alarme():
        global heure_present, alarme
        if alarme is not None and heure_present == alarme:
            print("ALARME !")

    def actualiser_heure():
        global heure_present
        while True:
            time.sleep(1)      
            heure_present[2] += 1
            if heure_present[2] == 60:
                heure_present[1] += 1
                heure_present[2] = 0
                if heure_present[1] == 60:
                    heure_present[0] += 1
                    heure_present[1] = 0

            clock.afficher_heure()           
            clock.verifier_alarme()
           

# Pour afficher l'heure
clock.regler_heure(heure, minute, seconde)

# Réglez l'alarme pour 10 secondes après l'heure 
clock.regler_alarme()

# Boucle pour actualiser l'heure indéfinimment
while True: 
    clock.actualiser_heure ()

