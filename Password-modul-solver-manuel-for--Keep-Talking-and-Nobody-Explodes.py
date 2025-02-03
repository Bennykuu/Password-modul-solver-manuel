words = [
    "angst", "atmen", "beten", "bombe", "danke",
    "draht", "druck", "drück", "farbe", "fehlt",
    "ferse", "kabel", "knall", "knapp", "knopf",
    "leere", "legal", "lehre", "mathe", "matte",
    "panik", "pieps", "rauch", "ruhig", "saite",
    "sehne", "seite", "sende", "strom", "super",
    "timer", "übrig", "verse", "warte", "zange"
]

# Input vom Benutzer
first = input("Input\033[1m first\033[0m column: \033[94m").lower().split(" ")
second = input("\033[0mInput\033[1m second\033[0m column: \033[94m").lower().split(" ")
third = input("\033[0mInput\033[1m third\033[0m column: \033[94m").lower().split(" ")
print("\033[0m")

# Umwandlung der Listen in Sets für schnelle Lookup
first_set = set(first)
second_set = set(second)
third_set = set(third)

# Lösung berechnen mit List Comprehension
solve = [
    word for word in words
    if word[0] in first_set and word[1] in second_set and word[2] in third_set
]

# Mögliche Lösungen ausgeben
print("Possible solutions: " + "\033[92m" + ", ".join(solve) + "\033[0m")
