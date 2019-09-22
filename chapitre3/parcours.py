from collections import deque

def parcours_profondeur_rec(G, v):
    V, E = G
    visite  = set()
    sommets = []

    def parcours(u):
        if u not in visite:
            visite.add(u)

            for v in E[u]:
                parcours(v)

            sommets.append(u)

    parcours(v)

    return sommets

def parcours_profondeur_iter(G, v):
    V, E = G
    visite    = set()
    candidats = [v]
    sommets   = []

    while len(candidats) > 0:
        u = candidats.pop()

        if u not in visite:
            visite.add(u)
            sommets.append(u)

            for v in E[u]:
                candidats.append(v)

    sommets.reverse()
    
    return sommets

def parcours_largeur(G, v):
    V, E = G

    visite    = set()
    candidats = deque(v)
    sommets   = []

    while len(candidats) > 0:
        u = candidats.popleft()

        if u not in visite:
            visite.add(u)
            sommets.append(u)

            for v in E[u]:
                candidats.append(v)

    return sommets

def est_acyclique(G):
    V, E = G
    visite = set()

    def possede_cycle(u):
        if u in visite:
            return True
        else:
            visite.add(u)
            
            for v in E[u]:
                possede_cycle(v)

            return False

    for v in V:
        if possede_cycle(v):
            return False
        
    return True

# Exemples
if __name__ == "__main__":
    V = {"a", "b", "c", "d", "e"}
    E = {"a": ["b"],
         "b": ["c"],
         "c": ["a", "d"],
         "d": ["b", "c", "e"],
         "e": []}
    G = (V, E)

    print("Parcours en profondeur:", parcours_profondeur_rec(G, "a"))
    print("Parcours en profondeur:", parcours_profondeur_iter(G, "a"))
    print("Parcours en largeur:   ", parcours_largeur(G, "a"))
    print("Graphe acyclique?      ", "Oui" if est_acyclique(G) else "Non")
