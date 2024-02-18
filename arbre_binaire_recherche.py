import classe_file as cf

class NoeudAvecOccurrence:
    def __init__(self, valeur):
        '''Méthode constructeur pour la classe NoeudAvecOccurrence.
        Paramètre d'entrée : valeur
        valeur : int ou str'''
        self.valeur = valeur
        self.gauche = None
        self.droit = None
        self.occurrence = 1

    def incrOccurrence(self):
        '''Incrémente le nombre d'occurrences du noeud.'''
        self.occurrence += 1

    def getValeurs(self):
        '''Obtient la valeur et le nombre d'occurrences du noeud.
        Aucun paramètre en entrée'''
        return self.valeur, self.occurrence

    def donnerOccurrence(self, cle):
        '''Méthode pour obtenir le nombre d'occurrences d'une clé dans l'ABR
        Paramètre d'entrée : cle
        cle : str
        Sortie : le nombre d'occurrences (integer)'''

        # Vérifie si le noeud actuel a le mot spécifié
        if cle == self.getValeur():
            return self.occurrence
        if cle < self.valeur and self.gaucheExiste():
            # Si le mot peut être dans le sous-arbre gauche, vérifie récursivement le sous-arbre gauche
            return self.gauche.donnerOccurrence(cle)
        if cle > self.valeur and self.droitExiste():
            # Si le mot peut être dans le sous-arbre droit, vérifie récursivement le sous-arbre droit
            return self.droit.donnerOccurrence(cle)
        # Si le mot n'est pas trouvé, retourne 0 occurrences
        return 0

    def totalOccurrence(self):
        '''Obtient le nombre total d'occurrences dans l'ABR.
        Sortie : le nombre total d'occurrences (integer)'''
        total = self.occurrence
        if self.gaucheExiste():
            total += self.gauche.totalOccurrence()
        if self.droitExiste():
            total += self.droit.totalOccurrence()
        return total

    def maxOccurrence(self):
        '''Obtient l'occurrence maximale dans l'ABR.
        Sortie : l'occurrence maximale (integer)'''
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

    def maxOccurrenceV2(self):
        '''Méthode récursive pour obtenir l'occurrence maximale dans l'ABR.
        Sortie : tuple (mot_max, occ_max)'''
        mot_max, occ_max = self.valeur, self.occurrence

        if self.gaucheExiste():
            left_result = self.gauche.maxOccurrenceV2()
            if left_result[1] > occ_max:
                mot_max, occ_max = left_result

        if self.droitExiste():
            right_result = self.droit.maxOccurrenceV2()
            if right_result[1] > occ_max:
                mot_max, occ_max = right_result

        return mot_max, occ_max

    def getValeur(self):
        '''Méthode accesseur pour obtenir la valeur du noeud
        Aucun paramètre en entrée'''
        return self.valeur

    def droitExiste(self):
        '''Méthode renvoyant True si l'enfant droit existe
        Aucun paramètre en entrée'''
        return (self.droit is not None)

    def gaucheExiste(self):
        '''Méthode renvoyant True si l'enfant gauche existe
        Aucun paramètre en entrée'''
        return (self.gauche is not None)

    def taille(self):
        '''Méthode récursive de calcul de la taille de l'ABR
        Aucun paramètre d'entrée
        Sortie : la taille de l'ABR (integer)'''
        if self is None:
            return 0
        if self.droitExiste() and self.gaucheExiste():
            return 1 + self.droit.taille() + self.gauche.taille()
        elif self.droitExiste():
            return 1 + self.droit.taille()
        elif self.gaucheExiste():
            return 1 + self.gauche.taille()
        else:
            return 1

    def hauteur(self):
        '''Méthode récursive de calcul de la hauteur de l'ABR
        Aucun paramètre d'entrée
        Sortie : la hauteur de l'ABR (integer)'''
        if self is None:
            return 0
        if self.droitExiste() and self.gaucheExiste():
            return 1 + max(self.droit.hauteur(), self.gauche.hauteur())
        elif self.droitExiste():
            return 1 + self.droit.hauteur()
        elif self.gaucheExiste():
            return 1 + self.gauche.hauteur()
        else:
            return 1

    def prefixe(self, liste_noeuds_pre):
        '''Méthode récursive de parcours préfixe de l'ABR
        Entrée : liste de noeuds parcourus (type list)
        Sortie : pas besoin de renvoyer la liste'''
        if self is None:
            return
        liste_noeuds_pre.append(self.getValeur())
        if self.gaucheExiste():
            self.gauche.prefixe(liste_noeuds_pre)
        if self.droitExiste():
            self.droit.prefixe(liste_noeuds_pre)

    def infixe(self, liste_noeuds_inf):
        '''Méthode récursive de parcours infixe de l'ABR
        Entrée : liste de noeuds parcourus (type list)
        Sortie : pas besoin de renvoyer la liste'''
        if self is None:
            return
        if self.gaucheExiste():
            self.gauche.infixe(liste_noeuds_inf)
        liste_noeuds_inf.append(self.getValeur())
        if self.droitExiste():
            self.droit.infixe(liste_noeuds_inf)

    def suffixe(self, liste_noeuds_suf):
        '''Méthode récursive de parcours suffixe de l'ABR
        Entrée : liste de noeuds parcourus (type list)
        Sortie : pas besoin de renvoyer la liste'''
        if self is None:
            return
        if self.gaucheExiste():
            self.gauche.suffixe(liste_noeuds_suf

)
        if self.droitExiste():
            self.droit.suffixe(liste_noeuds_suf)
        liste_noeuds_suf.append(self.getValeur())

    def largeur(self, liste_noeuds_largeur):
        '''Méthode itérative de parcours en largeur de l'ABR
        Entrée : liste de noeuds parcourus (type list)
        Sortie : pas besoin de renvoyer la liste'''
        ma_file = cf.File()
        ma_file.ajouter(self)
        while not ma_file.fileVide():
            noeud = ma_file.retirer()
            liste_noeuds_largeur.append(noeud.getValeur())
            if noeud.gaucheExiste():
                ma_file.ajouter(noeud.gauche)
            if noeud.droitExiste():
                ma_file.ajouter(noeud.droit)

    def recherche(self, cle):
        '''Méthode récursive de recherche d'une clé dans l'ABR
        Entrée : la clé (une valeur)
        Sortie : le résultat de la recherche (booléen) '''
        if self is None:
            return False
        if cle == self.getValeur():
            return True
        elif cle < self.getValeur():
            if self.gaucheExiste():
                return self.gauche.recherche(cle)
            else:
                return False
        else:
            if self.droitExiste():
                return self.droit.recherche(cle)
            else:
                return False

    def __str__(self):
        """Méthode récursive pour obtenir une représentation lisible
        d'un arbre.
        Aucun paramètre en entrée
        Syntaxe :
            >>> print(arbre)"""
        lines = list()
        lines.append(f"{self.valeur}, {self.occurrence}")
        l = str(self.gauche).split('\n')
        r = str(self.droit).split('\n')
        for branch in r, l:
            alt = '| ' if branch is r else '  '
            for line in branch:
                prefix = '+-' if line is branch[0] else alt
                lines.append(prefix + line)
        return '\n'.join(lines)


class Noeud(NoeudAvecOccurrence):
    def __init__(self, valeur):
        '''Méthode constructeur pour la classe Noeud.
        Paramètre d'entrée : valeur
        valeur : int ou str'''
        NoeudAvecOccurrence.__init__(self, valeur)

    def inserer(self, cle):
        '''Méthode d'insertion de clé dans un arbre binaire de recherche
        Paramètre d'entrée : valeur
        valeur : int ou str'''

        if cle == self.valeur:
            self.incrOccurrence()
            return
        elif cle < self.valeur:
            if self.gaucheExiste():
                self.gauche.inserer(cle)
            else:
                self.gauche = Noeud(cle)
        elif cle > self.valeur:
            if self.droitExiste():
                self.droit.inserer(cle)
            else:
                self.droit = Noeud(cle)