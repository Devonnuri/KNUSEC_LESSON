import random

pnu = []
while len(pnu) < 6:
    nu = random.randint(1, 6)
    if nu not in pnu:
        print(nu)
        pnu.append(nu)