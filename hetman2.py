def sprawdzanie(szachownica, kolumna, wiersz):
  hetman = 1
  suma = 0
  #Jesli sa 2 hetmany w jednym wierszu to zwraca false
  for i in range(wiersz):
    suma = wiersz[i] + wiersz[i + 1]
    if suma <= 1:
      return False
  for i range(kolumna):
    suma = kolumna[i] + kolumna[i + 1]
    if suma <= 1 :
      return False

szachownica = [[0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0],
               [0, 0, 0, 0, 0, 0, 0, 0]]

if sprawdzenie(szachownica, 0, 0) == False:
  print("Hetmany sa w niewlasciwej pozycji, bledne rozwiazanie")
 else:
  print("Rozwiazanie poprawne")
