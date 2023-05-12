def czy_mozna(szachownica, wiersz, kolumna):
    # Kolumna na lewo
    for i in range(kolumna):
        if szachownica[wiersz][i] == 1:
            return False

    # Gorna diagonalia na lewo
    for i, j in zip(range(wiersz, -1, -1), range(kolumna, -1, -1)):
        if szachownica[i][j] == 1:
            return False

    # Dolna diagonalia w lewo
    for i, j in zip(range(wiersz, 8, 1), range(kolumna, -1, -1)):
        if szachownica[i][j] == 1:
            return False

    return True


def rozwiazanie(szachownica, kolumna):
    # Jesli wszystko jest postawione to zwraca True
    if kolumna >= 8:
        return True

    # Stawia hetmany na kolumnach po kolei
    for i in range(8):
        if czy_mozna(szachownica, i, kolumna):
            # Stawia Hetmana
            szachownica[i][kolumna] = 1

            # Powtarza aby postawic hetmany
            if rozwiazanie(szachownica, kolumna + 1) == True:
                return True

            # jesli nie zgadza sie z rozwiazaniem to nie stawiaj
            szachownica[i][kolumna] = 0

    # Jeśli królowa nie może być umieszczona w żadnym rzędzie w tej kolumnie, zwróć fałsz
    return False


def pokaz_rozwiazanie(szachownica):
    for i in range(8):
        for j in range(8):
            print(szachownica[i][j], end=' ')
        print()


szachownica = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

if rozwiazanie(szachownica, 0) == False:
    print("Nie ma rozwiazania")
else:
    pokaz_rozwiazanie(szachownica)
