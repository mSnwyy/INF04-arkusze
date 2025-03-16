import tkinter as tk
from tkinter import ttk, messagebox
import random

# **********************************************
# nazwa funkcji: generator
# opis funkcji: 
# Funkcja generuje losowe hasło o zadanej długości i specyfikacji. Hasło może zawierać 
# małe i wielkie litery, cyfry oraz znaki specjalne, zależnie od wyboru użytkownika. 
# Wygenerowane hasło wyświetlane jest w osobnym oknie.
# parametry: 
# brak - Funkcja nie przyjmuje żadnych parametrów.
# zwracany typ i opis: 
# brak - Funkcja nie zwraca żadnej wartości. Wygenerowane hasło jest wyświetlane w osobnym oknie.
# autor: mSnwyy
# **********************************************

def generator():
    z_litery = "qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    z_cyfry = "0123456789"
    z_specjalne = "!@#$%^&*()_+"

    liczba_znakow = entry_password_length.get()
    try:
        liczba_znakow = int(liczba_znakow)
    except ValueError:
        messagebox.showerror("Błąd", "Podaj prawidłową liczbę znaków")
        return
    
    zestaw_znakow = z_litery

    if maleWielkie.get() == 1:
        zestaw_znakow += z_litery
    if cyfry.get() == 1:
        zestaw_znakow += z_cyfry
    if znakiSpecjalne.get() == 1:
        zestaw_znakow += z_specjalne

    if cyfry.get() == 1:
        haslo = random.choice(z_cyfry)
        liczba_znakow -= 1
    else:
        haslo = ""

    if znakiSpecjalne.get() == 1:
        haslo += random.choice(z_specjalne)
        liczba_znakow -= 1

    for _ in range(liczba_znakow):
        haslo += random.choice(zestaw_znakow)

    password_window = tk.Toplevel(window)
    password_window.title("Wygenerowane hasło")
    password_window.geometry("250x75")
    tk.Label(password_window, text="Wygenerowane hasło:").pack(pady=5)
    tk.Label(password_window, text=haslo).pack(pady=5)
    tk.Button(password_window, text="Zamknij", command=password_window.destroy).pack(pady=10)

    global current_password
    current_password = haslo

# **********************************************
# nazwa funkcji: zatwierdz
# opis funkcji: 
# Funkcja sprawdza, czy wszystkie dane wymagane przez użytkownika (imię, nazwisko, stanowisko, hasło) 
# zostały wprowadzone. Jeśli tak, otwiera nowe okno z potwierdzeniem, w którym wyświetlane są te dane. 
# Jeśli którekolwiek z wymaganych pól jest puste, użytkownik otrzymuje komunikat o błędzie.
# parametry: 
# brak - Funkcja nie przyjmuje żadnych parametrów.
# zwracany typ i opis: 
# brak - Funkcja nie zwraca żadnej wartości. Otwiera okno z potwierdzeniem danych lub wyświetla komunikat 
# o błędzie, jeśli jakieś dane są puste.
# autor: mSnwyy
# **********************************************

def zatwierdz():
    first_name = entry_first_name.get()
    last_name = entry_last_name.get()
    position = position_combobox.get()

    if not first_name or not last_name or not position or not current_password:
        messagebox.showerror("Błąd", "Proszę uzupełnić wszystkie dane i wygenerować hasło.")
        return

    confirmation_window = tk.Toplevel(window)
    confirmation_window.title("Potwierdzenie")
    confirmation_window.geometry("400x100")
    
    tk.Label(confirmation_window, text=f"Dane pracownika: {first_name} {last_name} {position}, hasło: {current_password}").pack(pady=10)   
    tk.Button(confirmation_window, text="Zamknij", command=confirmation_window.destroy).pack(pady=10)

window = tk.Tk()
window.title("Dodaj pracownika")
window.geometry("545x270")
window.configure(bg="#B0C4DE")

maleWielkie = tk.IntVar(value=1)
cyfry = tk.IntVar(value=0)
znakiSpecjalne = tk.IntVar(value=0)

frame_employee = tk.LabelFrame(window, text="Dane pracownika", bg="#B0C4DE", padx=10, pady=10)
frame_employee.grid(row=0, column=0, padx=10, pady=10, sticky="nw")

tk.Label(frame_employee, text="Imię", bg="#B0C4DE").grid(row=0, column=0, sticky="w", pady=5)
entry_first_name = tk.Entry(frame_employee)
entry_first_name.grid(row=0, column=1, pady=5)

tk.Label(frame_employee, text="Nazwisko", bg="#B0C4DE").grid(row=1, column=0, sticky="w", pady=5)
entry_last_name = tk.Entry(frame_employee)
entry_last_name.grid(row=1, column=1, pady=5)

tk.Label(frame_employee, text="Stanowisko", bg="#B0C4DE").grid(row=2, column=0, sticky="w", pady=5)
position_combobox = ttk.Combobox(frame_employee, width=17, values=["Kierownik", "Starszy programista", "Młodszy programista", "Tester"])
position_combobox.grid(row=2, column=1, pady=5)

frame_employee.grid_rowconfigure(3, minsize=39)

frame_password = tk.LabelFrame(window, text="Generowanie hasła", bg="#B0C4DE", padx=10, pady=10)
frame_password.grid(row=0, column=1, padx=10, pady=10, sticky="ne")

tk.Label(frame_password, text="Ile znaków?", bg="#B0C4DE").grid(row=0, column=0, sticky="w")
entry_password_length = tk.Entry(frame_password)
entry_password_length.grid(row=0, column=1)

tk.Checkbutton(frame_password, text="Małe i wielkie litery", bg="#B0C4DE", variable=maleWielkie).grid(row=1, column=0, sticky="w")
tk.Checkbutton(frame_password, text="Cyfry",bg="#B0C4DE", variable=cyfry).grid(row=2, column=0, sticky="w")
tk.Checkbutton(frame_password, text="Znaki specjalne", bg="#B0C4DE", variable=znakiSpecjalne).grid(row=3, column=0, sticky="w")

tk.Button(frame_password, text="Generuj hasło", bg="#4682B4", fg="white", command=generator).grid(row=4, column=0, columnspan=2, pady=5)

# Wartość globalna dla hasła
current_password = ""

tk.Button(window, text="Zatwierdź", bg="#4682B4", fg="white", width=30, command=zatwierdz).grid(row=1, column=0, columnspan=2, pady=10)

window.mainloop()
