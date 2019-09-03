class Region:
    def __init__(self, gauche, droite, haut, bas):
        self.gauche = gauche
        self.droite = droite
        self.haut   = haut
        self.bas    = bas

    def singleton(self):
        return (self.gauche == self.droite and self.haut == self.bas)

    def contient(self, t):
        i, j = t
        
        return (self.haut   <= i <= self.bas and
                self.gauche <= j <= self.droite)

def paver(r, t):    
    if r.singleton():
        return []
    else:
        # Scinder région r en quatre régions
        moitie_x = (r.droite + r.gauche) // 2
        moitie_y = (r.bas    + r.haut)   // 2
        
        r_hg = Region(r.gauche,     moitie_x, r.haut,       moitie_y)
        r_hd = Region(moitie_x + 1, r.droite, r.haut,       moitie_y)
        r_bg = Region(r.gauche,     moitie_x, moitie_y + 1, r.bas)
        r_bd = Region(moitie_x + 1, r.droite, moitie_y + 1, r.bas)

        tuiles         = []
        nouvelle_tuile = []

        # Paver région haut gauche
        if r_hg.contient(t):
            tuiles += paver(r_hg, t)
        else:
            trou    = (r_hg.bas, r_hg.droite)
            tuiles += paver(r_hg, trou)
            nouvelle_tuile.append(trou)

        # Paver région haut droite
        if r_hd.contient(t):
            tuiles += paver(r_hd, t)
        else:
            trou    = (r_hd.bas, r_hd.gauche)
            tuiles += paver(r_hd, trou)
            nouvelle_tuile.append(trou)

        # Paver région bas gauche
        if r_bg.contient(t):
            tuiles += paver(r_bg, t)
        else:
            trou    = (r_bg.haut, r_bg.droite)
            tuiles += paver(r_bg, trou)
            nouvelle_tuile.append(trou)

        # Paver région bas droite
        if r_bd.contient(t):
            tuiles += paver(r_bd, t)
        else:
            trou    = (r_bd.haut, r_bd.gauche)
            tuiles += paver(r_bd, trou)
            nouvelle_tuile.append(trou)

    # Ajouter la nouvelle tuile qui touche trois régions
    tuiles.append(tuple(nouvelle_tuile))

    return tuiles

# Exemple
if __name__ == "__main__":
    n = 2

    region = Region(1, 2**n, 1, 2**n)
    trou   = (1, 3)

    print("Pavage d'une grille {0} x {0} "
          "avec trou à la position ({1}, {2}):".format(2**n, *trou))
    print()
    print(paver(region, trou))
