#  Pré-condition: séquence s non vide, sans doublon et ordonnée circulairement
# Post-condition: max(s)
def max_circ(s):
    n = len(s)

    #  Pré-condition: s[lo] > s[hi]
    # Post-condition: max(s[lo : hi])
    def aux(lo, hi):
        if hi - lo <= 1:
           return s[lo]
        else:
            mid = (lo + hi) // 2

            if s[lo] > s[mid]:
                return aux(lo, mid)
            elif s[mid] > s[hi]:
                return aux(mid, hi)
            else:
                assert(False) # Impossible car séquence sans doublon

    return aux(0, n - 1) if s[0] > s[n - 1] else s[n - 1]

# Exemple des notes de cours
if __name__ == "__main__":
    s = [10, 12, 19, 1, 3, 4, 7]

    print("     s =", s)
    print("max(s) =", max_circ(s))
