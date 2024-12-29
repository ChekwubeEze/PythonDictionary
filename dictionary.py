

# Kirjoita kattava joukko yksikkötestejä python-kielellä alla olevalle koodille. Testin tulisi kattaa eri seniarot, kuten virheenkäsittely, erikoismerkkien syöttö jne. 

import tkinter as tk
from tkinter import messagebox


wordsandmeaning = {
    "hello": "hei",
    "thank you": "kiitos",
    "yes": "kyllä",
    "man": "mies",
    "woman": "nainen",
    "no": "ei",
    "please": "ole hyvä",
    "morning": "aamu",
    "love": "rakkaus",
    "rain": "sade",
    "snow": "lumi",
    "goodbye": "näkemiin",
    "night": "yö",
    "city": "kaupunki",
    "cat": "kissa",
    "dog": "koira",
    "friend": "ystävä",
    "brother": "veli",
    "sister": "sisko",
    "sorry": "anteeksi",
    "food": "ruoka",
    "water": "vesi",
    "baby": "vauva",
    "house": "talo",
    "school": "koulu",
    "car": "auto",
    "life": "elämä",
    "tree": "puu",
    "forest": "metsä",
    "child": "lapsi",
    "book": "kirja",
    "pen": "kynä",
    "moon": "kuu",
    "paper": "paperi",
    "phone": "puhelin",
    "computer": "tietokone",
    "family": "perhe",
    "keyboard": "näppäimistö",
    "mouse": "hiiri",
    "village": "kylä",
    "river": "joki",
    "lake": "järvi",
    "sea": "meri",
    "mountain": "vuori",
    "sun": "aurinko",
    "star": "tähti",
    "cloud": "pilvi",
    "wind": "tuuli",
    "fire": "tuli",
    "mother": "äiti",
    "father": "isä",
    "people": "ihmiset",
}


def translate_to_finnish():
    word = entry.get().strip().lower()  
    if word == "":
        messagebox.showinfo("Error", "Kirjoita sana, jonka haluat kääntää")
    else:
        käännös = wordsandmeaning.get(word, "Käännös ei löytynyt")
        result_label.config(text=f"suomi: {käännös}")


root = tk.Tk()
root.title("Kääntäjä englannista suomeksi")


frame = tk.Frame(root, padx=20, pady=20)
frame.pack()

title_label = tk.Label(frame, text="Suomi-englanti kääntäjä", font=("Helvetica", 16))
title_label.pack(pady=10)

entry_label = tk.Label(frame, text="Anna englanninkielinen sana:")
entry_label.pack()

entry = tk.Entry(frame, width=30)
entry.pack(pady=5)

translate_button = tk.Button(frame, text="Käännä", command=translate_to_finnish)
translate_button.pack(pady=10)

result_label = tk.Label(frame, text="Suomi: ", font=("Helvetica", 14))
result_label.pack(pady=10)


root.mainloop() 




