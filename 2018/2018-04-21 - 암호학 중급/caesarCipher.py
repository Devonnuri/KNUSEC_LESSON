str = "YVTLDHZUVAIBPSAPUHKHF"


print("Offset", "Decrypted String",sep='\t')
for offset in range(20):
    result = ""
    for ch in list(str):
        result += chr((ord(ch)+offset-65)%26+65)
    print(offset, result, sep='\t')