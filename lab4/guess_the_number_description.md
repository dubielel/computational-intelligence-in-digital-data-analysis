# Gra "Zgadnij liczbę"

## Opis:

Gra dwóch graczy: gracz i komputer.

Gracz wybiera przedział liczb, np. od 1 do 100.

Komputer losuje liczbę z tego przedziału, której gracz musi się domyślić.

Gracz próbuje zgadnąć liczbę, a komputer informuje, czy podana liczba jest za duża, za mała, czy trafiona.

## Implementacja:

1. Inicjalizacja gry:
    * Gracz wybiera przedział liczb.
    * Komputer losuje liczbę z tego przedziału.
    * Inicjalizacja licznika prób na 0.

2. Rozpoczęcie rundy:
    * Gracz podaje swoją propozycję liczby.
    * Komputer sprawdza, czy podana liczba jest prawidłowa:
        - Jeśli liczba jest trafiona, komputer informuje o tym gracza, a gra kończy się.
        - Jeśli liczba jest za duża lub za mała, komputer daje odpowiednią wskazówkę.
    * Zwiększenie licznika prób o 1.

3. Powtórzenie rundy, aż gracz zgadnie liczbę lub osiągnie maksymalną liczbę prób.

4. Podanie wyniku, czy gracz zgadł liczbę oraz ile prób mu to zajęło.

Ta gra wymaga od gracza logicznego myślenia i podejmowania decyzji na podstawie informacji zwrotnych, co czyni ją ciekawą do eksperymentowania z różnymi strategiami uczenia ze wzmocnieniem.
