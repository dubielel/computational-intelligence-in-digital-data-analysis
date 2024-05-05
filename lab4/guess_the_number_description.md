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

2. Rozpoczęcie rundy:
    * Gracz podaje swoją propozycję liczby.
    * Komputer sprawdza, czy podana liczba jest prawidłowa:
        - Jeśli liczba jest trafiona, komputer informuje o tym gracza, a gra kończy się.
        - Jeśli liczba jest za duża lub za mała, komputer daje odpowiednią wskazówkę.

3. Powtórzenie rundy, aż gracz zgadnie liczbę.

4. Podanie wyniku, czy gracz zgadł liczbę.

Ta gra wymaga od gracza logicznego myślenia i podejmowania decyzji na podstawie informacji zwrotnych, co czyni ją ciekawą do eksperymentowania z różnymi strategiami uczenia ze wzmocnieniem.

## Opisy algorytmów użytych do uczenia ze wzmocnieniem

W naszych eksperymentach wykorzystaliśmy dwa algorytmy QLearning i SARSA.

### Opis działania QLearning

Część teoretyczna działania algorytmu QLearning została przez nas dokładnie opisana w ramach poprzedniego laboratorium, zatem teraz przedstawimy tylko opis działania w naszej implementacji. Przy każdym zgadywaniu miał $\epsilon$ szans na wybranie losowej liczby i $1 - \epsilon$ na wybranie wartości z QTable. To podejście niestety nie jest dobre z dwóch powodów. Pierwszym powodem jest fakt, że QTable powinno być różne dla każdej możliwej liczby. Dla poprawnego działania algorytmu konieczne byłoby znanie liczby przez agenta, co w oczywisty sposób nie ma sensu. Drugi powód związany jest z innym podejściem do uczenia. Możnaby spróbować za pomoczą wartości w QTable ograniczać przedziały, w których może znaleźć się liczba. Jest to jednak przerost formy nad treścią, ponieważ dla każdej wylosowanej liczby przeprowadzony musiałby być osobny proces uczenia, który de facto sprowadziłby się do implementacji bin search, jednak dużo mniej efektywnej i niepotrzebnie skomplikowanej. Ostatecznie udawało się zakończyć działanie algorytmu po losowym wyborze liczby.

### Opis działania SARSA

Algorytm SARSA uczy się według wzoru:

$$Q(s_t, a_t) \leftarrow (1 - \alpha)Q(s_t, a_t) + \alpha \cdot [r_{t+1} + \gamma \cdot Q(s_{t+1}, a_{t+1})],$$

gdzie:
* $Q(s_t,a_t)$: aktualna ocena funkcji wartości akcji (Q-funkcji) dla stanu $s_t$ i akcji 
$a_t$. Oznacza oczekiwaną sumę nagród uzyskanych poprzez wykonanie akcji $a_t$ w stanie $s_t$.
* $\alpha$: współczynnik uczenia.
* $r_{t+1}$: natychmiastowa nagroda.
* $\gamma$: współczynnik zmniejszający wagę przyszłych nagród.
* $Q(s_{t+1}, a_{t+1})$: ocena wartości dla przyszłego stanu po przyszłej akcji wybranej według aktualnej polityki.

Algorytm SARSA jest wariacją na temat algorytmu QLearning. Główną różnicą jest podejście *off policy* w QLearning i *on policy* w SARSA. W pierwszej polityce agent wyciąga ocenę akcji z polityki, która nie jest aktualnie w użyciu. W drugim podejściu przeciwnie, agent ocenia wartość akcji na podstawie aktualnej polityki.

Źródło: [Artykuł na GeeksForGeeks](https://www.geeksforgeeks.org/sarsa-reinforcement-learning/).

W naszym przypadku uczenie algorytmem SARSA również okazało się nieskuteczne. Algorytm ostatecznie zgadywał liczbę ale działał losowo.

## Podsumowanie

Gra Zgadnij Liczbę nie jest grą dobrą do stosowania uczenia ze wzmocnieniem. Nauka algorytmów sprowadza się do implementacji algorytmu bin search, który jest niepotrzebnie skomplikowany. Kolejnym problemem jest różnorodność środowiska. Agent w idealnej sytuacji powinien się nauczyć akcji do zgadywania konkretnej liczby, jednak wymaga to znania liczby a priori, czyli sprawia, że uczenie nie ma sensu. Naszym innym pomysłem byłoby uzależnienie nagrody od tego jak daleko jest liczba, którą zgadł agent od oczekiwanej. To podejście również jest problematyczne, ponieważ zdradza zbyt dużo informacji agentowi na starcie i sprowadza się do poznania liczby na samym początku. Uczenie ze wzmocnieniem działa dobrze w grach takich jak blackjack, gdzie możemy stworzyć odpowiednią politykę. W grze Zgadnij Liczbę nie da się określić polityki, zaś agent musiałby się nauczyć algorytmu bin search.
