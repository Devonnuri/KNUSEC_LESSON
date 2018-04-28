original = "WPOUPMWPVSYQWNYPXWNWPVSQWPZYPVUPY"
table = {
    "P": "E",
    "O": "A",
    "R": "R",
    "V": "L",
    "J": "Y",
    "F": "B",
    "T": "I",
    "D": "D",
    "K": "C",
    "Q": "T",
    "W": "H",
    "Y": "S",
    "X": "W",
    "N": "O",
    "Z": "M"
}

result = ""
for i in range(len(original)):
    ch = list(original)[i]
    print(ch)
    if ch in table:
        result += table[ch]
    else:
        result += chr(ord(ch)+32)

print(result)