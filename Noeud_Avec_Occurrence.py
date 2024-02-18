# Importation de la classe Noeud d'un ABR
import arbre_binaire_recherche as abr

class NoeudAvecOccurence(abr.Noeud):
    def __init__(self, valeur):
        super().__init__(valeur)
        self.occurrence = 0

    def incrOccurrence(self):
        self.occurrence += 1

    def getValeurs(self):
        return self.valeur, self.occurrence

    def donnerOccurrence(self):
        return self.occurrence

    def totalOccurrence(self):
        total = self.occurrence
        if self.gaucheExiste():
            total += self.gauche.totalOccurrence()
        if self.droitExiste():
            total += self.droit.totalOccurrence()
        return total

    def maxOccurrence(self):
        max_occurrence = self.occurrence
        if self.gaucheExiste():
            gauche_max = self.gauche.maxOccurrence()
            if gauche_max > max_occurrence:
                max_occurrence = gauche_max
        if self.droitExiste():
            droit_max = self.droit.maxOccurrence()
            if droit_max > max_occurrence:
                max_occurrence = droit_max
        return max_occurrence
