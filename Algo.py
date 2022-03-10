
class Arbre:
    def __init__(self,val = None, pere = None):
        self.pere = pere
        self.fdroit = None
        self.fgauche = None
        self.val = val
    def ajouter(self, valu):
        if self.val == None :
            self.val = valu
        else:
            if valu > self.val:
                if self.fdroit is None:
                    self.fdroit = Arbre(valu,self)
                else:
                    return self.fdroit.ajouter(valu)
            elif  valu < self.val:
                if self.fgauche is None:
                    self.fgauche = Arbre(valu,self)
                else:
                    return self.fgauche.ajouter(valu)
            else:
                print("La valeur est déjà dans l'arbre!")
    def chercher(self,valu):
        if self.val == valu or self.val == None:
            return self
        elif valu > self.val and self.fdroit :
            return self.fdroit.chercher(valu)
        elif valu < self.val and self.fgauche :
            return self.fgauche.chercher(valu)
        else:
            return None

    def supprimer(self,valu):
        b = self.chercher(valu)
        if b:
            if b.fdroit is None and b.fgauche is None: #si pas de fils, on efface
                if b.pere:
                    if b.pere.fdroit == b:
                        self.chercher(valu).pere.fdroit = None
                    else :
                        self.chercher(valu).pere.fgauche = None
                else :
                    self.val = None
            elif b.fdroit and b.fgauche : #si deux fils, on remplace par le min du sous arbre droit
                c = b.fgauche
                while c.fdroit :
                    c = c.fdroit
                self.chercher(valu).val = c.val
                if c.pere.fdroit == c:
                    c.pere.fdroit = None
                else :
                    c.pere.fgauche = None
            elif b.fdroit:
                c = b.fdroit  
                self.chercher(valu).fdroit = c.fdroit
                self.chercher(valu).fgauche = c.fgauche
                self.chercher(valu).val = c.val
            else :
                c = b.fgauche
                self.chercher(valu).fdroit = c.fdroit
                self.chercher(valu).fgauche = c.fgauche
                self.chercher(valu).val = c.val
        else:
            print("La valeur n'est pas dans l'arbre")
            
    def affichecroissant(self):
        if self.fgauche :
            self.fgauche.affichecroissant()
        print(self.val,end=' ')
        if self.fdroit :
            self.fdroit.affichecroissant()
    def affichedecroissant(self):
        if self.fdroit :
            self.fdroit.affichedecroissant()
        print(self.val, end= ' ')
        if self.fgauche :
            self.fgauche.affichedecroissant()
def saisir():
    while True:
        x = input("Saisir un nombre entier pour l'ajouter à l'arbre binaire de recherche :")
        try :
            if type(eval(x)):
                break
        except :
            x = input("Saisir un nombre entier pour l'ajouter à l'arbre binaire de recherche :")
    return int(x)
def saisirsup():
    while True:
        x = input("Saisir un nombre entier pour supprimer de l'arbre binaire de recherche :")
        try :
            if type(eval(x)):
                break
        except :
            x = input("Saisir un nombre entier pour supprimer de l'arbre binaire de recherche :")
    return int(x)

def menu():
    print("Pour ajouter un nombre à l'arbre écrire: ajouter")
    print("Pour effacer un nombre de l'arbre écrire: supprimer")
    print("Pour afficher les nombres de l'arbre dans un ordre croissant écrire: croissant")
    print("Pour afficher les nombres de l'arbre dans un ordre décroissant écrire: décroissant")
    print("Pour fermer le programme écrire: fermer")
def vide(Arbre):
    if Arbre.val == None and Arbre.pere ==None :
        return True
    else:
        return False
#Programme Principale    
print("L'arbre est vide!")
print("Initialisation de l'arbre binaire:")
x = saisir()
a = Arbre(x)
print(" ")
menu()
while True :
    print("")
    if vide(a):
        print("L'arbre est vide!")
        print("Initialisation de l'arbre binaire:")
        x = saisir()
        a = Arbre(x)
    else:    
        x = input("Saisir une commande : ")
    if x == "ajouter" :
        y = saisir()
        a.ajouter(y)
        while True:
            z = input("Continuer ? (oui ou non) : ")
            if z == 'oui':
                y = saisir()
                a.ajouter(y)
            elif z == 'non':
                break
    elif x == "supprimer":
        y = saisirsup()
        a.supprimer(y)
        while vide(a) == False:
                z = input("Continuer ? (oui ou non) : ")
                if z == 'oui':
                    y= saisirsup()
                    a.supprimer(y)
                elif z == 'non':
                    break
    elif x == "croissant":
        a.affichecroissant()
    elif x == 'decroissant':
        a.affichedecroissant()
    elif x == 'fermer':
        break

    

                