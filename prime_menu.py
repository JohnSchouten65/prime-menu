
import csv
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from typing import Generator

def infinite_prime_generator() -> Generator[int, None, None]:
    yield 2
    yield 3
    yield 5
    yield 7
    primes = [2, 3, 5, 7]
    n = 11
    while True:
        is_prime = True
        for p in primes:
            if p * p > n:
                break
            if n % p == 0:
                is_prime = False
                break
        if is_prime:
            primes.append(n)
            yield n
        n += 2

def get_first_n_primes(limit: int):
    gen = infinite_prime_generator()
    return [next(gen) for _ in range(limit)]

def save_primes_to_csv(primes, filename="primes.csv"):
    with open(filename, mode="w", newline="") as f:
        writer = csv.writer(f)
        writer.writerow(["Index", "Prime"])
        for i, p in enumerate(primes, start=1):
            writer.writerow([i, p])
    print(f"✅ File salvato: {filename}")

def plot_prime_spiral(primes):
    import numpy as np
    theta = []
    r = []
    for i, p in enumerate(primes):
        theta.append(i * 0.15)
        r.append(p)
    x = [ri * np.cos(t) for ri, t in zip(r, theta)]
    y = [ri * np.sin(t) for ri, t in zip(r, theta)]

    plt.figure(figsize=(8, 8))
    plt.scatter(x, y, s=1)
    plt.title("Spirale dei Numeri Primi (2D)")
    plt.axis("equal")
    plt.grid(True)
    plt.show()

def plot_prime_spiral_3d(primes):
    import numpy as np
    fig = plt.figure(figsize=(10, 8))
    ax = fig.add_subplot(111, projection='3d')

    theta = []
    r = []
    for i, p in enumerate(primes):
        theta.append(i * 0.15)
        r.append(p)

    x = [ri * np.cos(t) for ri, t in zip(r, theta)]
    y = [ri * np.sin(t) for ri, t in zip(r, theta)]
    z = list(range(len(primes)))

    ax.scatter(x, y, z, c=z, cmap='viridis', s=2)
    ax.set_title("Spirale 3D dei Numeri Primi")
    plt.show()

def show_gaps(primes):
    gaps = [primes[i+1] - primes[i] for i in range(len(primes) - 1)]
    for i, gap in enumerate(gaps, start=1):
        print(f"d_{i} = {gap}")

def is_prime_custom(n: int) -> bool:
    if n < 2:
        return False
    for p in infinite_prime_generator():
        if p * p > n:
            break
        if n % p == 0:
            return False
    return True

def plot_pn_vs_n(primes):
    x = list(range(1, len(primes) + 1))
    y = primes
    plt.figure(figsize=(10, 5))
    plt.plot(x, y, linewidth=1)
    plt.title("Grafico: Primo pₙ vs Indice n")
    plt.xlabel("n")
    plt.ylabel("pₙ")
    plt.grid(True)
    plt.show()

def advanced_search():
    print("\n=== MODALITÀ RICERCA AVANZATA ===")
    print("a) Trova tutti i primi in un intervallo personalizzato")
    print("b) Calcola dₙ per primo specifico")
    print("c) Trova primi gemelli")
    choice = input("Scegli un'opzione (a-c): ").lower()

    if choice == "a":
        a = int(input("Inizio intervallo: "))
        b = int(input("Fine intervallo: "))
        primes = []
        for p in infinite_prime_generator():
            if p > b:
                break
            if p >= a:
                primes.append(p)
        print(f"Primi tra {a} e {b}:")
        print(primes)

    elif choice == "b":
        n = int(input("Numero di primi da generare: "))
        primes = get_first_n_primes(n)
        for i in range(n - 1):
            print(f"d_{i+1} = {primes[i+1]} - {primes[i]} = {primes[i+1] - primes[i]}")

    elif choice == "c":
        n = int(input("Numero di primi da analizzare: "))
        primes = get_first_n_primes(n)
        twins = [(primes[i], primes[i+1]) for i in range(len(primes)-1) if primes[i+1] - primes[i] == 2]
        print("Primi gemelli trovati:")
        for twin in twins:
            print(twin)
    else:
        print("Scelta non valida.")

def main():
    while True:
        print("\n=== GENERATORE INFINITO DI PRIMI ===")
        print("1. Mostra i primi N numeri primi")
        print("2. Salva su file CSV")
        print("3. Disegna spirale 2D")
        print("4. Disegna spirale 3D")
        print("5. Mostra i gap d_n (differenze tra primi consecutivi)")
        print("6. Verifica se un numero è primo")
        print("7. Grafico: primo pₙ vs n")
        print("8. Modalità Ricerca Avanzata")
        print("9. Esci")
        scelta = input("Scegli un'opzione (1-9): ")

        if scelta == "1":
            n = int(input("Quanti numeri primi vuoi vedere? "))
            primes = get_first_n_primes(n)
            print(primes)

        elif scelta == "2":
            n = int(input("Quanti numeri primi vuoi salvare su CSV? "))
            primes = get_first_n_primes(n)
            save_primes_to_csv(primes)

        elif scelta == "3":
            n = int(input("Quanti numeri primi vuoi disegnare in spirale 2D? "))
            primes = get_first_n_primes(n)
            plot_prime_spiral(primes)

        elif scelta == "4":
            n = int(input("Quanti numeri primi vuoi disegnare in spirale 3D? "))
            primes = get_first_n_primes(n)
            plot_prime_spiral_3d(primes)

        elif scelta == "5":
            n = int(input("Quanti numeri primi vuoi analizzare per gap d_n? "))
            primes = get_first_n_primes(n)
            show_gaps(primes)

        elif scelta == "6":
            number = int(input("Inserisci un numero da verificare: "))
            if is_prime_custom(number):
                print(f"{number} è un numero primo.")
            else:
                print(f"{number} NON è un numero primo.")

        elif scelta == "7":
            n = int(input("Quanti numeri primi vuoi visualizzare nel grafico pₙ vs n? "))
            primes = get_first_n_primes(n)
            plot_pn_vs_n(primes)

        elif scelta == "8":
            advanced_search()

        elif scelta == "9":
            print("Uscita dal programma.")
            break

        else:
            print("Scelta non valida. Riprova.")

if __name__ == "__main__":
    main()
