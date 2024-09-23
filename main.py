'''
blabla
'''
def artcode_i(s):
    """retourne la liste de tuples encodant une chaîne
    de caractères passée en argument selon un algorithme itératif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    #condition d'arret
    if not s:
        return []
    #code
    liste=[]
    caract = s[0]
    c=0
    for elt in s:
        if elt == caract:
            c+=1
        else :
            liste.append((caract,c))
            caract=elt
            c=1
    liste.append((caract,c))
    return liste


def artcode_r(s):
    """retourne la liste de tuples encodant 
    une chaîne de caractères passée en argument 
    selon un algorithme récursif

    Args:
        s (str): la chaîne de caractères à encoder

    Returns:
        list: la liste des tuples (caractère, nombre d'occurences)
    """
    if not s:
        return []
    c=0
    caract = s[0]
    while c < len(s) and s[c] == caract:
        c += 1
    return [(caract, c)] + artcode_r(s[c:])

def main():
    """ main
    """
    print(artcode_i('MMMMaaacXolloMM'))
    print(artcode_r('~~~~~@@@---@@@~~~~~'))

if __name__ == "__main__":
    main()
