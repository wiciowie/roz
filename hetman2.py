class Szachy:

  def __init__(self, szachownica):
    self.szachownica = szachownica

  def sprawdzanie(szachownica, wiersz, kolumna):
    suma = 0
    for i in range(kolumna):
      suma == szachownica[wiersz][i] + szachownica[wiersz][i + 1]
      if suma >= 1:
        return False


x = Szachy.szachownica = [[1, 1, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0],
                          [0, 0, 0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0, 0, 0]]

if Szachy.sprawdzanie(x, 0, 0) == False:
  print("Hetmany sa w niewlasciwej pozycji, bledne rozwiazanie")
else:
  print("Rozwiazanie poprawne")
