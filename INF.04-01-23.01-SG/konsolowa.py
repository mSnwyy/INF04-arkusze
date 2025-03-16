# **********************************************
# nazwa funkcji: euklides
# opis funkcji: 
# Funkcja implementuje algorytm Euklidesa do obliczania największego wspólnego dzielnika (NWD) 
# dwóch liczb całkowitych a i b. Jeśli którakolwiek z liczb jest mniejsza lub równa zero, 
# funkcja wypisuje komunikat o błędzie i zwraca None.
# parametry: 
# a - pierwsza liczba, dla której obliczany jest NWD
# b - druga liczba, dla której obliczany jest NWD
# zwracany typ i opis: 
# int - Funkcja zwraca NWD dwóch liczb całkowitych a i b, jeśli spełniają one kryteria (są większe od zera). 
# W przeciwnym razie zwraca None.
# autor: mSnwyy
# **********************************************

def euklides(a, b):
    if a <= 0 or b <= 0:
        print("Podane liczby nie spełniają kryteriów")
        return None
    else:
        while a!=b:
            if a > b:
                a = a-b
            else:
                b = b-a
        return a
try:
    a = int(input("podaj a: "))
    b = int(input("podaj b: "))
    nwd = euklides(a, b)
    if nwd is not None:
        print(f"NWD: {nwd}")
except ValueError:
    print("Podane liczby nie spełniają kryteriów.")


