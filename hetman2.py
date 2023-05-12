class Szachy:

  def __init__(self, szachownica):
    self.szachownica = szachownica

  def sprawdzanie(szachownica, wiersz, kolumna):
    for a in range(wiersz):
        for i in range(kolumna):
            if szachownica[a][i] == 1:
                return False
            else:
                continue

x = Szachy.szachownica = [[1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

wiersz = len(x)
kolumna = len(x[0])
if Szachy.sprawdzanie(x, wiersz,kolumna ) == False:
  print("Hetmany sa w niewlasciwej pozycji, bledne rozwiazanie")
else:
  print("Rozwiazanie poprawne")
