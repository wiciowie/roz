class Szachy:

    def __init__(self, szachownica):
        self.szachownica = szachownica

    def sprawdzanie(szachownica, wiersz, kolumna):
        for a in range(wiersz):
            suma = 0
            for i in range(kolumna):
                # sprawdza wiersz
                if szachownica[a][i] == "1":
                    suma += 1
                    if suma >= 2:
                        return False
                    #sprawdzanie kolumny
                    for k in range(a+1, 7):
                        if k == 7:
                            break
                        if a + k >= 7:
                            break
                        if szachownica[a+k][i] == "1":
                            return False
                    # sprawdzanie przekatnej
                    for c in range(a+1, 7):
                        if c == 7:
                            break
                        if a+c >= 7:
                            break
                        if i + c >=7:
                            break
                        if szachownica[a + c][i + c] == "1":
                            return False



x = Szachy.szachownica = [["1", "0", "0", "0", "0", "0", "0", "0"],
                          ["0", "0", "0", "0", "0", "0", "1", "0"],
                          ["0", "0", "0", "0", "1", "0", "0", "0"],
                          ["0", "0", "0", "0", "0", "0", "0", "1"],
                          ["0", "1", "0", "0", "0", "0", "0", "0"],
                          ["0", "0", "0", "1", "0", "0", "0", "0"],
                          ["0", "0", "0", "0", "0", "1", "0", "0"],
                          ["0", "0", "1", "0", "0", "0", "0", "0"]]

wiersz = len(x)
kolumna = len(x[0])
if Szachy.sprawdzanie(x, wiersz, kolumna) == False:
    print("Hetmany sa w niewlasciwej pozycji, bledne rozwiazanie")
else:
    print("Rozwiazanie poprawne")
