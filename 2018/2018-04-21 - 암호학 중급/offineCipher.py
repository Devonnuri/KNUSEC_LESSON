str = "HGOUAKQXGZTIEFZEXKIKS"

def egcd(a, b):
	if a == 0:
		return (b, 0, 1)
	g, y, x = egcd(b%a,a)
	return (g, x - (b//a) * y, y)

print("aOffset", "bOffset", "Decrypted String",sep='\t')
aOffset = 9
for aOffset in range(1, 20):
	for bOffset in range(1, 20):
		result = ""
		isContinue = False
		for ch in list(str):
			g, x, y = egcd(aOffset, 26)
			if g != 1:
				isContinue = True
				break
			result += chr((ord(ch)-bOffset-65)*(x%26)%26+65)
		if isContinue:
			continue
		print(aOffset, bOffset, result, sep='\t')