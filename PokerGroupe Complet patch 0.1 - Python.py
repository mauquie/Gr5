import random
import randint

couleur=["K", "C", "T", "P"]
rang=["2","3","4","5","6","7","8","9","10","V","D","R","A"]

C=[]
t=1
for i in range(couleur):
    for j in rang (rang):
        C[t]=carte(i,j)
    t=t+1

#Classe de Morgan KADDOURI

class PokerController():
    pass

class Coup(Partie):
    def __init__(self, joueurs):
        Partie.__init__(self, joueurs)
        self.croupier
        self.gagnant
        self.joueurs=[]
        
    def abattre():
        pass
    
    def distribuer():
        pass

#Classe de Emie COUREAU

class Carte():
    
    def __init__(self, couleur, rang):
        self.couleur=couleur
        self.rang=rang
        
class Joueur(Croupier):

    def __init__(self , nom = "Joueur", main = None, tapis=500):
        Croupier.__init__(self)
        self.nom=nom
        self.main=main
        self.tapis=tapis

    def vider_main(self):
        for i in range(0,5):
            self.main.pop()

    def recevoir(self):
        if len(self.main + 1)!= 0:
            vider_main()
        for i in range(5):
            self.main.append(self.paquet[-1])
            self.paquet.pop()
        
#Classe de Allan PECAL-THIRION  
    
class Croupier(Carte):
    
    def __init__(self):
        Carte.__init__(self)
        self.paquet=[]
        
    def rassembler(self):
        for i in range(0, len(self.couleur)):
            for j in range(0, len(self.rang)):
                self.paquet.append(self.couleur[i]+self.rang[j])
        
    def nouvelle_donne(self):
        self.rassembler()
        self.melanger()
        self.couper()
        
    def melanger(self):
        random.shuffle(self.paquet)
        
    def couper(self):
        c = randint(1,50)
        PM=[]
        for i in range(0, c):
            PM.append(self.paquet[0])
            self.paquet.pop(0)
        for i in range(0, len.PM):
            self.paquet.append(PM[0])
            PM.pop(0)
            
class Partie():
    def __init__(self, joueurs):
        self.joueurs=joueurs

        

        
        


