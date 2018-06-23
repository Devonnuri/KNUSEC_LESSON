phonebook = {
    "John": 938477566,
    "Jim": 938377264,
    "Jill": 947662781
}

name = input()
if name in phonebook:
    print(phonebook[name])
else:
    print('없음')