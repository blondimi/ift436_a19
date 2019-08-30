# Génère toutes les séquences de m éléments parmi {1, 2, ..., n}
def sequence(m, n):
    s = [1] * m

    while True:
        yield list(s)

        i = 0
        
        while i < m and s[i] == n:
            s[i] = 1
            i   += 1

        if i < m:
            s[i] += 1
        else:
            break

# Exemple d'usage de sequence(m, n)
if __name__ == "__main__":
    for s in sequence(3, 2):
        print(s)
